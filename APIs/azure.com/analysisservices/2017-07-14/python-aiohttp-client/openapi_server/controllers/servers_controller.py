from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis_services_server import AnalysisServicesServer
from openapi_server.models.analysis_services_server_update_parameters import AnalysisServicesServerUpdateParameters
from openapi_server.models.analysis_services_servers import AnalysisServicesServers
from openapi_server.models.check_server_name_availability_parameters import CheckServerNameAvailabilityParameters
from openapi_server.models.check_server_name_availability_result import CheckServerNameAvailabilityResult
from openapi_server.models.gateway_list_status_error import GatewayListStatusError
from openapi_server.models.gateway_list_status_live import GatewayListStatusLive
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.sku_enumeration_for_existing_resource_result import SkuEnumerationForExistingResourceResult
from openapi_server import util


async def servers_check_name_availability(request: web.Request, location, api_version, subscription_id, server_parameters) -> web.Response:
    """servers_check_name_availability

    Check the name availability in the target location.

    :param location: The region name which the operation will lookup into.
    :type location: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param server_parameters: Contains the information used to provision the Analysis Services server.
    :type server_parameters: dict | bytes

    """
    server_parameters = CheckServerNameAvailabilityParameters.from_dict(server_parameters)
    return web.Response(status=200)


async def servers_create(request: web.Request, resource_group_name, server_name, api_version, subscription_id, server_parameters) -> web.Response:
    """servers_create

    Provisions the specified Analysis Services server based on the configuration specified in the request.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param server_parameters: Contains the information used to provision the Analysis Services server.
    :type server_parameters: dict | bytes

    """
    server_parameters = AnalysisServicesServer.from_dict(server_parameters)
    return web.Response(status=200)


async def servers_delete(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_delete

    Deletes the specified Analysis Services server.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_dissociate_gateway(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_dissociate_gateway

    Dissociates a Unified Gateway associated with the server.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_get_details(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_get_details

    Gets details about the specified Analysis Services server.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """servers_list

    Lists all the Analysis Services servers for the given subscription.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """servers_list_by_resource_group

    Gets all the Analysis Services servers for the given resource group.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_gateway_status(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_list_gateway_status

    Return the gateway status of the specified Analysis Services server instance.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_operation_results(request: web.Request, location, operation_id, api_version, subscription_id) -> web.Response:
    """servers_list_operation_results

    List the result of the specified operation.

    :param location: The region name which the operation will lookup into.
    :type location: str
    :param operation_id: The target operation Id.
    :type operation_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_operation_statuses(request: web.Request, location, operation_id, api_version, subscription_id) -> web.Response:
    """servers_list_operation_statuses

    List the status of operation.

    :param location: The region name which the operation will lookup into.
    :type location: str
    :param operation_id: The target operation Id.
    :type operation_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_list_skus_for_existing(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_list_skus_for_existing

    Lists eligible SKUs for an Analysis Services resource.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_resume(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_resume

    Resumes operation of the specified Analysis Services server instance.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_suspend(request: web.Request, resource_group_name, server_name, api_version, subscription_id) -> web.Response:
    """servers_suspend

    Suspends operation of the specified Analysis Services server instance.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def servers_update(request: web.Request, resource_group_name, server_name, api_version, subscription_id, server_update_parameters) -> web.Response:
    """servers_update

    Updates the current state of the specified Analysis Services server.

    :param resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param server_name: The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    :type server_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param server_update_parameters: Request object that contains the updated information for the server.
    :type server_update_parameters: dict | bytes

    """
    server_update_parameters = AnalysisServicesServerUpdateParameters.from_dict(server_update_parameters)
    return web.Response(status=200)
