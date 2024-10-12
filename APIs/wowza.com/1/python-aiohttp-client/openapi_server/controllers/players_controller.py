from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_player_url200_response import CreatePlayerUrl200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.player_update_input import PlayerUpdateInput
from openapi_server.models.players import Players
from openapi_server.models.request_player_rebuild200_response import RequestPlayerRebuild200Response
from openapi_server.models.show_player200_response import ShowPlayer200Response
from openapi_server.models.show_player_state200_response import ShowPlayerState200Response
from openapi_server.models.url_create_input import UrlCreateInput
from openapi_server.models.url_update_input import UrlUpdateInput
from openapi_server.models.urls import Urls
from openapi_server import util


async def create_player_url(request: web.Request, player_id, url) -> web.Response:
    """Create a player URL

    This operation creates a new player URL.

    :param player_id: The unique alphanumeric string that identifies the player.
    :type player_id: str
    :param url: Provide the details of the player URL to create in the body of the request.
    :type url: dict | bytes

    """
    url = UrlCreateInput.from_dict(url)
    return web.Response(status=200)


async def delete_player_url(request: web.Request, player_id, id) -> web.Response:
    """Delete a player URL

    This operation deletes a player URL. 

    :param player_id: The unique alphanumeric string that identifies the player.
    :type player_id: str
    :param id: The unique alphanumeric string that identifies the player URL.
    :type id: str

    """
    return web.Response(status=200)


async def list_player_urls(request: web.Request, player_id) -> web.Response:
    """Fetch all player URLs

    This operation shows the details of all player URLs.

    :param player_id: The unique alphanumeric string that identifies the player.
    :type player_id: str

    """
    return web.Response(status=200)


async def list_players(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all players

    This operation shows the details of all of your players.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def request_player_rebuild(request: web.Request, id) -> web.Response:
    """Rebuild player code

    This operation rebuilds the player with the current configuration.

    :param id: The unique alphanumeric string that identifies the player.
    :type id: str

    """
    return web.Response(status=200)


async def show_player(request: web.Request, id) -> web.Response:
    """Fetch a player

    This operation shows details of a specific player.

    :param id: The unique alphanumeric string that identifies the player.
    :type id: str

    """
    return web.Response(status=200)


async def show_player_state(request: web.Request, id) -> web.Response:
    """Fetch the state of a player

    This operation shows the current state of a player.

    :param id: The unique alphanumeric string that identifies the player.
    :type id: str

    """
    return web.Response(status=200)


async def show_player_url(request: web.Request, player_id, id) -> web.Response:
    """Fetch a player URL

    This operation shows the details of a player URL.

    :param player_id: The unique alphanumeric string that identifies the player.
    :type player_id: str
    :param id: The unique alphanumeric string that identifies the player URL.
    :type id: str

    """
    return web.Response(status=200)


async def update_player(request: web.Request, id, player) -> web.Response:
    """Update a player

    This operation updates a player.

    :param id: The unique alphanumeric string that identifies the player.
    :type id: str
    :param player: Provide the details of the player to update in the body of the request.
    :type player: dict | bytes

    """
    player = PlayerUpdateInput.from_dict(player)
    return web.Response(status=200)


async def update_player_url(request: web.Request, player_id, id, url) -> web.Response:
    """Update a player URL

    This operation updates a player URL.

    :param player_id: The unique alphanumeric string that identifies the player.
    :type player_id: str
    :param id: The unique alphanumeric string that identifies the player URL.
    :type id: str
    :param url: Provide the details of the player URL to update in the body of the request.
    :type url: dict | bytes

    """
    url = UrlUpdateInput.from_dict(url)
    return web.Response(status=200)
