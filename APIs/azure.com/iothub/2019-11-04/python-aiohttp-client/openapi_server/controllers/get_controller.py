from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_health_data_list_result import EndpointHealthDataListResult
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.event_hub_consumer_group_info import EventHubConsumerGroupInfo
from openapi_server.models.event_hub_consumer_groups_list_result import EventHubConsumerGroupsListResult
from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server.models.iot_hub_description_list_result import IotHubDescriptionListResult
from openapi_server.models.iot_hub_quota_metric_info_list_result import IotHubQuotaMetricInfoListResult
from openapi_server.models.iot_hub_sku_description_list_result import IotHubSkuDescriptionListResult
from openapi_server.models.job_response import JobResponse
from openapi_server.models.job_response_list_result import JobResponseListResult
from openapi_server.models.registry_statistics import RegistryStatistics
from openapi_server.models.user_subscription_quota_list_result import UserSubscriptionQuotaListResult
from openapi_server import util


async def iot_hub_resource_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the non-security related metadata of an IoT hub

    Get the non-security related metadata of an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_endpoint_health(request: web.Request, subscription_id, resource_group_name, iot_hub_name, api_version) -> web.Response:
    """Get the health for routing endpoints

    Get the health for routing endpoints.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: 
    :type resource_group_name: str
    :param iot_hub_name: 
    :type iot_hub_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_event_hub_consumer_group(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, event_hub_endpoint_name, name) -> web.Response:
    """Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub

    Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param event_hub_endpoint_name: The name of the Event Hub-compatible endpoint in the IoT hub.
    :type event_hub_endpoint_name: str
    :param name: The name of the consumer group to retrieve.
    :type name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_job(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, job_id) -> web.Response:
    """Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry

    Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param job_id: The job identifier.
    :type job_id: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_quota_metrics(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the quota metrics for an IoT hub

    Get the quota metrics for an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_stats(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the statistics from an IoT hub

    Get the statistics from an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_get_valid_skus(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the list of valid SKUs for an IoT hub

    Get the list of valid SKUs for an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """Get all the IoT hubs in a resource group

    Get all the IoT hubs in a resource group.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """Get all the IoT hubs in a subscription

    Get all the IoT hubs in a subscription.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def iot_hub_resource_list_event_hub_consumer_groups(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, event_hub_endpoint_name) -> web.Response:
    """Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub

    Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param event_hub_endpoint_name: The name of the Event Hub-compatible endpoint.
    :type event_hub_endpoint_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_list_jobs(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry

    Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def resource_provider_common_get_subscription_quota(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get the number of iot hubs in the subscription

    Get the number of free and paid iot hubs in the subscription

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)
