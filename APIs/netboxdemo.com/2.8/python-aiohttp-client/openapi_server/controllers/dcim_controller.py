from typing import List, Dict
from aiohttp import web

from openapi_server.models.cable import Cable
from openapi_server.models.console_port import ConsolePort
from openapi_server.models.console_port_template import ConsolePortTemplate
from openapi_server.models.console_server_port import ConsoleServerPort
from openapi_server.models.console_server_port_template import ConsoleServerPortTemplate
from openapi_server.models.dcim_cables_list200_response import DcimCablesList200Response
from openapi_server.models.dcim_console_connections_list200_response import DcimConsoleConnectionsList200Response
from openapi_server.models.dcim_console_port_templates_list200_response import DcimConsolePortTemplatesList200Response
from openapi_server.models.dcim_console_server_port_templates_list200_response import DcimConsoleServerPortTemplatesList200Response
from openapi_server.models.dcim_console_server_ports_list200_response import DcimConsoleServerPortsList200Response
from openapi_server.models.dcim_device_bay_templates_list200_response import DcimDeviceBayTemplatesList200Response
from openapi_server.models.dcim_device_bays_list200_response import DcimDeviceBaysList200Response
from openapi_server.models.dcim_device_roles_list200_response import DcimDeviceRolesList200Response
from openapi_server.models.dcim_device_types_list200_response import DcimDeviceTypesList200Response
from openapi_server.models.dcim_devices_list200_response import DcimDevicesList200Response
from openapi_server.models.dcim_front_port_templates_list200_response import DcimFrontPortTemplatesList200Response
from openapi_server.models.dcim_front_ports_list200_response import DcimFrontPortsList200Response
from openapi_server.models.dcim_interface_connections_list200_response import DcimInterfaceConnectionsList200Response
from openapi_server.models.dcim_interface_templates_list200_response import DcimInterfaceTemplatesList200Response
from openapi_server.models.dcim_interfaces_list200_response import DcimInterfacesList200Response
from openapi_server.models.dcim_inventory_items_list200_response import DcimInventoryItemsList200Response
from openapi_server.models.dcim_manufacturers_list200_response import DcimManufacturersList200Response
from openapi_server.models.dcim_platforms_list200_response import DcimPlatformsList200Response
from openapi_server.models.dcim_power_connections_list200_response import DcimPowerConnectionsList200Response
from openapi_server.models.dcim_power_feeds_list200_response import DcimPowerFeedsList200Response
from openapi_server.models.dcim_power_outlet_templates_list200_response import DcimPowerOutletTemplatesList200Response
from openapi_server.models.dcim_power_outlets_list200_response import DcimPowerOutletsList200Response
from openapi_server.models.dcim_power_panels_list200_response import DcimPowerPanelsList200Response
from openapi_server.models.dcim_power_port_templates_list200_response import DcimPowerPortTemplatesList200Response
from openapi_server.models.dcim_rack_groups_list200_response import DcimRackGroupsList200Response
from openapi_server.models.dcim_rack_reservations_list200_response import DcimRackReservationsList200Response
from openapi_server.models.dcim_rack_roles_list200_response import DcimRackRolesList200Response
from openapi_server.models.dcim_racks_list200_response import DcimRacksList200Response
from openapi_server.models.dcim_rear_port_templates_list200_response import DcimRearPortTemplatesList200Response
from openapi_server.models.dcim_rear_ports_list200_response import DcimRearPortsList200Response
from openapi_server.models.dcim_regions_list200_response import DcimRegionsList200Response
from openapi_server.models.dcim_sites_list200_response import DcimSitesList200Response
from openapi_server.models.dcim_virtual_chassis_list200_response import DcimVirtualChassisList200Response
from openapi_server.models.device import Device
from openapi_server.models.device_bay import DeviceBay
from openapi_server.models.device_bay_template import DeviceBayTemplate
from openapi_server.models.device_interface import DeviceInterface
from openapi_server.models.device_napalm import DeviceNAPALM
from openapi_server.models.device_role import DeviceRole
from openapi_server.models.device_type import DeviceType
from openapi_server.models.device_with_config_context import DeviceWithConfigContext
from openapi_server.models.front_port import FrontPort
from openapi_server.models.front_port_template import FrontPortTemplate
from openapi_server.models.interface_template import InterfaceTemplate
from openapi_server.models.inventory_item import InventoryItem
from openapi_server.models.manufacturer import Manufacturer
from openapi_server.models.platform import Platform
from openapi_server.models.power_feed import PowerFeed
from openapi_server.models.power_outlet import PowerOutlet
from openapi_server.models.power_outlet_template import PowerOutletTemplate
from openapi_server.models.power_panel import PowerPanel
from openapi_server.models.power_port import PowerPort
from openapi_server.models.power_port_template import PowerPortTemplate
from openapi_server.models.rack import Rack
from openapi_server.models.rack_group import RackGroup
from openapi_server.models.rack_reservation import RackReservation
from openapi_server.models.rack_role import RackRole
from openapi_server.models.rack_unit import RackUnit
from openapi_server.models.rear_port import RearPort
from openapi_server.models.rear_port_template import RearPortTemplate
from openapi_server.models.region import Region
from openapi_server.models.site import Site
from openapi_server.models.virtual_chassis import VirtualChassis
from openapi_server.models.writable_cable import WritableCable
from openapi_server.models.writable_console_port import WritableConsolePort
from openapi_server.models.writable_console_port_template import WritableConsolePortTemplate
from openapi_server.models.writable_console_server_port import WritableConsoleServerPort
from openapi_server.models.writable_console_server_port_template import WritableConsoleServerPortTemplate
from openapi_server.models.writable_device_bay import WritableDeviceBay
from openapi_server.models.writable_device_bay_template import WritableDeviceBayTemplate
from openapi_server.models.writable_device_interface import WritableDeviceInterface
from openapi_server.models.writable_device_type import WritableDeviceType
from openapi_server.models.writable_device_with_config_context import WritableDeviceWithConfigContext
from openapi_server.models.writable_front_port import WritableFrontPort
from openapi_server.models.writable_front_port_template import WritableFrontPortTemplate
from openapi_server.models.writable_interface_template import WritableInterfaceTemplate
from openapi_server.models.writable_inventory_item import WritableInventoryItem
from openapi_server.models.writable_platform import WritablePlatform
from openapi_server.models.writable_power_feed import WritablePowerFeed
from openapi_server.models.writable_power_outlet import WritablePowerOutlet
from openapi_server.models.writable_power_outlet_template import WritablePowerOutletTemplate
from openapi_server.models.writable_power_panel import WritablePowerPanel
from openapi_server.models.writable_power_port import WritablePowerPort
from openapi_server.models.writable_power_port_template import WritablePowerPortTemplate
from openapi_server.models.writable_rack import WritableRack
from openapi_server.models.writable_rack_group import WritableRackGroup
from openapi_server.models.writable_rack_reservation import WritableRackReservation
from openapi_server.models.writable_rear_port import WritableRearPort
from openapi_server.models.writable_rear_port_template import WritableRearPortTemplate
from openapi_server.models.writable_region import WritableRegion
from openapi_server.models.writable_site import WritableSite
from openapi_server.models.writable_virtual_chassis import WritableVirtualChassis
from openapi_server import util


