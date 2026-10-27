import subprocess

command = input("Enter command: ")
subprocess.call(command, shell=True)
