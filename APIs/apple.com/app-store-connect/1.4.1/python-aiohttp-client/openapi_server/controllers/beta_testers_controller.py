from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.beta_groups_response import BetaGroupsResponse
from openapi_server.models.beta_tester_apps_linkages_request import BetaTesterAppsLinkagesRequest
from openapi_server.models.beta_tester_apps_linkages_response import BetaTesterAppsLinkagesResponse
from openapi_server.models.beta_tester_beta_groups_linkages_request import BetaTesterBetaGroupsLinkagesRequest
from openapi_server.models.beta_tester_beta_groups_linkages_response import BetaTesterBetaGroupsLinkagesResponse
from openapi_server.models.beta_tester_builds_linkages_request import BetaTesterBuildsLinkagesRequest
from openapi_server.models.beta_tester_builds_linkages_response import BetaTesterBuildsLinkagesResponse
from openapi_server.models.beta_tester_create_request import BetaTesterCreateRequest
from openapi_server.models.beta_tester_response import BetaTesterResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_testers_apps_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_testers_apps_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaTesterAppsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_apps_get_to_many_related(request: web.Request, id, fields_apps=None, limit=None) -> web.Response:
    """beta_testers_apps_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_apps_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """beta_testers_apps_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_beta_groups_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_testers_beta_groups_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaTesterBetaGroupsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_beta_groups_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_testers_beta_groups_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaTesterBetaGroupsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_beta_groups_get_to_many_related(request: web.Request, id, fields_beta_groups=None, limit=None) -> web.Response:
    """beta_testers_beta_groups_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_beta_groups_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """beta_testers_beta_groups_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_builds_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_testers_builds_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaTesterBuildsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_builds_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """beta_testers_builds_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BetaTesterBuildsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_builds_get_to_many_related(request: web.Request, id, fields_builds=None, limit=None) -> web.Response:
    """beta_testers_builds_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_builds_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """beta_testers_builds_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def beta_testers_create_instance(request: web.Request, body) -> web.Response:
    """beta_testers_create_instance

    

    :param body: BetaTester representation
    :type body: dict | bytes

    """
    body = BetaTesterCreateRequest.from_dict(body)
    return web.Response(status=200)


async def beta_testers_delete_instance(request: web.Request, id) -> web.Response:
    """beta_testers_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def beta_testers_get_collection(request: web.Request, filter_email=None, filter_first_name=None, filter_invite_type=None, filter_last_name=None, filter_apps=None, filter_beta_groups=None, filter_builds=None, sort=None, fields_beta_testers=None, limit=None, include=None, fields_beta_groups=None, fields_builds=None, fields_apps=None, limit_apps=None, limit_beta_groups=None, limit_builds=None) -> web.Response:
    """beta_testers_get_collection

    

    :param filter_email: filter by attribute &#39;email&#39;
    :type filter_email: List[str]
    :param filter_first_name: filter by attribute &#39;firstName&#39;
    :type filter_first_name: List[str]
    :param filter_invite_type: filter by attribute &#39;inviteType&#39;
    :type filter_invite_type: List[str]
    :param filter_last_name: filter by attribute &#39;lastName&#39;
    :type filter_last_name: List[str]
    :param filter_apps: filter by id(s) of related &#39;apps&#39;
    :type filter_apps: List[str]
    :param filter_beta_groups: filter by id(s) of related &#39;betaGroups&#39;
    :type filter_beta_groups: List[str]
    :param filter_builds: filter by id(s) of related &#39;builds&#39;
    :type filter_builds: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_apps: maximum number of related apps returned (when they are included)
    :type limit_apps: int
    :param limit_beta_groups: maximum number of related betaGroups returned (when they are included)
    :type limit_beta_groups: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int

    """
    return web.Response(status=200)


async def beta_testers_get_instance(request: web.Request, id, fields_beta_testers=None, include=None, fields_beta_groups=None, fields_builds=None, fields_apps=None, limit_apps=None, limit_beta_groups=None, limit_builds=None) -> web.Response:
    """beta_testers_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_apps: maximum number of related apps returned (when they are included)
    :type limit_apps: int
    :param limit_beta_groups: maximum number of related betaGroups returned (when they are included)
    :type limit_beta_groups: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int

    """
    return web.Response(status=200)
