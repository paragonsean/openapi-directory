from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_podcast_response import DeletePodcastResponse
from openapi_server.models.submit_podcast_response import SubmitPodcastResponse
from openapi_server import util


async def delete_podcast_by_id(request: web.Request, x_listen_api_key, id, reason=None) -> web.Response:
    """Request to delete a podcast

    Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the \&quot;status\&quot; field in the response will be \&quot;deleted\&quot;. Otherwise, the status field will be \&quot;in review\&quot;. If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;...
    :type id: str
    :param reason: The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put \&quot;testing\&quot; here to indicate that you are testing this endpoint, so we will not actually delete the podcast.
    :type reason: str

    """
    return web.Response(status=200)


async def submit_podcast(request: web.Request, x_listen_api_key, rss, email=None) -> web.Response:
    """Submit a podcast to Listen Notes database

    Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn&#39;t exist in the database, \&quot;status\&quot; in the response will be \&quot;in review\&quot;, and we&#39;ll review it within 12 hours. If the podcast exists, \&quot;status\&quot; in the response will be \&quot;found\&quot;. If this submission is rejected, \&quot;status\&quot; in the response will be \&quot;rejected\&quot;. You can use &#x60;POST /podcasts&#x60; to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the \&quot;email\&quot; parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param rss: A valid podcast rss url.
    :type rss: str
    :param email: A valid email address. If **email** is specified, then we&#39;ll notify this email address once the podcast is accepted.
    :type email: str

    """
    return web.Response(status=200)
