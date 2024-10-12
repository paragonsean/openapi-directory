from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.certificate_contract import CertificateContract
from openapi_server.models.certificate_create_or_update_parameters import CertificateCreateOrUpdateParameters
from openapi_server.models.certificate_list_by_service_default_response import CertificateListByServiceDefaultResponse
from openapi_server import util


async def certificate_create_or_update(request: web.Request, resource_group_name, service_name, certificate_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """certificate_create_or_update

    Creates or updates the certificate being used for authentication with the backend.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :type certificate_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or Update parameters.
    :type parameters: dict | bytes
    :param if_match: The entity state (Etag) version of the certificate to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation..
    :type if_match: str

    """
    parameters = CertificateCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def certificate_delete(request: web.Request, resource_group_name, service_name, certificate_id, if_match, api_version, subscription_id) -> web.Response:
    """certificate_delete

    Deletes specific certificate.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :type certificate_id: str
    :param if_match: The entity state (Etag) version of the certificate to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def certificate_get(request: web.Request, resource_group_name, service_name, certificate_id, api_version, subscription_id) -> web.Response:
    """certificate_get

    Gets the details of the certificate specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :type certificate_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def certificate_get_entity_tag(request: web.Request, resource_group_name, service_name, certificate_id, api_version, subscription_id) -> web.Response:
    """certificate_get_entity_tag

    Gets the entity state (Etag) version of the certificate specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :type certificate_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def certificate_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """certificate_list_by_service

    Lists a collection of all certificates in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field          | Supported operators    | Supported functions                         | |----------------|------------------------|---------------------------------------------| | id             | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | subject        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | thumbprint     | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | expirationDate | ge, le, eq, ne, gt, lt | N/A                                         |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
