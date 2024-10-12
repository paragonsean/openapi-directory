from typing import List, Dict
from aiohttp import web

from openapi_server.models.assessment_group_required import AssessmentGroupRequired
from openapi_server.models.assessment_group_response import AssessmentGroupResponse
from openapi_server.models.error import Error
from openapi_server.models.offerings_offering_id_groups_group_id_learners_post_request import OfferingsOfferingIdGroupsGroupIdLearnersPostRequest
from openapi_server.models.user_response import UserResponse
from openapi_server import util


async def offerings_offering_id_groups_get(request: web.Request, offering_id) -> web.Response:
    """Find assessment groups

    Responds with a list of assessment groups in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_groups_group_id_learners_get(request: web.Request, offering_id, group_id) -> web.Response:
    """Find learners in an assessment group

    Responds with a list of learners in a specified assessment group.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param group_id: Assessment group id
    :type group_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_groups_group_id_learners_post(request: web.Request, offering_id, group_id, body) -> web.Response:
    """Add a learner to an assessment group

    Adds a learner into the specified assessment group.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param group_id: Assessment group id
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OfferingsOfferingIdGroupsGroupIdLearnersPostRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_groups_group_id_learners_user_email_delete(request: web.Request, offering_id, group_id, user_email) -> web.Response:
    """Remove a learner from an assessment group

    Removes a learner from the specified assessment group.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param group_id: Assessment group id
    :type group_id: str
    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def offerings_offering_id_groups_post(request: web.Request, offering_id, body) -> web.Response:
    """Add an assessment group

    Creates a new assessment group in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssessmentGroupRequired.from_dict(body)
    return web.Response(status=200)
