from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_rule_request import CreateRuleRequest
from openapi_server.models.rule import Rule
from openapi_server.models.rule_execution_reportings import RuleExecutionReportings
from openapi_server.models.rule_list import RuleList
from openapi_server.models.update_rule_request import UpdateRuleRequest
from openapi_server import util


async def create_rule(request: web.Request, store_id, body) -> web.Response:
    """Rule creation

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Delete Rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def disable_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Disable rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def enable_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Enable rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def get_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Gets the rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def get_rules(request: web.Request, store_id) -> web.Response:
    """Gets the list of rules for a given store

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def get_rules_executions(request: web.Request, store_id, page_number, page_size) -> web.Response:
    """Get the rules execution history

    

    :param store_id: Your store identifier
    :type store_id: str
    :param page_number: The page to retrieve
    :type page_number: int
    :param page_size: The count of rule history to retrieve
    :type page_size: int

    """
    return web.Response(status=200)


async def move_down_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Move the rule down

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def move_up_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Move the rule up

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def run_rule(request: web.Request, store_id, rule_id) -> web.Response:
    """Run rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str

    """
    return web.Response(status=200)


async def run_rules(request: web.Request, store_id) -> web.Response:
    """Run all rules for this store

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def update_rule(request: web.Request, store_id, rule_id, body) -> web.Response:
    """Update Rule

    

    :param store_id: Your store identifier
    :type store_id: str
    :param rule_id: Your rule identifier
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateRuleRequest.from_dict(body)
    return web.Response(status=200)
