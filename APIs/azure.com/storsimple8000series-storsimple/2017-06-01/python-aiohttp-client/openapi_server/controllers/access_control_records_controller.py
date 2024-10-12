from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_control_record import AccessControlRecord
from openapi_server.models.access_control_record_list import AccessControlRecordList
from openapi_server import util


async def access_control_records_create_or_update(request: web.Request, access_control_record_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """access_control_records_create_or_update

    Creates or Updates an access control record.

    :param access_control_record_name: The name of the access control record.
    :type access_control_record_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The access control record to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = AccessControlRecord.from_dict(parameters)
    return web.Response(status=200)


async def access_control_records_delete(request: web.Request, access_control_record_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """access_control_records_delete

    Deletes the access control record.

    :param access_control_record_name: The name of the access control record to delete.
    :type access_control_record_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def access_control_records_get(request: web.Request, access_control_record_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """access_control_records_get

    Returns the properties of the specified access control record name.

    :param access_control_record_name: Name of access control record to be fetched.
    :type access_control_record_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def access_control_records_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """access_control_records_list_by_manager

    Retrieves all the access control records in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
