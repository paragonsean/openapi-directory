from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.podcast_episode_list import PodcastEpisodeList
from openapi_server.models.podcast_list import PodcastList
from openapi_server.models.single_podcast import SinglePodcast
from openapi_server import util


async def podcasts_get(request: web.Request, page=None, page_size=None, order=None, filters=None) -> web.Response:
    """podcasts_get

    Get the list of all podcasts.

    :param page: Provide the page number to fetch.
    :type page: str
    :param page_size: Provide the size of the page to fetch.
    :type page_size: str
    :param order: Order the items by &#39;newest&#39; | &#39;random&#39;
    :type order: str
    :param filters: Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson));
    :type filters: str

    """
    return web.Response(status=200)


async def podcasts_podcast_id_episodes_get(request: web.Request, podcast_id, page=None, page_size=None, order=None, filters=None) -> web.Response:
    """podcasts_podcast_id_episodes_get

    Get a list of all episodes under a podcast.

    :param podcast_id: Unique qualifier for a podcast.
    :type podcast_id: str
    :param page: Provide the page number to fetch.
    :type page: str
    :param page_size: Provide the size of the page to fetch.
    :type page_size: str
    :param order: Order the items by &#39;newest&#39; | &#39;random&#39;
    :type order: str
    :param filters: Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson));
    :type filters: str

    """
    return web.Response(status=200)


async def podcasts_podcast_id_get(request: web.Request, podcast_id) -> web.Response:
    """podcasts_podcast_id_get

    Get a single Podcast.

    :param podcast_id: Unique qualifier for a podcast.
    :type podcast_id: str

    """
    return web.Response(status=200)
