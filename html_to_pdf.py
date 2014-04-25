import subprocess, os

css = "./assets/css/main.css"
start_dir = "./s9ml/"
curr_dir = start_dir


for directory in os.listdir(start_dir):
	if os.path.isdir(start_dir+directory):
		if not os.path.exists("pdf/"+directory):
			os.mkdir("pdf/"+directory)
		for fil in os.listdir(start_dir+directory):
			if fil.endswith(".html"):
				subprocess.call(["prince","--no-author-style","-s",css,
					start_dir+directory+"/"+fil,
					"-o","pdf/"+directory+"/"+fil[:-5]+".pdf"])

	#if not os.path.exists(start_dir + directory):
	#	os.makedirs()
