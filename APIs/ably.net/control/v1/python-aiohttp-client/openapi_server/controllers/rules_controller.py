from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule_patch import RulePatch
from openapi_server.models.rule_post import RulePost
from openapi_server.models.rule_response import RuleResponse
from openapi_server import util


async def apps_app_id_rules_get(request: web.Request, app_id) -> web.Response:
    """Lists Integration rules

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a Integration Rule

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RulePost.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_delete(request: web.Request, app_id, rule_id) -> web.Response:
    """Deletes a Integration Rule

    

    :param app_id: 
    :type app_id: str
    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_get(request: web.Request, app_id, rule_id) -> web.Response:
    """Gets a Integration Rule by ID

    

    :param app_id: 
    :type app_id: str
    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def apps_app_id_rules_rule_id_patch(request: web.Request, app_id, rule_id, body=None) -> web.Response:
    """Updates a Integration Rule

    

    :param app_id: 
    :type app_id: str
    :param rule_id: 
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RulePatch.from_dict(body)
    return web.Response(status=200)
