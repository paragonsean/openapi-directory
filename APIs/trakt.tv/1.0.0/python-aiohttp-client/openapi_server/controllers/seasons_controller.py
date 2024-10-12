from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_all_people_for_a_season(request: web.Request, id, season, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all people for a season

    #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a season, including the &#x60;episode_count&#x60; for which they appear. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions).. Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the season.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_season_comments(request: web.Request, id, season, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all season comments

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a season. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param sort: how to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_season_translations(request: web.Request, id, season, language, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all season translations

    Returns all translations for an season, including language and translated values for title and overview.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param language: 2 character language code
    :type language: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_seasons_for_a_show(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all seasons for a show

    #### &amp;#10024; Extended Info  Returns all seasons for a show including the number of episodes in each season.  #### Episodes  If you add &#x60;?extended&#x3D;episodes&#x60; to the URL, it will return all episodes for all seasons.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_lists_containing_this_season(request: web.Request, id, season, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get lists containing this season

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this season. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
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


async def get_season_ratings(request: web.Request, id, season, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get season ratings

    Returns rating (between 0 and 10) and distribution for a season.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_season_stats(request: web.Request, id, season, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get season stats

    Returns lots of season stats.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_single_season_for_a_show(request: web.Request, id, season, translations=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get single season for a show

    #### &amp;#10024; Extended Info  Returns all episodes for a specific season of a show.  #### Translations  If you&#39;d like to included translated episode titles and overviews in the response, include the &#x60;translations&#x60; parameter in the URL. Include all languages by setting the parameter to &#x60;all&#x60; or use a specific 2 digit country language code to further limit it.  **Note:** This returns a lot of data, so please only use this parameter if you actually need it!

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param translations: include episode translations
    :type translations: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def shows_id_seasons_season_watching_get(request: web.Request, id, season, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get users watching right now

    #### &amp;#10024; Extended Info  Returns all users watching this season right now.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param season: season number
    :type season: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
