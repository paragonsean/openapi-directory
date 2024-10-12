from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering_user import OfferingUser
from openapi_server.models.offering_user_add_response import OfferingUserAddResponse
from openapi_server.models.offering_user_response import OfferingUserResponse
from openapi_server.models.offerings_offering_id_users_post207_response_inner import OfferingsOfferingIdUsersPost207ResponseInner
from openapi_server.models.transfer_request import TransferRequest
from openapi_server import util


async def offerings_offering_id_users_get(request: web.Request, offering_id, facilitators=None, learners=None, markers=None) -> web.Response:
    """Find offering&#39;s users

    Responds with a list of users in the offering (facilitators, learners and markers.).

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param facilitators: If true, facilitators are included in the results.
    :type facilitators: str
    :param learners: If true, learners are included in the results.
    :type learners: str
    :param markers: If true, markers are included in the results.
    :type markers: str

    """
    return web.Response(status=200)


async def offerings_offering_id_users_marker_email_marks_delete(request: web.Request, offering_id, marker_email, body) -> web.Response:
    """Remove learners from coach&#39;s marking list

    Removes an array of learners from coach&#39;s marking list.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param marker_email: marker&#39;s email
    :type marker_email: str
    :param body: array of learners e-mails
    :type body: List[str]

    """
    return web.Response(status=200)


async def offerings_offering_id_users_marker_email_marks_get(request: web.Request, offering_id, marker_email) -> web.Response:
    """Find Learners marked by a coach

    Responds with all learners marked by the specified coach.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param marker_email: marker&#39;s email
    :type marker_email: str

    """
    return web.Response(status=200)


async def offerings_offering_id_users_marker_email_marks_post(request: web.Request, offering_id, marker_email, body) -> web.Response:
    """Add learners to be marked by a coach

    Adds an array of learners to be marked by the specified coach.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param marker_email: marker&#39;s email
    :type marker_email: str
    :param body: array of learners e-mails
    :type body: List[str]

    """
    return web.Response(status=200)


async def offerings_offering_id_users_post(request: web.Request, offering_id, body) -> web.Response:
    """Adds user to the offering

    Adds one or more users to the offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [OfferingUser.from_dict(d) for d in body]
    return web.Response(status=200)


async def offerings_offering_id_users_user_email_delete(request: web.Request, offering_id, user_email) -> web.Response:
    """Removes user from the offering

    Removes a user from the offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def users_user_email_transfer_patch(request: web.Request, user_email, body) -> web.Response:
    """Transfer a user between offerings

    Moves the user&#39;s access and progress from one offering to another.

    :param user_email: user&#39;s email
    :type user_email: str
    :param body: transfer_data
    :type body: dict | bytes

    """
    body = TransferRequest.from_dict(body)
    return web.Response(status=200)
