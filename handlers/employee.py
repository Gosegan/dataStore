import webapp2
from webapp2_extras import jinja2


class EmployeeHandler(webapp2.RequestHandler):
    def post(self):
        self.name = self.request.get("input0", "anonymous")
        self.surname = self.request.get("input1", "anonymous")
        self.age = self.request.get("input2", "anonymous")

        jinja = jinja2.get_jinja2(app=self.app)
        object = {
            'name': self.name,
            'surname': self.surname,
            'age': self.age
        }
        self.response.write(
            jinja.render_template("response.html", **object)
        )


app = webapp2.WSGIApplication([
    ('/employee', EmployeeHandler)
], debug=True)
