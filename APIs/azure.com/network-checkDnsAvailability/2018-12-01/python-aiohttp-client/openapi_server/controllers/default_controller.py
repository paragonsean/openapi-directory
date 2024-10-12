from typing import List, Dict
from aiohttp import web

from openapi_server.models.dns_name_availability_result import DnsNameAvailabilityResult
from openapi_server import util


async def check_dns_name_availability(request: web.Request, location, domain_name_label, api_version, subscription_id) -> web.Response:
    """check_dns_name_availability

    Checks whether a domain name in the cloudapp.azure.com zone is available for use.

    :param location: The location of the domain name.
    :type location: str
    :param domain_name_label: The domain name to be verified. It must conform to the following regular expression: ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
    :type domain_name_label: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
