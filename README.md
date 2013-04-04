#Route 53 IP Update:

Using AWS Route 53 API this updates your DNS A Record after getting your public IP address. 
Perfect for self hosting or your own servers where you want to make available.

#What it needs:
- Boto (https://github.com/boto/boto)
- Slick53 (https://github.com/bluepines/slick53)

Setup a cron for automated updates: (Set hourly)
0 * * * * /home/steve/route53ip/ip.py

#Use as you wish!
Contact me with any questions @leggettsteven or create an issue.
