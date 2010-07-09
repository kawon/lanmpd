from django.db import models

# Create your models here.



class MPDperms(models.Model):

    class Meta:
        permissions = (
            ("playback", "Can control playback"), 
	    # In the future, playback will be split into more perms
            ("add", "Can add songs"),
            ("del", "Can remove songs")
        )