async def dcim_cables_create(request: web.Request, body) -> web.Response:
    """dcim_cables_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCable.from_dict(body)
    return web.Response(status=200)


async def dcim_cables_delete(request: web.Request, id) -> web.Response:
    """dcim_cables_delete

    

    :param id: A unique integer value identifying this cable.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_cables_list(request: web.Request, id=None, label=None, length=None, length_unit=None, q=None, type=None, status=None, color=None, device_id=None, device=None, rack_id=None, rack=None, site_id=None, site=None, tenant_id=None, tenant=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, length__n=None, length__lte=None, length__lt=None, length__gte=None, length__gt=None, length_unit__n=None, type__n=None, status__n=None, color__n=None, limit=None, offset=None) -> web.Response:
    """dcim_cables_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param label: 
    :type label: str
    :param length: 
    :type length: str
    :param length_unit: 
    :type length_unit: str
    :param q: 
    :type q: str
    :param type: 
    :type type: str
    :param status: 
    :type status: str
    :param color: 
    :type color: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param label__n: 
    :type label__n: str
    :param label__ic: 
    :type label__ic: str
    :param label__nic: 
    :type label__nic: str
    :param label__iew: 
    :type label__iew: str
    :param label__niew: 
    :type label__niew: str
    :param label__isw: 
    :type label__isw: str
    :param label__nisw: 
    :type label__nisw: str
    :param label__ie: 
    :type label__ie: str
    :param label__nie: 
    :type label__nie: str
    :param length__n: 
    :type length__n: str
    :param length__lte: 
    :type length__lte: str
    :param length__lt: 
    :type length__lt: str
    :param length__gte: 
    :type length__gte: str
    :param length__gt: 
    :type length__gt: str
    :param length_unit__n: 
    :type length_unit__n: str
    :param type__n: 
    :type type__n: str
    :param status__n: 
    :type status__n: str
    :param color__n: 
    :type color__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_cables_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_cables_partial_update

    

    :param id: A unique integer value identifying this cable.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCable.from_dict(body)
    return web.Response(status=200)


async def dcim_cables_read(request: web.Request, id) -> web.Response:
    """dcim_cables_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this cable.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_cables_update(request: web.Request, id, body) -> web.Response:
    """dcim_cables_update

    

    :param id: A unique integer value identifying this cable.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCable.from_dict(body)
    return web.Response(status=200)


async def dcim_connected_device_list(request: web.Request, peer_device, peer_interface) -> web.Response:
    """dcim_connected_device_list

    This endpoint allows a user to determine what device (if any) is connected to a given peer device and peer interface. This is useful in a situation where a device boots with no configuration, but can detect its neighbors via a protocol such as LLDP. Two query parameters must be included in the request:  * &#x60;peer_device&#x60;: The name of the peer device * &#x60;peer_interface&#x60;: The name of the peer interface

    :param peer_device: The name of the peer device
    :type peer_device: str
    :param peer_interface: The name of the peer interface
    :type peer_interface: str

    """
    return web.Response(status=200)


async def dcim_console_connections_list(request: web.Request, name=None, connection_status=None, site=None, device_id=None, device=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, connection_status__n=None, limit=None, offset=None) -> web.Response:
    """dcim_console_connections_list

    

    :param name: 
    :type name: str
    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_console_port_templates_create(request: web.Request, body) -> web.Response:
    """dcim_console_port_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_port_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_console_port_templates_delete

    

    :param id: A unique integer value identifying this console port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_port_templates_list(request: web.Request, id=None, name=None, type=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_console_port_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_console_port_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_port_templates_partial_update

    

    :param id: A unique integer value identifying this console port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_port_templates_read(request: web.Request, id) -> web.Response:
    """dcim_console_port_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this console port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_port_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_port_templates_update

    

    :param id: A unique integer value identifying this console port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_ports_create(request: web.Request, body) -> web.Response:
    """dcim_console_ports_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_ports_delete(request: web.Request, id) -> web.Response:
    """dcim_console_ports_delete

    

    :param id: A unique integer value identifying this console port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_ports_list(request: web.Request, id=None, name=None, description=None, connection_status=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, type=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, connection_status__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, type__n=None, limit=None, offset=None) -> web.Response:
    """dcim_console_ports_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param connection_status: 
    :type connection_status: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_console_ports_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_ports_partial_update

    

    :param id: A unique integer value identifying this console port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_ports_read(request: web.Request, id) -> web.Response:
    """dcim_console_ports_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this console port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_ports_trace(request: web.Request, id) -> web.Response:
    """dcim_console_ports_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this console port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_ports_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_ports_update

    

    :param id: A unique integer value identifying this console port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_port_templates_create(request: web.Request, body) -> web.Response:
    """dcim_console_server_port_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_port_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_console_server_port_templates_delete

    

    :param id: A unique integer value identifying this console server port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_server_port_templates_list(request: web.Request, id=None, name=None, type=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_port_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_console_server_port_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_server_port_templates_partial_update

    

    :param id: A unique integer value identifying this console server port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_port_templates_read(request: web.Request, id) -> web.Response:
    """dcim_console_server_port_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this console server port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_server_port_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_server_port_templates_update

    

    :param id: A unique integer value identifying this console server port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_ports_create(request: web.Request, body) -> web.Response:
    """dcim_console_server_ports_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_ports_delete(request: web.Request, id) -> web.Response:
    """dcim_console_server_ports_delete

    

    :param id: A unique integer value identifying this console server port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_server_ports_list(request: web.Request, id=None, name=None, description=None, connection_status=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, type=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, connection_status__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, type__n=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_ports_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param connection_status: 
    :type connection_status: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_console_server_ports_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_server_ports_partial_update

    

    :param id: A unique integer value identifying this console server port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_ports_read(request: web.Request, id) -> web.Response:
    """dcim_console_server_ports_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this console server port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_server_ports_trace(request: web.Request, id) -> web.Response:
    """dcim_console_server_ports_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this console server port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_console_server_ports_update(request: web.Request, id, body) -> web.Response:
    """dcim_console_server_ports_update

    

    :param id: A unique integer value identifying this console server port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bay_templates_create(request: web.Request, body) -> web.Response:
    """dcim_device_bay_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bay_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_device_bay_templates_delete

    

    :param id: A unique integer value identifying this device bay template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_bay_templates_list(request: web.Request, id=None, name=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bay_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_device_bay_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_bay_templates_partial_update

    

    :param id: A unique integer value identifying this device bay template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bay_templates_read(request: web.Request, id) -> web.Response:
    """dcim_device_bay_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this device bay template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_bay_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_bay_templates_update

    

    :param id: A unique integer value identifying this device bay template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bays_create(request: web.Request, body) -> web.Response:
    """dcim_device_bays_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBay.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bays_delete(request: web.Request, id) -> web.Response:
    """dcim_device_bays_delete

    

    :param id: A unique integer value identifying this device bay.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_bays_list(request: web.Request, id=None, name=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bays_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_device_bays_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_bays_partial_update

    

    :param id: A unique integer value identifying this device bay.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBay.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bays_read(request: web.Request, id) -> web.Response:
    """dcim_device_bays_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this device bay.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_bays_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_bays_update

    

    :param id: A unique integer value identifying this device bay.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBay.from_dict(body)
    return web.Response(status=200)


async def dcim_device_roles_create(request: web.Request, body) -> web.Response:
    """dcim_device_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeviceRole.from_dict(body)
    return web.Response(status=200)


async def dcim_device_roles_delete(request: web.Request, id) -> web.Response:
    """dcim_device_roles_delete

    

    :param id: A unique integer value identifying this device role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_roles_list(request: web.Request, id=None, name=None, slug=None, color=None, vm_role=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, limit=None, offset=None) -> web.Response:
    """dcim_device_roles_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param vm_role: 
    :type vm_role: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param color__n: 
    :type color__n: str
    :param color__ic: 
    :type color__ic: str
    :param color__nic: 
    :type color__nic: str
    :param color__iew: 
    :type color__iew: str
    :param color__niew: 
    :type color__niew: str
    :param color__isw: 
    :type color__isw: str
    :param color__nisw: 
    :type color__nisw: str
    :param color__ie: 
    :type color__ie: str
    :param color__nie: 
    :type color__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_device_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_roles_partial_update

    

    :param id: A unique integer value identifying this device role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceRole.from_dict(body)
    return web.Response(status=200)


async def dcim_device_roles_read(request: web.Request, id) -> web.Response:
    """dcim_device_roles_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this device role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_roles_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_roles_update

    

    :param id: A unique integer value identifying this device role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceRole.from_dict(body)
    return web.Response(status=200)


async def dcim_device_types_create(request: web.Request, body) -> web.Response:
    """dcim_device_types_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceType.from_dict(body)
    return web.Response(status=200)


async def dcim_device_types_delete(request: web.Request, id) -> web.Response:
    """dcim_device_types_delete

    

    :param id: A unique integer value identifying this device type.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_types_list(request: web.Request, id=None, model=None, slug=None, part_number=None, u_height=None, is_full_depth=None, subdevice_role=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, manufacturer_id=None, manufacturer=None, console_ports=None, console_server_ports=None, power_ports=None, power_outlets=None, interfaces=None, pass_through_ports=None, device_bays=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, model__n=None, model__ic=None, model__nic=None, model__iew=None, model__niew=None, model__isw=None, model__nisw=None, model__ie=None, model__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, part_number__n=None, part_number__ic=None, part_number__nic=None, part_number__iew=None, part_number__niew=None, part_number__isw=None, part_number__nisw=None, part_number__ie=None, part_number__nie=None, u_height__n=None, u_height__lte=None, u_height__lt=None, u_height__gte=None, u_height__gt=None, subdevice_role__n=None, manufacturer_id__n=None, manufacturer__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_device_types_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param model: 
    :type model: str
    :param slug: 
    :type slug: str
    :param part_number: 
    :type part_number: str
    :param u_height: 
    :type u_height: str
    :param is_full_depth: 
    :type is_full_depth: str
    :param subdevice_role: 
    :type subdevice_role: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param console_ports: 
    :type console_ports: str
    :param console_server_ports: 
    :type console_server_ports: str
    :param power_ports: 
    :type power_ports: str
    :param power_outlets: 
    :type power_outlets: str
    :param interfaces: 
    :type interfaces: str
    :param pass_through_ports: 
    :type pass_through_ports: str
    :param device_bays: 
    :type device_bays: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param model__n: 
    :type model__n: str
    :param model__ic: 
    :type model__ic: str
    :param model__nic: 
    :type model__nic: str
    :param model__iew: 
    :type model__iew: str
    :param model__niew: 
    :type model__niew: str
    :param model__isw: 
    :type model__isw: str
    :param model__nisw: 
    :type model__nisw: str
    :param model__ie: 
    :type model__ie: str
    :param model__nie: 
    :type model__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param part_number__n: 
    :type part_number__n: str
    :param part_number__ic: 
    :type part_number__ic: str
    :param part_number__nic: 
    :type part_number__nic: str
    :param part_number__iew: 
    :type part_number__iew: str
    :param part_number__niew: 
    :type part_number__niew: str
    :param part_number__isw: 
    :type part_number__isw: str
    :param part_number__nisw: 
    :type part_number__nisw: str
    :param part_number__ie: 
    :type part_number__ie: str
    :param part_number__nie: 
    :type part_number__nie: str
    :param u_height__n: 
    :type u_height__n: str
    :param u_height__lte: 
    :type u_height__lte: str
    :param u_height__lt: 
    :type u_height__lt: str
    :param u_height__gte: 
    :type u_height__gte: str
    :param u_height__gt: 
    :type u_height__gt: str
    :param subdevice_role__n: 
    :type subdevice_role__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_device_types_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_types_partial_update

    

    :param id: A unique integer value identifying this device type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceType.from_dict(body)
    return web.Response(status=200)


async def dcim_device_types_read(request: web.Request, id) -> web.Response:
    """dcim_device_types_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this device type.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_device_types_update(request: web.Request, id, body) -> web.Response:
    """dcim_device_types_update

    

    :param id: A unique integer value identifying this device type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceType.from_dict(body)
    return web.Response(status=200)


async def dcim_devices_create(request: web.Request, body) -> web.Response:
    """dcim_devices_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def dcim_devices_delete(request: web.Request, id) -> web.Response:
    """dcim_devices_delete

    

    :param id: A unique integer value identifying this device.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_devices_graphs(request: web.Request, id) -> web.Response:
    """dcim_devices_graphs

    A convenience method for rendering graphs for a particular Device.

    :param id: A unique integer value identifying this device.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_devices_list(request: web.Request, id=None, name=None, asset_tag=None, face=None, position=None, vc_position=None, vc_priority=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, local_context_data=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, manufacturer_id=None, manufacturer=None, device_type_id=None, role_id=None, role=None, platform_id=None, platform=None, region_id=None, region=None, site_id=None, site=None, rack_group_id=None, rack_id=None, cluster_id=None, model=None, status=None, is_full_depth=None, mac_address=None, serial=None, has_primary_ip=None, virtual_chassis_id=None, virtual_chassis_member=None, console_ports=None, console_server_ports=None, power_ports=None, power_outlets=None, interfaces=None, pass_through_ports=None, device_bays=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, face__n=None, position__n=None, position__lte=None, position__lt=None, position__gte=None, position__gt=None, vc_position__n=None, vc_position__lte=None, vc_position__lt=None, vc_position__gte=None, vc_position__gt=None, vc_priority__n=None, vc_priority__lte=None, vc_priority__lt=None, vc_priority__gte=None, vc_priority__gt=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, manufacturer_id__n=None, manufacturer__n=None, device_type_id__n=None, role_id__n=None, role__n=None, platform_id__n=None, platform__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, rack_group_id__n=None, rack_id__n=None, cluster_id__n=None, model__n=None, status__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, virtual_chassis_id__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_devices_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param asset_tag: 
    :type asset_tag: str
    :param face: 
    :type face: str
    :param position: 
    :type position: str
    :param vc_position: 
    :type vc_position: str
    :param vc_priority: 
    :type vc_priority: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param local_context_data: 
    :type local_context_data: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param device_type_id: 
    :type device_type_id: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param rack_group_id: 
    :type rack_group_id: str
    :param rack_id: 
    :type rack_id: str
    :param cluster_id: 
    :type cluster_id: str
    :param model: 
    :type model: str
    :param status: 
    :type status: str
    :param is_full_depth: 
    :type is_full_depth: str
    :param mac_address: 
    :type mac_address: str
    :param serial: 
    :type serial: str
    :param has_primary_ip: 
    :type has_primary_ip: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis_member: 
    :type virtual_chassis_member: str
    :param console_ports: 
    :type console_ports: str
    :param console_server_ports: 
    :type console_server_ports: str
    :param power_ports: 
    :type power_ports: str
    :param power_outlets: 
    :type power_outlets: str
    :param interfaces: 
    :type interfaces: str
    :param pass_through_ports: 
    :type pass_through_ports: str
    :param device_bays: 
    :type device_bays: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param asset_tag__n: 
    :type asset_tag__n: str
    :param asset_tag__ic: 
    :type asset_tag__ic: str
    :param asset_tag__nic: 
    :type asset_tag__nic: str
    :param asset_tag__iew: 
    :type asset_tag__iew: str
    :param asset_tag__niew: 
    :type asset_tag__niew: str
    :param asset_tag__isw: 
    :type asset_tag__isw: str
    :param asset_tag__nisw: 
    :type asset_tag__nisw: str
    :param asset_tag__ie: 
    :type asset_tag__ie: str
    :param asset_tag__nie: 
    :type asset_tag__nie: str
    :param face__n: 
    :type face__n: str
    :param position__n: 
    :type position__n: str
    :param position__lte: 
    :type position__lte: str
    :param position__lt: 
    :type position__lt: str
    :param position__gte: 
    :type position__gte: str
    :param position__gt: 
    :type position__gt: str
    :param vc_position__n: 
    :type vc_position__n: str
    :param vc_position__lte: 
    :type vc_position__lte: str
    :param vc_position__lt: 
    :type vc_position__lt: str
    :param vc_position__gte: 
    :type vc_position__gte: str
    :param vc_position__gt: 
    :type vc_position__gt: str
    :param vc_priority__n: 
    :type vc_priority__n: str
    :param vc_priority__lte: 
    :type vc_priority__lte: str
    :param vc_priority__lt: 
    :type vc_priority__lt: str
    :param vc_priority__gte: 
    :type vc_priority__gte: str
    :param vc_priority__gt: 
    :type vc_priority__gt: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param device_type_id__n: 
    :type device_type_id__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param platform_id__n: 
    :type platform_id__n: str
    :param platform__n: 
    :type platform__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param rack_group_id__n: 
    :type rack_group_id__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param cluster_id__n: 
    :type cluster_id__n: str
    :param model__n: 
    :type model__n: str
    :param status__n: 
    :type status__n: str
    :param mac_address__n: 
    :type mac_address__n: str
    :param mac_address__ic: 
    :type mac_address__ic: str
    :param mac_address__nic: 
    :type mac_address__nic: str
    :param mac_address__iew: 
    :type mac_address__iew: str
    :param mac_address__niew: 
    :type mac_address__niew: str
    :param mac_address__isw: 
    :type mac_address__isw: str
    :param mac_address__nisw: 
    :type mac_address__nisw: str
    :param mac_address__ie: 
    :type mac_address__ie: str
    :param mac_address__nie: 
    :type mac_address__nie: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_devices_napalm(request: web.Request, id, method) -> web.Response:
    """dcim_devices_napalm

    Execute a NAPALM method on a Device

    :param id: A unique integer value identifying this device.
    :type id: int
    :param method: 
    :type method: str

    """
    return web.Response(status=200)


async def dcim_devices_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_devices_partial_update

    

    :param id: A unique integer value identifying this device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def dcim_devices_read(request: web.Request, id) -> web.Response:
    """dcim_devices_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this device.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_devices_update(request: web.Request, id, body) -> web.Response:
    """dcim_devices_update

    

    :param id: A unique integer value identifying this device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def dcim_front_port_templates_create(request: web.Request, body) -> web.Response:
    """dcim_front_port_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_front_port_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_front_port_templates_delete

    

    :param id: A unique integer value identifying this front port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_port_templates_list(request: web.Request, id=None, name=None, type=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_front_port_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_front_port_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_front_port_templates_partial_update

    

    :param id: A unique integer value identifying this front port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_front_port_templates_read(request: web.Request, id) -> web.Response:
    """dcim_front_port_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this front port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_port_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_front_port_templates_update

    

    :param id: A unique integer value identifying this front port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_front_ports_create(request: web.Request, body) -> web.Response:
    """dcim_front_ports_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPort.from_dict(body)
    return web.Response(status=200)


async def dcim_front_ports_delete(request: web.Request, id) -> web.Response:
    """dcim_front_ports_delete

    

    :param id: A unique integer value identifying this front port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_ports_list(request: web.Request, id=None, name=None, type=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_front_ports_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_front_ports_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_front_ports_partial_update

    

    :param id: A unique integer value identifying this front port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPort.from_dict(body)
    return web.Response(status=200)


async def dcim_front_ports_read(request: web.Request, id) -> web.Response:
    """dcim_front_ports_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this front port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_ports_trace(request: web.Request, id) -> web.Response:
    """dcim_front_ports_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this front port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_ports_update(request: web.Request, id, body) -> web.Response:
    """dcim_front_ports_update

    

    :param id: A unique integer value identifying this front port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPort.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_connections_list(request: web.Request, connection_status=None, site=None, device_id=None, device=None, connection_status__n=None, limit=None, offset=None) -> web.Response:
    """dcim_interface_connections_list

    

    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_interface_templates_create(request: web.Request, body) -> web.Response:
    """dcim_interface_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_interface_templates_delete

    

    :param id: A unique integer value identifying this interface template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interface_templates_list(request: web.Request, id=None, name=None, type=None, mgmt_only=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_interface_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param mgmt_only: 
    :type mgmt_only: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_interface_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_interface_templates_partial_update

    

    :param id: A unique integer value identifying this interface template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_templates_read(request: web.Request, id) -> web.Response:
    """dcim_interface_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this interface template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interface_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_interface_templates_update

    

    :param id: A unique integer value identifying this interface template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_create(request: web.Request, body) -> web.Response:
    """dcim_interfaces_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_delete(request: web.Request, id) -> web.Response:
    """dcim_interfaces_delete

    

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_graphs(request: web.Request, id) -> web.Response:
    """dcim_interfaces_graphs

    A convenience method for rendering graphs for a particular interface.

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_list(request: web.Request, id=None, name=None, connection_status=None, type=None, enabled=None, mtu=None, mgmt_only=None, mode=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, cabled=None, kind=None, lag_id=None, mac_address=None, vlan_id=None, vlan=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, connection_status__n=None, type__n=None, mtu__n=None, mtu__lte=None, mtu__lt=None, mtu__gte=None, mtu__gt=None, mode__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, tag__n=None, lag_id__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, limit=None, offset=None) -> web.Response:
    """dcim_interfaces_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param connection_status: 
    :type connection_status: str
    :param type: 
    :type type: str
    :param enabled: 
    :type enabled: str
    :param mtu: 
    :type mtu: str
    :param mgmt_only: 
    :type mgmt_only: str
    :param mode: 
    :type mode: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param kind: 
    :type kind: str
    :param lag_id: 
    :type lag_id: str
    :param mac_address: 
    :type mac_address: str
    :param vlan_id: 
    :type vlan_id: str
    :param vlan: 
    :type vlan: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param type__n: 
    :type type__n: str
    :param mtu__n: 
    :type mtu__n: str
    :param mtu__lte: 
    :type mtu__lte: str
    :param mtu__lt: 
    :type mtu__lt: str
    :param mtu__gte: 
    :type mtu__gte: str
    :param mtu__gt: 
    :type mtu__gt: str
    :param mode__n: 
    :type mode__n: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param tag__n: 
    :type tag__n: str
    :param lag_id__n: 
    :type lag_id__n: str
    :param mac_address__n: 
    :type mac_address__n: str
    :param mac_address__ic: 
    :type mac_address__ic: str
    :param mac_address__nic: 
    :type mac_address__nic: str
    :param mac_address__iew: 
    :type mac_address__iew: str
    :param mac_address__niew: 
    :type mac_address__niew: str
    :param mac_address__isw: 
    :type mac_address__isw: str
    :param mac_address__nisw: 
    :type mac_address__nisw: str
    :param mac_address__ie: 
    :type mac_address__ie: str
    :param mac_address__nie: 
    :type mac_address__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_interfaces_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_interfaces_partial_update

    

    :param id: A unique integer value identifying this interface.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_read(request: web.Request, id) -> web.Response:
    """dcim_interfaces_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_trace(request: web.Request, id) -> web.Response:
    """dcim_interfaces_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_update(request: web.Request, id, body) -> web.Response:
    """dcim_interfaces_update

    

    :param id: A unique integer value identifying this interface.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_items_create(request: web.Request, body) -> web.Response:
    """dcim_inventory_items_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItem.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_items_delete(request: web.Request, id) -> web.Response:
    """dcim_inventory_items_delete

    

    :param id: A unique integer value identifying this inventory item.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_items_list(request: web.Request, id=None, name=None, part_id=None, asset_tag=None, discovered=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, parent_id=None, manufacturer_id=None, manufacturer=None, serial=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, part_id__n=None, part_id__ic=None, part_id__nic=None, part_id__iew=None, part_id__niew=None, part_id__isw=None, part_id__nisw=None, part_id__ie=None, part_id__nie=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, parent_id__n=None, manufacturer_id__n=None, manufacturer__n=None, limit=None, offset=None) -> web.Response:
    """dcim_inventory_items_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param part_id: 
    :type part_id: str
    :param asset_tag: 
    :type asset_tag: str
    :param discovered: 
    :type discovered: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param parent_id: 
    :type parent_id: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param serial: 
    :type serial: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param part_id__n: 
    :type part_id__n: str
    :param part_id__ic: 
    :type part_id__ic: str
    :param part_id__nic: 
    :type part_id__nic: str
    :param part_id__iew: 
    :type part_id__iew: str
    :param part_id__niew: 
    :type part_id__niew: str
    :param part_id__isw: 
    :type part_id__isw: str
    :param part_id__nisw: 
    :type part_id__nisw: str
    :param part_id__ie: 
    :type part_id__ie: str
    :param part_id__nie: 
    :type part_id__nie: str
    :param asset_tag__n: 
    :type asset_tag__n: str
    :param asset_tag__ic: 
    :type asset_tag__ic: str
    :param asset_tag__nic: 
    :type asset_tag__nic: str
    :param asset_tag__iew: 
    :type asset_tag__iew: str
    :param asset_tag__niew: 
    :type asset_tag__niew: str
    :param asset_tag__isw: 
    :type asset_tag__isw: str
    :param asset_tag__nisw: 
    :type asset_tag__nisw: str
    :param asset_tag__ie: 
    :type asset_tag__ie: str
    :param asset_tag__nie: 
    :type asset_tag__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_inventory_items_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_items_partial_update

    

    :param id: A unique integer value identifying this inventory item.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItem.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_items_read(request: web.Request, id) -> web.Response:
    """dcim_inventory_items_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this inventory item.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_items_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_items_update

    

    :param id: A unique integer value identifying this inventory item.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItem.from_dict(body)
    return web.Response(status=200)


async def dcim_manufacturers_create(request: web.Request, body) -> web.Response:
    """dcim_manufacturers_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Manufacturer.from_dict(body)
    return web.Response(status=200)


async def dcim_manufacturers_delete(request: web.Request, id) -> web.Response:
    """dcim_manufacturers_delete

    

    :param id: A unique integer value identifying this manufacturer.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_manufacturers_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, limit=None, offset=None) -> web.Response:
    """dcim_manufacturers_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_manufacturers_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_manufacturers_partial_update

    

    :param id: A unique integer value identifying this manufacturer.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Manufacturer.from_dict(body)
    return web.Response(status=200)


async def dcim_manufacturers_read(request: web.Request, id) -> web.Response:
    """dcim_manufacturers_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this manufacturer.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_manufacturers_update(request: web.Request, id, body) -> web.Response:
    """dcim_manufacturers_update

    

    :param id: A unique integer value identifying this manufacturer.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Manufacturer.from_dict(body)
    return web.Response(status=200)


async def dcim_platforms_create(request: web.Request, body) -> web.Response:
    """dcim_platforms_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePlatform.from_dict(body)
    return web.Response(status=200)


async def dcim_platforms_delete(request: web.Request, id) -> web.Response:
    """dcim_platforms_delete

    

    :param id: A unique integer value identifying this platform.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_platforms_list(request: web.Request, id=None, name=None, slug=None, napalm_driver=None, description=None, q=None, manufacturer_id=None, manufacturer=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, napalm_driver__n=None, napalm_driver__ic=None, napalm_driver__nic=None, napalm_driver__iew=None, napalm_driver__niew=None, napalm_driver__isw=None, napalm_driver__nisw=None, napalm_driver__ie=None, napalm_driver__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, manufacturer_id__n=None, manufacturer__n=None, limit=None, offset=None) -> web.Response:
    """dcim_platforms_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param napalm_driver: 
    :type napalm_driver: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param napalm_driver__n: 
    :type napalm_driver__n: str
    :param napalm_driver__ic: 
    :type napalm_driver__ic: str
    :param napalm_driver__nic: 
    :type napalm_driver__nic: str
    :param napalm_driver__iew: 
    :type napalm_driver__iew: str
    :param napalm_driver__niew: 
    :type napalm_driver__niew: str
    :param napalm_driver__isw: 
    :type napalm_driver__isw: str
    :param napalm_driver__nisw: 
    :type napalm_driver__nisw: str
    :param napalm_driver__ie: 
    :type napalm_driver__ie: str
    :param napalm_driver__nie: 
    :type napalm_driver__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_platforms_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_platforms_partial_update

    

    :param id: A unique integer value identifying this platform.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePlatform.from_dict(body)
    return web.Response(status=200)


async def dcim_platforms_read(request: web.Request, id) -> web.Response:
    """dcim_platforms_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this platform.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_platforms_update(request: web.Request, id, body) -> web.Response:
    """dcim_platforms_update

    

    :param id: A unique integer value identifying this platform.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePlatform.from_dict(body)
    return web.Response(status=200)


async def dcim_power_connections_list(request: web.Request, name=None, connection_status=None, site=None, device_id=None, device=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, connection_status__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_connections_list

    

    :param name: 
    :type name: str
    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_feeds_create(request: web.Request, body) -> web.Response:
    """dcim_power_feeds_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerFeed.from_dict(body)
    return web.Response(status=200)


async def dcim_power_feeds_delete(request: web.Request, id) -> web.Response:
    """dcim_power_feeds_delete

    

    :param id: A unique integer value identifying this power feed.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_feeds_list(request: web.Request, id=None, name=None, status=None, type=None, supply=None, phase=None, voltage=None, amperage=None, max_utilization=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, region_id=None, region=None, site_id=None, site=None, power_panel_id=None, rack_id=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, status__n=None, type__n=None, supply__n=None, phase__n=None, voltage__n=None, voltage__lte=None, voltage__lt=None, voltage__gte=None, voltage__gt=None, amperage__n=None, amperage__lte=None, amperage__lt=None, amperage__gte=None, amperage__gt=None, max_utilization__n=None, max_utilization__lte=None, max_utilization__lt=None, max_utilization__gte=None, max_utilization__gt=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, power_panel_id__n=None, rack_id__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_feeds_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param status: 
    :type status: str
    :param type: 
    :type type: str
    :param supply: 
    :type supply: str
    :param phase: 
    :type phase: str
    :param voltage: 
    :type voltage: str
    :param amperage: 
    :type amperage: str
    :param max_utilization: 
    :type max_utilization: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param power_panel_id: 
    :type power_panel_id: str
    :param rack_id: 
    :type rack_id: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param status__n: 
    :type status__n: str
    :param type__n: 
    :type type__n: str
    :param supply__n: 
    :type supply__n: str
    :param phase__n: 
    :type phase__n: str
    :param voltage__n: 
    :type voltage__n: str
    :param voltage__lte: 
    :type voltage__lte: str
    :param voltage__lt: 
    :type voltage__lt: str
    :param voltage__gte: 
    :type voltage__gte: str
    :param voltage__gt: 
    :type voltage__gt: str
    :param amperage__n: 
    :type amperage__n: str
    :param amperage__lte: 
    :type amperage__lte: str
    :param amperage__lt: 
    :type amperage__lt: str
    :param amperage__gte: 
    :type amperage__gte: str
    :param amperage__gt: 
    :type amperage__gt: str
    :param max_utilization__n: 
    :type max_utilization__n: str
    :param max_utilization__lte: 
    :type max_utilization__lte: str
    :param max_utilization__lt: 
    :type max_utilization__lt: str
    :param max_utilization__gte: 
    :type max_utilization__gte: str
    :param max_utilization__gt: 
    :type max_utilization__gt: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param power_panel_id__n: 
    :type power_panel_id__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_feeds_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_feeds_partial_update

    

    :param id: A unique integer value identifying this power feed.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerFeed.from_dict(body)
    return web.Response(status=200)


async def dcim_power_feeds_read(request: web.Request, id) -> web.Response:
    """dcim_power_feeds_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power feed.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_feeds_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_feeds_update

    

    :param id: A unique integer value identifying this power feed.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerFeed.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlet_templates_create(request: web.Request, body) -> web.Response:
    """dcim_power_outlet_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutletTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlet_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_power_outlet_templates_delete

    

    :param id: A unique integer value identifying this power outlet template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_outlet_templates_list(request: web.Request, id=None, name=None, type=None, feed_leg=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, feed_leg__n=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlet_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param feed_leg: 
    :type feed_leg: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param feed_leg__n: 
    :type feed_leg__n: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_outlet_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_outlet_templates_partial_update

    

    :param id: A unique integer value identifying this power outlet template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutletTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlet_templates_read(request: web.Request, id) -> web.Response:
    """dcim_power_outlet_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power outlet template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_outlet_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_outlet_templates_update

    

    :param id: A unique integer value identifying this power outlet template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutletTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlets_create(request: web.Request, body) -> web.Response:
    """dcim_power_outlets_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlets_delete(request: web.Request, id) -> web.Response:
    """dcim_power_outlets_delete

    

    :param id: A unique integer value identifying this power outlet.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_outlets_list(request: web.Request, id=None, name=None, feed_leg=None, description=None, connection_status=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, type=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, feed_leg__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, connection_status__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, type__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlets_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param feed_leg: 
    :type feed_leg: str
    :param description: 
    :type description: str
    :param connection_status: 
    :type connection_status: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param feed_leg__n: 
    :type feed_leg__n: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_outlets_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_outlets_partial_update

    

    :param id: A unique integer value identifying this power outlet.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlets_read(request: web.Request, id) -> web.Response:
    """dcim_power_outlets_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power outlet.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_outlets_trace(request: web.Request, id) -> web.Response:
    """dcim_power_outlets_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this power outlet.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_outlets_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_outlets_update

    

    :param id: A unique integer value identifying this power outlet.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
    return web.Response(status=200)


async def dcim_power_panels_create(request: web.Request, body) -> web.Response:
    """dcim_power_panels_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPanel.from_dict(body)
    return web.Response(status=200)


async def dcim_power_panels_delete(request: web.Request, id) -> web.Response:
    """dcim_power_panels_delete

    

    :param id: A unique integer value identifying this power panel.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_panels_list(request: web.Request, id=None, name=None, q=None, region_id=None, region=None, site_id=None, site=None, rack_group_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, rack_group_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_panels_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param rack_group_id: 
    :type rack_group_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param rack_group_id__n: 
    :type rack_group_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_panels_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_panels_partial_update

    

    :param id: A unique integer value identifying this power panel.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPanel.from_dict(body)
    return web.Response(status=200)


async def dcim_power_panels_read(request: web.Request, id) -> web.Response:
    """dcim_power_panels_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power panel.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_panels_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_panels_update

    

    :param id: A unique integer value identifying this power panel.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPanel.from_dict(body)
    return web.Response(status=200)


async def dcim_power_port_templates_create(request: web.Request, body) -> web.Response:
    """dcim_power_port_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_port_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_power_port_templates_delete

    

    :param id: A unique integer value identifying this power port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_port_templates_list(request: web.Request, id=None, name=None, type=None, maximum_draw=None, allocated_draw=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, maximum_draw__n=None, maximum_draw__lte=None, maximum_draw__lt=None, maximum_draw__gte=None, maximum_draw__gt=None, allocated_draw__n=None, allocated_draw__lte=None, allocated_draw__lt=None, allocated_draw__gte=None, allocated_draw__gt=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_port_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param maximum_draw: 
    :type maximum_draw: str
    :param allocated_draw: 
    :type allocated_draw: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param maximum_draw__n: 
    :type maximum_draw__n: str
    :param maximum_draw__lte: 
    :type maximum_draw__lte: str
    :param maximum_draw__lt: 
    :type maximum_draw__lt: str
    :param maximum_draw__gte: 
    :type maximum_draw__gte: str
    :param maximum_draw__gt: 
    :type maximum_draw__gt: str
    :param allocated_draw__n: 
    :type allocated_draw__n: str
    :param allocated_draw__lte: 
    :type allocated_draw__lte: str
    :param allocated_draw__lt: 
    :type allocated_draw__lt: str
    :param allocated_draw__gte: 
    :type allocated_draw__gte: str
    :param allocated_draw__gt: 
    :type allocated_draw__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_port_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_port_templates_partial_update

    

    :param id: A unique integer value identifying this power port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_port_templates_read(request: web.Request, id) -> web.Response:
    """dcim_power_port_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_port_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_port_templates_update

    

    :param id: A unique integer value identifying this power port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_ports_create(request: web.Request, body) -> web.Response:
    """dcim_power_ports_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_power_ports_delete(request: web.Request, id) -> web.Response:
    """dcim_power_ports_delete

    

    :param id: A unique integer value identifying this power port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_ports_list(request: web.Request, id=None, name=None, maximum_draw=None, allocated_draw=None, description=None, connection_status=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, type=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, maximum_draw__n=None, maximum_draw__lte=None, maximum_draw__lt=None, maximum_draw__gte=None, maximum_draw__gt=None, allocated_draw__n=None, allocated_draw__lte=None, allocated_draw__lt=None, allocated_draw__gte=None, allocated_draw__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, connection_status__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, type__n=None, limit=None, offset=None) -> web.Response:
    """dcim_power_ports_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param maximum_draw: 
    :type maximum_draw: str
    :param allocated_draw: 
    :type allocated_draw: str
    :param description: 
    :type description: str
    :param connection_status: 
    :type connection_status: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param maximum_draw__n: 
    :type maximum_draw__n: str
    :param maximum_draw__lte: 
    :type maximum_draw__lte: str
    :param maximum_draw__lt: 
    :type maximum_draw__lt: str
    :param maximum_draw__gte: 
    :type maximum_draw__gte: str
    :param maximum_draw__gt: 
    :type maximum_draw__gt: str
    :param allocated_draw__n: 
    :type allocated_draw__n: str
    :param allocated_draw__lte: 
    :type allocated_draw__lte: str
    :param allocated_draw__lt: 
    :type allocated_draw__lt: str
    :param allocated_draw__gte: 
    :type allocated_draw__gte: str
    :param allocated_draw__gt: 
    :type allocated_draw__gt: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param connection_status__n: 
    :type connection_status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_power_ports_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_ports_partial_update

    

    :param id: A unique integer value identifying this power port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_power_ports_read(request: web.Request, id) -> web.Response:
    """dcim_power_ports_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this power port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_ports_trace(request: web.Request, id) -> web.Response:
    """dcim_power_ports_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this power port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_ports_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_ports_update

    

    :param id: A unique integer value identifying this power port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_groups_create(request: web.Request, body) -> web.Response:
    """dcim_rack_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_groups_delete(request: web.Request, id) -> web.Response:
    """dcim_rack_groups_delete

    

    :param id: A unique integer value identifying this rack group.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, parent_id__n=None, parent__n=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_groups_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param parent_id: 
    :type parent_id: str
    :param parent: 
    :type parent: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_rack_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_groups_partial_update

    

    :param id: A unique integer value identifying this rack group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_groups_read(request: web.Request, id) -> web.Response:
    """dcim_rack_groups_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rack group.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_groups_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_groups_update

    

    :param id: A unique integer value identifying this rack group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_reservations_create(request: web.Request, body) -> web.Response:
    """dcim_rack_reservations_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackReservation.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_reservations_delete(request: web.Request, id) -> web.Response:
    """dcim_rack_reservations_delete

    

    :param id: A unique integer value identifying this rack reservation.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_reservations_list(request: web.Request, id=None, created=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, q=None, rack_id=None, site_id=None, site=None, group_id=None, group=None, user_id=None, user=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, rack_id__n=None, site_id__n=None, site__n=None, group_id__n=None, group__n=None, user_id__n=None, user__n=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_reservations_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param created: 
    :type created: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param q: 
    :type q: str
    :param rack_id: 
    :type rack_id: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param user_id__n: 
    :type user_id__n: str
    :param user__n: 
    :type user__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_rack_reservations_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_reservations_partial_update

    

    :param id: A unique integer value identifying this rack reservation.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackReservation.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_reservations_read(request: web.Request, id) -> web.Response:
    """dcim_rack_reservations_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rack reservation.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_reservations_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_reservations_update

    

    :param id: A unique integer value identifying this rack reservation.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackReservation.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_roles_create(request: web.Request, body) -> web.Response:
    """dcim_rack_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = RackRole.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_roles_delete(request: web.Request, id) -> web.Response:
    """dcim_rack_roles_delete

    

    :param id: A unique integer value identifying this rack role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_roles_list(request: web.Request, id=None, name=None, slug=None, color=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_roles_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param color__n: 
    :type color__n: str
    :param color__ic: 
    :type color__ic: str
    :param color__nic: 
    :type color__nic: str
    :param color__iew: 
    :type color__iew: str
    :param color__niew: 
    :type color__niew: str
    :param color__isw: 
    :type color__isw: str
    :param color__nisw: 
    :type color__nisw: str
    :param color__ie: 
    :type color__ie: str
    :param color__nie: 
    :type color__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_rack_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_roles_partial_update

    

    :param id: A unique integer value identifying this rack role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RackRole.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_roles_read(request: web.Request, id) -> web.Response:
    """dcim_rack_roles_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rack role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rack_roles_update(request: web.Request, id, body) -> web.Response:
    """dcim_rack_roles_update

    

    :param id: A unique integer value identifying this rack role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RackRole.from_dict(body)
    return web.Response(status=200)


async def dcim_racks_create(request: web.Request, body) -> web.Response:
    """dcim_racks_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRack.from_dict(body)
    return web.Response(status=200)


async def dcim_racks_delete(request: web.Request, id) -> web.Response:
    """dcim_racks_delete

    

    :param id: A unique integer value identifying this rack.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_racks_elevation(request: web.Request, id, q=None, face=None, render=None, unit_width=None, unit_height=None, legend_width=None, exclude=None, expand_devices=None, include_images=None) -> web.Response:
    """dcim_racks_elevation

    Rack elevation representing the list of rack units. Also supports rendering the elevation as an SVG.

    :param id: A unique integer value identifying this rack.
    :type id: int
    :param q: 
    :type q: str
    :param face: 
    :type face: str
    :param render: 
    :type render: str
    :param unit_width: 
    :type unit_width: int
    :param unit_height: 
    :type unit_height: int
    :param legend_width: 
    :type legend_width: int
    :param exclude: 
    :type exclude: int
    :param expand_devices: 
    :type expand_devices: bool
    :param include_images: 
    :type include_images: bool

    """
    return web.Response(status=200)


async def dcim_racks_list(request: web.Request, id=None, name=None, facility_id=None, asset_tag=None, type=None, width=None, u_height=None, desc_units=None, outer_width=None, outer_depth=None, outer_unit=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, region_id=None, region=None, site_id=None, site=None, group_id=None, group=None, status=None, role_id=None, role=None, serial=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, facility_id__n=None, facility_id__ic=None, facility_id__nic=None, facility_id__iew=None, facility_id__niew=None, facility_id__isw=None, facility_id__nisw=None, facility_id__ie=None, facility_id__nie=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, type__n=None, width__n=None, u_height__n=None, u_height__lte=None, u_height__lt=None, u_height__gte=None, u_height__gt=None, outer_width__n=None, outer_width__lte=None, outer_width__lt=None, outer_width__gte=None, outer_width__gt=None, outer_depth__n=None, outer_depth__lte=None, outer_depth__lt=None, outer_depth__gte=None, outer_depth__gt=None, outer_unit__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, group_id__n=None, group__n=None, status__n=None, role_id__n=None, role__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_racks_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param facility_id: 
    :type facility_id: str
    :param asset_tag: 
    :type asset_tag: str
    :param type: 
    :type type: str
    :param width: 
    :type width: str
    :param u_height: 
    :type u_height: str
    :param desc_units: 
    :type desc_units: str
    :param outer_width: 
    :type outer_width: str
    :param outer_depth: 
    :type outer_depth: str
    :param outer_unit: 
    :type outer_unit: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param status: 
    :type status: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param serial: 
    :type serial: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param facility_id__n: 
    :type facility_id__n: str
    :param facility_id__ic: 
    :type facility_id__ic: str
    :param facility_id__nic: 
    :type facility_id__nic: str
    :param facility_id__iew: 
    :type facility_id__iew: str
    :param facility_id__niew: 
    :type facility_id__niew: str
    :param facility_id__isw: 
    :type facility_id__isw: str
    :param facility_id__nisw: 
    :type facility_id__nisw: str
    :param facility_id__ie: 
    :type facility_id__ie: str
    :param facility_id__nie: 
    :type facility_id__nie: str
    :param asset_tag__n: 
    :type asset_tag__n: str
    :param asset_tag__ic: 
    :type asset_tag__ic: str
    :param asset_tag__nic: 
    :type asset_tag__nic: str
    :param asset_tag__iew: 
    :type asset_tag__iew: str
    :param asset_tag__niew: 
    :type asset_tag__niew: str
    :param asset_tag__isw: 
    :type asset_tag__isw: str
    :param asset_tag__nisw: 
    :type asset_tag__nisw: str
    :param asset_tag__ie: 
    :type asset_tag__ie: str
    :param asset_tag__nie: 
    :type asset_tag__nie: str
    :param type__n: 
    :type type__n: str
    :param width__n: 
    :type width__n: str
    :param u_height__n: 
    :type u_height__n: str
    :param u_height__lte: 
    :type u_height__lte: str
    :param u_height__lt: 
    :type u_height__lt: str
    :param u_height__gte: 
    :type u_height__gte: str
    :param u_height__gt: 
    :type u_height__gt: str
    :param outer_width__n: 
    :type outer_width__n: str
    :param outer_width__lte: 
    :type outer_width__lte: str
    :param outer_width__lt: 
    :type outer_width__lt: str
    :param outer_width__gte: 
    :type outer_width__gte: str
    :param outer_width__gt: 
    :type outer_width__gt: str
    :param outer_depth__n: 
    :type outer_depth__n: str
    :param outer_depth__lte: 
    :type outer_depth__lte: str
    :param outer_depth__lt: 
    :type outer_depth__lt: str
    :param outer_depth__gte: 
    :type outer_depth__gte: str
    :param outer_depth__gt: 
    :type outer_depth__gt: str
    :param outer_unit__n: 
    :type outer_unit__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param status__n: 
    :type status__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_racks_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_racks_partial_update

    

    :param id: A unique integer value identifying this rack.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRack.from_dict(body)
    return web.Response(status=200)


async def dcim_racks_read(request: web.Request, id) -> web.Response:
    """dcim_racks_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rack.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_racks_update(request: web.Request, id, body) -> web.Response:
    """dcim_racks_update

    

    :param id: A unique integer value identifying this rack.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRack.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_port_templates_create(request: web.Request, body) -> web.Response:
    """dcim_rear_port_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_port_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_rear_port_templates_delete

    

    :param id: A unique integer value identifying this rear port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_port_templates_list(request: web.Request, id=None, name=None, type=None, positions=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, positions__n=None, positions__lte=None, positions__lt=None, positions__gte=None, positions__gt=None, devicetype_id__n=None, limit=None, offset=None) -> web.Response:
    """dcim_rear_port_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param positions: 
    :type positions: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param positions__n: 
    :type positions__n: str
    :param positions__lte: 
    :type positions__lte: str
    :param positions__lt: 
    :type positions__lt: str
    :param positions__gte: 
    :type positions__gte: str
    :param positions__gt: 
    :type positions__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_rear_port_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_rear_port_templates_partial_update

    

    :param id: A unique integer value identifying this rear port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_port_templates_read(request: web.Request, id) -> web.Response:
    """dcim_rear_port_templates_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rear port template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_port_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_rear_port_templates_update

    

    :param id: A unique integer value identifying this rear port template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_ports_create(request: web.Request, body) -> web.Response:
    """dcim_rear_ports_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPort.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_ports_delete(request: web.Request, id) -> web.Response:
    """dcim_rear_ports_delete

    

    :param id: A unique integer value identifying this rear port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_ports_list(request: web.Request, id=None, name=None, type=None, positions=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, device_id=None, device=None, tag=None, cabled=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, type__n=None, positions__n=None, positions__lte=None, positions__lt=None, positions__gte=None, positions__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, device_id__n=None, device__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_rear_ports_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param positions: 
    :type positions: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param type__n: 
    :type type__n: str
    :param positions__n: 
    :type positions__n: str
    :param positions__lte: 
    :type positions__lte: str
    :param positions__lt: 
    :type positions__lt: str
    :param positions__gte: 
    :type positions__gte: str
    :param positions__gt: 
    :type positions__gt: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_rear_ports_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_rear_ports_partial_update

    

    :param id: A unique integer value identifying this rear port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPort.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_ports_read(request: web.Request, id) -> web.Response:
    """dcim_rear_ports_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this rear port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_ports_trace(request: web.Request, id) -> web.Response:
    """dcim_rear_ports_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

    :param id: A unique integer value identifying this rear port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_ports_update(request: web.Request, id, body) -> web.Response:
    """dcim_rear_ports_update

    

    :param id: A unique integer value identifying this rear port.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPort.from_dict(body)
    return web.Response(status=200)


async def dcim_regions_create(request: web.Request, body) -> web.Response:
    """dcim_regions_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRegion.from_dict(body)
    return web.Response(status=200)


async def dcim_regions_delete(request: web.Request, id) -> web.Response:
    """dcim_regions_delete

    

    :param id: A unique integer value identifying this region.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_regions_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, parent_id__n=None, parent__n=None, limit=None, offset=None) -> web.Response:
    """dcim_regions_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param parent_id: 
    :type parent_id: str
    :param parent: 
    :type parent: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_regions_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_regions_partial_update

    

    :param id: A unique integer value identifying this region.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRegion.from_dict(body)
    return web.Response(status=200)


async def dcim_regions_read(request: web.Request, id) -> web.Response:
    """dcim_regions_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this region.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_regions_update(request: web.Request, id, body) -> web.Response:
    """dcim_regions_update

    

    :param id: A unique integer value identifying this region.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRegion.from_dict(body)
    return web.Response(status=200)


async def dcim_sites_create(request: web.Request, body) -> web.Response:
    """dcim_sites_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSite.from_dict(body)
    return web.Response(status=200)


async def dcim_sites_delete(request: web.Request, id) -> web.Response:
    """dcim_sites_delete

    

    :param id: A unique integer value identifying this site.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_sites_graphs(request: web.Request, id) -> web.Response:
    """dcim_sites_graphs

    A convenience method for rendering graphs for a particular site.

    :param id: A unique integer value identifying this site.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_sites_list(request: web.Request, id=None, name=None, slug=None, facility=None, asn=None, latitude=None, longitude=None, contact_name=None, contact_phone=None, contact_email=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, status=None, region_id=None, region=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, facility__n=None, facility__ic=None, facility__nic=None, facility__iew=None, facility__niew=None, facility__isw=None, facility__nisw=None, facility__ie=None, facility__nie=None, asn__n=None, asn__lte=None, asn__lt=None, asn__gte=None, asn__gt=None, latitude__n=None, latitude__lte=None, latitude__lt=None, latitude__gte=None, latitude__gt=None, longitude__n=None, longitude__lte=None, longitude__lt=None, longitude__gte=None, longitude__gt=None, contact_name__n=None, contact_name__ic=None, contact_name__nic=None, contact_name__iew=None, contact_name__niew=None, contact_name__isw=None, contact_name__nisw=None, contact_name__ie=None, contact_name__nie=None, contact_phone__n=None, contact_phone__ic=None, contact_phone__nic=None, contact_phone__iew=None, contact_phone__niew=None, contact_phone__isw=None, contact_phone__nisw=None, contact_phone__ie=None, contact_phone__nie=None, contact_email__n=None, contact_email__ic=None, contact_email__nic=None, contact_email__iew=None, contact_email__niew=None, contact_email__isw=None, contact_email__nisw=None, contact_email__ie=None, contact_email__nie=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, status__n=None, region_id__n=None, region__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_sites_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param facility: 
    :type facility: str
    :param asn: 
    :type asn: str
    :param latitude: 
    :type latitude: str
    :param longitude: 
    :type longitude: str
    :param contact_name: 
    :type contact_name: str
    :param contact_phone: 
    :type contact_phone: str
    :param contact_email: 
    :type contact_email: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param status: 
    :type status: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param facility__n: 
    :type facility__n: str
    :param facility__ic: 
    :type facility__ic: str
    :param facility__nic: 
    :type facility__nic: str
    :param facility__iew: 
    :type facility__iew: str
    :param facility__niew: 
    :type facility__niew: str
    :param facility__isw: 
    :type facility__isw: str
    :param facility__nisw: 
    :type facility__nisw: str
    :param facility__ie: 
    :type facility__ie: str
    :param facility__nie: 
    :type facility__nie: str
    :param asn__n: 
    :type asn__n: str
    :param asn__lte: 
    :type asn__lte: str
    :param asn__lt: 
    :type asn__lt: str
    :param asn__gte: 
    :type asn__gte: str
    :param asn__gt: 
    :type asn__gt: str
    :param latitude__n: 
    :type latitude__n: str
    :param latitude__lte: 
    :type latitude__lte: str
    :param latitude__lt: 
    :type latitude__lt: str
    :param latitude__gte: 
    :type latitude__gte: str
    :param latitude__gt: 
    :type latitude__gt: str
    :param longitude__n: 
    :type longitude__n: str
    :param longitude__lte: 
    :type longitude__lte: str
    :param longitude__lt: 
    :type longitude__lt: str
    :param longitude__gte: 
    :type longitude__gte: str
    :param longitude__gt: 
    :type longitude__gt: str
    :param contact_name__n: 
    :type contact_name__n: str
    :param contact_name__ic: 
    :type contact_name__ic: str
    :param contact_name__nic: 
    :type contact_name__nic: str
    :param contact_name__iew: 
    :type contact_name__iew: str
    :param contact_name__niew: 
    :type contact_name__niew: str
    :param contact_name__isw: 
    :type contact_name__isw: str
    :param contact_name__nisw: 
    :type contact_name__nisw: str
    :param contact_name__ie: 
    :type contact_name__ie: str
    :param contact_name__nie: 
    :type contact_name__nie: str
    :param contact_phone__n: 
    :type contact_phone__n: str
    :param contact_phone__ic: 
    :type contact_phone__ic: str
    :param contact_phone__nic: 
    :type contact_phone__nic: str
    :param contact_phone__iew: 
    :type contact_phone__iew: str
    :param contact_phone__niew: 
    :type contact_phone__niew: str
    :param contact_phone__isw: 
    :type contact_phone__isw: str
    :param contact_phone__nisw: 
    :type contact_phone__nisw: str
    :param contact_phone__ie: 
    :type contact_phone__ie: str
    :param contact_phone__nie: 
    :type contact_phone__nie: str
    :param contact_email__n: 
    :type contact_email__n: str
    :param contact_email__ic: 
    :type contact_email__ic: str
    :param contact_email__nic: 
    :type contact_email__nic: str
    :param contact_email__iew: 
    :type contact_email__iew: str
    :param contact_email__niew: 
    :type contact_email__niew: str
    :param contact_email__isw: 
    :type contact_email__isw: str
    :param contact_email__nisw: 
    :type contact_email__nisw: str
    :param contact_email__ie: 
    :type contact_email__ie: str
    :param contact_email__nie: 
    :type contact_email__nie: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param status__n: 
    :type status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_sites_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_sites_partial_update

    

    :param id: A unique integer value identifying this site.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSite.from_dict(body)
    return web.Response(status=200)


async def dcim_sites_read(request: web.Request, id) -> web.Response:
    """dcim_sites_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this site.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_sites_update(request: web.Request, id, body) -> web.Response:
    """dcim_sites_update

    

    :param id: A unique integer value identifying this site.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSite.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_chassis_create(request: web.Request, body) -> web.Response:
    """dcim_virtual_chassis_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualChassis.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_chassis_delete(request: web.Request, id) -> web.Response:
    """dcim_virtual_chassis_delete

    

    :param id: A unique integer value identifying this virtual chassis.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_virtual_chassis_list(request: web.Request, id=None, domain=None, q=None, region_id=None, region=None, site_id=None, site=None, tenant_id=None, tenant=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, domain__n=None, domain__ic=None, domain__nic=None, domain__iew=None, domain__niew=None, domain__isw=None, domain__nisw=None, domain__ie=None, domain__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, tenant_id__n=None, tenant__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """dcim_virtual_chassis_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param domain: 
    :type domain: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param domain__n: 
    :type domain__n: str
    :param domain__ic: 
    :type domain__ic: str
    :param domain__nic: 
    :type domain__nic: str
    :param domain__iew: 
    :type domain__iew: str
    :param domain__niew: 
    :type domain__niew: str
    :param domain__isw: 
    :type domain__isw: str
    :param domain__nisw: 
    :type domain__nisw: str
    :param domain__ie: 
    :type domain__ie: str
    :param domain__nie: 
    :type domain__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_virtual_chassis_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_virtual_chassis_partial_update

    

    :param id: A unique integer value identifying this virtual chassis.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualChassis.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_chassis_read(request: web.Request, id) -> web.Response:
    """dcim_virtual_chassis_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this virtual chassis.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_virtual_chassis_update(request: web.Request, id, body) -> web.Response:
    """dcim_virtual_chassis_update

    

    :param id: A unique integer value identifying this virtual chassis.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualChassis.from_dict(body)
    return web.Response(status=200)
