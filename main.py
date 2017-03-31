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
<form action='/' method='post'>
<label>
  Username: <input type='text' name='username' value='%(username)s'/>{0}
</label><br>
<br><label>
  Password: <input type='password' name='password' value='%(password)s'/>{1}
</label><br>
<br><label>
  Re-enter <br>Password: <input type='password' name='verify' value='%(verify)s'/>{2}
</label><br>
<br><label>
  (Optional) Email: <input type='text' name='email' value='%(email)s'/>{3}
</label><br>
<br><input type='submit' value='Submit'/>
</form>
"""

thank_you = "<h3>Thank you for signing up!</h3>"

class MainPage(webapp2.RequestHandler):
    def get(self, username_error = "", password_error = "", verify_error = "", email_error = "", username = "", password = "", verify = "", email = ""):
      
      content = content_header + form.format(username_error, password_error, verify_error, email_error) % {"username":username, "password":password, "verify":verify, "email":email} + content_footer
      self.response.write(content)
    
    def post(self,username_error = "",password_error = "",verify_error = "",email_error = "", username = "", password = "", verify = "", email = ""):
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
        if email == "":
          return True
        else:
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
      
      if valid_username(username) and valid_password(password) and password == verify and valid_email(email):
        content = content_header + thank_you + content_footer
      else:
        content = content_header + form.format(username_error, password_error, verify_error, email_error) % {"username":username, "password":password, "verify":verify, "email":email} + content_footer
      self.response.write(content)

class SignupPage(webapp2.RequestHandler):
  def post(self,username_error = "",password_error = "",verify_error = "",email_error = "", username = "", password = "", verify = "", email = ""):
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
      if email == "":
        return True
      else:
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
    
    if valid_username(username) and valid_password(password) and password == verify and valid_email(email):
      content = content_header + thank_you + content_footer
    else:
      content = content_header + form.format(username_error, password_error, verify_error, email_error) % {"username":username, "password":password, "verify":verify, "email":email} + content_footer
    self.response.write(content)
    
    

app = webapp2.WSGIApplication([
    ('/', MainPage),('/signup', SignupPage)
], debug=True)
