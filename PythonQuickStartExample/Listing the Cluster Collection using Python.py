from ovirtsdk.api import API
from ovirtsdk.xml import params

try:
   api = API(url = "https://engine167.eayun.com:443/api",
             username = "admin@internal",
             password = "abc123",
             ca_file = "../ca.crt")

   cluster_list = api.clusters.list
   for c in cluster_list:
      print 
   api.disconnect()

except Exception as e:
   print "Unexpected error: %s" % e
