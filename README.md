# Pybuster

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/Percyjackson235/pybuster.git)

Pybuster is a Python based Web Directory and File Brute Forcer.
# Installtion
Github:
```
git clone http://github.com/PercyJackson235/pybuster.git
```
# Usage
Package Style:
```
>>> import pybuster
>>> webbuster = pybuster.Pybuster(url="http://doctor/",
... wordfile="/root/HackTheBox/tools/short.txt", exts=['php','html'])
>>> webbuster.Run()
=================================================================
Pybuster v0.02
=================================================================
Url:                http://doctor/
Threads:            15
Wordlist:           /root/HackTheBox/tools/short.txt
Status Codes:       200,204,301,302,307,401,403
User Agent:         python-requests/2.23.0
=================================================================
/.hta (Status : 403)
/.htaccess.php (Status : 403)
/.htaccess.html (Status : 403)
/.hta.html (Status : 403)
/.htpasswd (Status : 403)
/.htpasswd.php (Status : 403)
/.htpasswd.html (Status : 403)
/.hta.php (Status : 403)
/.htaccess (Status : 403)
/index.html (Status : 200)
=================================================================
Time elapsed : 1.7652253159903921
=================================================================
```
Commandline Style:
```
pybuster -u http://doctor -w short.txt -x php,html -t 20
```