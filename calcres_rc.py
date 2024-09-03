from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x8f\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 height=\x222\
4px\x22 viewBox=\x220 \
-960 960 960\x22 wi\
dth=\x2224px\x22 fill=\
\x22#e8eaed\x22><path \
d=\x22M360-200q-20 \
0-37.5-9T294-234\
L120-480l174-246\
q11-16 28.5-25t3\
7.5-9h400q33 0 5\
6.5 23.5T840-680\
v400q0 33-23.5 5\
6.5T760-200H360Z\
m400-80v-400 400\
Zm-400 0h400v-40\
0H360L218-480l14\
2 200Zm96-40 104\
-104 104 104 56-\
56-104-104 104-1\
04-56-56-104 104\
-104-104-56 56 1\
04 104-104 104 5\
6 56Z\x22/></svg>\
\x00\x00\x01\xe2\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 height=\x222\
4px\x22 viewBox=\x220 \
-960 960 960\x22 wi\
dth=\x2224px\x22 fill=\
\x22#e8eaed\x22><path \
d=\x22M320-240h60v-\
80h80v-60h-80v-8\
0h-60v80h-80v60h\
80v80Zm200-30h20\
0v-60H520v60Zm0-\
100h200v-60H520v\
60Zm44-152 56-56\
 56 56 42-42-56-\
58 56-56-42-42-5\
6 56-56-56-42 42\
 56 56-56 58 42 \
42Zm-314-70h200v\
-60H250v60Zm-50 \
472q-33 0-56.5-2\
3.5T120-200v-560\
q0-33 23.5-56.5T\
200-840h560q33 0\
 56.5 23.5T840-7\
60v560q0 33-23.5\
 56.5T760-120H20\
0Zm0-80h560v-560\
H200v560Zm0-560v\
560-560Z\x22/></svg\
>\
"

qt_resource_name = b"\
\x00\x05\
\x00o\xa6S\
\x00i\
\x00c\x00o\x00n\x00s\
\x00\x0d\
\x07d\x0f\xa7\
\x00b\
\x00a\x00c\x00k\x00s\x00p\x00a\x00c\x00e\x00.\x00s\x00v\x00g\
\x00\x0d\
\x0b\xa5\x03'\
\x00c\
\x00a\x00l\x00c\x00u\x00l\x00a\x00t\x00e\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x91'\xf5C\xf8\
\x00\x00\x000\x00\x00\x00\x00\x00\x01\x00\x00\x01\x93\
\x00\x00\x01\x91'\xf5\x1f\xb9\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
