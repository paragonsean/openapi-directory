from typing import List, Dict
from aiohttp import web

from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.cycle_device_switch_ports_request import CycleDeviceSwitchPortsRequest
from openapi_server.models.update_network_device_request import UpdateNetworkDeviceRequest
from openapi_server import util


async def claim_network_devices(request: web.Request, network_id, body=None) -> web.Response:
    """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed)

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed)

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimNetworkDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def cycle_device_switch_ports(request: web.Request, serial, body) -> web.Response:
    """Cycle a set of switch ports

    Cycle a set of switch ports

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CycleDeviceSwitchPortsRequest.from_dict(body)
    return web.Response(status=200)


async def get_network_device(request: web.Request, network_id, serial) -> web.Response:
    """Return a single device

    Return a single device

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_device_loss_and_latency_history(request: web.Request, network_id, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None) -> web.Response:
    """Get the uplink loss percentage and latency in milliseconds for a wired network device.

    Get the uplink loss percentage and latency in milliseconds for a wired network device.

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str
    :param ip: The destination IP used to obtain the requested stats. This is required.
    :type ip: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    :type resolution: int
    :param uplink: The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    :type uplink: str

    """
    return web.Response(status=200)


async def get_network_device_performance(request: web.Request, network_id, serial) -> web.Response:
    """Return the performance score for a single MX

    Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_device_uplink(request: web.Request, network_id, serial) -> web.Response:
    """Return the uplink information for a device.

    Return the uplink information for a device.

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_devices(request: web.Request, network_id) -> web.Response:
    """List the devices in a network

    List the devices in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_devices(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, configuration_updated_after=None) -> web.Response:
    """List the devices in an organization

    List the devices in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param configuration_updated_after: Filter results by whether or not the device&#39;s configuration has been updated after the given timestamp
    :type configuration_updated_after: str

    """
    return web.Response(status=200)


async def reboot_network_device(request: web.Request, network_id, serial) -> web.Response:
    """Reboot a device

    Reboot a device

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def remove_network_device(request: web.Request, network_id, serial) -> web.Response:
    """Remove a single device

    Remove a single device

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_network_device(request: web.Request, network_id, serial, body=None) -> web.Response:
    """Update the attributes of a device

    Update the attributes of a device

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkDeviceRequest.from_dict(body)
    return web.Response(status=200)
