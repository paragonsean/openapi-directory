from typing import List, Dict
from aiohttp import web

from openapi_server.models.podcast_audience_response import PodcastAudienceResponse
from openapi_server.models.podcast_domain_response import PodcastDomainResponse
from openapi_server import util


async def get_podcast_audience(request: web.Request, x_listen_api_key, id) -> web.Response:
    """Fetch audience demographics for a podcast

    Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Podcast id.
    :type id: str

    """
    return web.Response(status=200)


async def get_podcasts_by_domain_name(request: web.Request, x_listen_api_key, domain_name, page=None) -> web.Response:
    """Fetch podcasts by a publisher&#39;s domain name

    Fetch podcasts by a publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org... Each request will return up to 10 podcasts. You can use the &#x60;page&#x60; parameter to paginate. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param domain_name: A publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org...
    :type domain_name: str
    :param page: Page number of the podcasts from this domain name
    :type page: int

    """
    return web.Response(status=200)
