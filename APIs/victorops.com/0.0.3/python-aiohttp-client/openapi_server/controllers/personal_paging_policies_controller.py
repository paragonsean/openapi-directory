from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_group_payload import AddGroupPayload
from openapi_server.models.add_step_payload import AddStepPayload
from openapi_server.models.api_public_v1_profile_username_policies_get200_response import ApiPublicV1ProfileUsernamePoliciesGet200Response
from openapi_server.models.api_public_v1_profile_username_policies_post200_response import ApiPublicV1ProfileUsernamePoliciesPost200Response
from openapi_server.models.api_public_v1_profile_username_policies_step_post200_response import ApiPublicV1ProfileUsernamePoliciesStepPost200Response
from openapi_server import util


async def api_public_v1_profile_username_policies_get(request: web.Request, username, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get the user&#39;s paging policy

    Get all the paging policy steps for the user on the org associated with the API key  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_post(request: web.Request, username, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Create a paging policy step

    Create a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddGroupPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_get(request: web.Request, username, step, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get a paging policy step

    Get a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_post(request: web.Request, username, step, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Create a rule for a paging policy step

    Create a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddStepPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_put(request: web.Request, username, step, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Update a paging policy step

    Update a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddGroupPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_rule_delete(request: web.Request, username, step, rule, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Delete a rule from a paging policy step

    Delete a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param rule: Rule for a paging policy step
    :type rule: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_rule_get(request: web.Request, username, step, rule, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get a rule from a paging policy step

    Get a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param rule: Rule for a paging policy step
    :type rule: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_profile_username_policies_step_rule_put(request: web.Request, username, step, rule, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Update a rule for a paging policy step

    Update a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

    :param username: Your username
    :type username: str
    :param step: Paging policy step
    :type step: 
    :param rule: Rule for a paging policy step
    :type rule: 
    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddStepPayload.from_dict(body)
    return web.Response(status=200)
