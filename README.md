# `rss2twtxt`

Convert RSS feeds to TWTXT format.

## Usage

Copy `settings.py.skel` to `settings.py` and use the classes within.

To add a feed, supply a key to the `feeds` dictionary like so:

```python
feeds["twtxtfeed.txt"]=FeedClass(url,or_other_params)
```

3 feed classes are given for you:

1. `Feed` - just takes the description of the item and the pubdate. Base class to be subclassed.
2. `MastoFeed` - Given a server and a user from said server, will create a twtxt feed from their toots.
3. `LinkAndTitle` - Gives the link and the title of each item.

To subclass the `Feed` class, overwrite the `Feed._filter_item` method. If you return None or False, the feed item will be skipped. Otherwise, you should return a time and text.
