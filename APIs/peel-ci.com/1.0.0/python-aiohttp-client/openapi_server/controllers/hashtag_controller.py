from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_related_hashtags(request: web.Request, show_id, time_window=None) -> web.Response:
    """Gets related hashtags for a show.

    Returns any official hashtag and any hashtags which were learned within the most recent time window for the show.

    :param show_id: Unique ID for a show
    :type show_id: str
    :param time_window: Time window in seconds (default is 2 hours)
    :type time_window: str

    """
    return web.Response(status=200)


async def get_trending_shows(request: web.Request, limit=None, time_window=None) -> web.Response:
    """Gets trending shows.

    

    :param limit: Number of trending shows (default is 20)
    :type limit: str
    :param time_window: Time window in seconds (default is 2 hours)
    :type time_window: str

    """
    return web.Response(status=200)


async def get_tunein_links(request: web.Request, tweet=None, hashtags=None, show_id=None) -> web.Response:
    """Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID.

    Either use &lt;b&gt;tweet&lt;/b&gt;, &lt;b&gt;hashtags&lt;/b&gt;, or &lt;b&gt;showID&lt;/b&gt; as the parameter. The tunein URLs that match best are returned in order of best match.&lt;br/&gt;&lt;br/&gt;A &lt;b&gt;tweet&lt;/b&gt; in this context is shorthand for text from a social networking conversation, e.g., it could be from Facebook, Twitter, LinkedIn, etc., and be greater than 140 characters.

    :param tweet: Text from a social networking conversation
    :type tweet: str
    :param hashtags: Comma separated list of hashtags and @mentions
    :type hashtags: str
    :param show_id: Unique ID for a show
    :type show_id: str

    """
    return web.Response(status=200)
