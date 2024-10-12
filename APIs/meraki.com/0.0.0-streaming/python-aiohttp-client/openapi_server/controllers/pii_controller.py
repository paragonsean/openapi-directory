from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest
from openapi_server import util


async def create_network_pii_request(request: web.Request, network_id, body=None) -> web.Response:
    """Submit a new delete or restrict processing PII request

    Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkPiiRequestRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_pii_request(request: web.Request, network_id, request_id) -> web.Response:
    """Delete a restrict processing PII request

    Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def get_network_pii_pii_keys(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """List the keys required to access Personally Identifiable Information (PII) for a given identifier

    List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)


async def get_network_pii_request(request: web.Request, network_id, request_id) -> web.Response:
    """Return a PII request

    Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def get_network_pii_requests(request: web.Request, network_id) -> web.Response:
    """List the PII requests for this network or organization

    List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_pii_sm_devices_for_key(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smDevicesForKey &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)


async def get_network_pii_sm_owners_for_key(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smOwnersForKey &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)
