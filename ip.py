#!/usr/bin/python

#By Steven Leggett
#Make sure you install BOTO and Slick53
#Updates your current public A record to AWS, perfect for self hosting
#Don't forget to export your AWS_ACCESS and AWS_SECRET keys

from urllib import urlopen
from slick53 import route53
import re

#Fetch public IP of this server
ip = urlopen('http://www.wavepointmedia.com/ip/').read();

#domain zone to update in AWS Route 53
domain = 'wavepointmedia.net';
print 'Public IP:', ip

zone = route53.get_zone(domain)
aRecord =  str(zone.get_a(domain))
awsIP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', aRecord )
print 'AWS IP:', awsIP[0]

#update the zone
if (ip != awsIP[0]):
	print "updating.."
	zone.update_a(domain, ip, '800')
	print zone.get_a(domain)
