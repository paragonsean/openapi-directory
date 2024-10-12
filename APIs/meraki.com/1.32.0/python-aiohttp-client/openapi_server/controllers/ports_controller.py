from typing import List, Dict
from aiohttp import web

from openapi_server.models.cycle_device_switch_ports_request import CycleDeviceSwitchPortsRequest
from openapi_server.models.get_device_switch_ports200_response_inner import GetDeviceSwitchPorts200ResponseInner
from openapi_server.models.get_device_switch_ports_statuses200_response_inner import GetDeviceSwitchPortsStatuses200ResponseInner
from openapi_server.models.get_network_appliance_ports200_response_inner import GetNetworkAppliancePorts200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profile_ports200_response_inner import GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner
from openapi_server.models.get_organization_switch_ports_by_switch200_response_inner import GetOrganizationSwitchPortsBySwitch200ResponseInner
from openapi_server.models.update_device_switch_port_request import UpdateDeviceSwitchPortRequest
from openapi_server.models.update_network_appliance_port_request import UpdateNetworkAppliancePortRequest
from openapi_server.models.update_organization_config_template_switch_profile_port_request import UpdateOrganizationConfigTemplateSwitchProfilePortRequest
from openapi_server import util


async def cycle_device_switch_ports_1(request: web.Request, serial, body) -> web.Response:
    """Cycle a set of switch ports

    Cycle a set of switch ports

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CycleDeviceSwitchPortsRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_switch_port_1(request: web.Request, serial, port_id) -> web.Response:
    """Return a switch port

    Return a switch port

    :param serial: 
    :type serial: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_device_switch_ports_1(request: web.Request, serial) -> web.Response:
    """List the switch ports for a switch

    List the switch ports for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_1(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the status for all the ports of a switch

    Return the status for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_packets_1(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the packet counters for all the ports of a switch

    Return the packet counters for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_appliance_port_1(request: web.Request, network_id, port_id) -> web.Response:
    """Return per-port VLAN settings for a single MX port.

    Return per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_ports_1(request: web.Request, network_id) -> web.Response:
    """List per-port VLAN settings for all ports of a MX.

    List per-port VLAN settings for all ports of a MX.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_port_3(request: web.Request, organization_id, config_template_id, profile_id, port_id) -> web.Response:
    """Return a switch profile port

    Return a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_ports_3(request: web.Request, organization_id, config_template_id, profile_id) -> web.Response:
    """Return all the ports of a switch profile

    Return all the ports of a switch profile

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_organization_switch_ports_by_switch_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, port_profile_ids=None, name=None, mac=None, macs=None, serial=None, serials=None, configuration_updated_after=None) -> web.Response:
    """List the switchports in an organization by switch

    List the switchports in an organization by switch

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter switchports by network.
    :type network_ids: List[str]
    :param port_profile_ids: Optional parameter to filter switchports belonging to the specified switchport profiles.
    :type port_profile_ids: List[str]
    :param name: Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
    :type name: str
    :param mac: Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
    :type mac: str
    :param macs: Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    :type macs: List[str]
    :param serial: Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
    :type serial: str
    :param serials: Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    :type serials: List[str]
    :param configuration_updated_after: Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
    :type configuration_updated_after: str

    """
    return web.Response(status=200)


async def update_device_switch_port_1(request: web.Request, serial, port_id, body=None) -> web.Response:
    """Update a switch port

    Update a switch port

    :param serial: 
    :type serial: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchPortRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_port_1(request: web.Request, network_id, port_id, body=None) -> web.Response:
    """Update the per-port VLAN settings for a single MX port.

    Update the per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAppliancePortRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_config_template_switch_profile_port_3(request: web.Request, organization_id, config_template_id, profile_id, port_id, body=None) -> web.Response:
    """Update a switch profile port

    Update a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationConfigTemplateSwitchProfilePortRequest.from_dict(body)
    return web.Response(status=200)
