from flask import request, Blueprint

account = Blueprint('account', __name__)

@account.route('/register', methond=['post'])
@db_session

