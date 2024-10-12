from typing import List, Dict
from aiohttp import web

from openapi_server.models.best_podcasts_response import BestPodcastsResponse
from openapi_server.models.curated_list_full import CuratedListFull
from openapi_server.models.episode_full import EpisodeFull
from openapi_server.models.episode_simple import EpisodeSimple
from openapi_server.models.get_curated_podcasts_response import GetCuratedPodcastsResponse
from openapi_server.models.get_episode_recommendations_response import GetEpisodeRecommendationsResponse
from openapi_server.models.get_episodes_in_batch_response import GetEpisodesInBatchResponse
from openapi_server.models.get_genres_response import GetGenresResponse
from openapi_server.models.get_languages_response import GetLanguagesResponse
from openapi_server.models.get_podcast_recommendations_response import GetPodcastRecommendationsResponse
from openapi_server.models.get_podcasts_in_batch_response import GetPodcastsInBatchResponse
from openapi_server.models.get_regions_response import GetRegionsResponse
from openapi_server.models.podcast_full import PodcastFull
from openapi_server import util


async def get_best_podcasts(request: web.Request, x_listen_api_key, genre_id=None, page=None, region=None, publisher_region=None, language=None, sort=None, safe_mode=None) -> web.Response:
    """Fetch a list of best podcasts by genre

    Get a list of curated best podcasts by genre, which are curated by Listen Notes staffs based on various signals from the Internet, e.g., top charts on other podcast platforms, recommendations from mainstream media, user activities on listennotes.com... You can get the genre ids from &#x60;GET /genres&#x60; endpoint. This endpoint returns same data as https://www.listennotes.com/best-podcasts/ 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param genre_id: You can get the id from &#x60;GET /genres&#x60;. If not specified, it&#39;ll be the overall best podcasts, which can be considered as a special genre.
    :type genre_id: str
    :param page: Page number of those podcasts in this genre.
    :type page: int
    :param region: Filter best podcasts by country/region. Please note that podcasts that are \&quot;best\&quot; in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in United States. 
    :type region: str
    :param publisher_region: Filter best podcasts by the publisher&#39;s country/region. This is to narrow down the results to include \&quot;best podcasts\&quot; produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; produced in any country/region. If you want to get a country/region&#39;s \&quot;best podcasts\&quot; that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., &#x60;region&#x3D;jp&#x60; and &#x60;publisher_region&#x3D;jp&#x60;. 
    :type publisher_region: str
    :param language: Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from &#x60;GET /languages&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in any language. 
    :type language: str
    :param sort: How do you want to sort these podcasts? If you&#39;d like to sort by popularity, please use **listen_score**. 
    :type sort: str
    :param safe_mode: Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    :type safe_mode: int

    """
    return web.Response(status=200)


async def get_curated_podcast_by_id(request: web.Request, x_listen_api_key, id) -> web.Response:
    """Fetch a curated list of podcasts by id

    Get detailed meta data of all podcasts in a specific curated list. This endpoint returns same data as https://www.listennotes.com/curated-podcasts/ 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: id for a specific curated list of podcasts. You can get the id from the response of &#x60;GET /search?type&#x3D;curated&#x60; or &#x60;GET /curated_podcasts&#x60;. 
    :type id: str

    """
    return web.Response(status=200)


async def get_curated_podcasts(request: web.Request, x_listen_api_key, page=None) -> web.Response:
    """Fetch curated lists of podcasts

    A bunch of curated lists from online media. For each list, you&#39;ll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use &#x60;GET /curated_podcasts/{id}&#x60;. We add new curated lists to the database on a daily basis. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param page: Page number of curated lists.
    :type page: int

    """
    return web.Response(status=200)


async def get_episode_by_id(request: web.Request, x_listen_api_key, id, show_transcript=None) -> web.Response:
    """Fetch detailed meta data for an episode by id

    Fetch detailed meta data for a specific episode.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: id for a specific episode. You can get episode id from using other endpoints, e.g., &#x60;GET /search&#x60;...
    :type id: str
    :param show_transcript: To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don&#39;t include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.
    :type show_transcript: int

    """
    return web.Response(status=200)


