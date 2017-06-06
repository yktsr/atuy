import urllib.request, urllib.parse
import xml.etree.ElementTree as ET

params = {
   "any" : "",
   "nameOfMeeting" : "決算行政監視委員会",
   "from" : "2017-05-05",
   "until" : "2017-06-05",
}

p = urllib.parse.urlencode(params)
p = p.replace("=","%3D")
p = p.replace("&","%26")

with urllib.request.urlopen("http://kokkai.ndl.go.jp/api/1.0/speech?" + p) as res:
   html = res.read().decode("utf-8")
   print(html)
   xmldata = ET.fromstring(html)

