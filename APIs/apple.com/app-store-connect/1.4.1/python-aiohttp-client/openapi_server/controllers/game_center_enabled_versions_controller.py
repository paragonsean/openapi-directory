from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.game_center_enabled_version_compatible_versions_linkages_request import GameCenterEnabledVersionCompatibleVersionsLinkagesRequest
from openapi_server.models.game_center_enabled_version_compatible_versions_linkages_response import GameCenterEnabledVersionCompatibleVersionsLinkagesResponse
from openapi_server.models.game_center_enabled_versions_response import GameCenterEnabledVersionsResponse
from openapi_server import util


async def game_center_enabled_versions_compatible_versions_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """game_center_enabled_versions_compatible_versions_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def game_center_enabled_versions_compatible_versions_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """game_center_enabled_versions_compatible_versions_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def game_center_enabled_versions_compatible_versions_get_to_many_related(request: web.Request, id, filter_platform=None, filter_version_string=None, filter_app=None, filter_id=None, sort=None, fields_game_center_enabled_versions=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """game_center_enabled_versions_compatible_versions_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_version_string: filter by attribute &#39;versionString&#39;
    :type filter_version_string: List[str]
    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_game_center_enabled_versions: the fields to include for returned resources of type gameCenterEnabledVersions
    :type fields_game_center_enabled_versions: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def game_center_enabled_versions_compatible_versions_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """game_center_enabled_versions_compatible_versions_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def game_center_enabled_versions_compatible_versions_replace_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """game_center_enabled_versions_compatible_versions_replace_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.from_dict(body)
    return web.Response(status=200)
