"""
Routing configuration.
"""

import tornado.web
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler
from handlers.index_handler import IndexHandler
from handlers.register_handler import RegisterHandler
from handlers.register.culdap_register_handler import CuLdapRegisterHandler
from handlers.dashboard_handler import DashboardHandler
from handlers.api.survey_handler import SurveyHandler
from handlers.api.response_handler import ResponseHandler
from handlers.refresh_handler import RefreshHandler
from handlers.user_info_handler import UserInfoHandler
from handlers.user_info_update_handler import UserInfoUpdateHandler
from handlers.api.me_handler import MeHandler


# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/register/culdap", CuLdapRegisterHandler),
    (r"/register", CuLdapRegisterHandler),
    (r"/dashboard", DashboardHandler),
    (r"/api/surveys", SurveyHandler),
    (r"/api/response", ResponseHandler),
    (r"/api/me", MeHandler),
    (r"/api/refresh", RefreshHandler),
    (r"/userinfo", UserInfoHandler),
    (r"/userinfo/update", UserInfoUpdateHandler)
]