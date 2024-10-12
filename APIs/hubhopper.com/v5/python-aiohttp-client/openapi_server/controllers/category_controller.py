from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_list import CategoryList
from openapi_server.models.podcast_list import PodcastList
from openapi_server.models.single_category import SingleCategory
from openapi_server import util


async def categories_category_id_get(request: web.Request, category_id) -> web.Response:
    """categories_category_id_get

    Get specific content category.

    :param category_id: Unique qualifier for a category.
    :type category_id: str

    """
    return web.Response(status=200)


async def categories_category_id_podcasts_get(request: web.Request, category_id, page=None, page_size=None, order=None, filters=None) -> web.Response:
    """categories_category_id_podcasts_get

    Get a list of all podcasts under a category.

    :param category_id: Unique qualifier for a category.
    :type category_id: str
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


async def categories_get(request: web.Request, page_size=None, page=None) -> web.Response:
    """categories_get

    Get the list of all content categories.

    :param page_size: Provide the size of the page to fetch.
    :type page_size: str
    :param page: Provide the page number to fetch.
    :type page: str

    """
    return web.Response(status=200)
