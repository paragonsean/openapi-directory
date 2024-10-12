from typing import List, Dict
from aiohttp import web

from openapi_server.models.podcast_minimum_rss import PodcastMinimumRss
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE
from openapi_server import util


async def podcast_deleted_post(request: web.Request, podcast_minimum_rss=None) -> web.Response:
    """podcast_deleted_post

    

    :param podcast_minimum_rss: Triggered by your request to DELETE /podcasts/{id}, if the podcast is actually deleted.
    :type podcast_minimum_rss: dict | bytes

    """
    podcast_minimum_rss = PodcastMinimumRss.from_dict(podcast_minimum_rss)
    return web.Response(status=200)


async def podcasts_submit_accepted_post(request: web.Request, podcast_minimum_rss=None) -> web.Response:
    """podcasts_submit_accepted_post

    

    :param podcast_minimum_rss: Triggered by your request to POST /podcasts/submit, if the podcast submission is accepted.
    :type podcast_minimum_rss: dict | bytes

    """
    podcast_minimum_rss = PodcastMinimumRss.from_dict(podcast_minimum_rss)
    return web.Response(status=200)


async def podcasts_submit_rejected_post(request: web.Request, unknown_base_type=None) -> web.Response:
    """podcasts_submit_rejected_post

    

    :param unknown_base_type: Triggered by your request to POST /podcasts/submit, if the podcast submission is rejected.
    :type unknown_base_type: dict | bytes

    """
    unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(unknown_base_type)
    return web.Response(status=200)
