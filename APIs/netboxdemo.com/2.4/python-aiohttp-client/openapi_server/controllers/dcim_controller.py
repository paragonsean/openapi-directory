from typing import List, Dict
from aiohttp import web

from openapi_server.models.console_port import ConsolePort
from openapi_server.models.console_port_template import ConsolePortTemplate
from openapi_server.models.console_server_port import ConsoleServerPort
from openapi_server.models.console_server_port_template import ConsoleServerPortTemplate
from openapi_server.models.dcim_console_connections_list200_response import DcimConsoleConnectionsList200Response
from openapi_server.models.dcim_console_port_templates_list200_response import DcimConsolePortTemplatesList200Response
from openapi_server.models.dcim_console_server_port_templates_list200_response import DcimConsoleServerPortTemplatesList200Response
from openapi_server.models.dcim_console_server_ports_list200_response import DcimConsoleServerPortsList200Response
from openapi_server.models.dcim_device_bay_templates_list200_response import DcimDeviceBayTemplatesList200Response
from openapi_server.models.dcim_device_bays_list200_response import DcimDeviceBaysList200Response
from openapi_server.models.dcim_device_roles_list200_response import DcimDeviceRolesList200Response
from openapi_server.models.dcim_device_types_list200_response import DcimDeviceTypesList200Response
from openapi_server.models.dcim_devices_list200_response import DcimDevicesList200Response
from openapi_server.models.dcim_interface_connections_list200_response import DcimInterfaceConnectionsList200Response
from openapi_server.models.dcim_interface_templates_list200_response import DcimInterfaceTemplatesList200Response
from openapi_server.models.dcim_interfaces_list200_response import DcimInterfacesList200Response
from openapi_server.models.dcim_inventory_items_list200_response import DcimInventoryItemsList200Response
from openapi_server.models.dcim_manufacturers_list200_response import DcimManufacturersList200Response
from openapi_server.models.dcim_platforms_list200_response import DcimPlatformsList200Response
from openapi_server.models.dcim_power_connections_list200_response import DcimPowerConnectionsList200Response
from openapi_server.models.dcim_power_outlet_templates_list200_response import DcimPowerOutletTemplatesList200Response
from openapi_server.models.dcim_power_outlets_list200_response import DcimPowerOutletsList200Response
from openapi_server.models.dcim_power_port_templates_list200_response import DcimPowerPortTemplatesList200Response
from openapi_server.models.dcim_rack_groups_list200_response import DcimRackGroupsList200Response
from openapi_server.models.dcim_rack_reservations_list200_response import DcimRackReservationsList200Response
from openapi_server.models.dcim_rack_roles_list200_response import DcimRackRolesList200Response
from openapi_server.models.dcim_racks_list200_response import DcimRacksList200Response
from openapi_server.models.dcim_regions_list200_response import DcimRegionsList200Response
from openapi_server.models.dcim_sites_list200_response import DcimSitesList200Response
from openapi_server.models.dcim_virtual_chassis_list200_response import DcimVirtualChassisList200Response
from openapi_server.models.device import Device
from openapi_server.models.device_bay import DeviceBay
from openapi_server.models.device_bay_template import DeviceBayTemplate
from openapi_server.models.device_role import DeviceRole
from openapi_server.models.device_type import DeviceType
from openapi_server.models.device_with_config_context import DeviceWithConfigContext
from openapi_server.models.interface import Interface
from openapi_server.models.interface_connection import InterfaceConnection
from openapi_server.models.interface_template import InterfaceTemplate
from openapi_server.models.inventory_item import InventoryItem
from openapi_server.models.manufacturer import Manufacturer
from openapi_server.models.platform import Platform
from openapi_server.models.power_outlet import PowerOutlet
from openapi_server.models.power_outlet_template import PowerOutletTemplate
from openapi_server.models.power_port import PowerPort
from openapi_server.models.power_port_template import PowerPortTemplate
from openapi_server.models.rack import Rack
from openapi_server.models.rack_group import RackGroup
from openapi_server.models.rack_reservation import RackReservation
from openapi_server.models.rack_role import RackRole
from openapi_server.models.region import Region
from openapi_server.models.site import Site
from openapi_server.models.virtual_chassis import VirtualChassis
from openapi_server.models.writable_console_port import WritableConsolePort
from openapi_server.models.writable_console_port_template import WritableConsolePortTemplate
from openapi_server.models.writable_console_server_port import WritableConsoleServerPort
from openapi_server.models.writable_console_server_port_template import WritableConsoleServerPortTemplate
from openapi_server.models.writable_device import WritableDevice
from openapi_server.models.writable_device_bay import WritableDeviceBay
from openapi_server.models.writable_device_bay_template import WritableDeviceBayTemplate
from openapi_server.models.writable_device_type import WritableDeviceType
from openapi_server.models.writable_interface import WritableInterface
from openapi_server.models.writable_interface_connection import WritableInterfaceConnection
from openapi_server.models.writable_interface_template import WritableInterfaceTemplate
from openapi_server.models.writable_inventory_item import WritableInventoryItem
from openapi_server.models.writable_platform import WritablePlatform
from openapi_server.models.writable_power_outlet import WritablePowerOutlet
from openapi_server.models.writable_power_outlet_template import WritablePowerOutletTemplate
from openapi_server.models.writable_power_port import WritablePowerPort
from openapi_server.models.writable_power_port_template import WritablePowerPortTemplate
from openapi_server.models.writable_rack import WritableRack
from openapi_server.models.writable_rack_group import WritableRackGroup
from openapi_server.models.writable_rack_reservation import WritableRackReservation
from openapi_server.models.writable_region import WritableRegion
from openapi_server.models.writable_site import WritableSite
from openapi_server.models.writable_virtual_chassis import WritableVirtualChassis
from openapi_server import util


