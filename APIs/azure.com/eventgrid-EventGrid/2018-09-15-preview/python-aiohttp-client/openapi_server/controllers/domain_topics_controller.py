from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_topic import DomainTopic
from openapi_server.models.domain_topics_list_result import DomainTopicsListResult
from openapi_server import util


async def domain_topics_get(request: web.Request, subscription_id, resource_group_name, domain_name, topic_name, api_version) -> web.Response:
    """Get a domain topic

    Get properties of a domain topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domain_topics_list_by_domain(request: web.Request, subscription_id, resource_group_name, domain_name, api_version) -> web.Response:
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

    """
    return web.Response(status=200)
