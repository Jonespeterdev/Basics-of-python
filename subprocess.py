import sys
import subprocess

def listdir(dir):
  cmd = 'dir' + dir
  print("Command to run:", cmd)
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output)

listdir("path/of/your/folder")