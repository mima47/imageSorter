import os
import time
import shutil
import datetime

print('----Image organizer----')
print()
input('Press any key to continue...')

pictures = []
dates = []

for file in os.listdir():
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.dng') or file.endswith('.nef') or file.endswith('.mp4'):
        pictures.append(file)

for i in pictures:
    createTime = datetime.datetime.strptime(time.ctime(os.path.getmtime(i)), "%a %b %d %H:%M:%S %Y")
    dates.append(str(createTime.date()))

for i in dates:
    try:
        os.mkdir(i)
        print('Created directory: ' + i)
    except FileExistsError:
        pass

n = 0
for i in pictures:
    try:
        shutil.move(i, dates[n])
        print('Moved file: ' + i)
    except Exception:
        print('File: ' + i + ' already exists!')
    n += 1

input('DONE! Press any key to exit...')
