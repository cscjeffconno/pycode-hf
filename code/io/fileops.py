import os

if(not os.path.exists('c:/pythonplayground')):
    os.mkdir('c:/pythonplayground')

# r, rb, w,wb w+, rb+, wb+, a(append)
f = open('c:/pythonplayground/test.txt','w+')

f.write('testing writing file...')

print f.fileno()

f.seek(7)

print f.tell()

print f.read()

f.seek(0)



print f.read()




