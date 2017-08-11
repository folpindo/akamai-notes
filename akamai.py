#!/bin/env python

import os,sys,urllib,urllib2,time
from logbook import Logger,FileHandler


user = "username"
token = "password"

message = bytes(user).encode('utf-8')
secret = bytes(token).encode('utf-8')
logger = Logger("Cache Purge")
logfile = "cache-purge.log"

fh = FileHandler(logfile,"a")
fh.applicationbound()
fh.push_application()

api_root = "https://api.ccu.akamai.com"
get_call = "/ccu/v2/queues/default"
#data = {}


try:
        req = None
        url = api_root + get_call
        mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        mgr.add_password(None,api_root, user, token)
        handler = urllib2.HTTPBasicAuthHandler(mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        #req = urllib2.Request(api_root,urllib.urlencode(data))
        req.add_header('Application-Type','application/json')
        resp = urllib2.urlopen(req)
        logger.info("Response: %s" % resp.read())
        
except urllib2.HTTPError as e:
        logger.error("error: %s" % e)
        
