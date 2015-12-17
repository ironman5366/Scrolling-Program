import os
def main():
	programdir=os.path.dirname(os.path.realpath(__file__))
	os.chdir(programdir)
	os.chdir("program-files")
	os.system("main.exe")
if __name__=="__main__":
	main()