import json
from openalpr import Alpr

alpr = Alpr("eu","/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
results = alpr.recognize_file("/home/pi/Desktop/apiAlpr/fotos/camara2lente8.jpg")
i = 0
for plate in results['results']:
    i = 1 + i
print("     %12s  %12s"  % ("Plate", "Confidence"))
for candidate in plate['candidates']:
    prefix = "-"
    print("    %s %12s%12f" % (prefix,candidate["plate"],candidate["confidence"]))

#print(json.dumps(results, indent=4))


alpr.unload()
