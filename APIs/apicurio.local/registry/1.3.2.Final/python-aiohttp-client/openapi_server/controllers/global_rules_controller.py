from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType
from openapi_server import util


async def create_global_rule(request: web.Request, body) -> web.Response:
    """Create global rule

    Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error &#x60;400&#x60;) * The rule already exists (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param body: 
    :type body: dict | bytes

    """
    body = Rule.from_dict(body)
    return web.Response(status=200)


async def delete_all_global_rules(request: web.Request, ) -> web.Response:
    """Delete all global rules

    Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def delete_global_rule(request: web.Request, rule) -> web.Response:
    """Delete global rule

    Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * Rule cannot be deleted (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: str

    """
    return web.Response(status=200)


async def get_global_rule_config(request: web.Request, rule) -> web.Response:
    """Get global rule configuration

    Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: str

    """
    return web.Response(status=200)


async def list_global_rules(request: web.Request, ) -> web.Response:
    """List global rules

    Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def update_global_rule_config(request: web.Request, rule, body) -> web.Response:
    """Update global rule configuration

    Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: str
    :param body: 
    :type body: dict | bytes

    """
    body = Rule.from_dict(body)
    return web.Response(status=200)
