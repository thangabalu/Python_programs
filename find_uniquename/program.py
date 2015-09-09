#Limitation - Names are considered as case sensitive names

import urllib
import re

FOUND_MORE_THAN_ONE_UNIQUE_NAME = "Not expected"
FOUND_ONE_UNIQUE_NAME = "Expected"


def find_uniquename(url):
  webpage = urllib.urlopen(url).read()
  found_string = re.findall(r'"quiz":\s*\[(.*)\]\}',webpage)
  extract_names= [item.replace('"','') for item in found_string[0].split(",")]
  unique_name = [x for x in extract_names if extract_names.count(x) == 1]
  if len(unique_name) != 1:
    return unique_name,FOUND_MORE_THAN_ONE_UNIQUE_NAME
  elif len(unique_name) == 1:
    return unique_name[0], FOUND_ONE_UNIQUE_NAME

if __name__ == "__main__":
  url = "https://api2.appspotr.com/givemeachallenge"
  unique_name, error_code = find_uniquename(url)

  if error_code == FOUND_ONE_UNIQUE_NAME:
    print "Found one unique name - %s" %(unique_name)
  elif error_code == FOUND_MORE_THAN_ONE_UNIQUE_NAME:
    print "More than one unique name found"
    print "Unique name list - %s" %unique_name
  

