from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.classic_mobile_service_collection import ClassicMobileServiceCollection
from openapi_server.models.geo_region_collection import GeoRegionCollection
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.managed_hosting_environment_collection import ManagedHostingEnvironmentCollection
from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.user import User
from openapi_server import util


async def global_check_name_availability(request: web.Request, subscription_id, api_version, request) -> web.Response:
    """Check if resource name is available

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Name availability request
    :type request: dict | bytes

    """
    request = ResourceNameAvailabilityRequest.from_dict(request)
    return web.Response(status=200)


async def global_get_all_certificates(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all certificates for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_get_all_classic_mobile_services(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all mobile services for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_get_all_hosting_environments(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all hostingEnvironments (App Service Environment) for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_get_all_managed_hosting_environments(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all managed hosting environments for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_get_all_server_farms(request: web.Request, subscription_id, api_version, detailed=None) -> web.Response:
    """Gets all App Service Plans for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param detailed: False to return a subset of App Service Plan properties, true to return all of the properties.              Retrieval of all properties may increase the API latency.
    :type detailed: bool

    """
    return web.Response(status=200)


async def global_get_all_sites(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all Web Apps for a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_get_subscription_geo_regions(request: web.Request, subscription_id, api_version, sku=None, linux_workers_enabled=None) -> web.Response:
    """Gets list of available geo regions

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param sku: Filter only to regions that support this sku
    :type sku: str
    :param linux_workers_enabled: Filter only to regions that support linux workers
    :type linux_workers_enabled: bool

    """
    return web.Response(status=200)


async def global_get_subscription_publishing_credentials(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets publishing credentials for the subscription owner

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_is_hosting_environment_name_available(request: web.Request, name, subscription_id, api_version) -> web.Response:
    """Whether hosting environment name is available

    

    :param name: Hosting environment name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_is_hosting_environment_with_legacy_name_available(request: web.Request, name, subscription_id, api_version) -> web.Response:
    """Whether hosting environment name is available

    

    :param name: Hosting environment name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_list_premier_add_on_offers(request: web.Request, subscription_id, api_version) -> web.Response:
    """List premier add on offers

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_update_subscription_publishing_credentials(request: web.Request, subscription_id, api_version, request_message) -> web.Response:
    """Updates publishing credentials for the subscription owner

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request_message: requestMessage with new publishing credentials
    :type request_message: dict | bytes

    """
    request_message = User.from_dict(request_message)
    return web.Response(status=200)
