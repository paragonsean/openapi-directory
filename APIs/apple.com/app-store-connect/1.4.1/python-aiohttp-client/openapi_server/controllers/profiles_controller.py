from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_id_response import BundleIdResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.devices_response import DevicesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profile_create_request import ProfileCreateRequest
from openapi_server.models.profile_response import ProfileResponse
from openapi_server.models.profiles_response import ProfilesResponse
from openapi_server import util


async def profiles_bundle_id_get_to_one_related(request: web.Request, id, fields_bundle_ids=None) -> web.Response:
    """profiles_bundle_id_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_bundle_ids: the fields to include for returned resources of type bundleIds
    :type fields_bundle_ids: List[str]

    """
    return web.Response(status=200)


async def profiles_certificates_get_to_many_related(request: web.Request, id, fields_certificates=None, limit=None) -> web.Response:
    """profiles_certificates_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_certificates: the fields to include for returned resources of type certificates
    :type fields_certificates: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def profiles_create_instance(request: web.Request, body) -> web.Response:
    """profiles_create_instance

    

    :param body: Profile representation
    :type body: dict | bytes

    """
    body = ProfileCreateRequest.from_dict(body)
    return web.Response(status=200)


async def profiles_delete_instance(request: web.Request, id) -> web.Response:
    """profiles_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def profiles_devices_get_to_many_related(request: web.Request, id, fields_devices=None, limit=None) -> web.Response:
    """profiles_devices_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_devices: the fields to include for returned resources of type devices
    :type fields_devices: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def profiles_get_collection(request: web.Request, filter_name=None, filter_profile_state=None, filter_profile_type=None, filter_id=None, sort=None, fields_profiles=None, limit=None, include=None, fields_certificates=None, fields_devices=None, fields_bundle_ids=None, limit_certificates=None, limit_devices=None) -> web.Response:
    """profiles_get_collection

    

    :param filter_name: filter by attribute &#39;name&#39;
    :type filter_name: List[str]
    :param filter_profile_state: filter by attribute &#39;profileState&#39;
    :type filter_profile_state: List[str]
    :param filter_profile_type: filter by attribute &#39;profileType&#39;
    :type filter_profile_type: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_profiles: the fields to include for returned resources of type profiles
    :type fields_profiles: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_certificates: the fields to include for returned resources of type certificates
    :type fields_certificates: List[str]
    :param fields_devices: the fields to include for returned resources of type devices
    :type fields_devices: List[str]
    :param fields_bundle_ids: the fields to include for returned resources of type bundleIds
    :type fields_bundle_ids: List[str]
    :param limit_certificates: maximum number of related certificates returned (when they are included)
    :type limit_certificates: int
    :param limit_devices: maximum number of related devices returned (when they are included)
    :type limit_devices: int

    """
    return web.Response(status=200)


async def profiles_get_instance(request: web.Request, id, fields_profiles=None, include=None, fields_certificates=None, fields_devices=None, fields_bundle_ids=None, limit_certificates=None, limit_devices=None) -> web.Response:
    """profiles_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_profiles: the fields to include for returned resources of type profiles
    :type fields_profiles: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_certificates: the fields to include for returned resources of type certificates
    :type fields_certificates: List[str]
    :param fields_devices: the fields to include for returned resources of type devices
    :type fields_devices: List[str]
    :param fields_bundle_ids: the fields to include for returned resources of type bundleIds
    :type fields_bundle_ids: List[str]
    :param limit_certificates: maximum number of related certificates returned (when they are included)
    :type limit_certificates: int
    :param limit_devices: maximum number of related devices returned (when they are included)
    :type limit_devices: int

    """
    return web.Response(status=200)
