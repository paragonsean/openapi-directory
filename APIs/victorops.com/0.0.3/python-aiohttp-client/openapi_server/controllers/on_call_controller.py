from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_public_v1_oncall_current_get200_response import ApiPublicV1OncallCurrentGet200Response
from openapi_server.models.on_call_and_overrides import OnCallAndOverrides
from openapi_server.models.take_request import TakeRequest
from openapi_server.models.take_result import TakeResult
from openapi_server.models.team_schedule import TeamSchedule
from openapi_server.models.user_schedule import UserSchedule
from openapi_server import util


async def api_public_v1_oncall_current_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get an organization&#39;s on-call users

    Get all on-call users/teams for your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_policies_policy_oncall_user_patch(request: web.Request, x_vo_api_id, x_vo_api_key, policy, body) -> web.Response:
    """Create an on-call override (take on-call)

    Replaces a currently on-call user in the escalation policy with another.  In many cases, the policy slug will match the slug of the team that contains it.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param policy: The VictorOps policy &#39;slug&#39;
    :type policy: str
    :param body: The take on-call payload
    :type body: dict | bytes

    """
    body = TakeRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_team_team_oncall_schedule_get(request: web.Request, x_vo_api_id, x_vo_api_key, team, days_forward=None, days_skip=None, step=None) -> web.Response:
    """Get a team&#39;s on-call schedule

    __NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/team/{team}/oncall/schedule&#x60;.__  Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team &#39;slug&#39;
    :type team: str
    :param days_forward: Days to include in returned schedule (30 max)
    :type days_forward: 
    :param days_skip: Days to skip before computing schedule to return (90 max)
    :type days_skip: 
    :param step: Step of escalation policy (3 max)
    :type step: 

    """
    return web.Response(status=200)


async def api_public_v1_team_team_oncall_user_patch(request: web.Request, x_vo_api_id, x_vo_api_key, team, body) -> web.Response:
    """Create an on-call override (take on-call)

    __NOTE: This API call is deprecated. Please use &#x60;PATCH /api-public/v2/policies/{policy}/oncall/user&#x60;__  Replaces a currently on-call user on the team with another.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team &#39;slug&#39;
    :type team: str
    :param body: The take on-call payload
    :type body: dict | bytes

    """
    body = TakeRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_oncall_schedule_get(request: web.Request, x_vo_api_id, x_vo_api_key, user, days_forward=None, days_skip=None, step=None) -> web.Response:
    """Get a user&#39;s on-call schedule

    __NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/user/{user}/oncall/schedule&#x60;.__  Get the on-call schedule for a user for all teams, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param days_forward: Days to include in returned schedule (30 max)
    :type days_forward: 
    :param days_skip: Days to skip before computing schedule to return (90 max)
    :type days_skip: 
    :param step: Step of escalation policy (3 max)
    :type step: 

    """
    return web.Response(status=200)


async def api_public_v2_team_team_oncall_schedule_get(request: web.Request, x_vo_api_id, x_vo_api_key, team, days_forward=None, days_skip=None, step=None) -> web.Response:
    """Get a team&#39;s on-call schedule

    Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team &#39;slug&#39;
    :type team: str
    :param days_forward: Days to include in returned schedule (30 max)
    :type days_forward: 
    :param days_skip: Days to skip before computing schedule to return (90 max)
    :type days_skip: 
    :param step: Step of escalation policy (3 max)
    :type step: 

    """
    return web.Response(status=200)


async def api_public_v2_user_user_oncall_schedule_get(request: web.Request, x_vo_api_id, x_vo_api_key, user, days_forward=None, days_skip=None, step=None) -> web.Response:
    """Get a user&#39;s on-call schedule

    Get the on-call schedule for a user for all teams the user is on, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param days_forward: Days to include in returned schedule (30 max)
    :type days_forward: 
    :param days_skip: Days to skip before computing schedule to return (90 max)
    :type days_skip: 
    :param step: Step of escalation policy (3 max)
    :type step: 

    """
    return web.Response(status=200)
