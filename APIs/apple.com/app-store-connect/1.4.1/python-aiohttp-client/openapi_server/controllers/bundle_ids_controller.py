from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.bundle_id_capabilities_response import BundleIdCapabilitiesResponse
from openapi_server.models.bundle_id_create_request import BundleIdCreateRequest
from openapi_server.models.bundle_id_response import BundleIdResponse
from openapi_server.models.bundle_id_update_request import BundleIdUpdateRequest
from openapi_server.models.bundle_ids_response import BundleIdsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profiles_response import ProfilesResponse
from openapi_server import util


async def bundle_ids_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """bundle_ids_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def bundle_ids_bundle_id_capabilities_get_to_many_related(request: web.Request, id, fields_bundle_id_capabilities=None, limit=None) -> web.Response:
    """bundle_ids_bundle_id_capabilities_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_bundle_id_capabilities: the fields to include for returned resources of type bundleIdCapabilities
    :type fields_bundle_id_capabilities: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def bundle_ids_create_instance(request: web.Request, body) -> web.Response:
    """bundle_ids_create_instance

    

    :param body: BundleId representation
    :type body: dict | bytes

    """
    body = BundleIdCreateRequest.from_dict(body)
    return web.Response(status=200)


async def bundle_ids_delete_instance(request: web.Request, id) -> web.Response:
    """bundle_ids_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def bundle_ids_get_collection(request: web.Request, filter_identifier=None, filter_name=None, filter_platform=None, filter_seed_id=None, filter_id=None, sort=None, fields_bundle_ids=None, limit=None, include=None, fields_bundle_id_capabilities=None, fields_profiles=None, fields_apps=None, limit_bundle_id_capabilities=None, limit_profiles=None) -> web.Response:
    """bundle_ids_get_collection

    

    :param filter_identifier: filter by attribute &#39;identifier&#39;
    :type filter_identifier: List[str]
    :param filter_name: filter by attribute &#39;name&#39;
    :type filter_name: List[str]
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_seed_id: filter by attribute &#39;seedId&#39;
    :type filter_seed_id: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_bundle_ids: the fields to include for returned resources of type bundleIds
    :type fields_bundle_ids: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_bundle_id_capabilities: the fields to include for returned resources of type bundleIdCapabilities
    :type fields_bundle_id_capabilities: List[str]
    :param fields_profiles: the fields to include for returned resources of type profiles
    :type fields_profiles: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_bundle_id_capabilities: maximum number of related bundleIdCapabilities returned (when they are included)
    :type limit_bundle_id_capabilities: int
    :param limit_profiles: maximum number of related profiles returned (when they are included)
    :type limit_profiles: int

    """
    return web.Response(status=200)


async def bundle_ids_get_instance(request: web.Request, id, fields_bundle_ids=None, include=None, fields_bundle_id_capabilities=None, fields_profiles=None, fields_apps=None, limit_bundle_id_capabilities=None, limit_profiles=None) -> web.Response:
    """bundle_ids_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_bundle_ids: the fields to include for returned resources of type bundleIds
    :type fields_bundle_ids: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_bundle_id_capabilities: the fields to include for returned resources of type bundleIdCapabilities
    :type fields_bundle_id_capabilities: List[str]
    :param fields_profiles: the fields to include for returned resources of type profiles
    :type fields_profiles: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_bundle_id_capabilities: maximum number of related bundleIdCapabilities returned (when they are included)
    :type limit_bundle_id_capabilities: int
    :param limit_profiles: maximum number of related profiles returned (when they are included)
    :type limit_profiles: int

    """
    return web.Response(status=200)


async def bundle_ids_profiles_get_to_many_related(request: web.Request, id, fields_profiles=None, limit=None) -> web.Response:
    """bundle_ids_profiles_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_profiles: the fields to include for returned resources of type profiles
    :type fields_profiles: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def bundle_ids_update_instance(request: web.Request, id, body) -> web.Response:
    """bundle_ids_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BundleId representation
    :type body: dict | bytes

    """
    body = BundleIdUpdateRequest.from_dict(body)
    return web.Response(status=200)