async def get_episode_recommendations(request: web.Request, x_listen_api_key, id, safe_mode=None) -> web.Response:
    """Fetch recommendations for an episode

    Fetch up to 8 episode recommendations based on the given episode id.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Episode id.
    :type id: str
    :param safe_mode: Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    :type safe_mode: int

    """
    return web.Response(status=200)


async def get_episodes_in_batch(request: web.Request, x_listen_api_key, ids) -> web.Response:
    """Batch fetch basic meta data for episodes

    Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use &#x60;GET /episodes/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param ids: Comma-separated list of episode ids.
    :type ids: str

    """
    return web.Response(status=200)


async def get_genres(request: web.Request, x_listen_api_key, top_level_only=None) -> web.Response:
    """Fetch a list of podcast genres

    Get a list of podcast genres that are supported in Listen Notes. The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre, e.g., &#x60;GET /best_podcasts&#x60;, &#x60;GET /search&#x60;... You may want to cache the list of genres on the client side. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param top_level_only: Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres. 
    :type top_level_only: int

    """
    return web.Response(status=200)


async def get_languages(request: web.Request, x_listen_api_key) -> web.Response:
    """Fetch a list of supported languages for podcasts

    Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in &#x60;GET /search&#x60;. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str

    """
    return web.Response(status=200)


async def get_podcast_by_id(request: web.Request, x_listen_api_key, id, next_episode_pub_date=None, sort=None) -> web.Response:
    """Fetch detailed meta data and episodes for a podcast by id

    Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time). You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;...
    :type id: str
    :param next_episode_pub_date: For episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter. 
    :type next_episode_pub_date: int
    :param sort: How do you want to sort the episodes of this podcast? 
    :type sort: str

    """
    return web.Response(status=200)


async def get_podcast_recommendations(request: web.Request, x_listen_api_key, id, safe_mode=None) -> web.Response:
    """Fetch recommendations for a podcast

    Fetch up to 8 podcast recommendations based on the given podcast id.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Podcast id.
    :type id: str
    :param safe_mode: Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    :type safe_mode: int

    """
    return web.Response(status=200)


async def get_podcasts_in_batch(request: web.Request, x_listen_api_key, ids=None, itunes_ids=None, next_episode_pub_date=None, rsses=None, show_latest_episodes=None, spotify_ids=None) -> web.Response:
    """Batch fetch basic meta data for podcasts

    Batch fetch basic meta data for up to 10 podcasts. This endpoint could be used to build something like OPML import, allowing users to import a bunch of podcasts via rss urls. For detailed meta data (including episodes) of an individual podcast, you need to use &#x60;GET /podcasts/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param ids: Comma-separated list of podcast ids.
    :type ids: str
    :param itunes_ids: Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419
    :type itunes_ids: str
    :param next_episode_pub_date: For latest episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes. 
    :type next_episode_pub_date: int
    :param rsses: Comma-separated rss urls.
    :type rsses: str
    :param show_latest_episodes: Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no. 
    :type show_latest_episodes: int
    :param spotify_ids: Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4
    :type spotify_ids: str

    """
    return web.Response(status=200)


async def get_regions(request: web.Request, x_listen_api_key) -> web.Response:
    """Fetch a list of supported countries/regions for best podcasts

    It returns a dictionary of country codes (e.g., us, gb...) &amp; country names (United States, United Kingdom...). The country code is used in the query parameter **region** of &#x60;GET /best_podcasts&#x60;. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str

    """
    return web.Response(status=200)


async def just_listen(request: web.Request, x_listen_api_key) -> web.Response:
    """Fetch a random podcast episode

    Recently published episodes are more likely to be fetched. Good luck!

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str

    """
    return web.Response(status=200)
