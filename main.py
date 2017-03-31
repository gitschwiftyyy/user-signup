import webapp2
import re

content_header = """
<!DOCTYPE html>
<html>
<head>
  <title>User Signup</title>
</head>
<body>
<h1>User Signup</h1>
"""

content_footer = """
</body>
</html>
"""
username_error = ""
password_error = ""
verify_error = ""
email_error = ""

form = """
<form action='/welcome' method='post'>
<label>
  Username: <input type='text' name='username'/>{0}
</label><br>
<br><label>
  Password: <input type='password' name='password'/>{1}
</label><br>
<br><label>
  Re-enter Password: <input type='password' name='verify'/>{2}
</label><br>
<br><label>
  (Optional) Email: <input type='text' name='email'/>{3}
</label><br>
<br><input type='submit' value='Submit'/>
</form>
""".format(username_error, password_error, verify_error, email_error)

class MainPage(webapp2.RequestHandler):
    def get(self):
      
      content = content_header + form + content_footer
      self.response.write(content)

class WelcomePage(webapp2.RequestHandler):
  def post(self):
    username = self.request.get('username')
    password = self.request.get('password')
    verify = self.request.get('verify')
    email = self.request.get('email')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
