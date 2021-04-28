import webapp2
import time
from webapp2_extras import jinja2, users
from webapp2_extras.users import users

from model.EcoDto import EcoDto


class DoHandler(webapp2.RequestHandler):
    def post(self):
        eco_txt = self.request.get("edEco", "anonymous")
        usr = users.get_current_user()
        nick = "gosegan"

        if usr:
            nick = usr.nickname()
            # nick = usr.email()
            # nick = usr.user_id()
            # users.is_current_user_admin()


        # Guarder eco
        eco_dto = EcoDto(text=eco_txt, author=nick)
        eco_dto.put()
        time.sleep(1)

        # Recuparar todos los ecos
        lista_ecos = EcoDto.query().order(-EcoDto.hours)

        # Preparar pantilla
        jinja = jinja2.get_jinja2(app=self.app)
        sust = {
            'eco': eco_txt,
            'lista': ["Sociable", "Kind", "Hard-working", "Creative", "Advantage"],
            'lista_ecos': lista_ecos

        }
        self.response.write(
            jinja.render_template("requesta.html", **sust)
        )


app = webapp2.WSGIApplication([
    ('/do', DoHandler)
], debug=True)
