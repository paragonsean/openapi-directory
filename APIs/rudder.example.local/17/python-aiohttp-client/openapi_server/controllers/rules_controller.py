from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_rule200_response import CreateRule200Response
from openapi_server.models.create_rule_category200_response import CreateRuleCategory200Response
from openapi_server.models.delete_rule200_response import DeleteRule200Response
from openapi_server.models.delete_rule_category200_response import DeleteRuleCategory200Response
from openapi_server.models.get_rule_category_details200_response import GetRuleCategoryDetails200Response
from openapi_server.models.get_rule_tree200_response import GetRuleTree200Response
from openapi_server.models.list_rules200_response import ListRules200Response
from openapi_server.models.rule_category import RuleCategory
from openapi_server.models.rule_category_update import RuleCategoryUpdate
from openapi_server.models.rule_details200_response import RuleDetails200Response
from openapi_server.models.rule_new import RuleNew
from openapi_server.models.rule_with_category import RuleWithCategory
from openapi_server.models.update_rule200_response import UpdateRule200Response
from openapi_server.models.update_rule_category200_response import UpdateRuleCategory200Response
from openapi_server import util


async def create_rule(request: web.Request, body=None) -> web.Response:
    """Create a rule

    Create a new rule. You can specify a source rule to clone it.

    :param body: 
    :type body: dict | bytes

    """
    body = RuleNew.from_dict(body)
    return web.Response(status=200)


async def create_rule_category(request: web.Request, body) -> web.Response:
    """Create a rule category

    Create a new rule category

    :param body: 
    :type body: dict | bytes

    """
    body = RuleCategory.from_dict(body)
    return web.Response(status=200)


async def delete_rule(request: web.Request, rule_id) -> web.Response:
    """Delete a rule

    Delete a rule.

    :param rule_id: Id of the target rule
    :type rule_id: str
    :type rule_id: str

    """
    return web.Response(status=200)


async def delete_rule_category(request: web.Request, rule_category_id) -> web.Response:
    """Delete group category

    Delete a group category. It must have no child groups and no children categories.

    :param rule_category_id: 
    :type rule_category_id: str
    :type rule_category_id: str

    """
    return web.Response(status=200)


async def get_rule_category_details(request: web.Request, rule_category_id) -> web.Response:
    """Get rule category details

    Get detailed information about a rule category

    :param rule_category_id: 
    :type rule_category_id: str
    :type rule_category_id: str

    """
    return web.Response(status=200)


async def get_rule_tree(request: web.Request, ) -> web.Response:
    """Get rules tree

    Get all available rules and their categories in a tree


    """
    return web.Response(status=200)


async def list_rules(request: web.Request, ) -> web.Response:
    """List all rules

    List all rules


    """
    return web.Response(status=200)


async def rule_details(request: web.Request, rule_id) -> web.Response:
    """Get a rule details

    Get the details of a rule

    :param rule_id: Id of the target rule
    :type rule_id: str
    :type rule_id: str

    """
    return web.Response(status=200)


async def update_rule(request: web.Request, rule_id, body) -> web.Response:
    """Update a rule details

    Update the details of a rule

    :param rule_id: Id of the target rule
    :type rule_id: str
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RuleWithCategory.from_dict(body)
    return web.Response(status=200)


async def update_rule_category(request: web.Request, rule_category_id, body) -> web.Response:
    """Update rule category details

    Update detailed information about a rule category

    :param rule_category_id: 
    :type rule_category_id: str
    :type rule_category_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RuleCategoryUpdate.from_dict(body)
    return web.Response(status=200)
