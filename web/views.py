from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from os.path import basename
import forms
from mpd import CommandError, MPDClient


def index(request):
	return render_to_response('index.html', {})



def unauth(request):
	logout(request)
	return HttpResponseRedirect('/web/')


def change_song(request):
		"""
			As stated in player() (beyond)
			we atm have no way of saving an mpdclient instance
			read player() for more info

			TODO:
			+ change to POST, from GET?
		"""		


		client=MPDClient()
		client.connect("localhost", 6600)
		try:
			client.play(request.GET["list"])
			#general problem, someone deletes the song you want to
			# swtich playback to --> worst case:catch command error
		except CommandError:
			pass
		
		return HttpResponseRedirect("/web/player/")



def player(request):
	if request.user.is_authenticated():
		"""if "client" in session:
			client=request.session["client"]
		   else:
			client = MPDClient()
			request.session["client"] = client
		-------------------------------------------
			This does not work, as expected, pickeling such a complex object(with a connection maybe)
			raises problems, at this point it looks like we would have to create a new client object
			per page request :-(
			Unless django has a persistent object storage of some kind,
			and allows us to reference this object from the Session :-/
			When we do find a Solution for this, its simply a matter of creating the object
			if a user without one arrives or to retrieve the object if a user already has one,
			that said, we would have something like the outcommented code above, and replace
			the next 2 lines with it!



			TODO:
			+ playback
			+ search function
			+ browse inteface(?, js maybe?)
			+ maybe change to POST instead of GET?
			+ mounting your shares (should not be done on the player view!)
		"""
		## For now create a new instace everytime
		client = MPDClient()
		client.connect("localhost", 6600)
		# we should make a settings.py or some thing
		# so we can do: from settings import server, port
		list_data=[]
		index=0
		for path in client.playlist():
			list_data.append((index, basename(path)))
			index=index+1

		client = None


		perms = request.user.get_all_permissions()
		playback = False
		add = False
		rem = False
		if u'playback' in perms or request.user.is_superuser:
			playback = True
		elif u'add' in perms or request.user.is_superuser:
			add = True
		elif u'rem' in perms or request.user.is_superuser:
			rem = True
				
		
		playlist_form = forms.generate_playlist(list_data)



		return render_to_response('player.html', {'playback': playback, 'add': add, 
							 'del': rem, 'playlist': playlist_form})
	else:
		return HttpResponseRedirect('/web/')
