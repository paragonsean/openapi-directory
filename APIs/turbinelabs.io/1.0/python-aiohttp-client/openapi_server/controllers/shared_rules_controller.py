from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_shared_rules_result import MultiSharedRulesResult
from openapi_server.models.shared_rules import SharedRules
from openapi_server.models.shared_rules_create import SharedRulesCreate
from openapi_server.models.shared_rules_result import SharedRulesResult
from openapi_server import util


async def shared_rules_get(request: web.Request, filters=None) -> web.Response:
    """get shared_rules

    Get a list of shared_rules

    :param filters: A JSON encoded array of SharedRulesFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any SharedRulesFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def shared_rules_post(request: web.Request, shared_rules) -> web.Response:
    """create shared_rules

    Create a new shared_rules object

    :param shared_rules: the shared_rules object to create
    :type shared_rules: dict | bytes

    """
    shared_rules = SharedRulesCreate.from_dict(shared_rules)
    return web.Response(status=200)


async def shared_rules_shared_rules_key_get(request: web.Request, shared_rules_key) -> web.Response:
    """get shared_rules object

    Get details for an existing shared_rules object

    :param shared_rules_key: the shared_rules key
    :type shared_rules_key: str

    """
    return web.Response(status=200)


async def shared_rules_shared_rules_key_put(request: web.Request, shared_rules_key, shared_rules) -> web.Response:
    """modify shared_rules object

    Modify an existing shared_rules object

    :param shared_rules_key: the shared_rules key
    :type shared_rules_key: str
    :param shared_rules: the shared_rules object to modify
    :type shared_rules: dict | bytes

    """
    shared_rules = SharedRules.from_dict(shared_rules)
    return web.Response(status=200)
