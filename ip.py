#!/usr/bin/python

#By Steven Leggett
#Make sure you install BOTO and Slick53
#Updates your current public A record to AWS, perfect for self hosting
#Don't forget to export your AWS_ACCESS and AWS_SECRET keys

from urllib import urlopen
from slick53 import route53
import re

#host zone to update in AWS Route 53
host = 'wavepointmedia.com';
#subdomain record set (A record) use empty string to update root domain

#domain = 'example.wavepointmedia.com';
domain = '';

#No changes needed beyond this point

#Fetch public IP of this server
ip = urlopen('http://www.wavepointmedia.com/ip/').read();

print 'Public IP:', ip

# if the domain is an empty string use the host
if not domain: 
	domain = host

zone = route53.get_zone(host)
aRecord =  str(zone.get_a(domain))
awsIP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', aRecord )
print 'AWS IP:', awsIP[0]

#update the zone
if (ip != awsIP[0]):
	print "updating.."
	zone.update_a(domain, ip, '800')
	print zone.get_a(domain)
