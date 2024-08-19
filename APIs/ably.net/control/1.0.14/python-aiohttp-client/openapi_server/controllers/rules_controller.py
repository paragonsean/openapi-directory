from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule_patch import RulePatch
from openapi_server.models.rule_post import RulePost
from openapi_server.models.rule_response import RuleResponse
from openapi_server import util


async def apps_app_id_rules_get(request: web.Request, app_id) -> web.Response:
    """Lists Reactor rules

    Lists the rules for the application specified by the application ID.

    :param app_id: The application ID.
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a Reactor rule

    Creates a rule for the application with the specified application ID.

    :param app_id: The application ID.
    :type app_id: str
    :param body: The rule properties.
    :type body: dict | bytes

    """
    body = RulePost.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_delete(request: web.Request, app_id, rule_id) -> web.Response:
    """Deletes a Reactor rule

    

    :param app_id: The application ID.
    :type app_id: str
    :param rule_id: The rule ID.
    :type rule_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_get(request: web.Request, app_id, rule_id) -> web.Response:
    """Gets a reactor rule by rule ID

    Returns the rule specified by the rule ID, for the application specified by application ID.

    :param app_id: The application ID.
    :type app_id: str
    :param rule_id: The rule ID.
    :type rule_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_patch(request: web.Request, app_id, rule_id, body=None) -> web.Response:
    """Updates a Reactor rule

    

    :param app_id: The application ID.
    :type app_id: str
    :param rule_id: The rule ID.
    :type rule_id: str
    :param body: Properties for the rule.
    :type body: dict | bytes

    """
    body = RulePatch.from_dict(body)
    return web.Response(status=200)
