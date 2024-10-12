from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def qshow_delete(request: web.Request, id) -> web.Response:
    """qshow_delete

    Delete a qshow. 

    :param id: Qshow ID
    :type id: str

    """
    return web.Response(status=200)


async def qshow_get(request: web.Request, id) -> web.Response:
    """qshow_get

    Gets a details about a qshow. 

    :param id: Qshow ID
    :type id: str

    """
    return web.Response(status=200)


async def qshow_list_get(request: web.Request, start=None, public=None) -> web.Response:
    """qshow_list_get

    Get the list of Qshows in They Said So platform.

    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param public: Should include public qshows or not in the list
    :type public: bool

    """
    return web.Response(status=200)


async def qshow_patch(request: web.Request, id, title=None, description=None, tags=None) -> web.Response:
    """qshow_patch

    Update an existing qshow.

    :param id: Qshow ID
    :type id: str
    :param title: Qshow title
    :type title: str
    :param description: Qshow description
    :type description: str
    :param tags: Tags for the qshow
    :type tags: List[str]

    """
    return web.Response(status=200)


async def qshow_put(request: web.Request, title, description=None, tags=None) -> web.Response:
    """qshow_put

    Create and add a new qshow to your private collection.

    :param title: Qshow title
    :type title: str
    :param description: Qshow description
    :type description: str
    :param tags: Tags for the qshow
    :type tags: List[str]

    """
    return web.Response(status=200)


async def qshow_quotes_add_post(request: web.Request, id, quoteid) -> web.Response:
    """qshow_quotes_add_post

    Add a quote to a given Qshow.

    :param id: Qshow ID
    :type id: str
    :param quoteid: Quote ID to add the qshow collection
    :type quoteid: str

    """
    return web.Response(status=200)


async def qshow_quotes_get(request: web.Request, id) -> web.Response:
    """qshow_quotes_get

    Get the quotes in a given Qshow.

    :param id: Qshow ID
    :type id: str

    """
    return web.Response(status=200)


async def qshow_quotes_remove_post(request: web.Request, id, quoteid) -> web.Response:
    """qshow_quotes_remove_post

    Remove a quote to a given Qshow.

    :param id: Qshow ID
    :type id: str
    :param quoteid: Quote ID to remove from the qshow collection
    :type quoteid: str

    """
    return web.Response(status=200)
