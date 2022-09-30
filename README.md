This project was written in Python and implements a basic set of FTP client functionality. One operation can be performed when the client (3700ftp) is called via the command line. There are two to three arguments passed in, depending on the operation. The supported operations are: ls (path1), mkdir (path1), rm (path1), rmdir (path1), cp (path1) (path2), mv (path1) (path2). Exactly one path argument must be a FTP URL. Optionally included in this path is the given username, password, and port.
The program also supports the flags -h --help and -v --verbose. Adding -h gives a brief overview of the program. Adding -v makes the program print all messages with the server to std out.

An example command line call is:
python3 3700ftp cp send_test.txt ftp://username:password@ftp.3700.network/directory/send_test.txt -v
This command copies the file send_test.txt from the local directory and saves it in the path /directory/ with filename send_test.txt.
The default port of 21 is used. The URL hostname is ftp.3700.network, and the two paths are send_test.txt and /directory/send_test.txt. The verbose flag is also triggered.

The code is split into several stages.
1. The input is parsed. The URL, username, password, port, and paths are obtained, as well as whether the intent is to send a data from the local computer to the server or vice versa.
2. Log into the FTP client. The program creates a socket with the given port (default 21) and connects to the server. The program then sends the given username (default "anonymous") and then the corresponding password (if given). 
3. Enter a function that calls a sub-function that corresponds to the given operation.
4. If the operation doesn't require a data channel, then it skips to step 6. Otherwise, the program sends a PASV and parses the response to obtain an IP address and port for the data channel.
5. Call a sequence of FTP commands to change the connection to 8-bit binary mode, set the connection to stream mode, and set the connection to file-oriented mode. This is done in advance of downloading or uploading data from or to the FTP sever.
6. The program sends its given operation as a request to the server. If the operation requires a data transfer, it then opens a Data Channel using the IP and port obtained in step 2.
7. If the operation involves any local changes, a local file is either written or removed.

One of the main difficulties faced was getting the Data Channel working properly, since the way it is set up and operates is very opaque. The actual order of operations is to call PASV, send a request such as LIST, and then connect to the Data Channel, receive the data, and close the channel.

In order to avoid race conditions from the command socket, I implemented a receive_data function that loops until the string '\r\n' is received, signaling the end of the message.

The mv and cp operations were implemented with a single function, with an optional delete_after flag that deletes the file after it is copied should the operation be mv instead of cp.

The biggest challenge was in receiving a large amount of data in the data channel without an having an exit character to rely on to close a loop. Since the data received would all by in the 'bytes' class, a byte array was used to collect the potentially piecemeal data. I chose to loop until a byte package of length 0 was received, which should indicate the socket being closed.

For testing, I used a log function that prints its input. This makes it easy to spread them all around the code and toggle them on or off. Also, as I'm still building my familiarity with Python, I created a test file with different functions that can be called to test individual bits of python functionality.