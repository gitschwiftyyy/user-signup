import webapp2
import re

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
    password = self.request.get('password')
    verify = self.request.get('verify')
    email = self.request.get('email')
    
    if username == "":
      username_error = "<strong>   *Please enter a username*</strong>"
    
    if password == "":
      password_error = "<strong>   *Please enter a password*</strong>"
    
    if verify == "":
      verify_error = "<strong>   *Please re-enter your password*</strong>"

    content = content_header + form.format(username_error, password_error, verify_error, email_error) + content_footer
    self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/welcome', WelcomePage)
], debug=True)
