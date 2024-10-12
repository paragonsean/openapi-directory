from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_embed_preset_alt1_request import EditEmbedPresetAlt1Request
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.presets import Presets
from openapi_server import util


async def edit_embed_preset(request: web.Request, preset_id, user_id, body=None) -> web.Response:
    """Edit an embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditEmbedPresetAlt1Request.from_dict(body)
    return web.Response(status=200)


async def edit_embed_preset_alt1(request: web.Request, preset_id, body=None) -> web.Response:
    """Edit an embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditEmbedPresetAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_embed_preset(request: web.Request, preset_id, user_id) -> web.Response:
    """Get a specific embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_embed_preset_alt1(request: web.Request, preset_id) -> web.Response:
    """Get a specific embed preset

    

    :param preset_id: The ID of the preset.
    :type preset_id: 

    """
    return web.Response(status=200)


async def get_embed_presets(request: web.Request, user_id, page=None, per_page=None) -> web.Response:
    """Get all the embed presets that a user has created

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_embed_presets_alt1(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get all the embed presets that a user has created

    

    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
