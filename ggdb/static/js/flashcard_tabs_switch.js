function show_tab(current_elem, active_tab) {
	var n_flashcard = current_elem.closest("div.flashcard").id.slice(-1); 
	var tabs = ['combo_tab', 'desc_tab', 'chars_tab', 'video_tab'];
	flashcard = document.getElementById('flashcard_' + n_flashcard);

	for (var i = 0; i < tabs.length; ++i)
	{
		if (tabs[i] == active_tab)
		{
			flashcard.querySelector('div.' + active_tab).style.display = 'block';
		}
		else
		{
			flashcard.querySelector('div.' + tabs[i]).style.display = 'none';
		}
	}
}