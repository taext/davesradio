#!/home/dd/anaconda3/bin/python

import subprocess

subprocess.Popen(["vlc","http://raw.githubusercontent.com/taext/powercasts/master/newest.txt", "--random"]).wait()
