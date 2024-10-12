from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_a_single_person(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a single person

    #### &amp;#10024; Extended Info  Returns a single person&#39;s details.  #### Gender  If available, the &#x60;gender&#x60; property will be set to &#x60;male&#x60;, &#x60;female&#x60;, or &#x60;non_binary&#x60;.  #### Known For Department  If available, the &#x60;known_for_department&#x60; property will be set to &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, or &#x60;editing&#x60;. Many people have credits across departments, &#x60;known_for&#x60; allows you to select their default credits more accurately.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_lists_containing_this_person(request: web.Request, id, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get lists containing this person

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this person. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
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


async def get_movie_credits(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movie credits

    #### &amp;#10024; Extended Info  Returns all movies where this person is in the &#x60;cast&#x60; or &#x60;crew&#x60;. Each &#x60;cast&#x60; object will have a &#x60;characters&#x60; array and a standard &#x60;movie&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;movie&#x60; object.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_people(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated people

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all people updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_people_trakt_ids(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated people Trakt IDs

    #### &amp;#128196; Pagination  Returns all people Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_credits(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show credits

    #### &amp;#10024; Extended Info  Returns all shows where this person is in the &#x60;cast&#x60; or &#x60;crew&#x60;, including the &#x60;episode_count&#x60; for which they appear. Each &#x60;cast&#x60; object will have a &#x60;characters&#x60; array and a standard &#x60;show&#x60; object. If &#x60;series_regular&#x60; is &#x60;true&#x60;, this person is a series regular and not simply a guest star.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, &#x60;editing&#x60;, and &#x60;created  by&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;show&#x60; object.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
