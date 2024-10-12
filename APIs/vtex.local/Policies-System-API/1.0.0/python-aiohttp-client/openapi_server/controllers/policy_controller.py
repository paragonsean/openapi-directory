from typing import List, Dict
from aiohttp import web

from openapi_server.models.evaluate_policy_request import EvaluatePolicyRequest
from openapi_server.models.policy_action_get_response import PolicyActionGetResponse
from openapi_server.models.policy_get_response import PolicyGetResponse
from openapi_server.models.policy_save_request import PolicySaveRequest
from openapi_server import util


async def api_policy_engine_policies_id_put(request: web.Request, content_type, accept, id, body) -> web.Response:
    """Update Policy

    Updates an existing policy at your account.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param id: Policy ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PolicySaveRequest.from_dict(body)
    return web.Response(status=200)


async def policy_create_or_update(request: web.Request, content_type, accept, id, body=None) -> web.Response:
    """Create Policy

    Creates a new policy from scratch.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param id: Policy ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PolicySaveRequest.from_dict(body)
    return web.Response(status=200)


async def policy_delete(request: web.Request, content_type, accept, id) -> web.Response:
    """Delete Policy by ID

    Deletes a specific policy of the account by its ID.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param id: Policy ID
    :type id: str

    """
    return web.Response(status=200)


async def policy_evaluate(request: web.Request, content_type, accept, body) -> web.Response:
    """Evaluate Policies

    This endpoint consults all policies and checks the ones that satisfy the request body’s conditions.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = EvaluatePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policy_get(request: web.Request, content_type, accept, id) -> web.Response:
    """Get Policy by ID

    Retrieves general information of a policy by its ID.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param id: Policy ID
    :type id: str

    """
    return web.Response(status=200)


async def policy_list(request: web.Request, content_type, accept) -> web.Response:
    """Get Policy List

    Retrieves a list of all policies in the account and general information of each policy.

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str

    """
    return web.Response(status=200)
