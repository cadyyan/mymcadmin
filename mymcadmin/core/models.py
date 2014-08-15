from django.contrib.auth import models as auth_models
from django.core          import urlresolvers as django_urlresolvers
from django.db           import models as django_models

import os.path

# TODO: require permissions

class Server(django_models.Model):
	"""
	A Minecraft server
	"""

	class Meta:
		permissions = (
			('grant',  'Grant permissions'),
			('launch', 'Start/Stop/Restart the server'),
		)

	"""
	The name of the server
	"""
	name  = django_models.CharField(max_length = 32, unique = True)

	"""
	The user that created the server
	"""
	owner = django_models.ForeignKey(auth_models.User)

	"""
	The path to the server on the file system
	"""
	path  = django_models.FilePathField(allow_files = False, allow_folders = True, unique = True)

	@property
	def settings_file(self):
		"""
		Get the path to the settings file.
		"""

		return os.path.join(self.path, 'mcserver.settings')

	def get_absolute_url(self):
		return django_urlresolvers.reverse('server-view', args = [str(self.id)])

