##############
#INSTRUCTIONS#
##############

# Begin by checking out the files used for the Inkling project using SVN
## You'll need to have SVN installed on your computer. 
### Google that if you're on Windows. 
### If you're on Mac or Linux, it should already be there.
## Type into the command line: "svn checkout <URL>" 
### <URL> represents the URL for the repository
#### The URL for the repository should be "https://svn.inkling.com/svn/sbu101_2014_fork/trunk/" without the quotes
#####The password will be your stonybrook.edu email
#####When it prompts your username and password again, it will be your inkling account login
# You'll now need to download the conversion program
## http://wkhtmltopdf.org/downloads.html
## THIS IS ONLY available on Windows and Linux at the time of writing this.
# Place this Python script in the "trunk" directory
# Run the script
## You need to have Python installed on your computer
### Again, you'll need to google Python if you're on Windows probably
### Mac or Linux? You're already good
## Change the current directory in the command line to the trunk directory
### If you don't know how to do that, look up the "cd" command
## Type into the command line: "python <file>.py", again, whithout the quotation marks, where <file> is the name of this file.

import subprocess, os

#Directory in which the HTML documents are being stored
start_dir = "./s9ml/"
#Directory used to store all of the converted PDFs
pdf_dir = "./pdf/"

#Creates directory "dir" IFF it doesn't already exist.
def makedir(dir):
	try:
		os.stat(dir)
	except:
		os.mkdir(dir)

#MIf the directory for storing PDFs doesn't already exist, then create it
makedir(pdf_dir)

#Go through all of the files in the directory, "./s9ml/"
for directory in os.listdir(start_dir):
	#If the current file is a directory...
	if (os.path.isdir(start_dir+directory)):
		#...then make a directory for it in the PDF-storing directory.
		makedir(pdf_dir + directory)
		#Now go through all of the files in that directory...
		for fil in os.listdir(start_dir+directory):
			#and if you see an HTML file...
			if fil.endswith(".html"):
				#...then convert it to a PDF file and store it in the PDF directory
				#wkhtmltopdf <target> <source>
				subprocess.call(["wkhtmltopdf", "-q", start_dir+directory+"/"+fil, 
					pdf_dir+directory+"/"+fil[:-5]+".pdf"])