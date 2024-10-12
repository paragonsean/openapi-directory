from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.apply_to_resources_request import ApplyToResourcesRequest
from openapi_server.models.remove_from_resources_request import RemoveFromResourcesRequest
from openapi_server.models.set_rules_request import SetRulesRequest
from openapi_server import util


async def firewalls_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Firewall

    Returns a specific Action for a Firewall.

    :param id: ID of the Firewall
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def firewalls_id_actions_apply_to_resources_post(request: web.Request, id, body=None) -> web.Response:
    """Apply to Resources

    Applies one Firewall to multiple resources.  Currently servers (public network interface) and label selectors are supported.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_already_applied&#x60;    | Firewall was already applied on resource                      | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

    :param id: ID of the Firewall
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApplyToResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def firewalls_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Firewall

    Returns all Action objects for a Firewall. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Resource
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def firewalls_id_actions_remove_from_resources_post(request: web.Request, id, body=None) -> web.Response:
    """Remove from Resources

    Removes one Firewall from multiple resources.  Currently only Servers (and their public network interfaces) are supported.  #### Call specific error codes  | Code                                  | Description                                                            | |---------------------------------------|------------------------------------------------------------------------| | &#x60;firewall_already_removed&#x60;            | Firewall was already removed from the resource                         | | &#x60;firewall_resource_not_found&#x60;         | The resource the Firewall should be attached to was not found          | | &#x60;firewall_managed_by_label_selector&#x60;  | Firewall was applied via label selector and cannot be removed manually | 

    :param id: ID of the Firewall
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveFromResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def firewalls_id_actions_set_rules_post(request: web.Request, id, body=None) -> web.Response:
    """Set Rules

    Sets the rules of a Firewall.  All existing rules will be overwritten. Pass an empty &#x60;rules&#x60; array to remove all rules. The maximum amount of rules that can be defined is 50.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

    :param id: ID of the Firewall
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SetRulesRequest.from_dict(body)
    return web.Response(status=200)
