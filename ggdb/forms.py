from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, BooleanField, validators, SubmitField, SelectField, TextAreaField
from wtforms.validators import NumberRange, ValidationError, DataRequired, EqualTo, Length
from wtforms.widgets import TextArea


class ComboForm(FlaskForm):
	character 	= SelectField	('CHARACTER',
								choices=[('sol', 'Sol'), ('ky', 'Ky'), ('may', 'May'), ('millia', 'Millia'), ('zato-1', 'Zato-1'), ('potemkin', 'Potemkin'), ('chipp', 'Chipp'), ('faust', 'Faust'),
								('axl', 'Axl'), ('venom', 'Venom'), ('slayer', 'Slayer'), ('ino', 'I-no'), ('bedman', 'Bedman'), ('ramlethal', 'Ramlethal'), ('sin', 'Sin'), ('elphelt', 'Elphelt'),
								('leo', 'Leo'), ('johnny', 'Johnny'), ('jacko', 'Jack-O'), ('jam', 'Jam'), ('kum', 'Kum'), ('raven', 'Raven'), ('dizzy', 'Dizzy'), ('baiken', 'Baiken'), ('answer', 'Answer')])
	combo 		= StringField	('COMBO', 		validators=[DataRequired(), Length(min=5, max=300)])
	meter 		= IntegerField	('METER', 		validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={"placeholder": "0-100"}) #buggy, can't receive 0 as an input
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