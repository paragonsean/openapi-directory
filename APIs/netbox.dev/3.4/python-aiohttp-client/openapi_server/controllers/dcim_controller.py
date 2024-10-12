from typing import List, Dict
from aiohttp import web

from openapi_server.models.cable import Cable
from openapi_server.models.cable_termination import CableTermination
from openapi_server.models.console_port import ConsolePort
from openapi_server.models.console_port_template import ConsolePortTemplate
from openapi_server.models.console_server_port import ConsoleServerPort
from openapi_server.models.console_server_port_template import ConsoleServerPortTemplate
from openapi_server.models.dcim_cable_terminations_list200_response import DcimCableTerminationsList200Response
from openapi_server.models.dcim_cables_list200_response import DcimCablesList200Response
from openapi_server.models.dcim_console_port_templates_list200_response import DcimConsolePortTemplatesList200Response
from openapi_server.models.dcim_console_ports_list200_response import DcimConsolePortsList200Response
from openapi_server.models.dcim_console_server_port_templates_list200_response import DcimConsoleServerPortTemplatesList200Response
from openapi_server.models.dcim_console_server_ports_list200_response import DcimConsoleServerPortsList200Response
from openapi_server.models.dcim_device_bay_templates_list200_response import DcimDeviceBayTemplatesList200Response
from openapi_server.models.dcim_device_bays_list200_response import DcimDeviceBaysList200Response
from openapi_server.models.dcim_device_roles_list200_response import DcimDeviceRolesList200Response
from openapi_server.models.dcim_device_types_list200_response import DcimDeviceTypesList200Response
from openapi_server.models.dcim_devices_list200_response import DcimDevicesList200Response
from openapi_server.models.dcim_front_port_templates_list200_response import DcimFrontPortTemplatesList200Response
from openapi_server.models.dcim_front_ports_list200_response import DcimFrontPortsList200Response
from openapi_server.models.dcim_interface_templates_list200_response import DcimInterfaceTemplatesList200Response
from openapi_server.models.dcim_interfaces_list200_response import DcimInterfacesList200Response
from openapi_server.models.dcim_inventory_item_roles_list200_response import DcimInventoryItemRolesList200Response
from openapi_server.models.dcim_inventory_item_templates_list200_response import DcimInventoryItemTemplatesList200Response
from openapi_server.models.dcim_inventory_items_list200_response import DcimInventoryItemsList200Response
from openapi_server.models.dcim_locations_list200_response import DcimLocationsList200Response
from openapi_server.models.dcim_manufacturers_list200_response import DcimManufacturersList200Response
from openapi_server.models.dcim_module_bay_templates_list200_response import DcimModuleBayTemplatesList200Response
from openapi_server.models.dcim_module_bays_list200_response import DcimModuleBaysList200Response
from openapi_server.models.dcim_module_types_list200_response import DcimModuleTypesList200Response
from openapi_server.models.dcim_modules_list200_response import DcimModulesList200Response
from openapi_server.models.dcim_platforms_list200_response import DcimPlatformsList200Response
from openapi_server.models.dcim_power_feeds_list200_response import DcimPowerFeedsList200Response
from openapi_server.models.dcim_power_outlet_templates_list200_response import DcimPowerOutletTemplatesList200Response
from openapi_server.models.dcim_power_outlets_list200_response import DcimPowerOutletsList200Response
from openapi_server.models.dcim_power_panels_list200_response import DcimPowerPanelsList200Response
from openapi_server.models.dcim_power_port_templates_list200_response import DcimPowerPortTemplatesList200Response
from openapi_server.models.dcim_power_ports_list200_response import DcimPowerPortsList200Response
from openapi_server.models.dcim_rack_reservations_list200_response import DcimRackReservationsList200Response
from openapi_server.models.dcim_rack_roles_list200_response import DcimRackRolesList200Response
from openapi_server.models.dcim_racks_list200_response import DcimRacksList200Response
from openapi_server.models.dcim_rear_port_templates_list200_response import DcimRearPortTemplatesList200Response
from openapi_server.models.dcim_rear_ports_list200_response import DcimRearPortsList200Response
from openapi_server.models.dcim_regions_list200_response import DcimRegionsList200Response
from openapi_server.models.dcim_site_groups_list200_response import DcimSiteGroupsList200Response
from openapi_server.models.dcim_sites_list200_response import DcimSitesList200Response
from openapi_server.models.dcim_virtual_chassis_list200_response import DcimVirtualChassisList200Response
from openapi_server.models.dcim_virtual_device_contexts_list200_response import DcimVirtualDeviceContextsList200Response
from openapi_server.models.device import Device
from openapi_server.models.device_bay import DeviceBay
from openapi_server.models.device_bay_template import DeviceBayTemplate
from openapi_server.models.device_napalm import DeviceNAPALM
from openapi_server.models.device_role import DeviceRole
from openapi_server.models.device_type import DeviceType
from openapi_server.models.device_with_config_context import DeviceWithConfigContext
from openapi_server.models.front_port import FrontPort
from openapi_server.models.front_port_template import FrontPortTemplate
from openapi_server.models.interface import Interface
from openapi_server.models.interface_template import InterfaceTemplate
from openapi_server.models.inventory_item import InventoryItem
from openapi_server.models.inventory_item_role import InventoryItemRole
from openapi_server.models.inventory_item_template import InventoryItemTemplate
from openapi_server.models.location import Location
from openapi_server.models.manufacturer import Manufacturer
from openapi_server.models.module import Module
from openapi_server.models.module_bay import ModuleBay
from openapi_server.models.module_bay_template import ModuleBayTemplate
from openapi_server.models.module_type import ModuleType
from openapi_server.models.platform import Platform
from openapi_server.models.power_feed import PowerFeed
from openapi_server.models.power_outlet import PowerOutlet
from openapi_server.models.power_outlet_template import PowerOutletTemplate
from openapi_server.models.power_panel import PowerPanel
from openapi_server.models.power_port import PowerPort
from openapi_server.models.power_port_template import PowerPortTemplate
from openapi_server.models.rack import Rack
from openapi_server.models.rack_reservation import RackReservation
from openapi_server.models.rack_role import RackRole
from openapi_server.models.rack_unit import RackUnit
from openapi_server.models.rear_port import RearPort
from openapi_server.models.rear_port_template import RearPortTemplate
from openapi_server.models.region import Region
from openapi_server.models.site import Site
from openapi_server.models.site_group import SiteGroup
from openapi_server.models.virtual_chassis import VirtualChassis
from openapi_server.models.virtual_device_context import VirtualDeviceContext
from openapi_server.models.writable_cable import WritableCable
from openapi_server.models.writable_console_port import WritableConsolePort
from openapi_server.models.writable_console_port_template import WritableConsolePortTemplate
from openapi_server.models.writable_console_server_port import WritableConsoleServerPort
from openapi_server.models.writable_console_server_port_template import WritableConsoleServerPortTemplate
from openapi_server.models.writable_device_bay import WritableDeviceBay
from openapi_server.models.writable_device_bay_template import WritableDeviceBayTemplate
from openapi_server.models.writable_device_type import WritableDeviceType
from openapi_server.models.writable_device_with_config_context import WritableDeviceWithConfigContext
from openapi_server.models.writable_front_port import WritableFrontPort
from openapi_server.models.writable_front_port_template import WritableFrontPortTemplate
from openapi_server.models.writable_interface import WritableInterface
from openapi_server.models.writable_interface_template import WritableInterfaceTemplate
from openapi_server.models.writable_inventory_item import WritableInventoryItem
from openapi_server.models.writable_inventory_item_template import WritableInventoryItemTemplate
from openapi_server.models.writable_location import WritableLocation
from openapi_server.models.writable_module import WritableModule
from openapi_server.models.writable_module_bay import WritableModuleBay
from openapi_server.models.writable_module_bay_template import WritableModuleBayTemplate
from openapi_server.models.writable_module_type import WritableModuleType
from openapi_server.models.writable_platform import WritablePlatform
from openapi_server.models.writable_power_feed import WritablePowerFeed
from openapi_server.models.writable_power_outlet import WritablePowerOutlet
from openapi_server.models.writable_power_outlet_template import WritablePowerOutletTemplate
from openapi_server.models.writable_power_panel import WritablePowerPanel
from openapi_server.models.writable_power_port import WritablePowerPort
from openapi_server.models.writable_power_port_template import WritablePowerPortTemplate
from openapi_server.models.writable_rack import WritableRack
from openapi_server.models.writable_rack_reservation import WritableRackReservation
from openapi_server.models.writable_rear_port import WritableRearPort
from openapi_server.models.writable_rear_port_template import WritableRearPortTemplate
from openapi_server.models.writable_region import WritableRegion
from openapi_server.models.writable_site import WritableSite
from openapi_server.models.writable_site_group import WritableSiteGroup
from openapi_server.models.writable_virtual_chassis import WritableVirtualChassis
from openapi_server.models.writable_virtual_device_context import WritableVirtualDeviceContext
from openapi_server import util


