from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_data_collection import EventDataCollection
from openapi_server import util


async def tenant_activity_logs_list(request: web.Request, api_version, filter=None, select=None) -> web.Response:
    """tenant_activity_logs_list

    Gets the Activity Logs for the Tenant.&lt;br&gt;Everything that is applicable to the API to get the Activity Logs for the subscription is applicable to this API (the parameters, $filter, etc.).&lt;br&gt;One thing to point out here is that this API does *not* retrieve the logs at the individual subscription of the tenant but only surfaces the logs that were generated at the tenant level.

    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: Reduces the set of data collected. &lt;br&gt;The **$filter** is very restricted and allows only the following patterns.&lt;br&gt;- List events for a resource group: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceGroupName eq &#39;&lt;ResourceGroupName&gt;&#39;.&lt;br&gt;- List events for resource: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceUri eq &#39;&lt;ResourceURI&gt;&#39;.&lt;br&gt;- List events for a subscription: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39;.&lt;br&gt;- List events for a resource provider: $filter&#x3D;eventTimestamp ge &#39;&lt;Start Time&gt;&#39; and eventTimestamp le &#39;&lt;End Time&gt;&#39; and eventChannels eq &#39;Admin, Operation&#39; and resourceProvider eq &#39;&lt;ResourceProviderName&gt;&#39;.&lt;br&gt;- List events for a correlation Id: api-version&#x3D;2014-04-01&amp;$filter&#x3D;eventTimestamp ge &#39;2014-07-16T04:36:37.6407898Z&#39; and eventTimestamp le &#39;2014-07-20T04:36:37.6407898Z&#39; and eventChannels eq &#39;Admin, Operation&#39; and correlationId eq &#39;&lt;CorrelationID&gt;&#39;.&lt;br&gt;**NOTE**: No other syntax is allowed.
    :type filter: str
    :param select: Used to fetch events with only the given properties.&lt;br&gt;The **$select** argument is a comma separated list of property names to be returned. Possible values are: *authorization*, *claims*, *correlationId*, *description*, *eventDataId*, *eventName*, *eventTimestamp*, *httpRequest*, *level*, *operationId*, *operationName*, *properties*, *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*, *submissionTimestamp*, *subStatus*, *subscriptionId*
    :type select: str

    """
    return web.Response(status=200)
