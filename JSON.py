import urllib2
import json

def main():
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
  webUrl = urllib2.urlopen(urlData)
  print webUrl.getcode()
  if (webUrl.getcode() ==200):
    data = webUrl.read()
    printResults(data)
  else:
    print "receieved and error from server:" + str(webUrl.getcode())

def printResults(data):
  theJSON = json.loads(data)

  if "title" in theJSON["metadata"]:
    print theJSON["metadata"]["title"]
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"
    
    for i in theJSON["features"]:
      #print i["properties"]["place"]
      if i["properties"]["mag"] >= 4.0:
        print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
if __name__=="__main__":
  main()
