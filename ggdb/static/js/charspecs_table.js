/* 	We retrieve each thumbnails class (table of charspecs).
	For each existing character we create their picture.
	If the combo works on a character, his class is "bright".
	If the img class is not "bright", we darken the picture.
*/
var list_chars = ['sol', 'ky', 'may', 'millia', 'zato1', 'potemkin', 'chipp', 'faust', 'axl', 'venom', 'slayer', 'ino', 'bedman', 'ramlethal', 'sin', 'elphelt', 'leo', 'johnny', 'jacko', 'jam', 'kum', 'raven', 'dizzy', 'baiken', 'answer'];
var chars_tab_subdiv = document.getElementsByClassName('thumbnails');
for (var i = 0; i < chars_tab_subdiv.length; i++)
{
	var post_characters = chars_tab_subdiv[i].classList;
	
	var displayed_chars = 0;
	for (var j = 0; j < list_chars.length; j++)
	{
		++displayed_chars;
		if (displayed_chars % 9 == 8)
			chars_tab_subdiv[i].appendChild(document.createElement('br'));


		var img = document.createElement("img");
		img.width = "50";
		img.src = "/static/img/" + list_chars[j] + ".png";

		for (var k = 1; k < post_characters.length; k++)
			if (post_characters[k] == list_chars[j])
				img.className = "bright";

		if (!img.classList.contains("bright"))
			img.style.filter = "brightness(0.25)";


		chars_tab_subdiv[i].appendChild(img);
	}
}