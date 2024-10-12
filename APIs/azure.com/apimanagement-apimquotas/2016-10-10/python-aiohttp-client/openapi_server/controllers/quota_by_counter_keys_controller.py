from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota_by_counter_keys_list_by_service_default_response import QuotaByCounterKeysListByServiceDefaultResponse
from openapi_server.models.quota_counter_collection import QuotaCounterCollection
from openapi_server.models.quota_counter_value_contract import QuotaCounterValueContract
from openapi_server import util


async def quota_by_counter_keys_list_by_service(request: web.Request, subscription_id, resource_group_name, service_name, quota_counter_key, api_version) -> web.Response:
    """quota_by_counter_keys_list_by_service

    Lists a collection of current quota counter periods associated with the counter-key configured in the policy on the specified service instance. The api does not support paging yet.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param quota_counter_key: Quota counter key identifier.
    :type quota_counter_key: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def quota_by_counter_keys_update(request: web.Request, resource_group_name, service_name, quota_counter_key, api_version, subscription_id, parameters) -> web.Response:
    """quota_by_counter_keys_update

    Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param quota_counter_key: Quota counter key identifier.
    :type quota_counter_key: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The value of the quota counter to be applied to all quota counter periods.
    :type parameters: dict | bytes

    """
    parameters = QuotaCounterValueContract.from_dict(parameters)
    return web.Response(status=200)
