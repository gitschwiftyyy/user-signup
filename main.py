import webapp2
import re

content_header = """
<!DOCTYPE html>
<html>
<head>
  <title>User Signup</title>
</head>
<body>
<t1>User Signup</t1>
"""

content_footer = """
</body>
</html>
"""
form = """
<form action='/welcome' method='post'>
<label>
  Username <input type='text' name='username'/>
</label><br>
<label>
  Password <input type='password' name='password'/>
</label><br>
<label>
  Re-enter Password <input type='password' name='verify'/>
</label><br>
<label>
  (Optional) Email <input type='text' name='email'/>
</label><br>
<input type='submit' value='Submit'/>
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
      content = content_header + form + content_footer
      self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
