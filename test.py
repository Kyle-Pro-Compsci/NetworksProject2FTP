from types import NoneType
from urllib.parse import urlparse

def urlparse_test():
    print("ftp://bob:s3cr3t@ftp.example.com/")
    u1 = urlparse("ftp://bob:s3cr3t@ftp.example.com/")
    print(u1, "\n")

    print("ftp://bob:s3cr3t@ftp.example.com/documents/homeworks")
    u2 = urlparse("ftp://bob:s3cr3t@ftp.example.com/documents/homeworks")
    print(u2)
    print(u2.username)
    print(u2.password, "\n")

    print("other-hw/essay.pdf")
    u3 = urlparse("other-hw/essay.pdf")
    print(u3)
    print(u3.username, type(u3.username), "\n")

    print("ftp://bob@ftp.example.com/")
    u4 = urlparse("ftp://bob@ftp.example.com/")
    print(u4)
    print(u4.username)
    print("password check")
    print(u4.password)
    print(isinstance(u4.password, NoneType))
    print(u4.password == None)
    print(isinstance(u4.username, NoneType))
    print(u4.scheme)
    print(u4.hostname)
    print(u4.port)

def byte_test():
    string_input = '220 Welcome to Khoury CS3700 FTP Server\r\n'
    print(string_input)
    print('\r\n' in string_input)
    print('\n\n\n' in string_input)
    encoded = string_input.encode()
    print(encoded)
    decoded = encoded.decode()
    print(decoded)
    print('\r\n' in decoded)

def partition_test():
    string = "227 Entering Passive Mode (54,88,34,75,4,188)."
    after_partition = string.partition("(")
    print(type(after_partition))
    print(after_partition)
    nums = after_partition[2]
    print(nums.partition(")")[0])

    one_move = string.partition('(')[2].partition(')')[0].split(',')
    print(one_move)
    print(type(one_move))
    ip = one_move[0] + '.' + one_move[1] + '.' + one_move[2] + '.' + one_move[3]
    port = int(one_move[4]) * pow(2, 8) + int(one_move[5])
    print(ip)
    print(type(port), port)
    print(195 * pow(2, 8) + 149)

    lhs = '{0:08b}'.format(int(one_move[4]))
    rhs = '{0:08b}'.format(int(one_move[5]))
    print(lhs)
    print(rhs)
    print(int(lhs + rhs, 2))

    lhs_test = '{0:08b}'.format(195)
    rhs_test = '{0:08b}'.format(149)
    print(lhs_test)

    print(int(lhs_test+rhs_test, 2))

def url_parse_test_2():
    test1 = "ftp://bob:s3cr3t@ftp.example.com/"
    test2 = "ftp://bob:s3cr3t@ftp.example.com/documents/homeworks/homework1.docx"
    test3 = "other-hw/essay.pdf"

    u = urlparse(test3)
    print(u.path)

if __name__ == '__main__':
    url_parse_test_2()