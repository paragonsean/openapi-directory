from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.required_parameters_to_create_a_view import RequiredParametersToCreateAView
from openapi_server.models.view import View
from openapi_server import util


async def sessions_id_views_get(request: web.Request, session_id) -> web.Response:
    """Views: List Session Views

    Get data for all views in a session

    :param session_id: The primary key for a view session
    :type session_id: str
    :type session_id: str

    """
    return web.Response(status=200)


async def sessions_id_views_post(request: web.Request, session_id, body) -> web.Response:
    """Views: Create A Session View

    Create a page view object for a viewing session

    :param session_id: The primary key for a view session
    :type session_id: str
    :type session_id: str
    :param body: Collaborator user id and permission type
    :type body: dict | bytes

    """
    body = RequiredParametersToCreateAView.from_dict(body)
    return web.Response(status=200)


async def views_id_delete(request: web.Request, view_id) -> web.Response:
    """Views: Delete by Id

    Remove a view and dependant data.

    :param view_id: The primary key for a page view within a session
    :type view_id: str
    :type view_id: str

    """
    return web.Response(status=200)


async def views_id_get(request: web.Request, view_id) -> web.Response:
    """Views: Get View

    Get view meta data

    :param view_id: The primary key for a page view within a session
    :type view_id: str
    :type view_id: str

    """
    return web.Response(status=200)
