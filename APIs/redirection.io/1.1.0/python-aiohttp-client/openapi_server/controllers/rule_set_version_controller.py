from typing import List, Dict
from aiohttp import web

from openapi_server.models.rule_set_version import RuleSetVersion
from openapi_server.models.rule_set_version_read import RuleSetVersionRead
from openapi_server import util


async def clear_rule_set_version_item(request: web.Request, id, rule_set_version) -> web.Response:
    """Clear a version

    

    :param id: The id of the version
    :type id: str
    :param rule_set_version: The new RuleSetVersion resource
    :type rule_set_version: dict | bytes

    """
    rule_set_version = RuleSetVersion.from_dict(rule_set_version)
    return web.Response(status=200)


async def get_rule_set_version_collection(request: web.Request, project_id, sort_created_at=None, page=None) -> web.Response:
    """Retrieves the collection of RuleSetVersion resources.

    

    :param project_id: 
    :type project_id: str
    :param sort_created_at: 
    :type sort_created_at: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_rule_set_version_item(request: web.Request, id) -> web.Response:
    """Retrieves a RuleSetVersion resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def publish_rule_set_version_item(request: web.Request, id, rule_set_version) -> web.Response:
    """Publish a version

    

    :param id: The id of the version
    :type id: str
    :param rule_set_version: The new RuleSetVersion resource
    :type rule_set_version: dict | bytes

    """
    rule_set_version = RuleSetVersion.from_dict(rule_set_version)
    return web.Response(status=200)
