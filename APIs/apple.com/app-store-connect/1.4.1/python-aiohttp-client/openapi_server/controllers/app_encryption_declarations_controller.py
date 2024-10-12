from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_encryption_declaration_builds_linkages_request import AppEncryptionDeclarationBuildsLinkagesRequest
from openapi_server.models.app_encryption_declaration_response import AppEncryptionDeclarationResponse
from openapi_server.models.app_encryption_declarations_response import AppEncryptionDeclarationsResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_encryption_declarations_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """app_encryption_declarations_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def app_encryption_declarations_builds_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """app_encryption_declarations_builds_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = AppEncryptionDeclarationBuildsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def app_encryption_declarations_get_collection(request: web.Request, filter_platform=None, filter_app=None, filter_builds=None, fields_app_encryption_declarations=None, limit=None, include=None, fields_apps=None) -> web.Response:
    """app_encryption_declarations_get_collection

    

    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param filter_builds: filter by id(s) of related &#39;builds&#39;
    :type filter_builds: List[str]
    :param fields_app_encryption_declarations: the fields to include for returned resources of type appEncryptionDeclarations
    :type fields_app_encryption_declarations: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def app_encryption_declarations_get_instance(request: web.Request, id, fields_app_encryption_declarations=None, include=None, fields_apps=None) -> web.Response:
    """app_encryption_declarations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_encryption_declarations: the fields to include for returned resources of type appEncryptionDeclarations
    :type fields_app_encryption_declarations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)
