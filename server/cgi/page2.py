#!/usr/bin/env python

# CMPUT 410 Lab3
# Dylan Stankievech
# Jan 28, 2015
#


import cgi
 
form = cgi.FieldStorage()
 
name = form.getvalue('name')
family = form.getvalue('family')
city = form.getvalue('city')
password = form.getvalue('password')
 
print "Content-type: text/html"
print
print "<html><head><title>Page2</title></head><body>"

if (name or family or city or password):
    print "<p>The data from page1 is:<br/><br/>"

if (name):
    print "First Name: " + name + "<br/>"
if (family):
    print "Last Name: " + family + "<br/>"
if (city):
    print "Best City: " + city + "<br/>"
if (password):
    print "Password: " + password + "<br/>"
    
if (name or family or city or password):
    print "</p>"

print """<p>Please enter the following information:</p><form method="post" action="page1.py">
Birthdate: <input type="date" name="birthdate" value=""></input><br/>
Hobby: <input type="text" name="hobby" value=""></input><br/>
Credit Card Number: <input type="number" name="credit" value=""></input><br/>
<input type="radio" name="gender" value="male" checked>Male</input><br/>
<input type="radio" name="gender" value="female">Female</input><br/>
<input type="radio" name="gender" value="other">Other</input><br/>
<input type="submit" value="Submit">
</form></body></html>"""