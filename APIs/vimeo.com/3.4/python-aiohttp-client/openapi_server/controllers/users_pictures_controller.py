from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_picture_alt1_request import EditPictureAlt1Request
from openapi_server.models.picture import Picture
from openapi_server import util


async def create_picture(request: web.Request, user_id) -> web.Response:
    """Add a user picture

    

    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def create_picture_alt1(request: web.Request, ) -> web.Response:
    """Add a user picture

    


    """
    return web.Response(status=200)


async def delete_picture(request: web.Request, portraitset_id, user_id) -> web.Response:
    """Delete a user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def delete_picture_alt1(request: web.Request, portraitset_id) -> web.Response:
    """Delete a user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 

    """
    return web.Response(status=200)


async def edit_picture(request: web.Request, portraitset_id, user_id, body=None) -> web.Response:
    """Edit a user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditPictureAlt1Request.from_dict(body)
    return web.Response(status=200)


async def edit_picture_alt1(request: web.Request, portraitset_id, body=None) -> web.Response:
    """Edit a user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditPictureAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_picture(request: web.Request, portraitset_id, user_id) -> web.Response:
    """Get a specific user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_picture_alt1(request: web.Request, portraitset_id) -> web.Response:
    """Get a specific user picture

    

    :param portraitset_id: The ID of the picture.
    :type portraitset_id: 

    """
    return web.Response(status=200)


async def get_pictures(request: web.Request, user_id, page=None, per_page=None) -> web.Response:
    """Get all the pictures that belong to a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_pictures_alt1(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get all the pictures that belong to a user

    

    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
