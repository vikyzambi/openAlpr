import json
import sys
from betacam import take_pictures
from openalpr import Alpr
import os

def license_recognition(rango):
    alpr = Alpr("eu","/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
    alpr.set_default_region("al")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    for i in range(rango):
        take_pictures(i)
        path = "/home/pi/Desktop/apiAlpr/foto{}.jpg".format(i)    
        results = alpr.recognize_file(path)
        #print(json.dumps(results, indent=4))
        print_license(results)
    alpr.unload()

def print_license(results):
    i = 0
    for plate in results['results']:
        i = 1 + i
    print("\n    %12s  %12s \n"  % ("Plate", "Confidence"))
    cont = 0
    for candidate in plate['candidates']:
        #if cont == 2:
         #   break
        prefix = "-"
        if candidate["matches_template"]: 
            print("    %s %12s%12f" % (prefix,candidate["plate"],candidate["confidence"]))
            cont += 1



def take_pictures(index):
	command = ("foto{}.jpg".format(index))
	os.system("raspistill  -o {}".format(command))
	
def main():
    valor = sys.argv[1]
    valor = int(valor)
    print(valor)
    license_recognition(valor)

main()    



