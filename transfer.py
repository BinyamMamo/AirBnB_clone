#!/usr/bin/python3
from fabric.api import *
from sys import argv

env.use_ssh_config = True
env.hosts = ['web01']

if __name__ == "__main__":
	file = argv[1]
	path = argv[2] if len(argv) > 1 is None else "/" 
	put(file, path)
