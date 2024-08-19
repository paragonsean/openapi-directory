from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_public_v1_overrides_get200_response import ApiPublicV1OverridesGet200Response
from openapi_server.models.api_public_v1_overrides_post200_response import ApiPublicV1OverridesPost200Response
from openapi_server.models.api_public_v1_overrides_public_id_get200_response import ApiPublicV1OverridesPublicIdGet200Response
from openapi_server.models.assignment import Assignment
from openapi_server.models.scheduled_override_payload import ScheduledOverridePayload
from openapi_server.models.update_assignment import UpdateAssignment
from openapi_server import util


async def api_public_v1_overrides_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """List the scheduled overrides

    List all the scheduled overrides on the organization  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_overrides_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Creates a new scheduled override

    Creates a new scheduled override. Start and end dates are in ISO8601 format. E.g. &#x60;2018-09-28&#39;T&#39;05:00:00Z&#x60;  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduledOverridePayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_assignments_get(request: web.Request, x_vo_api_id, x_vo_api_key, public_id) -> web.Response:
    """Get the specified scheduled override

    Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str

    """
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_assignments_policy_slug_delete(request: web.Request, x_vo_api_id, x_vo_api_key, public_id, policy_slug) -> web.Response:
    """Delete the scheduled override assignment

    Delete the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str
    :param policy_slug: The policySlug of the assignment
    :type policy_slug: str

    """
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_assignments_policy_slug_get(request: web.Request, x_vo_api_id, x_vo_api_key, public_id, policy_slug) -> web.Response:
    """Get the specified scheduled override assignment

    Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str
    :param policy_slug: The policySlug of the assignment
    :type policy_slug: str

    """
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_assignments_policy_slug_put(request: web.Request, x_vo_api_id, x_vo_api_key, public_id, policy_slug, body) -> web.Response:
    """Update the scheduled override assignment

    Update the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str
    :param policy_slug: The policySlug of the assignment
    :type policy_slug: str
    :param body: The policy and username we are assigning
    :type body: dict | bytes

    """
    body = UpdateAssignment.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_delete(request: web.Request, x_vo_api_id, x_vo_api_key, public_id) -> web.Response:
    """Deletes a scheduled override

    Deletes a scheduled override  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str

    """
    return web.Response(status=200)


async def api_public_v1_overrides_public_id_get(request: web.Request, x_vo_api_id, x_vo_api_key, public_id) -> web.Response:
    """Get the specified scheduled override

    Get the specified scheduled override  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param public_id: The publicId of the scheduled override
    :type public_id: str

    """
    return web.Response(status=200)
