from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_group_beta_testers_linkages_request import BetaGroupBetaTestersLinkagesRequest
from openapi_server.models.beta_group_beta_testers_linkages_response import BetaGroupBetaTestersLinkagesResponse
from openapi_server.models.beta_group_builds_linkages_request import BetaGroupBuildsLinkagesRequest
from openapi_server.models.beta_group_builds_linkages_response import BetaGroupBuildsLinkagesResponse
from openapi_server.models.beta_group_create_request import BetaGroupCreateRequest
from openapi_server.models.beta_group_response import BetaGroupResponse
from openapi_server.models.beta_group_update_request import BetaGroupUpdateRequest
from openapi_server.models.beta_groups_response import BetaGroupsResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_groups_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """beta_groups_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_groups_beta_testers_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_groups_beta_testers_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaGroupBetaTestersLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_groups_beta_testers_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_groups_beta_testers_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaGroupBetaTestersLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_groups_beta_testers_get_to_many_related(request: web.Request, id, fields_beta_testers=None, limit=None) -> web.Response:
    """beta_groups_beta_testers_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_groups_beta_testers_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """beta_groups_beta_testers_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_groups_builds_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_groups_builds_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaGroupBuildsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_groups_builds_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_groups_builds_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaGroupBuildsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_groups_builds_get_to_many_related(request: web.Request, id, fields_builds=None, limit=None) -> web.Response:
    """beta_groups_builds_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_groups_builds_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """beta_groups_builds_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_groups_create_instance(request: web.Request, body) -> web.Response:
    """beta_groups_create_instance

    

    :param body: BetaGroup representation
    :type body: dict | bytes

    """
    body = BetaGroupCreateRequest.from_dict(body)
    return web.Response(status=200)


async def beta_groups_delete_instance(request: web.Request, id) -> web.Response:
    """beta_groups_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def beta_groups_get_collection(request: web.Request, filter_is_internal_group=None, filter_name=None, filter_public_link=None, filter_public_link_enabled=None, filter_public_link_limit_enabled=None, filter_app=None, filter_builds=None, filter_id=None, sort=None, fields_beta_groups=None, limit=None, include=None, fields_builds=None, fields_beta_testers=None, fields_apps=None, limit_beta_testers=None, limit_builds=None) -> web.Response:
    """beta_groups_get_collection

    

    :param filter_is_internal_group: filter by attribute &#39;isInternalGroup&#39;
    :type filter_is_internal_group: List[str]
    :param filter_name: filter by attribute &#39;name&#39;
    :type filter_name: List[str]
    :param filter_public_link: filter by attribute &#39;publicLink&#39;
    :type filter_public_link: List[str]
    :param filter_public_link_enabled: filter by attribute &#39;publicLinkEnabled&#39;
    :type filter_public_link_enabled: List[str]
    :param filter_public_link_limit_enabled: filter by attribute &#39;publicLinkLimitEnabled&#39;
    :type filter_public_link_limit_enabled: List[str]
    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param filter_builds: filter by id(s) of related &#39;builds&#39;
    :type filter_builds: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_beta_testers: maximum number of related betaTesters returned (when they are included)
    :type limit_beta_testers: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int

    """
    return web.Response(status=200)


async def beta_groups_get_instance(request: web.Request, id, fields_beta_groups=None, include=None, fields_builds=None, fields_beta_testers=None, fields_apps=None, limit_beta_testers=None, limit_builds=None) -> web.Response:
    """beta_groups_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_beta_testers: maximum number of related betaTesters returned (when they are included)
    :type limit_beta_testers: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int

    """
    return web.Response(status=200)


async def beta_groups_update_instance(request: web.Request, id, body) -> web.Response:
    """beta_groups_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BetaGroup representation
    :type body: dict | bytes

    """
    body = BetaGroupUpdateRequest.from_dict(body)
    return web.Response(status=200)
