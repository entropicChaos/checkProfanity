#This program checks if there are an profanites inside a given text file


def read_file():
	fileToVerify = open("/home/bios-hock/Documenti/programmiPython/howToOpenAFileInPython.txt")
	contens=fileToVerify.read()
	print(contens)
	fileToVerify.close()
read_file()
