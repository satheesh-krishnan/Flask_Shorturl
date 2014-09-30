from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class foorms(Form):
    logi=TextField('logi',validators=[Required()])
   
