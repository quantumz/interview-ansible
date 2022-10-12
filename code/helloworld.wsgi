#!/usr/bin/python
import sys
import os

sys.path.insert (0,'/opt/helloworld')
os.chdir("/opt/helloworld")
from helloworld import app as application
