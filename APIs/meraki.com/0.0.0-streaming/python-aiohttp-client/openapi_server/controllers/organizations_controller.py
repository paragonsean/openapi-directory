from typing import List, Dict
from aiohttp import web

from openapi_server.models.claim_into_organization_request import ClaimIntoOrganizationRequest
from openapi_server.models.clone_organization_request import CloneOrganizationRequest
from openapi_server.models.update_organization_third_party_vpn_peers_request import UpdateOrganizationThirdPartyVPNPeersRequest
from openapi_server import util


async def claim_into_organization(request: web.Request, organization_id, body=None) -> web.Response:
    """Claim a list of devices, licenses, and/or orders into an organization

    Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimIntoOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def clone_organization(request: web.Request, organization_id, body) -> web.Response:
    """Create a new organization by cloning the addressed organization

    Create a new organization by cloning the addressed organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloneOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization(request: web.Request, organization_id) -> web.Response:
    """Return an organization

    Return an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_device_statuses(request: web.Request, organization_id) -> web.Response:
    """List the status of every Meraki device in the organization

    List the status of every Meraki device in the organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_inventory(request: web.Request, organization_id, include_license_info=None) -> web.Response:
    """Return the inventory for an organization

    Return the inventory for an organization

    :param organization_id: 
    :type organization_id: str
    :param include_license_info: When this parameter is true, each entity in the response will include the license expiration date of the device (if any). Only applies to organizations that are on the per-device licensing model. Defaults to false.
    :type include_license_info: bool

    """
    return web.Response(status=200)


async def get_organization_third_party_vpn_peers(request: web.Request, organization_id) -> web.Response:
    """Return the third party VPN peers for an organization

    Return the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_uplinks_loss_and_latency(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
    """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    :type timespan: float
    :param uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    :type uplink: str
    :param ip: Optional filter for a specific destination IP. Default will return all destination IPs.
    :type ip: str

    """
    return web.Response(status=200)


async def get_organizations(request: web.Request, ) -> web.Response:
    """List the organizations that the user has privileges on

    List the organizations that the user has privileges on


    """
    return web.Response(status=200)


async def update_organization_third_party_vpn_peers(request: web.Request, organization_id, body) -> web.Response:
    """Update the third party VPN peers for an organization

    Update the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationThirdPartyVPNPeersRequest.from_dict(body)
    return web.Response(status=200)
