from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_providers_list import AvailableProvidersList
from openapi_server.models.available_providers_list_parameters import AvailableProvidersListParameters
from openapi_server.models.azure_reachability_report import AzureReachabilityReport
from openapi_server.models.azure_reachability_report_parameters import AzureReachabilityReportParameters
from openapi_server.models.connectivity_information import ConnectivityInformation
from openapi_server.models.connectivity_parameters import ConnectivityParameters
from openapi_server.models.flow_log_information import FlowLogInformation
from openapi_server.models.flow_log_status_parameters import FlowLogStatusParameters
from openapi_server.models.network_watcher import NetworkWatcher
from openapi_server.models.network_watcher_list_result import NetworkWatcherListResult
from openapi_server.models.network_watchers_update_tags_request import NetworkWatchersUpdateTagsRequest
from openapi_server.models.next_hop_parameters import NextHopParameters
from openapi_server.models.next_hop_result import NextHopResult
from openapi_server.models.query_troubleshooting_parameters import QueryTroubleshootingParameters
from openapi_server.models.security_group_view_parameters import SecurityGroupViewParameters
from openapi_server.models.security_group_view_result import SecurityGroupViewResult
from openapi_server.models.topology import Topology
from openapi_server.models.topology_parameters import TopologyParameters
from openapi_server.models.troubleshooting_parameters import TroubleshootingParameters
from openapi_server.models.troubleshooting_result import TroubleshootingResult
from openapi_server.models.verification_ip_flow_parameters import VerificationIPFlowParameters
from openapi_server.models.verification_ip_flow_result import VerificationIPFlowResult
from openapi_server import util


async def network_watchers_check_connectivity(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_check_connectivity

    Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that determine how the connectivity check will be performed.
    :type parameters: dict | bytes

    """
    parameters = ConnectivityParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_create_or_update(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_create_or_update

    Creates or updates a network watcher in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the network watcher resource.
    :type parameters: dict | bytes

    """
    parameters = NetworkWatcher.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_delete(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id) -> web.Response:
    """network_watchers_delete

    Deletes the specified network watcher resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_watchers_get(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id) -> web.Response:
    """network_watchers_get

    Gets the specified network watcher by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_watchers_get_azure_reachability_report(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_azure_reachability_report

    Gets the relative latency score for internet service providers from a specified location to Azure regions.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that determine Azure reachability report configuration.
    :type parameters: dict | bytes

    """
    parameters = AzureReachabilityReportParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_flow_log_status(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_flow_log_status

    Queries status of flow log and traffic analytics (optional) on a specified resource.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define a resource to query flow log and traffic analytics (optional)  status.
    :type parameters: dict | bytes

    """
    parameters = FlowLogStatusParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_next_hop(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_next_hop

    Gets the next hop from the specified VM.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the source and destination endpoint.
    :type parameters: dict | bytes

    """
    parameters = NextHopParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_topology(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_topology

    Gets the current network topology by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the representation of topology.
    :type parameters: dict | bytes

    """
    parameters = TopologyParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_troubleshooting(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_troubleshooting

    Initiate troubleshooting on a specified resource

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the resource to troubleshoot.
    :type parameters: dict | bytes

    """
    parameters = TroubleshootingParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_troubleshooting_result(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_troubleshooting_result

    Get the last completed troubleshooting result on a specified resource

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the resource to query the troubleshooting result.
    :type parameters: dict | bytes

    """
    parameters = QueryTroubleshootingParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_get_vm_security_rules(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_get_vm_security_rules

    Gets the configured and effective security group rules on the specified VM.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the VM to check security groups for.
    :type parameters: dict | bytes

    """
    parameters = SecurityGroupViewParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """network_watchers_list

    Gets all network watchers by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_watchers_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """network_watchers_list_all

    Gets all network watchers by subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_watchers_list_available_providers(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_list_available_providers

    Lists all available internet service providers for a specified Azure region.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that scope the list of available providers.
    :type parameters: dict | bytes

    """
    parameters = AvailableProvidersListParameters.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_set_flow_log_configuration(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_set_flow_log_configuration

    Configures flow log  and traffic analytics (optional) on a specified resource.

    :param resource_group_name: The name of the network watcher resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher resource.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the configuration of flow log.
    :type parameters: dict | bytes

    """
    parameters = FlowLogInformation.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_update_tags(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_update_tags

    Updates a network watcher tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update network watcher tags.
    :type parameters: dict | bytes

    """
    parameters = NetworkWatchersUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)


async def network_watchers_verify_ip_flow(request: web.Request, resource_group_name, network_watcher_name, api_version, subscription_id, parameters) -> web.Response:
    """network_watchers_verify_ip_flow

    Verify IP flow from the specified VM to a location given the currently configured NSG rules.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_watcher_name: The name of the network watcher.
    :type network_watcher_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters that define the IP flow to be verified.
    :type parameters: dict | bytes

    """
    parameters = VerificationIPFlowParameters.from_dict(parameters)
    return web.Response(status=200)
