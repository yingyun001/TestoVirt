# Accessing the API Entry Point using Python
   
from ovirtsdk.api import API
from ovirtsdk.xml import params

try:
   api = API(url = "https://engine167.eayun.com:443/api",
             username = "admin@internal",
             password = "abc123",
             ca_file = "../ca.crt")
   
   print "Connected to %s successfully!" % api.get_product_info().name
   
   api.disconnect()

except Exception as e:
   print "Unexecpted error: %s" % e
  
