/**
 * Highlights the portraits of each character on which the combo is effective.
 */

var list_chars = ['sol', 'ky', 'may', 'millia', 'zato1', 'potemkin', 'chipp', 'faust', 'axl', 'venom', 'slayer', 'ino', 'bedman', 'ramlethal', 'sin', 'elphelt', 'leo', 'johnny', 'jacko', 'jam', 'kum', 'raven', 'dizzy', 'baiken', 'answer'];
var chars_tab_subdiv = document.getElementsByClassName('thumbnails');	

for (var i = 0; i < chars_tab_subdiv.length; i++)
{
	// Get the array of classes for each flashcard 
	var post_characters = chars_tab_subdiv[i].className.split(" ");

	// We create the portraits img on the fly
	var displayed_chars = 0;
	for (var j = 0; j < list_chars.length; j++)
	{
		++displayed_chars;
		// Simple display formatting
		if (displayed_chars % 9 == 8)
			chars_tab_subdiv[i].appendChild(document.createElement('br'));

		var img = document.createElement("img");
		img.width = "50";
		img.src = "/static/img/" + list_chars[j] + ".png";

		//If the current character has its associated array[index] as False, they will be darkened
		if (post_characters[j+1] == "False")
			img.className = "darken";

		if (img.classList.contains("darken"))
			img.style.filter = "brightness(0.25)";

		// Append the created image to the div "thumbnails"
		chars_tab_subdiv[i].appendChild(img);
	}
}