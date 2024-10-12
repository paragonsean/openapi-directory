from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_vpn_sites_configuration_request import GetVpnSitesConfigurationRequest
from openapi_server.models.hub_virtual_network_connection import HubVirtualNetworkConnection
from openapi_server.models.list_hub_virtual_network_connections_result import ListHubVirtualNetworkConnectionsResult
from openapi_server.models.list_virtual_hubs_result import ListVirtualHubsResult
from openapi_server.models.list_virtual_wans_result import ListVirtualWANsResult
from openapi_server.models.list_vpn_connections_result import ListVpnConnectionsResult
from openapi_server.models.list_vpn_gateways_result import ListVpnGatewaysResult
from openapi_server.models.list_vpn_sites_result import ListVpnSitesResult
from openapi_server.models.virtual_hub import VirtualHub
from openapi_server.models.virtual_hubs_list_default_response import VirtualHubsListDefaultResponse
from openapi_server.models.virtual_wan import VirtualWAN
from openapi_server.models.vpn_connection import VpnConnection
from openapi_server.models.vpn_gateway import VpnGateway
from openapi_server.models.vpn_site import VpnSite
from openapi_server import util


async def hub_virtual_network_connections_get(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, connection_name, api_version) -> web.Response:
    """hub_virtual_network_connections_get

    Retrieves the details of a HubVirtualNetworkConnection.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param connection_name: The name of the vpn connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def hub_virtual_network_connections_list(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, api_version) -> web.Response:
    """hub_virtual_network_connections_list

    Retrieves the details of all HubVirtualNetworkConnections.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_hubs_create_or_update(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, api_version, virtual_hub_parameters) -> web.Response:
    """virtual_hubs_create_or_update

    Creates a VirtualHub resource if it doesn&#39;t exist else updates the existing VirtualHub.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_hub_parameters: Parameters supplied to create or update VirtualHub.
    :type virtual_hub_parameters: dict | bytes

    """
    virtual_hub_parameters = VirtualHub.from_dict(virtual_hub_parameters)
    return web.Response(status=200)


async def virtual_hubs_delete(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, api_version) -> web.Response:
    """virtual_hubs_delete

    Deletes a VirtualHub.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_hubs_get(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, api_version) -> web.Response:
    """virtual_hubs_get

    Retrieves the details of a VirtualHub.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_hubs_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """virtual_hubs_list

    Lists all the VirtualHubs in a subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_hubs_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """virtual_hubs_list_by_resource_group

    Lists all the VirtualHubs in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_wans_create_or_update(request: web.Request, subscription_id, resource_group_name, virtual_wan_name, api_version, wan_parameters) -> web.Response:
    """virtual_wans_create_or_update

    Creates a VirtualWAN resource if it doesn&#39;t exist else updates the existing VirtualWAN.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualWan.
    :type resource_group_name: str
    :param virtual_wan_name: The name of the VirtualWAN being created or updated.
    :type virtual_wan_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param wan_parameters: Parameters supplied to create or update VirtualWAN.
    :type wan_parameters: dict | bytes

    """
    wan_parameters = VirtualWAN.from_dict(wan_parameters)
    return web.Response(status=200)


async def virtual_wans_delete(request: web.Request, subscription_id, resource_group_name, virtual_wan_name, api_version) -> web.Response:
    """virtual_wans_delete

    Deletes a VirtualWAN.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualWan.
    :type resource_group_name: str
    :param virtual_wan_name: The name of the VirtualWAN being deleted.
    :type virtual_wan_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_wans_get(request: web.Request, resource_group_name, virtual_wan_name, api_version, subscription_id) -> web.Response:
    """virtual_wans_get

    Retrieves the details of a VirtualWAN.

    :param resource_group_name: The resource group name of the VirtualWan.
    :type resource_group_name: str
    :param virtual_wan_name: The name of the VirtualWAN being retrieved.
    :type virtual_wan_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_wans_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """virtual_wans_list

    Lists all the VirtualWANs in a subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_wans_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """virtual_wans_list_by_resource_group

    Lists all the VirtualWANs in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualWan.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_connections_create_or_update(request: web.Request, subscription_id, resource_group_name, gateway_name, connection_name, api_version, vpn_connection_parameters) -> web.Response:
    """vpn_connections_create_or_update

    Creates a vpn connection to a scalable vpn gateway if it doesn&#39;t exist else updates the existing connection.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param connection_name: The name of the connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param vpn_connection_parameters: Parameters supplied to create or Update a VPN Connection.
    :type vpn_connection_parameters: dict | bytes

    """
    vpn_connection_parameters = VpnConnection.from_dict(vpn_connection_parameters)
    return web.Response(status=200)


