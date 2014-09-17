# PyPostTumblr

Posts pictures that are in your directory on tumblr informed (need API Tumblr)

## Need Install 

PyTumblr (A Python Tumblr API v2 Client ) see -> https://github.com/jhoonb/pytumblr


### Example:

1) - Configure file config.json

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
