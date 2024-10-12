from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_panelist import CreatedPanelist
from openapi_server.models.panelist import Panelist
from openapi_server.models.panelist_req_create import PanelistReqCreate
from openapi_server import util


async def create_panelists(request: web.Request, authorization, organizer_key, webinar_key, body) -> web.Response:
    """Create Panelists

    Create panelists for a specified webinar

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param body: Array of panelists
    :type body: list | bytes

    """
    body = [PanelistReqCreate.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_webinar_panelist(request: web.Request, authorization, organizer_key, webinar_key, panelist_key) -> web.Response:
    """Delete webinar panelist

    Removes a webinar panelist.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param panelist_key: The key of the webinar panelist
    :type panelist_key: int

    """
    return web.Response(status=200)


async def get_panelists(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get webinar panelists

    Retrieves all the panelists for a specific webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def resend_panelist_invitation(request: web.Request, authorization, organizer_key, webinar_key, panelist_key) -> web.Response:
    """Resend panelist invitation

    Resend the panelist invitation email.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param panelist_key: The key of the webinar panelist
    :type panelist_key: int

    """
    return web.Response(status=200)
