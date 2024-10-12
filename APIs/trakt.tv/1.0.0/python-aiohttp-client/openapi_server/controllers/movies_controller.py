from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_a_movie(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a movie

    #### &amp;#10024; Extended Info  Returns a single movie&#39;s details.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;released&#x60;, &#x60;in production&#x60;, &#x60;post production&#x60;, &#x60;planned&#x60;, &#x60;rumored&#x60;, or &#x60;canceled&#x60;.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_movie_aliases(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all movie aliases

    Returns all title aliases for a movie.  Includes country where name is different.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_movie_comments(request: web.Request, id, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all movie comments

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a movie. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

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


async def get_all_movie_releases(request: web.Request, id, country, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all movie releases

    Returns all releases for a movie including country, certification, release date, release type, and note. The release type can be set to &#x60;unknown&#x60;, &#x60;premiere&#x60;, &#x60;limited&#x60;, &#x60;theatrical&#x60;, &#x60;digital&#x60;, &#x60;physical&#x60;, or &#x60;tv&#x60;. The &#x60;note&#x60; might have optional info such as the film festival name for a &#x60;premiere&#x60; release or Blu-ray specs for a &#x60;physical&#x60; release. We pull this info from [TMDB](https://developers.themoviedb.org/3/movies/get-movie-release-dates).

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param country: 2 character country code
    :type country: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_movie_translations(request: web.Request, id, language, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all movie translations

    Returns all translations for a movie, including language and translated values for title, tagline and overview.

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


async def get_all_people_for_a_movie(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all people for a movie

    #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a movie. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_lists_containing_this_movie(request: web.Request, id, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get lists containing this movie

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this movie. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

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


async def get_movie_ratings(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movie ratings

    Returns rating (between 0 and 10) and distribution for a movie.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_movie_stats(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movie stats

    Returns lots of movie stats.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_movie_studios(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movie studios

    Returns all studios for a movie.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_popular_movies(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get popular movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular movies. Popularity is calculated using the rating percentage and the number of ratings.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_movie_trakt_ids(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated movie Trakt IDs

    #### &amp;#128196; Pagination  Returns all movie Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_updated_movies(request: web.Request, start_date, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all movies updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

    :param start_date: Updated since this date and time.
    :type start_date: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_related_movies(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get related movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar movies.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_anticipated_movies(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most anticipated movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated movies based on the number of lists a movie appears on.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_collected_movies(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most Collected movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_played_movies(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most played movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple times) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_recommended_movies(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most recommended movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_most_watched_movies(request: web.Request, period, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the most watched movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

    :param period: Time period.
    :type period: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_weekend_box_office(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the weekend box office

    #### &amp;#10024; Extended Info  Returns the top 10 grossing movies in the U.S. box office last weekend. Updated every Monday morning.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_trending_movies(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get trending movies

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies being watched right now. Movies with the most users are returned first.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_users_watching_right_now(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get users watching right now

    #### &amp;#10024; Extended Info  Returns all users watching this movie right now.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
