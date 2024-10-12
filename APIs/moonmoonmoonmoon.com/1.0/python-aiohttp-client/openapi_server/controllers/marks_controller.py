from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def marks_hashtags(request: web.Request, tag=None) -> web.Response:
    """Fetches popular hashtags or marks tagged with specified hashtag

    Search for specified tag (no pound sign necessary). If &lt;b&gt;tag&lt;/b&gt; is empty, the 50 most popular hashtags will be returned.

    :param tag: Hashtag to search for
    :type tag: str

    """
    return web.Response(status=200)


async def marks_index(request: web.Request, before=None, popular=None, last_popular_id=None, featured=None, x=None, y=None, user=None, collection=None) -> web.Response:
    """Fetches marks

    The main method for querying the marks database. You may use the following options:         &lt;ol style&#x3D;&#39;list-style-type: lower-roman;&#39;&gt;         &lt;li&gt;No parameters to retrieve all marks in descending chronological order (use &lt;b&gt;before&lt;/b&gt; for pagination)&lt;/li&gt;         &lt;li&gt;&lt;b&gt;popular&lt;/b&gt; (and optionally &lt;b&gt;last_popular_id&lt;/b&gt;) to retrieve all popular marks&lt;/li&gt;         &lt;li&gt;&lt;b&gt;featured&lt;/b&gt; to retrieve all featured marks&lt;/li&gt;         &lt;li&gt;&lt;b&gt;x &amp; y&lt;/b&gt; to retrieve mark at specific coordinate&lt;/li&gt;         &lt;li&gt;&lt;b&gt;user&lt;/b&gt; to retrieve all marks created by the specified user&lt;/li&gt;         &lt;li&gt;&lt;b&gt;collection&lt;/b&gt; to retrieve all marks collected by the specified user&lt;/li&gt;         &lt;/ol&gt;

    :param before: Before ID (pagination purposes)
    :type before: str
    :param popular: Popular marks
    :type popular: bool
    :param last_popular_id: Last popular ID (for pagination purposes)
    :type last_popular_id: str
    :param featured: Featured marks
    :type featured: bool
    :param x: X coordinate
    :type x: int
    :param y: Y coordinate
    :type y: int
    :param user: Created by user ID
    :type user: str
    :param collection: Collection ID
    :type collection: str

    """
    return web.Response(status=200)
