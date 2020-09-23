import shutil
from datetime import datetime

total, used, free = shutil.disk_usage('/')
time = datetime.now()

file = open('asdf.csv', 'a')
file.write(time.strftime("%Y-%m-%d, "))
file.write('%d, %d\n' % (used // (2**30), free // (2**30)))