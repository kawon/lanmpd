from django import forms
from django.forms import MultipleChoiceField as mcf
from django.forms import SelectMultiple



"""
	It would be nice to use a single place to define all our forms in,
	i propose we use this form.py (maybe change name to costum_forms.py....)
	!!
"""





"""
	this sucks, defing a class
	EVERYTIME this function is called, the problem:
	when defining playlist(form) we need to prepare a list of
	acceptable choices(mcf is somewhat the unfriendliest field for that matter)
	, with other fields we could just return an unbounded form
	and maybe bind data to it EVEN in the view itself,
	but as mentioned we need the data AT defining time :-/
"""

def generate_playlist(list_of_tuples):
	class playlist(forms.Form):
		list = mcf(list_of_tuples, widget=SelectMultiple(attrs={"size": 20}), label="")
	return playlist()
