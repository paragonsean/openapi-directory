from typing import List, Dict
from aiohttp import web

from openapi_server.models.reports_list_by_api200_response import ReportsListByApi200Response
from openapi_server.models.reports_list_by_request200_response import ReportsListByRequest200Response
from openapi_server import util


async def reports_list_by_api(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_api

    Lists report records by API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)


async def reports_list_by_geo(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None) -> web.Response:
    """reports_list_by_geo

    Lists report records by geography.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| country | select |     |     | &lt;/br&gt;| region | select |     |     | &lt;/br&gt;| zip | select |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select |     |     | &lt;/br&gt;| callCountBlocked | select |     |     | &lt;/br&gt;| callCountFailed | select |     |     | &lt;/br&gt;| callCountOther | select |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_operation(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_operation

    Lists report records by API Operations.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | select, filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)


async def reports_list_by_product(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_product

    Lists report records by Product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | select, filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)


async def reports_list_by_request(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None) -> web.Response:
    """reports_list_by_request

    Lists report records by Request.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_subscription(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_subscription

    Lists report records by subscription.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | select, filter | eq |     | &lt;/br&gt;| productId | select, filter | eq |     | &lt;/br&gt;| subscriptionId | select, filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)


async def reports_list_by_time(request: web.Request, resource_group_name, service_name, filter, interval, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_time

    Lists report records by Time.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter, select | ge, le |     | &lt;/br&gt;| interval | select |     |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| userId | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select |     |     | &lt;/br&gt;| callCountBlocked | select |     |     | &lt;/br&gt;| callCountFailed | select |     |     | &lt;/br&gt;| callCountOther | select |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param interval: By time interval. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds)).
    :type interval: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)


async def reports_list_by_user(request: web.Request, resource_group_name, service_name, filter, api_version, subscription_id, top=None, skip=None, orderby=None) -> web.Response:
    """reports_list_by_user

    Lists report records by User.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| timestamp | filter | ge, le |     | &lt;/br&gt;| displayName | select, orderBy |     |     | &lt;/br&gt;| userId | select, filter | eq |     | &lt;/br&gt;| apiRegion | filter | eq |     | &lt;/br&gt;| productId | filter | eq |     | &lt;/br&gt;| subscriptionId | filter | eq |     | &lt;/br&gt;| apiId | filter | eq |     | &lt;/br&gt;| operationId | filter | eq |     | &lt;/br&gt;| callCountSuccess | select, orderBy |     |     | &lt;/br&gt;| callCountBlocked | select, orderBy |     |     | &lt;/br&gt;| callCountFailed | select, orderBy |     |     | &lt;/br&gt;| callCountOther | select, orderBy |     |     | &lt;/br&gt;| callCountTotal | select, orderBy |     |     | &lt;/br&gt;| bandwidth | select, orderBy |     |     | &lt;/br&gt;| cacheHitsCount | select |     |     | &lt;/br&gt;| cacheMissCount | select |     |     | &lt;/br&gt;| apiTimeAvg | select, orderBy |     |     | &lt;/br&gt;| apiTimeMin | select |     |     | &lt;/br&gt;| apiTimeMax | select |     |     | &lt;/br&gt;| serviceTimeAvg | select |     |     | &lt;/br&gt;| serviceTimeMin | select |     |     | &lt;/br&gt;| serviceTimeMax | select |     |     | &lt;/br&gt;
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param orderby: OData order by query option.
    :type orderby: str

    """
    return web.Response(status=200)
