from typing import List, Dict
from aiohttp import web

from openapi_server.models.connectors import Connectors
from openapi_server.models.credentials import Credentials
from openapi_server.models.data_freshness_details import DataFreshnessDetails
from openapi_server.models.export_statuses import ExportStatuses
from openapi_server.models.global_configurations import GlobalConfigurations
from openapi_server.models.service_configuration import ServiceConfiguration
from openapi_server.models.service_member import ServiceMember
from openapi_server.models.service_members import ServiceMembers
from openapi_server import util


async def service_members_add(request: web.Request, service_name, api_version, service_member) -> web.Response:
    """service_members_add

    Onboards  a server, for a given service, to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service under which the server is to be onboarded.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service_member: The server object.
    :type service_member: dict | bytes

    """
    service_member = ServiceMember.from_dict(service_member)
    return web.Response(status=200)


async def service_members_delete(request: web.Request, service_name, service_member_id, api_version, confirm=None) -> web.Response:
    """service_members_delete

    Deletes a server that has been onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param confirm: Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
    :type confirm: bool

    """
    return web.Response(status=200)


async def service_members_delete_data(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_delete_data

    Deletes the data uploaded by the server to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_get(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_get

    Gets the details of a server, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_get_service_configuration(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_get_service_configuration

    Gets the service configuration.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_list(request: web.Request, service_name, api_version, filter=None, dimension_type=None, dimension_signature=None) -> web.Response:
    """service_members_list

    Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str
    :param dimension_type: The server specific dimension.
    :type dimension_type: str
    :param dimension_signature: The value of the dimension.
    :type dimension_signature: str

    """
    return web.Response(status=200)


async def service_members_list_connectors(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_list_connectors

    Gets the connector details for a service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_list_credentials(request: web.Request, service_name, service_member_id, api_version, filter=None) -> web.Response:
    """service_members_list_credentials

    Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The property filter to apply.
    :type filter: str

    """
    return web.Response(status=200)


async def service_members_list_data_freshness(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_list_data_freshness

    Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_list_export_status(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_list_export_status

    Gets the export status.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_list_global_configuration(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """service_members_list_global_configuration

    Gets the global configuration.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server id.
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
