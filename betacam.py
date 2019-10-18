import os

def take_pictures(index):
	command = ("perro{}.jpg".format(index))
	os.system("raspistill -n -o {}".format(command))
	
#def main():
#	take_pictures()

#main()
