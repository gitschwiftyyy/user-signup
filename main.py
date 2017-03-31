import webapp2
import re
import cgi

content_header = """
<!DOCTYPE html>
<html>
<head>
  <title>User Signup</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>
<body>
<h1>User Signup</h1>
"""

content_footer = """
</body>
</html>
"""






form = """
<form action='/welcome' method='post'>
<label>
  Username: <input type='text' name='username'/>{0}
</label><br>
<br><label>
  Password: <input type='password' name='password'/>{1}
</label><br>
<br><label>
  Re-enter <br>Password: <input type='password' name='verify'/>{2}
</label><br>
<br><label>
  (Optional) Email: <input type='text' name='email'/>{3}
</label><br>
<br><input type='submit' value='Submit'/>
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self,username_error = "",password_error = "",verify_error = "",email_error = ""):
      
      content = content_header + form.format(username_error, password_error, verify_error, email_error) + content_footer
      self.response.write(content)

class WelcomePage(webapp2.RequestHandler):
  def post(self,username_error = "",password_error = "",verify_error = "",email_error = ""):
    username = self.request.get('username')
    username = cgi.escape(username,quote=True)
    password = self.request.get('password')
    password = cgi.escape(password,quote=True)
    verify = self.request.get('verify')
    verify = cgi.escape(verify,quote=True)
    email = self.request.get('email')
    email = cgi.escape(email,quote=True)
    
    username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    password_re = re.compile(r".{3,20}$")
    email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    
    def valid_username(username):
      return username_re.match(username)
    def valid_password(password):
      return password_re.match(password)
    def valid_email(email):
      return email_re.match(email)
      
      
    if not valid_username(username):
      username_error = "<strong>   *Username must be 3-20 characters and may contain only numbers, letters, '-', and '_'*</strong>"
      if username == "":
        username_error = "<strong>   *Please enter a username*</strong>"
    
    if not valid_password(password):
      password_error = "<strong>   *Password must be 3-20 characters in length*</strong>"
      if password == "":
        password_error = "<strong>   *Please enter a password*</strong>"
    
    if verify != password:
      verify_error = "<strong>   *Passwords did not match*</strong>"
      if verify == "":
        verify_error = "<strong>   *Please re-enter your password*</strong>"
    
    if verify == "":
      verify_error = "<strong>   *Please re-enter your password*</strong>"
    
    if not valid_email(email):
      email_error = "<strong>   *Please enter a valid email*</strong>"
      if email == "":
        email_error = ""
    
    content = content_header + form.format(username_error, password_error, verify_error, email_error) + content_footer
    self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/welcome', WelcomePage)
], debug=True)
