import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
print("Content-Type: text/html")
print()   
print("<TITLE>CGI script output</TITLE>")
print("<h1>Hello", str(form["name"].value).lower().title(), "</h1>")
