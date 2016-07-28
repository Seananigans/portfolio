# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

# with open("main.html") as fhand:
# 	form = fhand.read()

form = """
<form method="post" action="/testform">
	<input type="text" name="q">
	<input type="submit">
</form>
"""

test = """
<option value="{}">Three</option>
"""
tester = "\n".join([test.format(i) for i in range(5)])

form = """
<form>
	<input type="password" name="q">
	<input type="checkbox" name="jeff">
	<br>
	<label>One
		<input type="radio" name="l" value="one">
	</label>
	<label>Two
		<input type="radio" name="l" value="two">
	</label>
	<label>Three
		<input type="radio" name="l" value="three">
	</label>
	<br>
	<select name="list">
		<option value="1">One</option>
		<option value="2">Two</option>
		<option value="3">Three</option>
		{}
	</select>
	<br>
	<input type="submit">

</form>
""".format(tester)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

    def post(self):
    	self.response.write("Thanks for the info!")

class TestHandler(webapp2.RequestHandler):
	def post(self):
		# q = self.request.get("q")
		# self.response.out.write(q)

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)
