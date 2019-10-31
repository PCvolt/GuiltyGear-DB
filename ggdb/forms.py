from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, BooleanField, validators, SubmitField, SelectField, TextAreaField
from wtforms.validators import NumberRange, ValidationError, DataRequired, EqualTo, Length
from wtforms.widgets import TextArea


class ComboForm(FlaskForm):
	character 	= SelectField	('CHARACTER',
								choices=[('Sol', 'Sol'), ('Ky', 'Ky'), ('May', 'May'), ('Millia', 'Millia'), ('Zato-1', 'Zato-1'), ('Potemkin', 'Potemkin'), ('Chipp', 'Chipp'), ('Faust', 'Faust'),
								('Axl', 'Axl'), ('Venom', 'Venom'), ('Slayer', 'Slayer'), ('I-no', 'I-no'), ('Bedman', 'Bedman'), ('Ramlethal', 'Ramlethal'), ('Sin', 'Sin'), ('Elphelt', 'Elphelt'),
								('Leo', 'Leo'), ('Johnny', 'Johnny'), ('Jack-O', 'Jack-O'), ('Jam', 'Jam'), ('Kum', 'Kum'), ('Raven', 'Raven'), ('Dizzy', 'Dizzy'), ('Baiken', 'Baiken'), ('Answer', 'Answer')])
	combo 		= StringField	('COMBO', 		validators=[DataRequired(), Length(min=5)])
	meter 		= IntegerField	('METER', 		validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={"placeholder": "0-100"})
	damage 		= IntegerField	('DAMAGE', 		validators=[DataRequired(), NumberRange(min=0, max=420)], render_kw={"placeholder": "0-420"})
	standing 	= BooleanField	('Standing')
	crouching 	= BooleanField	('Crouching')
	jumping 	= BooleanField	('Jumping')
	midscreen 	= BooleanField	('Midscreen')
	nearcorner 	= BooleanField	('Nearcorner')
	corner 		= BooleanField	('Corner')
	comment 	= TextAreaField	('COMMENT', 	validators=[Length(max=2000)], widget=TextArea())
	videolink 	= StringField	('VIDEO LINK',	validators=[Length(max=200)], render_kw={"placeholder":"https://... (youtube, twitter, streamable)", "type":"url"})
	submit 		= SubmitField	('Submit combo!')

	sol 	= BooleanField('Sol')
	ky 		= BooleanField('Ky')
	may 	= BooleanField('May')
	millia 	= BooleanField('Millia')
	zato1 	= BooleanField('Zato-1')
	potemkin= BooleanField('Potemkin')
	chipp 	= BooleanField('Chipp')
	faust 	= BooleanField('Faust')
	axl 	= BooleanField('Axl')
	venom 	= BooleanField('Venom')
	slayer 	= BooleanField('Slayer')
	ino 	= BooleanField('I-no')
	bedman 	= BooleanField('Bedman')
	ramlethal= BooleanField('Ramlethal')
	sin 	= BooleanField('Sin')
	elphelt = BooleanField('Elphelt')
	leo 	= BooleanField('Leo')
	johnny 	= BooleanField('Johnny')
	jacko 	= BooleanField('Jack-o')
	jam 	= BooleanField('Jam')
	kum 	= BooleanField('Kum')
	raven 	= BooleanField('Raven')
	dizzy 	= BooleanField('Dizzy')
	baiken 	= BooleanField('Baiken')
	answer 	= BooleanField('Answer')