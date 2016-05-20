import urllib2

def main():
  webUrl = urllib2.urlopen("http://joemarini.com")

  print str(webUrl.getcode())
  data = webUrl.read()
  print data

if __name__=="__main__":
  main()