async def dcim_choices_list(request: web.Request, ) -> web.Response:
    """dcim_choices_list

    


    """
    return web.Response(status=200)


async def dcim_choices_read(request: web.Request, id) -> web.Response:
    """dcim_choices_read

    

    :param id: 
    :type id: str

    """
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


async def dcim_console_connections_list(request: web.Request, name=None, connection_status=None, site=None, device=None, limit=None, offset=None) -> web.Response:
    """dcim_console_connections_list

    

    :param name: 
    :type name: str
    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device: 
    :type device: str
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


async def dcim_console_port_templates_list(request: web.Request, name=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_console_port_templates_list

    

    :param name: 
    :type name: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_console_ports_list(request: web.Request, name=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_console_ports_list

    

    :param name: 
    :type name: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
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


async def dcim_console_server_port_templates_list(request: web.Request, name=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_port_templates_list

    

    :param name: 
    :type name: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_console_server_ports_list(request: web.Request, name=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_console_server_ports_list

    

    :param name: 
    :type name: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
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


async def dcim_device_bay_templates_list(request: web.Request, name=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bay_templates_list

    

    :param name: 
    :type name: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_device_bays_list(request: web.Request, name=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_device_bays_list

    

    :param name: 
    :type name: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
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


async def dcim_device_roles_list(request: web.Request, name=None, slug=None, color=None, vm_role=None, limit=None, offset=None) -> web.Response:
    """dcim_device_roles_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param vm_role: 
    :type vm_role: str
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


