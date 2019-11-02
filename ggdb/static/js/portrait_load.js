/**
 * Load the portrait of the character dealing the combo.
 */

var portraits = document.getElementsByClassName('portrait'); 

for (var i = 0; i < portraits.length; ++i)
	portraits[i].src = "/static/img/" + portraits[i].className.replace('portrait ','') + ".png";