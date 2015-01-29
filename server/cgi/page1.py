#!/usr/bin/env python

# CMPUT 410 Lab3
# Dylan Stankievech
# Jan 28, 2015
#

import cgi
 
form = cgi.FieldStorage()
 
birthdate = form.getvalue('birthdate')
hobby = form.getvalue('hobby')
gender = form.getvalue('gender')
card = form.getvalue('credit')
 
print "Content-type: text/html"
print
print "<html><head><title>Page1</title></head><body>"

if (birthdate or hobby or gender or card):
    print "<p>The data from page2 is:<br/><br/>"

if (birthdate):
    print "Birthdate: " + birthdate + "<br/>"
if (hobby):
    print "Hobby: " + hobby + "<br/>"
if (gender):
    print "Gender: " + gender + "<br/>"
if (card):
    print "Credit Card: " + card + "<br/>"
    
if (birthdate or hobby or gender or card):
    print "</p>"

print """<p>Please enter the following information:</p><form method="post" action="page2.py">
First Name: <input type="text" name="name" value=""></input><br/>
Last Name: <input type="text" name="family" value=""></input><br/>
Password: <input type="password" name="password" value=""></input><br/>
Which is better: <br/><input type="radio" name="city" value="Edmonton" checked>Edmonton</input><br/>
<input type="radio" name="city" value="Calgary" disabled="disabled">Calgary</input><br/>
<input type="submit" value="Submit">
</form></body></html>"""