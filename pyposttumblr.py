# -*- coding: utf-8 -*-

"""
 pyposttumblr.py
 jhoonb.com | jpbanczek@gmail.com
 2014
"""

import pytumblr
import json
import os


class PyPostTumblr(object):
	"""
	PyPostTumblr:
	posts pictures that are in your directory on tumblr informed
	see config.json ou parameter conf:
	{
	"consumer_key" : "",
	"consumer_secret" : "",
	"oauth_token" : "",
	"oauth_secret" : "",
	"path_file" : "/path/",
	"blogname" : "<yourtumblr>.tumblr.com",
	"last_id_file" : <int: id incremental>,
	"caption" : "caption in post"
	}
	"""

	def __init__(self, conf=""):
		"""
		Initializes the PyPostTumblr object
		"""

		if conf == "":
			conf = 'config.json'
		
		with open(conf) as data_file:
			self._config = json.load(data_file)
		
		# last id
		self._id = int(self._config['last_id_file']) + 1
		# list photo in dir
		self._listfiles = None

		# object from pytumblr
		self._client = pytumblr.TumblrRestClient(
			self._config['consumer_key'],
			self._config['consumer_secret'],
			self._config['oauth_token'],
			self._config['oauth_secret'],
			)


	def _get_files(self):
		"""
		Get list file name in dir
		"""
		self._listfiles = os.listdir(self._config['path_file'])
		self._listfiles = [i for i in self._listfiles if i.find(".") != -1]


	def _post_photo(self):
		"""
		Create a photo post or photoset on a blog using
		methods .create_photo() from object TumblrRestClient
		"""

		# check list
		check = []
		path_file_ok = self._config['path_file']
		ftags = []

		for i in self._listfiles:
			if i not in check:
				check.append(i)
				ftags.append(str(self._id))
				if i.split('.')[1] == 'gif':
					ftags.append('gif')
				
				print("select img: ", i)
				# api tumblr .create_photo
				ok = self._client.create_photo(self._config['blogname'],
					state='published',
					tags=ftags,
					data=path_file_ok+i,
					caption=self._config['caption'])

				print("response: ", ok)
					
				# reset
				ftags = []
				self._id += 1


	def run(self):
		"""
		run actions
		"""

		self._get_files()
		self._post_photo()


if __name__== '__main__':

	# pypost = PyPostTumblr('other-file-config.json')
	pypost = PyPostTumblr()
	pypost.run()