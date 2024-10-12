from typing import List, Dict
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_note_controller_note_request import API2ControllersWebAPINoteControllerNoteRequest
from openapi_server.models.big_oven_model_api2_recipe_note import BigOvenModelAPI2RecipeNote
from openapi_server.models.big_oven_model_api_recipe_note import BigOvenModelAPIRecipeNote
from openapi_server.models.big_oven_model_api_recipe_note_list import BigOvenModelAPIRecipeNoteList
from openapi_server import util


async def note_delete(request: web.Request, recipe_id, note_id) -> web.Response:
    """Delete a review                  do a DELETE Http request of /note/{ID}

    

    :param recipe_id: recipeId (int)
    :type recipe_id: int
    :param note_id: noteId (int)
    :type note_id: int

    """
    return web.Response(status=200)


async def note_get(request: web.Request, recipe_id, note_id) -> web.Response:
    """Get a given note. Make sure you&#39;re passing authentication information in the header for the user who owns the note.

    

    :param recipe_id: recipe identifier (integer)
    :type recipe_id: int
    :param note_id: The note ID (note -- it&#39;s not the RecipeID)
    :type note_id: int

    """
    return web.Response(status=200)


async def note_get_notes(request: web.Request, recipe_id, pg=None, rpp=None) -> web.Response:
    """recipe/100/notes

    

    :param recipe_id: recipeId (int)
    :type recipe_id: int
    :param pg: page (int, starting from 1)
    :type pg: int
    :param rpp: recipeId
    :type rpp: int

    """
    return web.Response(status=200)


async def note_post(request: web.Request, recipe_id, body) -> web.Response:
    """HTTP POST a new note into the system.

    

    :param recipe_id: recipeId (int)
    :type recipe_id: int
    :param body: a recipe note, with fields: Date (YYYY-MM-DD string), Notes (string), People (string), Variations (string), RecipeID (int?)
    :type body: dict | bytes

    """
    body = API2ControllersWebAPINoteControllerNoteRequest.from_dict(body)
    return web.Response(status=200)


async def note_put(request: web.Request, recipe_id, note_id, body) -> web.Response:
    """HTTP PUT (update) a Recipe note (RecipeNote).

    

    :param recipe_id: 
    :type recipe_id: int
    :param note_id: 
    :type note_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPINoteControllerNoteRequest.from_dict(body)
    return web.Response(status=200)
