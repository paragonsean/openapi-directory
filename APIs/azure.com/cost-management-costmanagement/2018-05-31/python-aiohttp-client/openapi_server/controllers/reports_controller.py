from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.report_config import ReportConfig
from openapi_server.models.report_config_list_result import ReportConfigListResult
from openapi_server import util


async def report_config_create_or_update(request: web.Request, api_version, subscription_id, report_config_name, parameters) -> web.Response:
    """report_config_create_or_update

    The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report Config operation.
    :type parameters: dict | bytes

    """
    parameters = ReportConfig.from_dict(parameters)
    return web.Response(status=200)


async def report_config_create_or_update_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_config_name, parameters) -> web.Response:
    """report_config_create_or_update_by_resource_group_name

    The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report Config operation.
    :type parameters: dict | bytes

    """
    parameters = ReportConfig.from_dict(parameters)
    return web.Response(status=200)


async def report_config_delete(request: web.Request, api_version, subscription_id, report_config_name) -> web.Response:
    """report_config_delete

    The operation to delete a report.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str

    """
    return web.Response(status=200)


async def report_config_delete_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_config_name) -> web.Response:
    """report_config_delete_by_resource_group_name

    The operation to delete a report config.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str

    """
    return web.Response(status=200)


async def report_config_get(request: web.Request, api_version, subscription_id, report_config_name) -> web.Response:
    """report_config_get

    Gets the report config for a subscription by report config name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str

    """
    return web.Response(status=200)


async def report_config_get_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_config_name) -> web.Response:
    """report_config_get_by_resource_group_name

    Gets the report config for a resource group under a subscription by report config name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_config_name: Report Config Name.
    :type report_config_name: str

    """
    return web.Response(status=200)


async def report_config_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """report_config_list

    Lists all report configs for a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def report_config_list_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """report_config_list_by_resource_group_name

    Lists all report configs for a resource group under a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str

    """
    return web.Response(status=200)
