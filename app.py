from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

combos = [
	{
		'character': 'sin',
		'standing': 'true',
		'crouching': 'true',
		'jumping': 'false',
		'midscreen': 'true',
		'nearcorner': 'true',
		'corner': 'true',
		'combo': '2K cS 2D',
		'damage': '~70',
		'resources': '0kcal',
		'meter': 0,
		'characters': 'sol johnny axl i-no',
		'comment': 'Basic combo.',
		'youtube_video': 'https://www.youtube.com/embed/oDQyQtZbwqY',
		'twitter_video': ''
	},
	{
		'character': 'sin',
		'standing': 'false',
		'crouching': 'false',
		'jumping': 'true',
		'midscreen': 'true',
		'nearcorner': 'true',
		'corner': 'false',
		'combo': '6P cS 5H 6H j8 jS j6H j236236P 66 214S 214K j6H cS 5H 214H',
		'damage': '~200',
		'resources': '3kcal',
		'meter': 50,
		'characters': 'sol ky may millia zato-1 potemkin chipp faust axl venom slayer i-no bedman ramlethal sin elphelt leo johnny jack-o jam kum raven dizzy baiken answer',
		'comment': 'Tu autem, Fanni, quod mihi tantum tribui dicis quantum ego nec adgnosco nec postulo, facis amice; sed, ut mihi videris, non recte iudicas de Catone; aut enim nemo, quod quidem magis credo, aut si quisquam, ille sapiens fuit. Quo modo, ut alia omittam, mortem filii tulit! memineram Paulum, videram Galum, sed hi in pueris, Cato in perfecto et spectato viro. Iam in altera philosophiae parte. quae est quaerendi ac disserendi, quae logikh dicitur, iste vester plane, ut mihi quidem videtur, inermis ac nudus est. tollit definitiones, nihil de dividendo ac partiendo docet, non quo modo efficiatur concludaturque ratio tradit, non qua via captiosa solvantur ambigua distinguantur ostendit; iudicia rerum in sensibus ponit, quibus si semel aliquid falsi pro vero probatum sit, sublatum esse omne iudicium veri et falsi putat. Nec minus feminae quoque calamitatum participes fuere similium. nam ex hoc quoque sexu peremptae sunt originis altae conplures, adulteriorum flagitiis obnoxiae vel stuprorum. inter quas notiores fuere Claritas et Flaviana, quarum altera cum duceretur ad mortem, indumento, quo vestita erat, abrepto, ne velemen quidem secreto membrorum sufficiens retinere permissa est. ideoque carnifex nefas admisisse convictus inmane, vivus exustus est. At nunc si ad aliquem bene nummatum tumentemque ideo honestus advena salutatum introieris, primitus tamquam exoptatus suscipieris et interrogatus multa coactusque mentiri, miraberis numquam antea visus summatem virum tenuem te sic enixius observantem, ut paeniteat ob haec bona tamquam praecipua non vidisse ante decennium Romam. Quis enim aut eum diligat quem metuat, aut eum a quo se metui putet? Coluntur tamen simulatione dumtaxat ad tempus. Quod si forte, ut fit plerumque, ceciderunt, tum intellegitur quam fuerint inopes amicorum. Quod Tarquinium dixisse ferunt, tum exsulantem se intellexisse quos fidos amicos habuisset, quos infidos, cum iam neutris gratiam referre posset.',
		'youtube_video': '',
		'twitter_video': ''
	},
	{
		'character': 'sin',
		'standing': 'true',
		'crouching': 'true',
		'jumping': 'false',
		'midscreen': 'false',
		'nearcorner': 'true',
		'corner': 'true',
		'combo': '2K 2D 236K 623S 214S 236[H] 66 5D(6) 2P 3K 236[H] 214H 2D 236H RRC 66 5H 632146H 6H 6H into run very far in the far west',
		'damage': '~200',
		'resources': '8kcal',
		'meter': 50,
		'characters': 'not checked',
		'comment': 'Unstable',
		'youtube_video': '',
		'twitter_video': ''
	},
	{
		'character': 'sol',
		'standing': 'true',
		'crouching': 'true',
		'jumping': 'false',
		'midscreen': 'true',
		'nearcorner': 'true',
		'corner': 'true',
		'combo': '66 cS tk.623S cS 2H j9 jD jD 41236H 66 236P 2D 236K',
		'damage': '~220',
		'resources': '⠀', #INVISIBLE CHARACTER !
		'meter': 0,
		'characters': 'ky may',
		'comment': 'Delay the tk until the cS animation ends.',
		'youtube_video': '',
		'twitter_video': 'https://twitter.com/nyphi7/status/1174728068629508096'
	},
]


@app.route('/')
def index():
	return render_template('index.html', posts=combos)

@app.route('/submit')
def submit():
	return render_template('submit.html')

# 5P, 2P, 4P, 3P, 6P,
# 5K, 2K, 3K, 6K
# cS, fS, 2S
# 5H, 2H, 3H, 6H
# 5D, 2D, 4D
# jP, jK, jS, jH, jD, j6P, j6K, j2K, j2S, j2H

# 236P/K/S/H/D
# 46PP, 46PK


# 236236P, 236236K

#Redimension stances picture so they are already 70*70 or smtg