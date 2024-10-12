from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.player import Player
from openapi_server.models.player_creation_payload import PlayerCreationPayload
from openapi_server.models.player_update_payload import PlayerUpdatePayload
from openapi_server.models.players_list_response import PlayersListResponse
from openapi_server import util


async def d_elete_players_player_id(request: web.Request, player_id) -> web.Response:
    """Delete a player

    Delete a player if you no longer need it. You can delete any player that you have the player ID for.

    :param player_id: The unique identifier for the player you want to delete.
    :type player_id: str

    """
    return web.Response(status=200)


async def d_elete_players_player_id_logo(request: web.Request, player_id) -> web.Response:
    """Delete logo

    

    :param player_id: The unique identifier for the player.
    :type player_id: str

    """
    return web.Response(status=200)


async def g_et_players(request: web.Request, sort_by=None, sort_order=None, current_page=None, page_size=None) -> web.Response:
    """List all players

    Retrieve a list of all the players you created, as well as details about each one. Tutorials that use the [player endpoint](https://api.video/blog/endpoints/player).

    :param sort_by: createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format.
    :type sort_by: str
    :param sort_order: Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones.
    :type sort_order: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_players_player_id(request: web.Request, player_id) -> web.Response:
    """Show a player

    Use a player ID to retrieve details about the player and display it for viewers.

    :param player_id: The unique identifier for the player you want to retrieve. 
    :type player_id: str

    """
    return web.Response(status=200)


async def p_atch_players_player_id(request: web.Request, player_id, body) -> web.Response:
    """Update a player

    Use a player ID to update specific details for a player. NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

    :param player_id: The unique identifier for the player.
    :type player_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlayerUpdatePayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_players(request: web.Request, body) -> web.Response:
    """Create a player

    Create a player for your video, and customise it.

    :param body: 
    :type body: dict | bytes

    """
    body = PlayerCreationPayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_players_player_id_logo(request: web.Request, player_id, file, link) -> web.Response:
    """Upload a logo

    The uploaded image maximum size should be 200x100 and its weight should be 200KB.  It will be scaled down to 30px height and converted to PNG to be displayed in the player.

    :param player_id: The unique identifier for the player.
    :type player_id: str
    :param file: The name of the file you want to use for your logo.
    :type file: str
    :param link: The path to the file you want to upload and use as a logo.
    :type link: str

    """
    return web.Response(status=200)
