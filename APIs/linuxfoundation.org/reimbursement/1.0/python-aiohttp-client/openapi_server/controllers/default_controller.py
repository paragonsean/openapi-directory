from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.health import Health
from openapi_server.models.policy_reset_input import PolicyResetInput
from openapi_server.models.policy_tag_input import PolicyTagInput
from openapi_server import util


async def expense_action(request: web.Request, action, report_id) -> web.Response:
    """Expense Action

    approves or rejects expense report

    :param action: 
    :type action: str
    :param report_id: 
    :type report_id: str

    """
    return web.Response(status=200)


async def health_check(request: web.Request, ) -> web.Response:
    """Get API Health Status

    


    """
    return web.Response(status=200)


async def reset_policy(request: web.Request, body) -> web.Response:
    """Reset Policy

    Reset an existing policy to match with templatePolicy

    :param body: 
    :type body: dict | bytes

    """
    body = PolicyResetInput.from_dict(body)
    return web.Response(status=200)


async def tag_policy(request: web.Request, body) -> web.Response:
    """Tag Policy

    Tag adds a tag to the policy

    :param body: 
    :type body: dict | bytes

    """
    body = PolicyTagInput.from_dict(body)
    return web.Response(status=200)
