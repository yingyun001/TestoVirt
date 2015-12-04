# _*_ coding:utf-8 _*_

from ovirtsdk.api import API
from ovirtsdk.xml import params

try:
   api = API(url = "https://engine167.eayun.com:443/api",
             username = "admin@internal",
             password = "abc123",
             ca_file = "../ca.crt")

   dc_list = api.datacenters.list()
   print dc_list
   print '------------------------------'
   for dc in dc_list:
      """
      所有的属性都在 /usr/lib/python2.7/site-packages/ovirtsdk/xml 的 BaseResource 类中。
      """
      print "datacenter name: %s\nid: %s\ndescription: %s\ncomment: %s\ncreation_status: %s\nget_link: %s\nget_href: %s\nget_extensiontype_: %s\nstorage_type: %s\nlocal: %s\nstorage_format: %s\nversion: %s\nsupported_versions: %s\nstatus: %s" % (dc.get_name(), dc.get_id(), dc.get_description(), dc.get_comment(), dc.get_creation_status(), dc.get_link(), dc.get_href(), dc.get_extensiontype_(), dc.storage_type, dc.local, dc.storage_format, dc.version, dc.supported_versions, dc.status)

      print '-------------------------'
      print dc.name
   api.disconnect()

except Exception as e:
   print "Unexpected error: %s" % e
