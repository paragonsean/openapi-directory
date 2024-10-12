from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_a_single_show(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a single show

    #### &amp;#10024; Extended Info  Returns a single shows&#39;s details. If you request extended info, the &#x60;airs&#x60; object is relative to the show&#39;s country. You can use the &#x60;day&#x60;, &#x60;time&#x60;, and &#x60;timezone&#x60; to construct your own date then convert it to whatever timezone your user is in.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;returning series&#x60; (airing right now),  &#x60;continuing&#x60; (airing right now), &#x60;in production&#x60; (airing soon), &#x60;planned&#x60; (in development), &#x60;upcoming&#x60; (in development),  &#x60;pilot&#x60;, &#x60;canceled&#x60;, or &#x60;ended&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_people_for_a_show(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all people for a show

    #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a show, including the &#x60;episode_count&#x60; for which they appears. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, &#x60;editing&#x60;, and &#x60;created  by&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the show.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_show_aliases(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all show aliases

    Returns all title aliases for a show.  Includes country where name is different.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_show_certifications(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all show certifications

    Returns all content certifications for a show, including the country.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_show_comments(request: web.Request, id, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all show comments

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a show. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param sort: how to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_show_translations(request: web.Request, id, language, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all show translations

    Returns all translations for a show, including language and translated values for title and overview.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param language: 2 character language code
    :type language: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_last_episode(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get last episode

    #### &amp;#10024; Extended Info  Returns the most recently aired episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_lists_containing_this_show(request: web.Request, id, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get lists containing this show

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this show. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

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


async def get_next_episode(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get next episode

    #### &amp;#10024; Extended Info  Returns the next scheduled to air episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_popular_shows(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get popular shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular shows. Popularity is calculated using the rating percentage and the number of ratings.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_show_trakt_ids(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated show Trakt IDs

    #### &amp;#128196; Pagination  Returns all show Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_shows(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all shows updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_related_shows(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get related shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar shows.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_collection_progress(request: web.Request, id, body, hidden=None, specials=None, count_specials=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show collection progress

    #### &amp;#128274; OAuth Required  Returns collection progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should collect, if there are no upcoming episodes it will be set to &#x60;null&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has collected, even if they&#39;ve collected older episodes more recently. To use their last collected episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;collected&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param body: 
    :type body: str
    :param hidden: include any hidden seasons
    :type hidden: str
    :param specials: include specials as season 0
    :type specials: str
    :param count_specials: count specials in the overall stats (only applies if specials are included)
    :type count_specials: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_ratings(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show ratings

    Returns rating (between 0 and 10) and distribution for a show.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_stats(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show stats

    Returns lots of show stats.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_studios(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show studios

    Returns all studios for a show.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_watched_progress(request: web.Request, id, body, hidden=None, specials=None, count_specials=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show watched progress

    #### &amp;#128274; OAuth Required  Returns watched progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should watch, if there are no upcoming episodes it will be set to &#x60;null&#x60;. If not &#x60;null&#x60;, the &#x60;reset_at&#x60; date is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has watched, even if they&#39;ve watched older episodes more recently. To use their last watched episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;watched&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param body: 
    :type body: str
    :param hidden: include any hidden seasons
    :type hidden: str
    :param specials: include specials as season 0
    :type specials: str
    :param count_specials: count specials in the overall stats (only applies if specials are included)
    :type count_specials: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_anticipated_shows(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most anticipated shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated shows based on the number of lists a show appears on.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_collected_shows(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most collected shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_played_shows(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most played shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple episodes multiple times) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_recommended_shows(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most recommended shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_watched_shows(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most watched shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_trending_shows(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get trending shows

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows being watched right now. Shows with the most users are returned first.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def reset_show_progress(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Reset show progress

    #### &amp;#128274; OAuth Required 🔥 VIP Only  Reset a show&#39;s progress when the user started re-watching the show. You can optionally specify the &#x60;reset_at&#x60; date to have it calculate progress from that specific date onwards.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def shows_id_watching_get(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get users watching right now

    #### &amp;#10024; Extended Info  Returns all users watching this show right now.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def undo_reset_show_progress(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Undo reset show progress

    #### &amp;#128274; OAuth Required 🔥 VIP Only  Undo the reset and have watched progress use all watched history for the show.

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