async def dcim_cable_terminations_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_cable_terminations_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_cable_terminations_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_cable_terminations_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = CableTermination.from_dict(body)
    return web.Response(status=200)


async def dcim_cable_terminations_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_cable_terminations_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = CableTermination.from_dict(body)
    return web.Response(status=200)


async def dcim_cable_terminations_create(request: web.Request, body) -> web.Response:
    """dcim_cable_terminations_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CableTermination.from_dict(body)
    return web.Response(status=200)


async def dcim_cable_terminations_delete(request: web.Request, id) -> web.Response:
    """dcim_cable_terminations_delete

    

    :param id: A unique integer value identifying this cable termination.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_cable_terminations_list(request: web.Request, id=None, cable=None, cable_end=None, termination_type=None, termination_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, cable__n=None, cable_end__n=None, termination_type__n=None, termination_id__n=None, termination_id__lte=None, termination_id__lt=None, termination_id__gte=None, termination_id__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_cable_terminations_list

    

    :param id: 
    :type id: str
    :param cable: 
    :type cable: str
    :param cable_end: 
    :type cable_end: str
    :param termination_type: 
    :type termination_type: str
    :param termination_id: 
    :type termination_id: str
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
    :param cable__n: 
    :type cable__n: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param termination_type__n: 
    :type termination_type__n: str
    :param termination_id__n: 
    :type termination_id__n: str
    :param termination_id__lte: 
    :type termination_id__lte: str
    :param termination_id__lt: 
    :type termination_id__lt: str
    :param termination_id__gte: 
    :type termination_id__gte: str
    :param termination_id__gt: 
    :type termination_id__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_cable_terminations_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_cable_terminations_partial_update

    

    :param id: A unique integer value identifying this cable termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CableTermination.from_dict(body)
    return web.Response(status=200)


async def dcim_cable_terminations_read(request: web.Request, id) -> web.Response:
    """dcim_cable_terminations_read

    

    :param id: A unique integer value identifying this cable termination.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_cable_terminations_update(request: web.Request, id, body) -> web.Response:
    """dcim_cable_terminations_update

    

    :param id: A unique integer value identifying this cable termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CableTermination.from_dict(body)
    return web.Response(status=200)


async def dcim_cables_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_cables_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_cables_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_cables_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCable.from_dict(body)
    return web.Response(status=200)


async def dcim_cables_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_cables_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCable.from_dict(body)
    return web.Response(status=200)


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


async def dcim_cables_list(request: web.Request, id=None, label=None, length=None, length_unit=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, last_updated=None, q=None, tag=None, termination_a_type=None, termination_a_id=None, termination_b_type=None, termination_b_id=None, type=None, status=None, color=None, device_id=None, device=None, rack_id=None, rack=None, location_id=None, location=None, site_id=None, site=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, length__n=None, length__lte=None, length__lt=None, length__gte=None, length__gt=None, length_unit__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, termination_a_type__n=None, termination_a_id__n=None, termination_a_id__lte=None, termination_a_id__lt=None, termination_a_id__gte=None, termination_a_id__gt=None, termination_b_type__n=None, termination_b_id__n=None, termination_b_id__lte=None, termination_b_id__lt=None, termination_b_id__gte=None, termination_b_id__gt=None, type__n=None, status__n=None, color__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_cables_list

    

    :param id: 
    :type id: str
    :param label: 
    :type label: str
    :param length: 
    :type length: str
    :param length_unit: 
    :type length_unit: str
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
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param termination_a_type: 
    :type termination_a_type: str
    :param termination_a_id: 
    :type termination_a_id: str
    :param termination_b_type: 
    :type termination_b_type: str
    :param termination_b_id: 
    :type termination_b_id: str
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
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param termination_a_type__n: 
    :type termination_a_type__n: str
    :param termination_a_id__n: 
    :type termination_a_id__n: str
    :param termination_a_id__lte: 
    :type termination_a_id__lte: str
    :param termination_a_id__lt: 
    :type termination_a_id__lt: str
    :param termination_a_id__gte: 
    :type termination_a_id__gte: str
    :param termination_a_id__gt: 
    :type termination_a_id__gt: str
    :param termination_b_type__n: 
    :type termination_b_type__n: str
    :param termination_b_id__n: 
    :type termination_b_id__n: str
    :param termination_b_id__lte: 
    :type termination_b_id__lte: str
    :param termination_b_id__lt: 
    :type termination_b_id__lt: str
    :param termination_b_id__gte: 
    :type termination_b_id__gte: str
    :param termination_b_id__gt: 
    :type termination_b_id__gt: str
    :param type__n: 
    :type type__n: str
    :param status__n: 
    :type status__n: str
    :param color__n: 
    :type color__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_console_port_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_console_port_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_console_port_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_console_port_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_port_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_console_port_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePortTemplate.from_dict(body)
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


async def dcim_console_port_templates_list(request: web.Request, id=None, name=None, type=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_console_port_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_console_ports_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_console_ports_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_console_ports_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_console_ports_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_ports_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_console_ports_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsolePort.from_dict(body)
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


async def dcim_console_ports_list(request: web.Request, id=None, name=None, label=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, connected=None, type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_console_ports_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param type: 
    :type type: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_console_server_port_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_console_server_port_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_console_server_port_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_console_server_port_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_port_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_console_server_port_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPortTemplate.from_dict(body)
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


async def dcim_console_server_port_templates_list(request: web.Request, id=None, name=None, type=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_port_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_console_server_ports_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_console_server_ports_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_console_server_ports_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_console_server_ports_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_console_server_ports_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_console_server_ports_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConsoleServerPort.from_dict(body)
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


async def dcim_console_server_ports_list(request: web.Request, id=None, name=None, label=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, connected=None, type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_ports_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param type: 
    :type type: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_device_bay_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_device_bay_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_device_bay_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_device_bay_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bay_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_device_bay_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBayTemplate.from_dict(body)
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


async def dcim_device_bay_templates_list(request: web.Request, id=None, name=None, created=None, last_updated=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bay_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_device_bays_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_device_bays_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_device_bays_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_device_bays_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBay.from_dict(body)
    return web.Response(status=200)


async def dcim_device_bays_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_device_bays_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceBay.from_dict(body)
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


async def dcim_device_bays_list(request: web.Request, id=None, name=None, label=None, description=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, created=None, last_updated=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bays_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_device_roles_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_device_roles_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_device_roles_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_device_roles_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeviceRole.from_dict(body)
    return web.Response(status=200)


async def dcim_device_roles_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_device_roles_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeviceRole.from_dict(body)
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


async def dcim_device_roles_list(request: web.Request, id=None, name=None, slug=None, color=None, vm_role=None, description=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_device_roles_list

    

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
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_device_types_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_device_types_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_device_types_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_device_types_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceType.from_dict(body)
    return web.Response(status=200)


async def dcim_device_types_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_device_types_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceType.from_dict(body)
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


async def dcim_device_types_list(request: web.Request, id=None, model=None, slug=None, part_number=None, u_height=None, is_full_depth=None, subdevice_role=None, airflow=None, weight=None, weight_unit=None, created=None, last_updated=None, q=None, tag=None, manufacturer_id=None, manufacturer=None, has_front_image=None, has_rear_image=None, console_ports=None, console_server_ports=None, power_ports=None, power_outlets=None, interfaces=None, pass_through_ports=None, module_bays=None, device_bays=None, inventory_items=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, model__n=None, model__ic=None, model__nic=None, model__iew=None, model__niew=None, model__isw=None, model__nisw=None, model__ie=None, model__nie=None, model__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, part_number__n=None, part_number__ic=None, part_number__nic=None, part_number__iew=None, part_number__niew=None, part_number__isw=None, part_number__nisw=None, part_number__ie=None, part_number__nie=None, part_number__empty=None, u_height__n=None, u_height__lte=None, u_height__lt=None, u_height__gte=None, u_height__gt=None, subdevice_role__n=None, airflow__n=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, weight_unit__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, manufacturer_id__n=None, manufacturer__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_device_types_list

    

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
    :param airflow: 
    :type airflow: str
    :param weight: 
    :type weight: str
    :param weight_unit: 
    :type weight_unit: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param has_front_image: 
    :type has_front_image: str
    :param has_rear_image: 
    :type has_rear_image: str
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
    :param module_bays: 
    :type module_bays: str
    :param device_bays: 
    :type device_bays: str
    :param inventory_items: 
    :type inventory_items: str
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
    :param model__empty: 
    :type model__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param part_number__empty: 
    :type part_number__empty: str
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
    :param airflow__n: 
    :type airflow__n: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param weight_unit__n: 
    :type weight_unit__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_devices_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_devices_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_devices_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_devices_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def dcim_devices_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_devices_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDeviceWithConfigContext.from_dict(body)
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


async def dcim_devices_list(request: web.Request, id=None, asset_tag=None, face=None, position=None, airflow=None, vc_position=None, vc_priority=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, contact=None, contact_role=None, contact_group=None, local_context_data=None, manufacturer_id=None, manufacturer=None, device_type=None, device_type_id=None, role_id=None, role=None, parent_device_id=None, platform_id=None, platform=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, rack_id=None, cluster_id=None, model=None, name=None, status=None, is_full_depth=None, mac_address=None, serial=None, has_primary_ip=None, virtual_chassis_id=None, virtual_chassis_member=None, console_ports=None, console_server_ports=None, power_ports=None, power_outlets=None, interfaces=None, pass_through_ports=None, module_bays=None, device_bays=None, primary_ip4_id=None, primary_ip6_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, asset_tag__empty=None, face__n=None, position__n=None, position__lte=None, position__lt=None, position__gte=None, position__gt=None, airflow__n=None, vc_position__n=None, vc_position__lte=None, vc_position__lt=None, vc_position__gte=None, vc_position__gt=None, vc_priority__n=None, vc_priority__lte=None, vc_priority__lt=None, vc_priority__gte=None, vc_priority__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, manufacturer_id__n=None, manufacturer__n=None, device_type__n=None, device_type_id__n=None, role_id__n=None, role__n=None, parent_device_id__n=None, platform_id__n=None, platform__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, rack_id__n=None, cluster_id__n=None, model__n=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, status__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, serial__n=None, serial__ic=None, serial__nic=None, serial__iew=None, serial__niew=None, serial__isw=None, serial__nisw=None, serial__ie=None, serial__nie=None, serial__empty=None, virtual_chassis_id__n=None, primary_ip4_id__n=None, primary_ip6_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_devices_list

    

    :param id: 
    :type id: str
    :param asset_tag: 
    :type asset_tag: str
    :param face: 
    :type face: str
    :param position: 
    :type position: str
    :param airflow: 
    :type airflow: str
    :param vc_position: 
    :type vc_position: str
    :param vc_priority: 
    :type vc_priority: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param local_context_data: 
    :type local_context_data: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param device_type: 
    :type device_type: str
    :param device_type_id: 
    :type device_type_id: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param parent_device_id: 
    :type parent_device_id: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param rack_id: 
    :type rack_id: str
    :param cluster_id: 
    :type cluster_id: str
    :param model: 
    :type model: str
    :param name: 
    :type name: str
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
    :param module_bays: 
    :type module_bays: str
    :param device_bays: 
    :type device_bays: str
    :param primary_ip4_id: 
    :type primary_ip4_id: str
    :param primary_ip6_id: 
    :type primary_ip6_id: str
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
    :param asset_tag__empty: 
    :type asset_tag__empty: str
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
    :param airflow__n: 
    :type airflow__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param device_type__n: 
    :type device_type__n: str
    :param device_type_id__n: 
    :type device_type_id__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param parent_device_id__n: 
    :type parent_device_id__n: str
    :param platform_id__n: 
    :type platform_id__n: str
    :param platform__n: 
    :type platform__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param cluster_id__n: 
    :type cluster_id__n: str
    :param model__n: 
    :type model__n: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param serial__n: 
    :type serial__n: str
    :param serial__ic: 
    :type serial__ic: str
    :param serial__nic: 
    :type serial__nic: str
    :param serial__iew: 
    :type serial__iew: str
    :param serial__niew: 
    :type serial__niew: str
    :param serial__isw: 
    :type serial__isw: str
    :param serial__nisw: 
    :type serial__nisw: str
    :param serial__ie: 
    :type serial__ie: str
    :param serial__nie: 
    :type serial__nie: str
    :param serial__empty: 
    :type serial__empty: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param primary_ip4_id__n: 
    :type primary_ip4_id__n: str
    :param primary_ip6_id__n: 
    :type primary_ip6_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_front_port_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_front_port_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_front_port_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_front_port_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_front_port_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_front_port_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPortTemplate.from_dict(body)
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


async def dcim_front_port_templates_list(request: web.Request, id=None, name=None, type=None, color=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_front_port_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param color: 
    :type color: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_front_ports_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_front_ports_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_front_ports_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_front_ports_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPort.from_dict(body)
    return web.Response(status=200)


async def dcim_front_ports_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_front_ports_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFrontPort.from_dict(body)
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


async def dcim_front_ports_list(request: web.Request, id=None, name=None, label=None, type=None, color=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, type__n=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_front_ports_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param type: 
    :type type: str
    :param color: 
    :type color: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
    :param type__n: 
    :type type__n: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_front_ports_paths(request: web.Request, id) -> web.Response:
    """dcim_front_ports_paths

    Return all CablePaths which traverse a given pass-through port.

    :param id: A unique integer value identifying this front port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_front_ports_read(request: web.Request, id) -> web.Response:
    """dcim_front_ports_read

    

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


async def dcim_interface_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_interface_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_interface_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_interface_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_interface_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceTemplate.from_dict(body)
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


async def dcim_interface_templates_list(request: web.Request, id=None, name=None, type=None, mgmt_only=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, poe_mode=None, poe_type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, poe_mode__n=None, poe_type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_interface_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param mgmt_only: 
    :type mgmt_only: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
    :param poe_mode: 
    :type poe_mode: str
    :param poe_type: 
    :type poe_type: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param poe_mode__n: 
    :type poe_mode__n: str
    :param poe_type__n: 
    :type poe_type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_interfaces_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_interfaces_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_interfaces_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_interfaces_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_interfaces_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_create(request: web.Request, body) -> web.Response:
    """dcim_interfaces_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_delete(request: web.Request, id) -> web.Response:
    """dcim_interfaces_delete

    

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_list(request: web.Request, id=None, name=None, label=None, type=None, enabled=None, mtu=None, mgmt_only=None, poe_mode=None, poe_type=None, mode=None, rf_role=None, rf_channel=None, rf_channel_frequency=None, rf_channel_width=None, tx_power=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, connected=None, kind=None, parent_id=None, bridge_id=None, lag_id=None, speed=None, duplex=None, mac_address=None, wwn=None, vlan_id=None, vlan=None, vrf_id=None, vrf=None, vdc_id=None, vdc_identifier=None, vdc=None, l2vpn_id=None, l2vpn=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, type__n=None, mtu__n=None, mtu__lte=None, mtu__lt=None, mtu__gte=None, mtu__gt=None, poe_mode__n=None, poe_type__n=None, mode__n=None, rf_role__n=None, rf_channel__n=None, rf_channel_frequency__n=None, rf_channel_frequency__lte=None, rf_channel_frequency__lt=None, rf_channel_frequency__gte=None, rf_channel_frequency__gt=None, rf_channel_width__n=None, rf_channel_width__lte=None, rf_channel_width__lt=None, rf_channel_width__gte=None, rf_channel_width__gt=None, tx_power__n=None, tx_power__lte=None, tx_power__lt=None, tx_power__gte=None, tx_power__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, parent_id__n=None, bridge_id__n=None, lag_id__n=None, speed__n=None, speed__lte=None, speed__lt=None, speed__gte=None, speed__gt=None, duplex__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, wwn__n=None, wwn__ic=None, wwn__nic=None, wwn__iew=None, wwn__niew=None, wwn__isw=None, wwn__nisw=None, wwn__ie=None, wwn__nie=None, vrf_id__n=None, vrf__n=None, vdc_id__n=None, vdc_identifier__n=None, vdc__n=None, l2vpn_id__n=None, l2vpn__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_interfaces_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param type: 
    :type type: str
    :param enabled: 
    :type enabled: str
    :param mtu: 
    :type mtu: str
    :param mgmt_only: 
    :type mgmt_only: str
    :param poe_mode: 
    :type poe_mode: str
    :param poe_type: 
    :type poe_type: str
    :param mode: 
    :type mode: str
    :param rf_role: 
    :type rf_role: str
    :param rf_channel: 
    :type rf_channel: str
    :param rf_channel_frequency: 
    :type rf_channel_frequency: str
    :param rf_channel_width: 
    :type rf_channel_width: str
    :param tx_power: 
    :type tx_power: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param kind: 
    :type kind: str
    :param parent_id: 
    :type parent_id: str
    :param bridge_id: 
    :type bridge_id: str
    :param lag_id: 
    :type lag_id: str
    :param speed: 
    :type speed: str
    :param duplex: 
    :type duplex: str
    :param mac_address: 
    :type mac_address: str
    :param wwn: 
    :type wwn: str
    :param vlan_id: 
    :type vlan_id: str
    :param vlan: 
    :type vlan: str
    :param vrf_id: 
    :type vrf_id: str
    :param vrf: 
    :type vrf: str
    :param vdc_id: 
    :type vdc_id: str
    :param vdc_identifier: 
    :type vdc_identifier: str
    :param vdc: 
    :type vdc: str
    :param l2vpn_id: 
    :type l2vpn_id: str
    :param l2vpn: 
    :type l2vpn: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param poe_mode__n: 
    :type poe_mode__n: str
    :param poe_type__n: 
    :type poe_type__n: str
    :param mode__n: 
    :type mode__n: str
    :param rf_role__n: 
    :type rf_role__n: str
    :param rf_channel__n: 
    :type rf_channel__n: str
    :param rf_channel_frequency__n: 
    :type rf_channel_frequency__n: str
    :param rf_channel_frequency__lte: 
    :type rf_channel_frequency__lte: str
    :param rf_channel_frequency__lt: 
    :type rf_channel_frequency__lt: str
    :param rf_channel_frequency__gte: 
    :type rf_channel_frequency__gte: str
    :param rf_channel_frequency__gt: 
    :type rf_channel_frequency__gt: str
    :param rf_channel_width__n: 
    :type rf_channel_width__n: str
    :param rf_channel_width__lte: 
    :type rf_channel_width__lte: str
    :param rf_channel_width__lt: 
    :type rf_channel_width__lt: str
    :param rf_channel_width__gte: 
    :type rf_channel_width__gte: str
    :param rf_channel_width__gt: 
    :type rf_channel_width__gt: str
    :param tx_power__n: 
    :type tx_power__n: str
    :param tx_power__lte: 
    :type tx_power__lte: str
    :param tx_power__lt: 
    :type tx_power__lt: str
    :param tx_power__gte: 
    :type tx_power__gte: str
    :param tx_power__gt: 
    :type tx_power__gt: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param bridge_id__n: 
    :type bridge_id__n: str
    :param lag_id__n: 
    :type lag_id__n: str
    :param speed__n: 
    :type speed__n: str
    :param speed__lte: 
    :type speed__lte: str
    :param speed__lt: 
    :type speed__lt: str
    :param speed__gte: 
    :type speed__gte: str
    :param speed__gt: 
    :type speed__gt: str
    :param duplex__n: 
    :type duplex__n: str
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
    :param wwn__n: 
    :type wwn__n: str
    :param wwn__ic: 
    :type wwn__ic: str
    :param wwn__nic: 
    :type wwn__nic: str
    :param wwn__iew: 
    :type wwn__iew: str
    :param wwn__niew: 
    :type wwn__niew: str
    :param wwn__isw: 
    :type wwn__isw: str
    :param wwn__nisw: 
    :type wwn__nisw: str
    :param wwn__ie: 
    :type wwn__ie: str
    :param wwn__nie: 
    :type wwn__nie: str
    :param vrf_id__n: 
    :type vrf_id__n: str
    :param vrf__n: 
    :type vrf__n: str
    :param vdc_id__n: 
    :type vdc_id__n: str
    :param vdc_identifier__n: 
    :type vdc_identifier__n: str
    :param vdc__n: 
    :type vdc__n: str
    :param l2vpn_id__n: 
    :type l2vpn_id__n: str
    :param l2vpn__n: 
    :type l2vpn__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_interfaces_read(request: web.Request, id) -> web.Response:
    """dcim_interfaces_read

    

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
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_roles_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_inventory_item_roles_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_inventory_item_roles_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_roles_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = InventoryItemRole.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_roles_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_roles_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = InventoryItemRole.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_roles_create(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = InventoryItemRole.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_roles_delete(request: web.Request, id) -> web.Response:
    """dcim_inventory_item_roles_delete

    

    :param id: A unique integer value identifying this inventory item role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_roles_list(request: web.Request, id=None, name=None, slug=None, color=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_inventory_item_roles_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_item_roles_partial_update

    

    :param id: A unique integer value identifying this inventory item role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = InventoryItemRole.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_roles_read(request: web.Request, id) -> web.Response:
    """dcim_inventory_item_roles_read

    

    :param id: A unique integer value identifying this inventory item role.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_roles_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_item_roles_update

    

    :param id: A unique integer value identifying this inventory item role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = InventoryItemRole.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_inventory_item_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_inventory_item_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItemTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItemTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_templates_create(request: web.Request, body) -> web.Response:
    """dcim_inventory_item_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItemTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_inventory_item_templates_delete

    

    :param id: A unique integer value identifying this inventory item template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_templates_list(request: web.Request, id=None, name=None, label=None, part_id=None, created=None, last_updated=None, q=None, devicetype_id=None, parent_id=None, manufacturer_id=None, manufacturer=None, role_id=None, role=None, component_type=None, component_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, part_id__n=None, part_id__ic=None, part_id__nic=None, part_id__iew=None, part_id__niew=None, part_id__isw=None, part_id__nisw=None, part_id__ie=None, part_id__nie=None, part_id__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, parent_id__n=None, manufacturer_id__n=None, manufacturer__n=None, role_id__n=None, role__n=None, component_type__n=None, component_id__n=None, component_id__lte=None, component_id__lt=None, component_id__gte=None, component_id__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_inventory_item_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param part_id: 
    :type part_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param parent_id: 
    :type parent_id: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param component_type: 
    :type component_type: str
    :param component_id: 
    :type component_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param part_id__empty: 
    :type part_id__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param component_type__n: 
    :type component_type__n: str
    :param component_id__n: 
    :type component_id__n: str
    :param component_id__lte: 
    :type component_id__lte: str
    :param component_id__lt: 
    :type component_id__lt: str
    :param component_id__gte: 
    :type component_id__gte: str
    :param component_id__gt: 
    :type component_id__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_item_templates_partial_update

    

    :param id: A unique integer value identifying this inventory item template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItemTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_item_templates_read(request: web.Request, id) -> web.Response:
    """dcim_inventory_item_templates_read

    

    :param id: A unique integer value identifying this inventory item template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_inventory_item_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_inventory_item_templates_update

    

    :param id: A unique integer value identifying this inventory item template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItemTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_items_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_inventory_items_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_inventory_items_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_items_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItem.from_dict(body)
    return web.Response(status=200)


async def dcim_inventory_items_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_inventory_items_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInventoryItem.from_dict(body)
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


async def dcim_inventory_items_list(request: web.Request, id=None, name=None, label=None, part_id=None, asset_tag=None, discovered=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, created=None, last_updated=None, tag=None, parent_id=None, manufacturer_id=None, manufacturer=None, role_id=None, role=None, component_type=None, component_id=None, serial=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, part_id__n=None, part_id__ic=None, part_id__nic=None, part_id__iew=None, part_id__niew=None, part_id__isw=None, part_id__nisw=None, part_id__ie=None, part_id__nie=None, part_id__empty=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, asset_tag__empty=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, parent_id__n=None, manufacturer_id__n=None, manufacturer__n=None, role_id__n=None, role__n=None, component_type__n=None, component_id__n=None, component_id__lte=None, component_id__lt=None, component_id__gte=None, component_id__gt=None, serial__n=None, serial__ic=None, serial__nic=None, serial__iew=None, serial__niew=None, serial__isw=None, serial__nisw=None, serial__ie=None, serial__nie=None, serial__empty=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_inventory_items_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
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
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param parent_id: 
    :type parent_id: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param component_type: 
    :type component_type: str
    :param component_id: 
    :type component_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param part_id__empty: 
    :type part_id__empty: str
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
    :param asset_tag__empty: 
    :type asset_tag__empty: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param component_type__n: 
    :type component_type__n: str
    :param component_id__n: 
    :type component_id__n: str
    :param component_id__lte: 
    :type component_id__lte: str
    :param component_id__lt: 
    :type component_id__lt: str
    :param component_id__gte: 
    :type component_id__gte: str
    :param component_id__gt: 
    :type component_id__gt: str
    :param serial__n: 
    :type serial__n: str
    :param serial__ic: 
    :type serial__ic: str
    :param serial__nic: 
    :type serial__nic: str
    :param serial__iew: 
    :type serial__iew: str
    :param serial__niew: 
    :type serial__niew: str
    :param serial__isw: 
    :type serial__isw: str
    :param serial__nisw: 
    :type serial__nisw: str
    :param serial__ie: 
    :type serial__ie: str
    :param serial__nie: 
    :type serial__nie: str
    :param serial__empty: 
    :type serial__empty: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_locations_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_locations_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_locations_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_locations_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableLocation.from_dict(body)
    return web.Response(status=200)


async def dcim_locations_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_locations_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableLocation.from_dict(body)
    return web.Response(status=200)


async def dcim_locations_create(request: web.Request, body) -> web.Response:
    """dcim_locations_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableLocation.from_dict(body)
    return web.Response(status=200)


async def dcim_locations_delete(request: web.Request, id) -> web.Response:
    """dcim_locations_delete

    

    :param id: A unique integer value identifying this location.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_locations_list(request: web.Request, id=None, name=None, slug=None, status=None, description=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, contact=None, contact_role=None, contact_group=None, created=None, last_updated=None, q=None, tag=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, status__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_locations_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param status: 
    :type status: str
    :param description: 
    :type description: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
    :param status__n: 
    :type status__n: str
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
    :param description__empty: 
    :type description__empty: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_locations_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_locations_partial_update

    

    :param id: A unique integer value identifying this location.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableLocation.from_dict(body)
    return web.Response(status=200)


async def dcim_locations_read(request: web.Request, id) -> web.Response:
    """dcim_locations_read

    

    :param id: A unique integer value identifying this location.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_locations_update(request: web.Request, id, body) -> web.Response:
    """dcim_locations_update

    

    :param id: A unique integer value identifying this location.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableLocation.from_dict(body)
    return web.Response(status=200)


async def dcim_manufacturers_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_manufacturers_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_manufacturers_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_manufacturers_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Manufacturer.from_dict(body)
    return web.Response(status=200)


async def dcim_manufacturers_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_manufacturers_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Manufacturer.from_dict(body)
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


async def dcim_manufacturers_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, contact=None, contact_role=None, contact_group=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_manufacturers_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_module_bay_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_module_bay_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_module_bay_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_module_bay_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bay_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_module_bay_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bay_templates_create(request: web.Request, body) -> web.Response:
    """dcim_module_bay_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bay_templates_delete(request: web.Request, id) -> web.Response:
    """dcim_module_bay_templates_delete

    

    :param id: A unique integer value identifying this module bay template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_bay_templates_list(request: web.Request, id=None, name=None, created=None, last_updated=None, q=None, devicetype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_module_bay_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_module_bay_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_bay_templates_partial_update

    

    :param id: A unique integer value identifying this module bay template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bay_templates_read(request: web.Request, id) -> web.Response:
    """dcim_module_bay_templates_read

    

    :param id: A unique integer value identifying this module bay template.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_bay_templates_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_bay_templates_update

    

    :param id: A unique integer value identifying this module bay template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBayTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bays_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_module_bays_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_module_bays_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_module_bays_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBay.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bays_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_module_bays_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBay.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bays_create(request: web.Request, body) -> web.Response:
    """dcim_module_bays_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBay.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bays_delete(request: web.Request, id) -> web.Response:
    """dcim_module_bays_delete

    

    :param id: A unique integer value identifying this module bay.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_bays_list(request: web.Request, id=None, name=None, label=None, description=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, created=None, last_updated=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_module_bays_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_module_bays_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_bays_partial_update

    

    :param id: A unique integer value identifying this module bay.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBay.from_dict(body)
    return web.Response(status=200)


async def dcim_module_bays_read(request: web.Request, id) -> web.Response:
    """dcim_module_bays_read

    

    :param id: A unique integer value identifying this module bay.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_bays_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_bays_update

    

    :param id: A unique integer value identifying this module bay.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleBay.from_dict(body)
    return web.Response(status=200)


async def dcim_module_types_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_module_types_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_module_types_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_module_types_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleType.from_dict(body)
    return web.Response(status=200)


async def dcim_module_types_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_module_types_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleType.from_dict(body)
    return web.Response(status=200)


async def dcim_module_types_create(request: web.Request, body) -> web.Response:
    """dcim_module_types_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleType.from_dict(body)
    return web.Response(status=200)


async def dcim_module_types_delete(request: web.Request, id) -> web.Response:
    """dcim_module_types_delete

    

    :param id: A unique integer value identifying this module type.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_types_list(request: web.Request, id=None, model=None, part_number=None, weight=None, weight_unit=None, created=None, last_updated=None, q=None, tag=None, manufacturer_id=None, manufacturer=None, console_ports=None, console_server_ports=None, power_ports=None, power_outlets=None, interfaces=None, pass_through_ports=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, model__n=None, model__ic=None, model__nic=None, model__iew=None, model__niew=None, model__isw=None, model__nisw=None, model__ie=None, model__nie=None, model__empty=None, part_number__n=None, part_number__ic=None, part_number__nic=None, part_number__iew=None, part_number__niew=None, part_number__isw=None, part_number__nisw=None, part_number__ie=None, part_number__nie=None, part_number__empty=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, weight_unit__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, manufacturer_id__n=None, manufacturer__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_module_types_list

    

    :param id: 
    :type id: str
    :param model: 
    :type model: str
    :param part_number: 
    :type part_number: str
    :param weight: 
    :type weight: str
    :param weight_unit: 
    :type weight_unit: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
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
    :param model__empty: 
    :type model__empty: str
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
    :param part_number__empty: 
    :type part_number__empty: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param weight_unit__n: 
    :type weight_unit__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_module_types_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_types_partial_update

    

    :param id: A unique integer value identifying this module type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleType.from_dict(body)
    return web.Response(status=200)


async def dcim_module_types_read(request: web.Request, id) -> web.Response:
    """dcim_module_types_read

    

    :param id: A unique integer value identifying this module type.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_module_types_update(request: web.Request, id, body) -> web.Response:
    """dcim_module_types_update

    

    :param id: A unique integer value identifying this module type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModuleType.from_dict(body)
    return web.Response(status=200)


async def dcim_modules_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_modules_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_modules_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_modules_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModule.from_dict(body)
    return web.Response(status=200)


async def dcim_modules_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_modules_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModule.from_dict(body)
    return web.Response(status=200)


async def dcim_modules_create(request: web.Request, body) -> web.Response:
    """dcim_modules_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableModule.from_dict(body)
    return web.Response(status=200)


async def dcim_modules_delete(request: web.Request, id) -> web.Response:
    """dcim_modules_delete

    

    :param id: A unique integer value identifying this module.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_modules_list(request: web.Request, id=None, status=None, asset_tag=None, created=None, last_updated=None, q=None, tag=None, manufacturer_id=None, manufacturer=None, module_type_id=None, module_type=None, module_bay_id=None, device_id=None, serial=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, status__n=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, asset_tag__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, manufacturer_id__n=None, manufacturer__n=None, module_type_id__n=None, module_type__n=None, module_bay_id__n=None, device_id__n=None, serial__n=None, serial__ic=None, serial__nic=None, serial__iew=None, serial__niew=None, serial__isw=None, serial__nisw=None, serial__ie=None, serial__nie=None, serial__empty=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_modules_list

    

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param asset_tag: 
    :type asset_tag: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param module_type_id: 
    :type module_type_id: str
    :param module_type: 
    :type module_type: str
    :param module_bay_id: 
    :type module_bay_id: str
    :param device_id: 
    :type device_id: str
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
    :param status__n: 
    :type status__n: str
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
    :param asset_tag__empty: 
    :type asset_tag__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param module_type_id__n: 
    :type module_type_id__n: str
    :param module_type__n: 
    :type module_type__n: str
    :param module_bay_id__n: 
    :type module_bay_id__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param serial__n: 
    :type serial__n: str
    :param serial__ic: 
    :type serial__ic: str
    :param serial__nic: 
    :type serial__nic: str
    :param serial__iew: 
    :type serial__iew: str
    :param serial__niew: 
    :type serial__niew: str
    :param serial__isw: 
    :type serial__isw: str
    :param serial__nisw: 
    :type serial__nisw: str
    :param serial__ie: 
    :type serial__ie: str
    :param serial__nie: 
    :type serial__nie: str
    :param serial__empty: 
    :type serial__empty: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_modules_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_modules_partial_update

    

    :param id: A unique integer value identifying this module.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModule.from_dict(body)
    return web.Response(status=200)


async def dcim_modules_read(request: web.Request, id) -> web.Response:
    """dcim_modules_read

    

    :param id: A unique integer value identifying this module.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_modules_update(request: web.Request, id, body) -> web.Response:
    """dcim_modules_update

    

    :param id: A unique integer value identifying this module.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableModule.from_dict(body)
    return web.Response(status=200)


async def dcim_platforms_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_platforms_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_platforms_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_platforms_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePlatform.from_dict(body)
    return web.Response(status=200)


async def dcim_platforms_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_platforms_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePlatform.from_dict(body)
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


async def dcim_platforms_list(request: web.Request, id=None, name=None, slug=None, napalm_driver=None, description=None, created=None, last_updated=None, q=None, tag=None, manufacturer_id=None, manufacturer=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, napalm_driver__n=None, napalm_driver__ic=None, napalm_driver__nic=None, napalm_driver__iew=None, napalm_driver__niew=None, napalm_driver__isw=None, napalm_driver__nisw=None, napalm_driver__ie=None, napalm_driver__nie=None, napalm_driver__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, manufacturer_id__n=None, manufacturer__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_platforms_list

    

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
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param napalm_driver__empty: 
    :type napalm_driver__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param manufacturer_id__n: 
    :type manufacturer_id__n: str
    :param manufacturer__n: 
    :type manufacturer__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_power_feeds_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_feeds_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_feeds_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_feeds_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerFeed.from_dict(body)
    return web.Response(status=200)


async def dcim_power_feeds_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_feeds_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerFeed.from_dict(body)
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


async def dcim_power_feeds_list(request: web.Request, id=None, name=None, status=None, type=None, supply=None, phase=None, voltage=None, amperage=None, max_utilization=None, cable_end=None, created=None, last_updated=None, q=None, tag=None, cabled=None, occupied=None, connected=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, power_panel_id=None, rack_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, status__n=None, type__n=None, supply__n=None, phase__n=None, voltage__n=None, voltage__lte=None, voltage__lt=None, voltage__gte=None, voltage__gt=None, amperage__n=None, amperage__lte=None, amperage__lt=None, amperage__gte=None, amperage__gt=None, max_utilization__n=None, max_utilization__lte=None, max_utilization__lt=None, max_utilization__gte=None, max_utilization__gt=None, cable_end__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, power_panel_id__n=None, rack_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_feeds_list

    

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
    :param cable_end: 
    :type cable_end: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param power_panel_id: 
    :type power_panel_id: str
    :param rack_id: 
    :type rack_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param cable_end__n: 
    :type cable_end__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param power_panel_id__n: 
    :type power_panel_id__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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

    

    :param id: A unique integer value identifying this power feed.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_power_feeds_trace(request: web.Request, id) -> web.Response:
    """dcim_power_feeds_trace

    Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

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


async def dcim_power_outlet_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_outlet_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_outlet_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_outlet_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutletTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlet_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_outlet_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutletTemplate.from_dict(body)
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


async def dcim_power_outlet_templates_list(request: web.Request, id=None, name=None, type=None, feed_leg=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, feed_leg__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlet_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param feed_leg: 
    :type feed_leg: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
    :param feed_leg__n: 
    :type feed_leg__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_power_outlets_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_outlets_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_outlets_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_outlets_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
    return web.Response(status=200)


async def dcim_power_outlets_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_outlets_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
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


async def dcim_power_outlets_list(request: web.Request, id=None, name=None, label=None, feed_leg=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, connected=None, type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, feed_leg__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlets_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param feed_leg: 
    :type feed_leg: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param type: 
    :type type: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_power_panels_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_panels_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_panels_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_panels_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPanel.from_dict(body)
    return web.Response(status=200)


async def dcim_power_panels_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_panels_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPanel.from_dict(body)
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


async def dcim_power_panels_list(request: web.Request, id=None, name=None, created=None, last_updated=None, q=None, tag=None, contact=None, contact_role=None, contact_group=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_panels_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_power_port_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_port_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_port_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_port_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_power_port_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_port_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPortTemplate.from_dict(body)
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


async def dcim_power_port_templates_list(request: web.Request, id=None, name=None, type=None, maximum_draw=None, allocated_draw=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, maximum_draw__n=None, maximum_draw__lte=None, maximum_draw__lt=None, maximum_draw__gte=None, maximum_draw__gt=None, allocated_draw__n=None, allocated_draw__lte=None, allocated_draw__lt=None, allocated_draw__gte=None, allocated_draw__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_port_templates_list

    

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
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_power_ports_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_power_ports_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_power_ports_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_power_ports_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPort.from_dict(body)
    return web.Response(status=200)


async def dcim_power_ports_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_power_ports_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerPort.from_dict(body)
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


async def dcim_power_ports_list(request: web.Request, id=None, name=None, label=None, maximum_draw=None, allocated_draw=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, connected=None, type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, maximum_draw__n=None, maximum_draw__lte=None, maximum_draw__lt=None, maximum_draw__gte=None, maximum_draw__gt=None, allocated_draw__n=None, allocated_draw__lte=None, allocated_draw__lt=None, allocated_draw__gte=None, allocated_draw__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_power_ports_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param maximum_draw: 
    :type maximum_draw: str
    :param allocated_draw: 
    :type allocated_draw: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
    :param connected: 
    :type connected: str
    :param type: 
    :type type: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param type__n: 
    :type type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_rack_reservations_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_rack_reservations_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_rack_reservations_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_rack_reservations_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackReservation.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_reservations_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_rack_reservations_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRackReservation.from_dict(body)
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


async def dcim_rack_reservations_list(request: web.Request, id=None, created=None, description=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, rack_id=None, site_id=None, site=None, region_id=None, region=None, site_group_id=None, site_group=None, location_id=None, location=None, user_id=None, user=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, rack_id__n=None, site_id__n=None, site__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, location_id__n=None, location__n=None, user_id__n=None, user__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_reservations_list

    

    :param id: 
    :type id: str
    :param created: 
    :type created: str
    :param description: 
    :type description: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param rack_id: 
    :type rack_id: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
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
    :param description__empty: 
    :type description__empty: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
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
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param user_id__n: 
    :type user_id__n: str
    :param user__n: 
    :type user__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_rack_roles_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_rack_roles_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_rack_roles_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_rack_roles_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = RackRole.from_dict(body)
    return web.Response(status=200)


async def dcim_rack_roles_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_rack_roles_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = RackRole.from_dict(body)
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


async def dcim_rack_roles_list(request: web.Request, id=None, name=None, slug=None, color=None, description=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_roles_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_racks_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_racks_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_racks_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_racks_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRack.from_dict(body)
    return web.Response(status=200)


async def dcim_racks_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_racks_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRack.from_dict(body)
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


async def dcim_racks_elevation(request: web.Request, id, q=None, face=None, render=None, unit_width=None, unit_height=None, legend_width=None, margin_width=None, exclude=None, expand_devices=None, include_images=None) -> web.Response:
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
    :param margin_width: 
    :type margin_width: int
    :param exclude: 
    :type exclude: int
    :param expand_devices: 
    :type expand_devices: bool
    :param include_images: 
    :type include_images: bool

    """
    return web.Response(status=200)


async def dcim_racks_list(request: web.Request, id=None, name=None, facility_id=None, asset_tag=None, u_height=None, desc_units=None, outer_width=None, outer_depth=None, outer_unit=None, mounting_depth=None, weight=None, max_weight=None, weight_unit=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, contact=None, contact_role=None, contact_group=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, status=None, type=None, width=None, role_id=None, role=None, serial=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, facility_id__n=None, facility_id__ic=None, facility_id__nic=None, facility_id__iew=None, facility_id__niew=None, facility_id__isw=None, facility_id__nisw=None, facility_id__ie=None, facility_id__nie=None, facility_id__empty=None, asset_tag__n=None, asset_tag__ic=None, asset_tag__nic=None, asset_tag__iew=None, asset_tag__niew=None, asset_tag__isw=None, asset_tag__nisw=None, asset_tag__ie=None, asset_tag__nie=None, asset_tag__empty=None, u_height__n=None, u_height__lte=None, u_height__lt=None, u_height__gte=None, u_height__gt=None, outer_width__n=None, outer_width__lte=None, outer_width__lt=None, outer_width__gte=None, outer_width__gt=None, outer_depth__n=None, outer_depth__lte=None, outer_depth__lt=None, outer_depth__gte=None, outer_depth__gt=None, outer_unit__n=None, mounting_depth__n=None, mounting_depth__lte=None, mounting_depth__lt=None, mounting_depth__gte=None, mounting_depth__gt=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, max_weight__n=None, max_weight__lte=None, max_weight__lt=None, max_weight__gte=None, max_weight__gt=None, weight_unit__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, status__n=None, type__n=None, width__n=None, role_id__n=None, role__n=None, serial__n=None, serial__ic=None, serial__nic=None, serial__iew=None, serial__niew=None, serial__isw=None, serial__nisw=None, serial__ie=None, serial__nie=None, serial__empty=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_racks_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param facility_id: 
    :type facility_id: str
    :param asset_tag: 
    :type asset_tag: str
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
    :param mounting_depth: 
    :type mounting_depth: str
    :param weight: 
    :type weight: str
    :param max_weight: 
    :type max_weight: str
    :param weight_unit: 
    :type weight_unit: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param status: 
    :type status: str
    :param type: 
    :type type: str
    :param width: 
    :type width: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param facility_id__empty: 
    :type facility_id__empty: str
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
    :param asset_tag__empty: 
    :type asset_tag__empty: str
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
    :param mounting_depth__n: 
    :type mounting_depth__n: str
    :param mounting_depth__lte: 
    :type mounting_depth__lte: str
    :param mounting_depth__lt: 
    :type mounting_depth__lt: str
    :param mounting_depth__gte: 
    :type mounting_depth__gte: str
    :param mounting_depth__gt: 
    :type mounting_depth__gt: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param max_weight__n: 
    :type max_weight__n: str
    :param max_weight__lte: 
    :type max_weight__lte: str
    :param max_weight__lt: 
    :type max_weight__lt: str
    :param max_weight__gte: 
    :type max_weight__gte: str
    :param max_weight__gt: 
    :type max_weight__gt: str
    :param weight_unit__n: 
    :type weight_unit__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param status__n: 
    :type status__n: str
    :param type__n: 
    :type type__n: str
    :param width__n: 
    :type width__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param serial__n: 
    :type serial__n: str
    :param serial__ic: 
    :type serial__ic: str
    :param serial__nic: 
    :type serial__nic: str
    :param serial__iew: 
    :type serial__iew: str
    :param serial__niew: 
    :type serial__niew: str
    :param serial__isw: 
    :type serial__isw: str
    :param serial__nisw: 
    :type serial__nisw: str
    :param serial__ie: 
    :type serial__ie: str
    :param serial__nie: 
    :type serial__nie: str
    :param serial__empty: 
    :type serial__empty: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_rear_port_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_rear_port_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_rear_port_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_rear_port_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPortTemplate.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_port_templates_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_rear_port_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPortTemplate.from_dict(body)
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


async def dcim_rear_port_templates_list(request: web.Request, id=None, name=None, type=None, color=None, positions=None, created=None, last_updated=None, q=None, devicetype_id=None, moduletype_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, type__n=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, positions__n=None, positions__lte=None, positions__lt=None, positions__gte=None, positions__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, devicetype_id__n=None, moduletype_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_rear_port_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type: 
    :type type: str
    :param color: 
    :type color: str
    :param positions: 
    :type positions: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param devicetype_id: 
    :type devicetype_id: str
    :param moduletype_id: 
    :type moduletype_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param type__n: 
    :type type__n: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param devicetype_id__n: 
    :type devicetype_id__n: str
    :param moduletype_id__n: 
    :type moduletype_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_rear_ports_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_rear_ports_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_rear_ports_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_rear_ports_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPort.from_dict(body)
    return web.Response(status=200)


async def dcim_rear_ports_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_rear_ports_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRearPort.from_dict(body)
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


async def dcim_rear_ports_list(request: web.Request, id=None, name=None, label=None, type=None, color=None, positions=None, description=None, cable_end=None, q=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, location_id=None, location=None, rack_id=None, rack=None, device_id=None, device=None, virtual_chassis_id=None, virtual_chassis=None, module_id=None, created=None, last_updated=None, tag=None, cabled=None, occupied=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, label__n=None, label__ic=None, label__nic=None, label__iew=None, label__niew=None, label__isw=None, label__nisw=None, label__ie=None, label__nie=None, label__empty=None, type__n=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, positions__n=None, positions__lte=None, positions__lt=None, positions__gte=None, positions__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, cable_end__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, rack_id__n=None, rack__n=None, device_id__n=None, device__n=None, virtual_chassis_id__n=None, virtual_chassis__n=None, module_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_rear_ports_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param label: 
    :type label: str
    :param type: 
    :type type: str
    :param color: 
    :type color: str
    :param positions: 
    :type positions: str
    :param description: 
    :type description: str
    :param cable_end: 
    :type cable_end: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param rack_id: 
    :type rack_id: str
    :param rack: 
    :type rack: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param virtual_chassis: 
    :type virtual_chassis: str
    :param module_id: 
    :type module_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param tag: 
    :type tag: str
    :param cabled: 
    :type cabled: str
    :param occupied: 
    :type occupied: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param label__empty: 
    :type label__empty: str
    :param type__n: 
    :type type__n: str
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
    :param color__empty: 
    :type color__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param cable_end__n: 
    :type cable_end__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param rack_id__n: 
    :type rack_id__n: str
    :param rack__n: 
    :type rack__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_chassis_id__n: 
    :type virtual_chassis_id__n: str
    :param virtual_chassis__n: 
    :type virtual_chassis__n: str
    :param module_id__n: 
    :type module_id__n: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_rear_ports_paths(request: web.Request, id) -> web.Response:
    """dcim_rear_ports_paths

    Return all CablePaths which traverse a given pass-through port.

    :param id: A unique integer value identifying this rear port.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_rear_ports_read(request: web.Request, id) -> web.Response:
    """dcim_rear_ports_read

    

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


async def dcim_regions_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_regions_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_regions_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_regions_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRegion.from_dict(body)
    return web.Response(status=200)


async def dcim_regions_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_regions_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRegion.from_dict(body)
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


async def dcim_regions_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, contact=None, contact_role=None, contact_group=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_regions_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_site_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_site_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_site_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_site_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSiteGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_site_groups_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_site_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSiteGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_site_groups_create(request: web.Request, body) -> web.Response:
    """dcim_site_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSiteGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_site_groups_delete(request: web.Request, id) -> web.Response:
    """dcim_site_groups_delete

    

    :param id: A unique integer value identifying this site group.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_site_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, contact=None, contact_role=None, contact_group=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_site_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_site_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_site_groups_partial_update

    

    :param id: A unique integer value identifying this site group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSiteGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_site_groups_read(request: web.Request, id) -> web.Response:
    """dcim_site_groups_read

    

    :param id: A unique integer value identifying this site group.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_site_groups_update(request: web.Request, id, body) -> web.Response:
    """dcim_site_groups_update

    

    :param id: A unique integer value identifying this site group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSiteGroup.from_dict(body)
    return web.Response(status=200)


async def dcim_sites_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_sites_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_sites_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_sites_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSite.from_dict(body)
    return web.Response(status=200)


async def dcim_sites_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_sites_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSite.from_dict(body)
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


async def dcim_sites_list(request: web.Request, id=None, name=None, slug=None, facility=None, latitude=None, longitude=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, contact=None, contact_role=None, contact_group=None, status=None, region_id=None, region=None, group_id=None, group=None, asn=None, asn_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, facility__n=None, facility__ic=None, facility__nic=None, facility__iew=None, facility__niew=None, facility__isw=None, facility__nisw=None, facility__ie=None, facility__nie=None, facility__empty=None, latitude__n=None, latitude__lte=None, latitude__lt=None, latitude__gte=None, latitude__gt=None, longitude__n=None, longitude__lte=None, longitude__lt=None, longitude__gte=None, longitude__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, status__n=None, region_id__n=None, region__n=None, group_id__n=None, group__n=None, asn__n=None, asn_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_sites_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param facility: 
    :type facility: str
    :param latitude: 
    :type latitude: str
    :param longitude: 
    :type longitude: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param status: 
    :type status: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param asn: 
    :type asn: str
    :param asn_id: 
    :type asn_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param facility__empty: 
    :type facility__empty: str
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
    :param description__empty: 
    :type description__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param status__n: 
    :type status__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param asn__n: 
    :type asn__n: str
    :param asn_id__n: 
    :type asn_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_virtual_chassis_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_virtual_chassis_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_virtual_chassis_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_virtual_chassis_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualChassis.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_chassis_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_virtual_chassis_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualChassis.from_dict(body)
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


async def dcim_virtual_chassis_list(request: web.Request, id=None, domain=None, name=None, created=None, last_updated=None, q=None, tag=None, master_id=None, master=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, tenant_id=None, tenant=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, domain__n=None, domain__ic=None, domain__nic=None, domain__iew=None, domain__niew=None, domain__isw=None, domain__nisw=None, domain__ie=None, domain__nie=None, domain__empty=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, master_id__n=None, master__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, tenant_id__n=None, tenant__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_virtual_chassis_list

    

    :param id: 
    :type id: str
    :param domain: 
    :type domain: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param master_id: 
    :type master_id: str
    :param master: 
    :type master: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
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
    :param domain__empty: 
    :type domain__empty: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param master_id__n: 
    :type master_id__n: str
    :param master__n: 
    :type master__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def dcim_virtual_device_contexts_bulk_delete(request: web.Request, ) -> web.Response:
    """dcim_virtual_device_contexts_bulk_delete

    


    """
    return web.Response(status=200)


async def dcim_virtual_device_contexts_bulk_partial_update(request: web.Request, body) -> web.Response:
    """dcim_virtual_device_contexts_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualDeviceContext.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_device_contexts_bulk_update(request: web.Request, body) -> web.Response:
    """dcim_virtual_device_contexts_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualDeviceContext.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_device_contexts_create(request: web.Request, body) -> web.Response:
    """dcim_virtual_device_contexts_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualDeviceContext.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_device_contexts_delete(request: web.Request, id) -> web.Response:
    """dcim_virtual_device_contexts_delete

    

    :param id: A unique integer value identifying this virtual device context.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_virtual_device_contexts_list(request: web.Request, id=None, device=None, name=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, device_id=None, status=None, has_primary_ip=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, device__n=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, device_id__n=None, status__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """dcim_virtual_device_contexts_list

    

    :param id: 
    :type id: str
    :param device: 
    :type device: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param device_id: 
    :type device_id: str
    :param status: 
    :type status: str
    :param has_primary_ip: 
    :type has_primary_ip: str
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
    :param device__n: 
    :type device__n: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param status__n: 
    :type status__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_virtual_device_contexts_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_virtual_device_contexts_partial_update

    

    :param id: A unique integer value identifying this virtual device context.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualDeviceContext.from_dict(body)
    return web.Response(status=200)


async def dcim_virtual_device_contexts_read(request: web.Request, id) -> web.Response:
    """dcim_virtual_device_contexts_read

    

    :param id: A unique integer value identifying this virtual device context.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_virtual_device_contexts_update(request: web.Request, id, body) -> web.Response:
    """dcim_virtual_device_contexts_update

    

    :param id: A unique integer value identifying this virtual device context.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualDeviceContext.from_dict(body)
    return web.Response(status=200)
