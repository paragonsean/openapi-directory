from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_topic import DomainTopic
from openapi_server.models.domain_topics_list_result import DomainTopicsListResult
from openapi_server import util


async def domain_topics_create_or_update(request: web.Request, subscription_id, resource_group_name, domain_name, domain_topic_name, api_version) -> web.Response:
    """Create or update a domain topic

    Asynchronously creates or updates a new domain topic with the specified parameters.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param domain_topic_name: Name of the domain topic
    :type domain_topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domain_topics_delete(request: web.Request, subscription_id, resource_group_name, domain_name, domain_topic_name, api_version) -> web.Response:
    """Delete a domain topic

    Delete existing domain topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param domain_topic_name: Name of the domain topic
    :type domain_topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domain_topics_get(request: web.Request, subscription_id, resource_group_name, domain_name, domain_topic_name, api_version) -> web.Response:
    """Get a domain topic

    Get properties of a domain topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param domain_topic_name: Name of the topic
    :type domain_topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domain_topics_list_by_domain(request: web.Request, subscription_id, resource_group_name, domain_name, api_version, filter=None, top=None) -> web.Response:
    """List domain topics.

    List all the topics in a domain.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Domain name.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)
