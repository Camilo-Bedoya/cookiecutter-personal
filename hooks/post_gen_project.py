import subprocess

subprocess.call(['git', 'init'], shell=True)
subprocess.call(['git', 'add', '*'], shell=True)

print("Done....")