from typing import List, Dict
from aiohttp import web

from openapi_server.models.rule import Rule
from openapi_server.models.rule_full_response import RuleFullResponse
from openapi_server.models.rule_short_response import RuleShortResponse
from openapi_server import util


async def add_rule(request: web.Request, rule_object) -> web.Response:
    """add_rule

    Create a new rule

    :param rule_object: Rule information
    :type rule_object: dict | bytes

    """
    rule_object = Rule.from_dict(rule_object)
    return web.Response(status=200)


async def get_rule(request: web.Request, rule_id) -> web.Response:
    """get_rule

    Get a rule

    :param rule_id: Id of rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def list_rules(request: web.Request, ) -> web.Response:
    """list_rules

    List rules


    """
    return web.Response(status=200)


async def remove_rule(request: web.Request, rule_id) -> web.Response:
    """remove_rule

    Delete a rule

    :param rule_id: Id of rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def run_rule(request: web.Request, rule_id, initial_data=None) -> web.Response:
    """run_rule

    Run a rule

    :param rule_id: Id of rule
    :type rule_id: str
    :param initial_data: Initial data
    :type initial_data: 

    """
    return web.Response(status=200)


async def update_rule(request: web.Request, rule_id, rule_object) -> web.Response:
    """update_rule

    Update information about a specific rule

    :param rule_id: Id of user
    :type rule_id: str
    :param rule_object: Rule information
    :type rule_object: dict | bytes

    """
    rule_object = Rule.from_dict(rule_object)
    return web.Response(status=200)