async def vpn_connections_delete(request: web.Request, subscription_id, resource_group_name, gateway_name, connection_name, api_version) -> web.Response:
    """vpn_connections_delete

    Deletes a vpn connection.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param connection_name: The name of the connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_connections_get(request: web.Request, subscription_id, resource_group_name, gateway_name, connection_name, api_version) -> web.Response:
    """vpn_connections_get

    Retrieves the details of a vpn connection.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param connection_name: The name of the vpn connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_connections_list_by_vpn_gateway(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version) -> web.Response:
    """vpn_connections_list_by_vpn_gateway

    Retrieves all vpn connections for a particular virtual wan vpn gateway.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_gateways_create_or_update(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version, vpn_gateway_parameters) -> web.Response:
    """vpn_gateways_create_or_update

    Creates a virtual wan vpn gateway if it doesn&#39;t exist else updates the existing gateway.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param vpn_gateway_parameters: Parameters supplied to create or Update a virtual wan vpn gateway.
    :type vpn_gateway_parameters: dict | bytes

    """
    vpn_gateway_parameters = VpnGateway.from_dict(vpn_gateway_parameters)
    return web.Response(status=200)


async def vpn_gateways_delete(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version) -> web.Response:
    """vpn_gateways_delete

    Deletes a virtual wan vpn gateway.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_gateways_get(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version) -> web.Response:
    """vpn_gateways_get

    Retrieves the details of a virtual wan vpn gateway.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_gateways_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """vpn_gateways_list

    Lists all the VpnGateways in a subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_gateways_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """vpn_gateways_list_by_resource_group

    Lists all the VpnGateways in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_sites_configuration_download(request: web.Request, subscription_id, resource_group_name, virtual_wan_name, api_version, request) -> web.Response:
    """vpn_sites_configuration_download

    Gives the sas-url to download the configurations for vpn-sites in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param virtual_wan_name: The name of the VirtualWAN for which configuration of all vpn-sites is needed.
    :type virtual_wan_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param request: Parameters supplied to download vpn-sites configuration.
    :type request: dict | bytes

    """
    request = GetVpnSitesConfigurationRequest.from_dict(request)
    return web.Response(status=200)


async def vpn_sites_create_or_update(request: web.Request, subscription_id, resource_group_name, vpn_site_name, api_version, vpn_site_parameters) -> web.Response:
    """vpn_sites_create_or_update

    Creates a VpnSite resource if it doesn&#39;t exist else updates the existing VpnSite.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnSite.
    :type resource_group_name: str
    :param vpn_site_name: The name of the VpnSite being created or updated.
    :type vpn_site_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param vpn_site_parameters: Parameters supplied to create or update VpnSite.
    :type vpn_site_parameters: dict | bytes

    """
    vpn_site_parameters = VpnSite.from_dict(vpn_site_parameters)
    return web.Response(status=200)


async def vpn_sites_delete(request: web.Request, subscription_id, resource_group_name, vpn_site_name, api_version) -> web.Response:
    """vpn_sites_delete

    Deletes a VpnSite.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnSite.
    :type resource_group_name: str
    :param vpn_site_name: The name of the VpnSite being deleted.
    :type vpn_site_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_sites_get(request: web.Request, subscription_id, resource_group_name, vpn_site_name, api_version) -> web.Response:
    """vpn_sites_get

    Retrieves the details of a VPN site.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnSite.
    :type resource_group_name: str
    :param vpn_site_name: The name of the VpnSite being retrieved.
    :type vpn_site_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_sites_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """vpn_sites_list

    Lists all the VpnSites in a subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vpn_sites_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """vpn_sites_list_by_resource_group

    Lists all the vpnSites in a resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnSite.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
