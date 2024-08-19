from typing import List, Dict
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.language import Language
from openapi_server.models.podcast import Podcast
from openapi_server.models.podcast_category import PodcastCategory
from openapi_server.models.podcast_episode import PodcastEpisode
from openapi_server.models.podcast_episode_list import PodcastEpisodeList
from openapi_server.models.podcast_search_params import PodcastSearchParams
from openapi_server.models.podcast_search_results import PodcastSearchResults
from openapi_server.models.station_genre import StationGenre
from openapi_server.models.station_list import StationList
from openapi_server.models.station_search_params import StationSearchParams
from openapi_server.models.station_search_results import StationSearchResults
from openapi_server import util


async def create_podcast(request: web.Request, file_logo, podcast) -> web.Response:
    """create_podcast

    Create podcast

    :param file_logo: 
    :type file_logo: str
    :param podcast: 
    :type podcast: dict | bytes

    """
    podcast = Podcast.from_dict(podcast)
    return web.Response(status=200)


async def create_podcast_episode(request: web.Request, podcast_key, episode, file_logo, file_media) -> web.Response:
    """create_podcast_episode

    Create podcast episode

    :param podcast_key: 
    :type podcast_key: str
    :param episode: 
    :type episode: dict | bytes
    :param file_logo: 
    :type file_logo: str
    :param file_media: 
    :type file_media: str

    """
    episode = PodcastEpisode.from_dict(episode)
    return web.Response(status=200)


async def delete_podcast(request: web.Request, podcast_key) -> web.Response:
    """delete_podcast

    Delete podcast

    :param podcast_key: 
    :type podcast_key: str

    """
    return web.Response(status=200)


async def delete_podcast1(request: web.Request, podcast_key, episode_key) -> web.Response:
    """delete_podcast1

    Delete podcast episode

    :param podcast_key: 
    :type podcast_key: str
    :param episode_key: 
    :type episode_key: str

    """
    return web.Response(status=200)


async def get_partner_aggregator_stations(request: web.Request, page=None, hits_per_page=None) -> web.Response:
    """get_partner_aggregator_stations

    List stations

    :param page: 
    :type page: str
    :param hits_per_page: 
    :type hits_per_page: str

    """
    return web.Response(status=200)


async def get_podcast(request: web.Request, podcast_key) -> web.Response:
    """get_podcast

    Get podcast

    :param podcast_key: 
    :type podcast_key: str

    """
    return web.Response(status=200)


async def get_podcast_categories(request: web.Request, ) -> web.Response:
    """get_podcast_categories

    Get the list of Categories that can be used to filter podcasts in the search podcasts request


    """
    return web.Response(status=200)


async def get_podcast_countries(request: web.Request, ) -> web.Response:
    """get_podcast_countries

    Get the list of Countries that can be used to filter podcasts in the search podcasts request


    """
    return web.Response(status=200)


async def get_podcast_episode(request: web.Request, podcast_key, episode_key) -> web.Response:
    """get_podcast_episode

    Get podcast episode

    :param podcast_key: 
    :type podcast_key: str
    :param episode_key: 
    :type episode_key: str

    """
    return web.Response(status=200)


async def get_podcast_episodes(request: web.Request, podcast_key, limit=None, offset=None) -> web.Response:
    """get_podcast_episodes

    Get podcast episodes

    :param podcast_key: 
    :type podcast_key: str
    :param limit: 
    :type limit: str
    :param offset: 
    :type offset: str

    """
    return web.Response(status=200)


async def get_podcast_languages(request: web.Request, ) -> web.Response:
    """get_podcast_languages

    Get the list of Languages that can be used to filter podcasts in the search podcasts request


    """
    return web.Response(status=200)


async def get_station_countries(request: web.Request, ) -> web.Response:
    """get_station_countries

    Get the list of Countries that can be used to filter stations in the search stations request


    """
    return web.Response(status=200)


async def get_station_genres(request: web.Request, ) -> web.Response:
    """get_station_genres

    Get the list of Genres that can be used to filter stations in the search stations request


    """
    return web.Response(status=200)


async def get_station_languages(request: web.Request, ) -> web.Response:
    """get_station_languages

    Get the list of Languages that can be used to filter stations in the search stations request


    """
    return web.Response(status=200)


async def search_podcasts(request: web.Request, body) -> web.Response:
    """search_podcasts

    Search podcasts

    :param body: 
    :type body: dict | bytes

    """
    body = PodcastSearchParams.from_dict(body)
    return web.Response(status=200)


async def search_stations(request: web.Request, body) -> web.Response:
    """search_stations

    Search stations

    :param body: 
    :type body: dict | bytes

    """
    body = StationSearchParams.from_dict(body)
    return web.Response(status=200)


async def update_podcast(request: web.Request, podcast_key, podcast, file_logo=None) -> web.Response:
    """update_podcast

    Update podcast

    :param podcast_key: 
    :type podcast_key: str
    :param podcast: 
    :type podcast: dict | bytes
    :param file_logo: 
    :type file_logo: str

    """
    podcast = Podcast.from_dict(podcast)
    return web.Response(status=200)


async def update_podcast_episode(request: web.Request, podcast_key, episode_key, episode, file_logo=None) -> web.Response:
    """update_podcast_episode

    Update podcast episode

    :param podcast_key: 
    :type podcast_key: str
    :param episode_key: 
    :type episode_key: str
    :param episode: 
    :type episode: dict | bytes
    :param file_logo: 
    :type file_logo: str

    """
    episode = PodcastEpisode.from_dict(episode)
    return web.Response(status=200)
