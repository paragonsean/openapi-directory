from typing import List, Dict
from aiohttp import web

from openapi_server.models.podcast_episode_index import PodcastEpisodeIndex
from openapi_server import util


async def get_podcast_episodes(request: web.Request, page=None, per_page=None, username=None) -> web.Response:
    """Podcast Episodes

    This endpoint allows the client to retrieve a list of podcast episodes.         \&quot;Podcast episodes\&quot; are episodes belonging to podcasts.         It will only return active (reachable) podcast episodes that belong to published podcasts available on the platform, ordered by descending publication date.         It supports pagination, each page will contain 30 articles by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int
    :param username: Using this parameter will retrieve episodes belonging to a specific podcast.
    :type username: str

    """
    return web.Response(status=200)
