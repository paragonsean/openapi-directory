from typing import List, Dict
from aiohttp import web

from openapi_server.models.awarded_response import AwardedResponse
from openapi_server.models.badge import Badge
from openapi_server.models.error import Error
from openapi_server.models.user_badge import UserBadge
from openapi_server import util


async def offerings_offering_id_badges_get(request: web.Request, offering_id) -> web.Response:
    """Find offering badges

    Responds with the badge for an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_users_user_email_badges_award_post(request: web.Request, offering_id, user_email) -> web.Response:
    """Award badge

    Awards a badge to a user in the offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def users_user_email_badges_get(request: web.Request, user_email) -> web.Response:
    """Find user&#39;s badges

    Responds with all badges that the specified user has been awarded.

    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)
