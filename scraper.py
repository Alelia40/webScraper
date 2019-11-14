from bs4 import BeautifulSoup
import os

for filename in os.listdir('directory'):
    with open(filename) as fp:
        soup = BeautifulSoup(fp)
        #do stuff with the soup here