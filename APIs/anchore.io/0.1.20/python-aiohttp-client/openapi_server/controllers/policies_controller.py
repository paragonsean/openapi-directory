from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.policy_bundle import PolicyBundle
from openapi_server.models.policy_bundle_record import PolicyBundleRecord
from openapi_server import util


async def add_policy(request: web.Request, body, x_anchore_account=None) -> web.Response:
    """Add a new policy

    Adds a new policy bundle to the system

    :param body: 
    :type body: dict | bytes
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = PolicyBundle.from_dict(body)
    return web.Response(status=200)


async def delete_policy(request: web.Request, policy_id, x_anchore_account=None) -> web.Response:
    """Delete policy

    Delete the specified policy

    :param policy_id: 
    :type policy_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_policy(request: web.Request, policy_id, detail=None, x_anchore_account=None) -> web.Response:
    """Get specific policy

    Get the policy bundle content

    :param policy_id: 
    :type policy_id: str
    :param detail: Include policy bundle detail in the form of the full bundle content for each entry
    :type detail: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_policies(request: web.Request, detail=None, x_anchore_account=None) -> web.Response:
    """List policies

    List all saved policy bundles

    :param detail: Include policy bundle detail in the form of the full bundle content for each entry
    :type detail: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def update_policy(request: web.Request, policy_id, body, active=None, x_anchore_account=None) -> web.Response:
    """Update policy

    Update/replace and existing policy

    :param policy_id: 
    :type policy_id: str
    :param body: 
    :type body: dict | bytes
    :param active: Mark policy as active
    :type active: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = PolicyBundleRecord.from_dict(body)
    return web.Response(status=200)
