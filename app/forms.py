from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    img = FileField('Image File', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])