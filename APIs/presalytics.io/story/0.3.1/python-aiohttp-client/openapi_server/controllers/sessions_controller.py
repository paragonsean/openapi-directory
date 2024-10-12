from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_session_request import CreateSessionRequest
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.session import Session
from openapi_server import util


async def session_id_delete(request: web.Request, session_id) -> web.Response:
    """Sessions: Delete by Id

    Remove a session and dependant data.

    :param session_id: The primary key for a view session
    :type session_id: str
    :type session_id: str

    """
    return web.Response(status=200)


async def session_id_get(request: web.Request, session_id, include_relationships=None) -> web.Response:
    """Sessions: Get

    Get session metadata

    :param session_id: The primary key for a view session
    :type session_id: str
    :type session_id: str
    :param include_relationships: Indicate whether the returned object should include child relationships
    :type include_relationships: bool

    """
    return web.Response(status=200)


async def story_id_session_post(request: web.Request, id, body) -> web.Response:
    """Sessions: Create a Session

    Create a new session

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: Collaborator user id and permission type
    :type body: dict | bytes

    """
    body = CreateSessionRequest.from_dict(body)
    return web.Response(status=200)


async def story_id_sessions_get(request: web.Request, id, include_relationships=None) -> web.Response:
    """Sessions: List Story Sessions

    Get a list of sessions asscoaited with this story

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param include_relationships: Indicate whether the returned object should include child relationships
    :type include_relationships: bool

    """
    return web.Response(status=200)
