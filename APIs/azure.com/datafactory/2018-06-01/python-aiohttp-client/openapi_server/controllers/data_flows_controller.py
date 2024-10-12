from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_flow_list_response import DataFlowListResponse
from openapi_server.models.data_flow_resource import DataFlowResource
from openapi_server import util


async def data_flows_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, data_flow_name, api_version, data_flow, if_match=None) -> web.Response:
    """data_flows_create_or_update

    Creates or updates a data flow.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param data_flow_name: The data flow name.
    :type data_flow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param data_flow: Data flow resource definition.
    :type data_flow: dict | bytes
    :param if_match: ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    data_flow = DataFlowResource.from_dict(data_flow)
    return web.Response(status=200)


async def data_flows_delete(request: web.Request, subscription_id, resource_group_name, factory_name, data_flow_name, api_version) -> web.Response:
    """data_flows_delete

    Deletes a data flow.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param data_flow_name: The data flow name.
    :type data_flow_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_flows_get(request: web.Request, subscription_id, resource_group_name, factory_name, data_flow_name, api_version, if_none_match=None) -> web.Response:
    """data_flows_get

    Gets a data flow.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param data_flow_name: The data flow name.
    :type data_flow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param if_none_match: ETag of the data flow entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def data_flows_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """data_flows_list_by_factory

    Lists data flows.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
