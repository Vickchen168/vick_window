from flask import Blueprint

auth_blueprint=Blueprint('auth', __name__)

@auth_blueprint.route("/auth/")
def index():
    return "<h1>我是auth的首頁</h1>"


# simple_page = Blueprint('simple_page', __name__,
#                         template_folder='templates')

# @simple_page.route('/', defaults={'page': 'index'})
# @simple_page.route('/<page>')