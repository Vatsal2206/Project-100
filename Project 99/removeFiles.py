import time
import shutil
import os

path = input('Enter your folder path here :')

if(os.path.exists(path)):
    movingToPath = os.walk(path)
    os.path.join(movingToPath)