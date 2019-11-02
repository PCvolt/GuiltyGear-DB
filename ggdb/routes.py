from flask import render_template, url_for, redirect, flash
from ggdb import app, db, bcrypt
from ggdb.forms import ComboForm
from ggdb.models import Combo

"""
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
		'meter': 0,
		'characters': 'sol johnny axl i-no',
		'comment': 'Basic combo.',
		'youtube_video': 'https://www.youtube.com/embed/oDQyQtZbwqY',
		'twitter_video': ''
	},
	{
		'character': 'jam',
		'standing': 'true',
		'crouching': 'true',
		'jumping': 'false',
		'midscreen': 'true',
		'nearcorner': 'true',
		'corner': 'true',
		'combo': '5K cS 5H(3) 6K 6H kicks',
		'damage': '~130',
		'meter': 0,
		'characters': 'everyone?',
		'comment': '',
		'youtube_video': '',
		'twitter_video': ''
	},
	{
		'character': 'jam',
		'standing': 'true',
		'crouching': 'false',
		'jumping': 'false',
		'midscreen': 'true',
		'nearcorner': 'true',
		'corner': 'true',
		'combo': 'fS.CH iad jPPKS 2H 46PK 236SSH',
		'damage': '~160',
		'meter': 0,
		'characters': 'sol chipp',
		'comment': 'I love this one. run 2S 2H 236236H on females.',
		'youtube_video': '',
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
		'meter': 0,
		'characters': 'ky may',
		'comment': 'Delay the tk until the cS animation ends.',
		'youtube_video': '',
		'twitter_video': 'https://twitter.com/nyphi7/status/1174728068629508096'
	},
]
"""

@app.route('/')
def index():
	combos = Combo.query.all()

	return render_template('index.html', posts=combos)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	form = ComboForm()
	if form.validate_on_submit():
		combo = Combo(character=form.character.data, combo=form.combo.data, meter=form.meter.data, damage=form.damage.data,
				standing=form.standing.data, crouching=form.crouching.data, jumping=form.jumping.data,
				midscreen=form.midscreen.data, nearcorner=form.nearcorner.data, corner=form.corner.data,
				comment=form.comment.data, videolink=form.videolink.data,
				sol=form.sol.data, ky=form.ky.data, may=form.may.data, millia=form.millia.data, zato1=form.zato1.data,
				potemkin=form.potemkin.data, chipp=form.chipp.data, faust=form.faust.data, axl=form.axl.data, venom=form.venom.data,
				slayer=form.slayer.data, ino=form.ino.data, bedman=form.bedman.data, ramlethal=form.ramlethal.data, sin=form.sin.data,
				elphelt=form.elphelt.data, leo=form.leo.data, johnny=form.johnny.data, jacko=form.jacko.data, jam=form.jam.data,
				kum=form.kum.data, raven=form.raven.data, dizzy=form.dizzy.data, baiken=form.baiken.data, answer=form.answer.data)

		db.session.add(combo)
		db.create_all()
		db.session.commit()
		flash(f'Combo added : {form.character.data} - {form.combo.data}', 'success')
		return redirect(url_for('index'))

	return render_template('submit.html', form=form)

