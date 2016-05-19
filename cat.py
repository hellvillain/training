import random
import os
import tempfile
import shutil

folder = './random_files'

# creating random number of files with random lines inside
def random_files(folder):
    for files in range(random.randint(3, 15)):
        with open(folder + '/' + str(files) + '.txt', 'w+') as f:
            for line in range(random.randint(10, 50)):
                f.writelines(''.join(random.choice('Chewbacca') for _ in range(random.randint(10, 50))) + '\n')

# cat!
def cat(folder):
    random_files(folder)
    with tempfile.TemporaryFile() as tmp:
        for every in os.listdir(folder):
            tmp.writelines(line if '\n' in line else "%s\n" % line for line in open(folder + '/' + every, 'r'))
        tmp.seek(0)
        print tmp.read()
    shutil.rmtree(folder)

os.makedirs(folder)
cat(folder)
