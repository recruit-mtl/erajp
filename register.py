# -*- coding: utf-8 -*-
import os
import pypandoc

f = open('README.txt', 'w+')
f.write(pypandoc.convert('README.md', 'rst').encode("utf-8"))
f.close()
os.system("python setup.py sdist upload")
os.remove('README.txt')