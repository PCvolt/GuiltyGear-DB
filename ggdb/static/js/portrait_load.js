var portraits = document.getElementsByClassName('portrait'); //bleh

for (var i = 0; i < portraits.length; ++i)
	portraits[i].src = "/static/img/" + portraits[i].className.replace('portrait ','') + ".png";