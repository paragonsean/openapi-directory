from typing import List, Dict
from aiohttp import web

from openapi_server.models.image import Image
from openapi_server.models.images_post_request import ImagesPostRequest
from openapi_server.models.import_session import ImportSession
from openapi_server import util


async def import_sessions_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """import_sessions_get

    Returns a list of available import sessions.

    :param startindex: start index of returned slice of import sessions
    :type startindex: int
    :param count: size of returned slice of import sessions
    :type count: int

    """
    return web.Response(status=200)


async def import_sessions_id_delete(request: web.Request, id) -> web.Response:
    """import_sessions_id_delete

    deletes the import session with the supplied ID

    :param id: ID of import session to delete
    :type id: int

    """
    return web.Response(status=200)


async def import_sessions_id_get(request: web.Request, id) -> web.Response:
    """import_sessions_id_get

    Returns the import sessions with the supplied ID

    :param id: ID of session
    :type id: int

    """
    return web.Response(status=200)


async def import_sessions_id_images_get(request: web.Request, id) -> web.Response:
    """import_sessions_id_images_get

    get the imported images corresponding to the import session with the supplied ID

    :param id: ID of import session
    :type id: int

    """
    return web.Response(status=200)


async def import_sessions_id_images_post(request: web.Request, id, body) -> web.Response:
    """import_sessions_id_images_post

    add a DICOM dataset to the import session with the supplied ID

    :param id: ID of session
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ImagesPostRequest.from_dict(body)
    return web.Response(status=200)


async def import_sessions_post(request: web.Request, import_session) -> web.Response:
    """import_sessions_post

    create a new import sessions

    :param import_session: The import session to create containing the user defined name of the session
    :type import_session: dict | bytes

    """
    import_session = ImportSession.from_dict(import_session)
    return web.Response(status=200)
