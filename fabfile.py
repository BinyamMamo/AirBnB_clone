#!/usr/bin/python3
from fabric.api import *

env.use_ssh_config = True
env.hosts = ['web01']

def transfer(file=None):
	if (file is None):
		print("file is not provided!")
		return
	# file = prompt("file to transfer: ")
	path = prompt("remote path: ")
	path = "/tmp" if path is None else path
	put(file, path)
