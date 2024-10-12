from typing import List, Dict
from aiohttp import web

from openapi_server.models.bind_network_request import BindNetworkRequest
from openapi_server.models.combine_organization_networks_request import CombineOrganizationNetworksRequest
from openapi_server.models.create_organization_network_request import CreateOrganizationNetworkRequest
from openapi_server.models.update_network_request import UpdateNetworkRequest
from openapi_server.models.update_network_site_to_site_vpn_request import UpdateNetworkSiteToSiteVpnRequest
from openapi_server import util


async def bind_network(request: web.Request, network_id, body) -> web.Response:
    """Bind a network to a template.

    Bind a network to a template.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BindNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def combine_organization_networks(request: web.Request, organization_id, body) -> web.Response:
    """Combine multiple networks into a single network

    Combine multiple networks into a single network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CombineOrganizationNetworksRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_network(request: web.Request, organization_id, body) -> web.Response:
    """Create a network

    Create a network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network(request: web.Request, network_id) -> web.Response:
    """Delete a network

    Delete a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network(request: web.Request, network_id) -> web.Response:
    """Return a network

    Return a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_air_marshal(request: web.Request, network_id, t0=None, timespan=None) -> web.Response:
    """List Air Marshal scan results from a network

    List Air Marshal scan results from a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_site_to_site_vpn(request: web.Request, network_id) -> web.Response:
    """Return the site-to-site VPN settings of a network

    Return the site-to-site VPN settings of a network. Only valid for MX networks.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic(request: web.Request, network_id, t0=None, timespan=None, device_type=None) -> web.Response:
    """Return the traffic analysis data for this network

    Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
    :type timespan: float
    :param device_type: Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage.
    :type device_type: str

    """
    return web.Response(status=200)


async def get_organization_networks(request: web.Request, organization_id, config_template_id=None) -> web.Response:
    """List the networks in an organization

    List the networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: An optional parameter that is the ID of a config template. Will return all networks bound to that template.
    :type config_template_id: str

    """
    return web.Response(status=200)


async def split_network(request: web.Request, network_id) -> web.Response:
    """Split a combined network into individual networks for each type of device

    Split a combined network into individual networks for each type of device

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def unbind_network(request: web.Request, network_id) -> web.Response:
    """Unbind a network from a template.

    Unbind a network from a template.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network(request: web.Request, network_id, body=None) -> web.Response:
    """Update a network

    Update a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_site_to_site_vpn(request: web.Request, network_id, body) -> web.Response:
    """Update the site-to-site VPN settings of a network

    Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSiteToSiteVpnRequest.from_dict(body)
    return web.Response(status=200)
