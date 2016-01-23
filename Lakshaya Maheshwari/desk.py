import shutil,os


destDir=r'C:\Users\Admin\Desktop\mixed'

dest='C:\Users\Admin\Desktop\mixed'
destDir1=dest+"\images"
destDir2=dest+"\songs"
destDir3=dest+"\docs"
destDir4=dest+"\documents"
destDir5=dest+"\Exe"
destDir6=dest+"\Compressed"
destDir7=dest+"\movies"
#destDir1='C:\Users\Admin\Desktop\mixed\images'
#destDir2='C:\Users\Admin\Desktop\mixed\songs'
#destDir3='C:\Users\Admin\Desktop\mixed\docs'
#destDir4='C:\Users\Admin\Desktop\mixed\documents'
#destDir5='C:\Users\Admin\Desktop\mixed\Exe'
#destDir6='C:\Users\Admin\Desktop\mixed\Compressed'
#destDir7='C:\Users\Admin\Desktop\mixed\movies'
os.chdir(destDir)
if os.path.exists(destDir1):
 print "Yes, Image folder exists"
else:
 os.makedirs(destDir1)

if os.path.exists(destDir2):
 print "Yes, Songs folder exists"
else:
 os.makedirs(destDir2)


if os.path.exists(destDir3):
 print "Yes, docs folder exists"
else:
 os.makedirs(destDir3)

if os.path.exists(destDir4):
 print "Yes, Documents folder exists"
else:
 os.makedirs(destDir4)


if os.path.exists(destDir5):
 print "Yes, Exe folder exists"
else:
 os.makedirs(destDir5)

if os.path.exists(destDir6):
 print "Yes, Compressed folder exists"
else:
 os.makedirs(destDir6)

if os.path.exists(destDir7):
 print "Yes, Movies folder exists"
else:
 os.makedirs(destDir7)

for file in os.listdir(destDir):
    ending =file.split(".")
    print ending
    end=str(ending[-1])
    print end
    if end in["JPG","jpg","png","PNG","gif"]:
        print "i am in image"
        shutil.move(file,destDir1)
        del ending[:]
    elif end in["mp3"]:
        print "i am in song"
        shutil.move(file,destDir2)
        del ending[:]
    elif end in["txt","xml","csv"]:
        print "i am in txt"
        shutil.move(file,destDir3)
        del ending[:]
    elif end in["docx","pptx","pdf","ppt"]:
        print "i am in docx"
        shutil.move(file,destDir4)
        del ending[:]
    elif end in["exe","bat"]:
        print "i am in exe"
        shutil.move(file,destDir5)
        del ending[:]
    elif end in["zip","rar"]:
        print "i am in compressed"
        shutil.move(file,destDir6)
        del ending[:]
    elif end in["mkv","mp4","avi"]:
        print "i am in movies"
        shutil.move(file,destDir7)
        del ending[:]






