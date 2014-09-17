# PyPostTumblr

Posts pictures that are in your directory on tumblr informed (need API Tumblr)

## Need Install 

PyTumblr (A Python Tumblr API v2 Client ) see -> https://github.com/jhoonb/pytumblr


### Example:

1) - Configure file config.json

```json
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
```

2) - upload photos and create posts

```python
from pyposttumblr import PyPostTumblr
p = PyPostTumblr() # or PyPostTumblr('your-config.json')
ids = p.create_photos() # add in your tumblr photos in dir "path_file"
```

3) - Delete posts

```python
from pyposttumblr import PyPostTumblr
p = PyPostTumblr() # or PyPostTumblr('your-config.json')
ids = p.create_photos() # add in your tumblr photos in dir "path_file"
p.delete_posts(ids) # delete posts param: list
```

See example: http://jhoonb.tumblr.com/post/97600066821/tutorial-pyposttumblr

:)
