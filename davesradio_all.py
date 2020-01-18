#!/home/dd/anaconda3/bin/python

import subprocess

subprocess.Popen(["vlc","https://raw.githubusercontent.com/taext/powercasts/master/podcasts_opml.txt", "--random"]).wait()