async def dcim_device_types_list(request: web.Request, model=None, slug=None, part_number=None, u_height=None, is_full_depth=None, is_console_server=None, is_pdu=None, is_network_device=None, subdevice_role=None, id__in=None, q=None, manufacturer_id=None, manufacturer=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_device_types_list

    

    :param model: 
    :type model: str
    :param slug: 
    :type slug: str
    :param part_number: 
    :type part_number: str
    :param u_height: 
    :type u_height: 
    :param is_full_depth: 
    :type is_full_depth: str
    :param is_console_server: 
    :type is_console_server: str
    :param is_pdu: 
    :type is_pdu: str
    :param is_network_device: 
    :type is_network_device: str
    :param subdevice_role: 
    :type subdevice_role: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
    :param tag: 
    :type tag: str
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


async def dcim_devices_create(request: web.Request, body) -> web.Response:
    """dcim_devices_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableDevice.from_dict(body)
    return web.Response(status=200)


async def dcim_devices_delete(request: web.Request, id) -> web.Response:
    """dcim_devices_delete

    

    :param id: A unique integer value identifying this device.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_devices_list(request: web.Request, serial=None, position=None, id__in=None, q=None, manufacturer_id=None, manufacturer=None, device_type_id=None, role_id=None, role=None, tenant_id=None, tenant=None, platform_id=None, platform=None, name=None, asset_tag=None, region_id=None, region=None, site_id=None, site=None, rack_group_id=None, rack_id=None, cluster_id=None, model=None, status=None, is_full_depth=None, is_console_server=None, is_pdu=None, is_network_device=None, mac_address=None, has_primary_ip=None, virtual_chassis_id=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_devices_list

    

    :param serial: 
    :type serial: str
    :param position: 
    :type position: 
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
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
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param name: 
    :type name: str
    :param asset_tag: 
    :type asset_tag: str
    :param region_id: 
    :type region_id: 
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
    :param is_console_server: 
    :type is_console_server: str
    :param is_pdu: 
    :type is_pdu: str
    :param is_network_device: 
    :type is_network_device: str
    :param mac_address: 
    :type mac_address: str
    :param has_primary_ip: 
    :type has_primary_ip: str
    :param virtual_chassis_id: 
    :type virtual_chassis_id: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_devices_napalm(request: web.Request, id) -> web.Response:
    """dcim_devices_napalm

    Execute a NAPALM method on a Device

    :param id: A unique integer value identifying this device.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_devices_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_devices_partial_update

    

    :param id: A unique integer value identifying this device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableDevice.from_dict(body)
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
    body = WritableDevice.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_connections_create(request: web.Request, body) -> web.Response:
    """dcim_interface_connections_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceConnection.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_connections_delete(request: web.Request, id) -> web.Response:
    """dcim_interface_connections_delete

    

    :param id: A unique integer value identifying this interface connection.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interface_connections_list(request: web.Request, connection_status=None, site=None, device=None, limit=None, offset=None) -> web.Response:
    """dcim_interface_connections_list

    

    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device: 
    :type device: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def dcim_interface_connections_partial_update(request: web.Request, id, body) -> web.Response:
    """dcim_interface_connections_partial_update

    

    :param id: A unique integer value identifying this interface connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceConnection.from_dict(body)
    return web.Response(status=200)


async def dcim_interface_connections_read(request: web.Request, id) -> web.Response:
    """dcim_interface_connections_read

    

    :param id: A unique integer value identifying this interface connection.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interface_connections_update(request: web.Request, id, body) -> web.Response:
    """dcim_interface_connections_update

    

    :param id: A unique integer value identifying this interface connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterfaceConnection.from_dict(body)
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


async def dcim_interface_templates_list(request: web.Request, name=None, form_factor=None, mgmt_only=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_interface_templates_list

    

    :param name: 
    :type name: str
    :param form_factor: 
    :type form_factor: str
    :param mgmt_only: 
    :type mgmt_only: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_interfaces_graphs(request: web.Request, id) -> web.Response:
    """dcim_interfaces_graphs

    A convenience method for rendering graphs for a particular interface.

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def dcim_interfaces_list(request: web.Request, name=None, enabled=None, mtu=None, mgmt_only=None, device=None, device_id=None, type=None, lag_id=None, mac_address=None, tag=None, vlan_id=None, vlan=None, form_factor=None, limit=None, offset=None) -> web.Response:
    """dcim_interfaces_list

    

    :param name: 
    :type name: str
    :param enabled: 
    :type enabled: str
    :param mtu: 
    :type mtu: 
    :param mgmt_only: 
    :type mgmt_only: str
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: 
    :param type: 
    :type type: str
    :param lag_id: 
    :type lag_id: str
    :param mac_address: 
    :type mac_address: str
    :param tag: 
    :type tag: str
    :param vlan_id: 
    :type vlan_id: str
    :param vlan: 
    :type vlan: str
    :param form_factor: 
    :type form_factor: str
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


async def dcim_interfaces_update(request: web.Request, id, body) -> web.Response:
    """dcim_interfaces_update

    

    :param id: A unique integer value identifying this interface.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableInterface.from_dict(body)
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


async def dcim_inventory_items_list(request: web.Request, name=None, part_id=None, serial=None, asset_tag=None, discovered=None, device_id=None, device=None, tag=None, q=None, parent_id=None, manufacturer_id=None, manufacturer=None, limit=None, offset=None) -> web.Response:
    """dcim_inventory_items_list

    

    :param name: 
    :type name: str
    :param part_id: 
    :type part_id: str
    :param serial: 
    :type serial: str
    :param asset_tag: 
    :type asset_tag: str
    :param discovered: 
    :type discovered: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param q: 
    :type q: str
    :param parent_id: 
    :type parent_id: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
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


async def dcim_manufacturers_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """dcim_manufacturers_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
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


async def dcim_platforms_list(request: web.Request, name=None, slug=None, manufacturer_id=None, manufacturer=None, limit=None, offset=None) -> web.Response:
    """dcim_platforms_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param manufacturer_id: 
    :type manufacturer_id: str
    :param manufacturer: 
    :type manufacturer: str
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


async def dcim_power_connections_list(request: web.Request, name=None, connection_status=None, site=None, device=None, limit=None, offset=None) -> web.Response:
    """dcim_power_connections_list

    

    :param name: 
    :type name: str
    :param connection_status: 
    :type connection_status: str
    :param site: 
    :type site: str
    :param device: 
    :type device: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
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


async def dcim_power_outlet_templates_list(request: web.Request, name=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlet_templates_list

    

    :param name: 
    :type name: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_power_outlets_list(request: web.Request, name=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_power_outlets_list

    

    :param name: 
    :type name: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
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


async def dcim_power_outlets_update(request: web.Request, id, body) -> web.Response:
    """dcim_power_outlets_update

    

    :param id: A unique integer value identifying this power outlet.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePowerOutlet.from_dict(body)
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


async def dcim_power_port_templates_list(request: web.Request, name=None, devicetype_id=None, limit=None, offset=None) -> web.Response:
    """dcim_power_port_templates_list

    

    :param name: 
    :type name: str
    :param devicetype_id: 
    :type devicetype_id: str
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


async def dcim_power_ports_list(request: web.Request, name=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_power_ports_list

    

    :param name: 
    :type name: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
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


async def dcim_rack_groups_list(request: web.Request, site_id=None, name=None, slug=None, q=None, site=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_groups_list

    

    :param site_id: 
    :type site_id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param site: 
    :type site: str
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


async def dcim_rack_reservations_list(request: web.Request, created=None, id__in=None, q=None, rack_id=None, site_id=None, site=None, group_id=None, group=None, tenant_id=None, tenant=None, user_id=None, user=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_reservations_list

    

    :param created: 
    :type created: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
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
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: str
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


async def dcim_rack_roles_list(request: web.Request, name=None, slug=None, color=None, limit=None, offset=None) -> web.Response:
    """dcim_rack_roles_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
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


async def dcim_racks_list(request: web.Request, name=None, serial=None, type=None, width=None, u_height=None, desc_units=None, id__in=None, q=None, facility_id=None, site_id=None, site=None, group_id=None, group=None, tenant_id=None, tenant=None, role_id=None, role=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_racks_list

    

    :param name: 
    :type name: str
    :param serial: 
    :type serial: str
    :param type: 
    :type type: str
    :param width: 
    :type width: str
    :param u_height: 
    :type u_height: 
    :param desc_units: 
    :type desc_units: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param facility_id: 
    :type facility_id: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param tag: 
    :type tag: str
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


async def dcim_racks_units(request: web.Request, id) -> web.Response:
    """dcim_racks_units

    List rack units (by rack)

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


async def dcim_regions_list(request: web.Request, name=None, slug=None, q=None, parent_id=None, parent=None, limit=None, offset=None) -> web.Response:
    """dcim_regions_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param parent_id: 
    :type parent_id: str
    :param parent: 
    :type parent: str
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


async def dcim_sites_list(request: web.Request, q=None, name=None, slug=None, facility=None, asn=None, contact_name=None, contact_phone=None, contact_email=None, id__in=None, status=None, region_id=None, region=None, tenant_id=None, tenant=None, tag=None, limit=None, offset=None) -> web.Response:
    """dcim_sites_list

    

    :param q: 
    :type q: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param facility: 
    :type facility: str
    :param asn: 
    :type asn: 
    :param contact_name: 
    :type contact_name: str
    :param contact_phone: 
    :type contact_phone: str
    :param contact_email: 
    :type contact_email: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param status: 
    :type status: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param tag: 
    :type tag: str
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


async def dcim_virtual_chassis_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """dcim_virtual_chassis_list

    

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
