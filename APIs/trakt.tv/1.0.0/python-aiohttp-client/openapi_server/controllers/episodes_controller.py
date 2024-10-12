from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_a_single_episode_for_a_show(request: web.Request, id, season, episode, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a single episode for a show

    #### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_episode_comments(request: web.Request, id, season, episode, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all episode comments

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param sort: how to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_episode_translations(request: web.Request, id, season, episode, language, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all episode translations

    Returns all translations for an episode, including language and translated values for title and overview.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param language: 2 character language code
    :type language: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_people_for_an_episode(request: web.Request, id, season, episode, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all people for an episode

    #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_episode_ratings(request: web.Request, id, season, episode, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get episode ratings

    Returns rating (between 0 and 10) and distribution for an episode.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_episode_stats(request: web.Request, id, season, episode, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get episode stats

    Returns lots of episode stats.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_lists_containing_this_episode(request: web.Request, id, season, episode, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get lists containing this episode

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param type: Filter for a specific list type
    :type type: str
    :param sort: How to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def shows_id_seasons_season_episodes_episode_watching_get(request: web.Request, id, season, episode, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get users watching right now

    #### &amp;#10024; Extended Info  Returns all users watching this episode right now.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param episode: episode number
    :type episode: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
