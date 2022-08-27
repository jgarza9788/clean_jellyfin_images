# import stuff
import os, random

# update this to be your movie directory
directories = [
    r'D:\Torrents\Movies',
    r'D:\Torrents\Shows',
    ]

strings = [
    '-logo',
    '-poster',
    '-backdrop',
    '-folder'
    'logo',
    'poster',
    'backdrop',
    'folder'
    ]

extensions = [
    'png',
    'jpg',
    'svg'
    ]

image_files = []

for d in directories:
    for subdir, dirs, files in os.walk(d):

        # print('subdir: ',subdir)
        # print('dirs: ',dirs)
        # print('files: ',files)

        for index,file in enumerate(files):

            try:
                # print(subdir,'{:.2f}'.format(index/len(files)))
                thisFile = os.path.join(subdir, file)
                
                score = 0 
                for s in strings:
                    if s in thisFile:
                        score += 1
                for e in extensions:
                    if e in thisFile:
                        score += 1
                                
                if score >= 2:
                    image_files.append(thisFile)
            except Exception as ex:
                # print(subdir, file)
                # print(ex)
                pass


# print(*files,sep='\n')
print('file count: ',len(image_files))
for f in image_files:
    print(f)
    # os.remove(f)
