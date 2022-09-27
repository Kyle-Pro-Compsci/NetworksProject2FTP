from types import NoneType
from urllib.parse import urlparse

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
