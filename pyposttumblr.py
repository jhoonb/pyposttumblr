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
	see model config.json ou parameter conf:
	{
	"consumer_key" : "",
	"consumer_secret" : "",
	"oauth_token" : "",
	"oauth_secret" : "",
	"path_file" : "/path/",
	"blogname" : "<yourtumblr>.tumblr.com",
	"last_id_file" : <int: id incremental>,
	"caption" : "caption in post",
	"tags": ["tags1", "tags2"]
	}

	use:
	>>> from pyposttumblr import PyPostTumblr
	>>>
	>>> p = PyPostTumblr() # PyPostTumblr('your-config.json')
	>>> ids = p.create_photos() # add in your tumblr photos in dir "path_file"
	>>> p.delete_posts(ids) # delete posts param: list

	:) simple 

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

		# load files in dir
		self._get_files()

	def _get_files(self):
		"""
		Get list file name in dir
		"""
		self._listfiles = os.listdir(self._config['path_file'])
		self._listfiles = [i for i in self._listfiles if i.find(".") != -1]

	def create_photos(self):
		"""
		Create a photo post or photoset on a blog using
		methods .create_photo() from object TumblrRestClient
		Return list with id of post create 
		"""

		path_file_ok = self._config['path_file']
		id_post = []
		if self._config['tags'] == []:
			self._config['tags'] = ["tumblr"]

		for i in self._listfiles:

			ftags = []
			ftags.extend(self._config['tags'])
			ftags.append(str(self._id))

			if i.split('.')[1] == 'gif':
				ftags.append('gif')

			print("select img: {}".format(i))
			# api tumblr .create_photo
			resp = self._client.create_photo(self._config['blogname'],
				state='published',
				tags=ftags,
				data=path_file_ok+i,
				caption=self._config['caption'])

			print("response: {}".format(resp['id']))
			id_post.append(resp['id'])
			self._id += 1

		return id_post

	def delete_posts(self, id_list):
		"""
		delete post in <blogname>
		param: id_list list
		"""

		for k in id_list:
			resp = self._client.delete_post(self._config['blogname'], k)
			print("del id: {}".format(resp['id']))