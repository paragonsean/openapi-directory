from typing import List, Dict
from aiohttp import web

from openapi_server.models.episode_object import EpisodeObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_episodes200_response import GetMultipleEpisodes200Response
from openapi_server.models.paging_saved_episode_object import PagingSavedEpisodeObject
from openapi_server.models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from openapi_server.models.remove_episodes_user_request import RemoveEpisodesUserRequest
from openapi_server.models.save_episodes_user_request import SaveEpisodesUserRequest
from openapi_server import util


async def check_users_saved_episodes(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Episodes 

    Check if one or more episodes is already saved in the current Spotify user&#39;s &#39;Your Episodes&#39; library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_a_shows_episodes_0(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
    """Get Show Episodes 

    Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_an_episode(request: web.Request, id, market=None) -> web.Response:
    """Get Episode 

    Get Spotify catalog information for a single episode identified by its unique Spotify ID. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_multiple_episodes(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Episodes 

    Get Spotify catalog information for several episodes based on their Spotify IDs. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_users_saved_episodes(request: web.Request, market=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Episodes 

    Get a list of the episodes saved in the current Spotify user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def remove_episodes_user(request: web.Request, ids, body=None) -> web.Response:
    """Remove User&#39;s Saved Episodes 

    Remove one or more episodes from the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveEpisodesUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_episodes_user(request: web.Request, ids, body=None) -> web.Response:
    """Save Episodes for Current User 

    Save one or more episodes to the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveEpisodesUserRequest.from_dict(body)
    return web.Response(status=200)
