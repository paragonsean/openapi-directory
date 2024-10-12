# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_bulk_delete(client):
    """Test case for dcim_cable_terminations_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/cable-terminations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_bulk_partial_update(client):
    """Test case for dcim_cable_terminations_bulk_partial_update

    
    """
    body = {"termination":"{}","termination_type":"termination_type","termination_id":2147483647,"display":"display","cable_end":"A","id":1,"cable":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/cable-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_bulk_update(client):
    """Test case for dcim_cable_terminations_bulk_update

    
    """
    body = {"termination":"{}","termination_type":"termination_type","termination_id":2147483647,"display":"display","cable_end":"A","id":1,"cable":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/cable-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_create(client):
    """Test case for dcim_cable_terminations_create

    
    """
    body = {"termination":"{}","termination_type":"termination_type","termination_id":2147483647,"display":"display","cable_end":"A","id":1,"cable":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/cable-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_delete(client):
    """Test case for dcim_cable_terminations_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/cable-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_list(client):
    """Test case for dcim_cable_terminations_list

    
    """
    params = [('id', 'id_example'),
                    ('cable', 'cable_example'),
                    ('cable_end', 'cable_end_example'),
                    ('termination_type', 'termination_type_example'),
                    ('termination_id', 'termination_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('cable__n', 'cable__n_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('termination_type__n', 'termination_type__n_example'),
                    ('termination_id__n', 'termination_id__n_example'),
                    ('termination_id__lte', 'termination_id__lte_example'),
                    ('termination_id__lt', 'termination_id__lt_example'),
                    ('termination_id__gte', 'termination_id__gte_example'),
                    ('termination_id__gt', 'termination_id__gt_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/cable-terminations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_partial_update(client):
    """Test case for dcim_cable_terminations_partial_update

    
    """
    body = {"termination":"{}","termination_type":"termination_type","termination_id":2147483647,"display":"display","cable_end":"A","id":1,"cable":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/cable-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_read(client):
    """Test case for dcim_cable_terminations_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/cable-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cable_terminations_update(client):
    """Test case for dcim_cable_terminations_update

    
    """
    body = {"termination":"{}","termination_type":"termination_type","termination_id":2147483647,"display":"display","cable_end":"A","id":1,"cable":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/cable-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_bulk_delete(client):
    """Test case for dcim_cables_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/cables/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_bulk_partial_update(client):
    """Test case for dcim_cables_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","length":6.027456183070403,"description":"description","label":"label","type":"cat3","url":"https://openapi-generator.tech","length_unit":"km","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"a_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"b_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"id":0,"tenant":1,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/cables/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_bulk_update(client):
    """Test case for dcim_cables_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","length":6.027456183070403,"description":"description","label":"label","type":"cat3","url":"https://openapi-generator.tech","length_unit":"km","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"a_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"b_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"id":0,"tenant":1,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/cables/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_create(client):
    """Test case for dcim_cables_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","length":6.027456183070403,"description":"description","label":"label","type":"cat3","url":"https://openapi-generator.tech","length_unit":"km","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"a_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"b_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"id":0,"tenant":1,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/cables/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_delete(client):
    """Test case for dcim_cables_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/cables/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_list(client):
    """Test case for dcim_cables_list

    
    """
    params = [('id', 'id_example'),
                    ('label', 'label_example'),
                    ('length', 'length_example'),
                    ('length_unit', 'length_unit_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('termination_a_type', 'termination_a_type_example'),
                    ('termination_a_id', 'termination_a_id_example'),
                    ('termination_b_type', 'termination_b_type_example'),
                    ('termination_b_id', 'termination_b_id_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('color', 'color_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('length__n', 'length__n_example'),
                    ('length__lte', 'length__lte_example'),
                    ('length__lt', 'length__lt_example'),
                    ('length__gte', 'length__gte_example'),
                    ('length__gt', 'length__gt_example'),
                    ('length_unit__n', 'length_unit__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('termination_a_type__n', 'termination_a_type__n_example'),
                    ('termination_a_id__n', 'termination_a_id__n_example'),
                    ('termination_a_id__lte', 'termination_a_id__lte_example'),
                    ('termination_a_id__lt', 'termination_a_id__lt_example'),
                    ('termination_a_id__gte', 'termination_a_id__gte_example'),
                    ('termination_a_id__gt', 'termination_a_id__gt_example'),
                    ('termination_b_type__n', 'termination_b_type__n_example'),
                    ('termination_b_id__n', 'termination_b_id__n_example'),
                    ('termination_b_id__lte', 'termination_b_id__lte_example'),
                    ('termination_b_id__lt', 'termination_b_id__lt_example'),
                    ('termination_b_id__gte', 'termination_b_id__gte_example'),
                    ('termination_b_id__gt', 'termination_b_id__gt_example'),
                    ('type__n', 'type__n_example'),
                    ('status__n', 'status__n_example'),
                    ('color__n', 'color__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/cables/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_partial_update(client):
    """Test case for dcim_cables_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","length":6.027456183070403,"description":"description","label":"label","type":"cat3","url":"https://openapi-generator.tech","length_unit":"km","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"a_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"b_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"id":0,"tenant":1,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/cables/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_read(client):
    """Test case for dcim_cables_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/cables/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_update(client):
    """Test case for dcim_cables_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","length":6.027456183070403,"description":"description","label":"label","type":"cat3","url":"https://openapi-generator.tech","length_unit":"km","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"a_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"b_terminations":[{"object_type":"object_type","object_id":6,"object":"{}"},{"object_type":"object_type","object_id":6,"object":"{}"}],"id":0,"tenant":1,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/cables/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_connected_device_list(client):
    """Test case for dcim_connected_device_list

    
    """
    params = [('peer_device', 'peer_device_example'),
                    ('peer_interface', 'peer_interface_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/connected-device/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_bulk_delete(client):
    """Test case for dcim_console_port_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-port-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_bulk_partial_update(client):
    """Test case for dcim_console_port_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_bulk_update(client):
    """Test case for dcim_console_port_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_create(client):
    """Test case for dcim_console_port_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/console-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_delete(client):
    """Test case for dcim_console_port_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_list(client):
    """Test case for dcim_console_port_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-port-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_partial_update(client):
    """Test case for dcim_console_port_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_read(client):
    """Test case for dcim_console_port_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_update(client):
    """Test case for dcim_console_port_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_bulk_delete(client):
    """Test case for dcim_console_ports_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-ports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_bulk_partial_update(client):
    """Test case for dcim_console_ports_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_bulk_update(client):
    """Test case for dcim_console_ports_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_create(client):
    """Test case for dcim_console_ports_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/console-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_delete(client):
    """Test case for dcim_console_ports_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_list(client):
    """Test case for dcim_console_ports_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('type', 'type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-ports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_partial_update(client):
    """Test case for dcim_console_ports_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_read(client):
    """Test case for dcim_console_ports_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_trace(client):
    """Test case for dcim_console_ports_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-ports/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_ports_update(client):
    """Test case for dcim_console_ports_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_bulk_delete(client):
    """Test case for dcim_console_server_port_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-server-port-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_bulk_partial_update(client):
    """Test case for dcim_console_server_port_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-server-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_bulk_update(client):
    """Test case for dcim_console_server_port_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-server-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_create(client):
    """Test case for dcim_console_server_port_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/console-server-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_delete(client):
    """Test case for dcim_console_server_port_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-server-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_list(client):
    """Test case for dcim_console_server_port_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-server-port-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_partial_update(client):
    """Test case for dcim_console_server_port_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-server-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_read(client):
    """Test case for dcim_console_server_port_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-server-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_port_templates_update(client):
    """Test case for dcim_console_server_port_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","type":"de-9","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-server-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_bulk_delete(client):
    """Test case for dcim_console_server_ports_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-server-ports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_bulk_partial_update(client):
    """Test case for dcim_console_server_ports_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-server-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_bulk_update(client):
    """Test case for dcim_console_server_ports_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-server-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_create(client):
    """Test case for dcim_console_server_ports_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/console-server-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_delete(client):
    """Test case for dcim_console_server_ports_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/console-server-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_list(client):
    """Test case for dcim_console_server_ports_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('type', 'type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-server-ports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_partial_update(client):
    """Test case for dcim_console_server_ports_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/console-server-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_read(client):
    """Test case for dcim_console_server_ports_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-server-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_trace(client):
    """Test case for dcim_console_server_ports_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-server-ports/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_server_ports_update(client):
    """Test case for dcim_console_server_ports_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"de-9","link_peers_type":"link_peers_type","speed":5,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/console-server-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_bulk_delete(client):
    """Test case for dcim_device_bay_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-bay-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_bulk_partial_update(client):
    """Test case for dcim_device_bay_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_bulk_update(client):
    """Test case for dcim_device_bay_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_create(client):
    """Test case for dcim_device_bay_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/device-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_delete(client):
    """Test case for dcim_device_bay_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-bay-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_list(client):
    """Test case for dcim_device_bay_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-bay-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_partial_update(client):
    """Test case for dcim_device_bay_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-bay-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_read(client):
    """Test case for dcim_device_bay_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-bay-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bay_templates_update(client):
    """Test case for dcim_device_bay_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-bay-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_bulk_delete(client):
    """Test case for dcim_device_bays_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-bays/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_bulk_partial_update(client):
    """Test case for dcim_device_bays_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","installed_device":1,"name":"name","description":"description","id":6,"label":"label","device":0,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_bulk_update(client):
    """Test case for dcim_device_bays_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","installed_device":1,"name":"name","description":"description","id":6,"label":"label","device":0,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_create(client):
    """Test case for dcim_device_bays_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","installed_device":1,"name":"name","description":"description","id":6,"label":"label","device":0,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/device-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_delete(client):
    """Test case for dcim_device_bays_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-bays/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_list(client):
    """Test case for dcim_device_bays_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-bays/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_partial_update(client):
    """Test case for dcim_device_bays_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","installed_device":1,"name":"name","description":"description","id":6,"label":"label","device":0,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-bays/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_read(client):
    """Test case for dcim_device_bays_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-bays/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_bays_update(client):
    """Test case for dcim_device_bays_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","installed_device":1,"name":"name","description":"description","id":6,"label":"label","device":0,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-bays/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_bulk_delete(client):
    """Test case for dcim_device_roles_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-roles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_bulk_partial_update(client):
    """Test case for dcim_device_roles_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vm_role":True,"name":"name","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_bulk_update(client):
    """Test case for dcim_device_roles_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vm_role":True,"name":"name","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_create(client):
    """Test case for dcim_device_roles_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vm_role":True,"name":"name","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/device-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_delete(client):
    """Test case for dcim_device_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_list(client):
    """Test case for dcim_device_roles_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
                    ('vm_role', 'vm_role_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_partial_update(client):
    """Test case for dcim_device_roles_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vm_role":True,"name":"name","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_read(client):
    """Test case for dcim_device_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_roles_update(client):
    """Test case for dcim_device_roles_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vm_role":True,"name":"name","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_bulk_delete(client):
    """Test case for dcim_device_types_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_bulk_partial_update(client):
    """Test case for dcim_device_types_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":0.5962133916683182,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","is_full_depth":True,"description":"description","weight":5.637376656633329,"url":"https://openapi-generator.tech","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"subdevice_role":"parent","weight_unit":"kg","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_bulk_update(client):
    """Test case for dcim_device_types_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":0.5962133916683182,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","is_full_depth":True,"description":"description","weight":5.637376656633329,"url":"https://openapi-generator.tech","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"subdevice_role":"parent","weight_unit":"kg","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_create(client):
    """Test case for dcim_device_types_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":0.5962133916683182,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","is_full_depth":True,"description":"description","weight":5.637376656633329,"url":"https://openapi-generator.tech","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"subdevice_role":"parent","weight_unit":"kg","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/device-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_delete(client):
    """Test case for dcim_device_types_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/device-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_list(client):
    """Test case for dcim_device_types_list

    
    """
    params = [('id', 'id_example'),
                    ('model', 'model_example'),
                    ('slug', 'slug_example'),
                    ('part_number', 'part_number_example'),
                    ('u_height', 'u_height_example'),
                    ('is_full_depth', 'is_full_depth_example'),
                    ('subdevice_role', 'subdevice_role_example'),
                    ('airflow', 'airflow_example'),
                    ('weight', 'weight_example'),
                    ('weight_unit', 'weight_unit_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('has_front_image', 'has_front_image_example'),
                    ('has_rear_image', 'has_rear_image_example'),
                    ('console_ports', 'console_ports_example'),
                    ('console_server_ports', 'console_server_ports_example'),
                    ('power_ports', 'power_ports_example'),
                    ('power_outlets', 'power_outlets_example'),
                    ('interfaces', 'interfaces_example'),
                    ('pass_through_ports', 'pass_through_ports_example'),
                    ('module_bays', 'module_bays_example'),
                    ('device_bays', 'device_bays_example'),
                    ('inventory_items', 'inventory_items_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('model__n', 'model__n_example'),
                    ('model__ic', 'model__ic_example'),
                    ('model__nic', 'model__nic_example'),
                    ('model__iew', 'model__iew_example'),
                    ('model__niew', 'model__niew_example'),
                    ('model__isw', 'model__isw_example'),
                    ('model__nisw', 'model__nisw_example'),
                    ('model__ie', 'model__ie_example'),
                    ('model__nie', 'model__nie_example'),
                    ('model__empty', 'model__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('part_number__n', 'part_number__n_example'),
                    ('part_number__ic', 'part_number__ic_example'),
                    ('part_number__nic', 'part_number__nic_example'),
                    ('part_number__iew', 'part_number__iew_example'),
                    ('part_number__niew', 'part_number__niew_example'),
                    ('part_number__isw', 'part_number__isw_example'),
                    ('part_number__nisw', 'part_number__nisw_example'),
                    ('part_number__ie', 'part_number__ie_example'),
                    ('part_number__nie', 'part_number__nie_example'),
                    ('part_number__empty', 'part_number__empty_example'),
                    ('u_height__n', 'u_height__n_example'),
                    ('u_height__lte', 'u_height__lte_example'),
                    ('u_height__lt', 'u_height__lt_example'),
                    ('u_height__gte', 'u_height__gte_example'),
                    ('u_height__gt', 'u_height__gt_example'),
                    ('subdevice_role__n', 'subdevice_role__n_example'),
                    ('airflow__n', 'airflow__n_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('weight_unit__n', 'weight_unit__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_partial_update(client):
    """Test case for dcim_device_types_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":0.5962133916683182,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","is_full_depth":True,"description":"description","weight":5.637376656633329,"url":"https://openapi-generator.tech","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"subdevice_role":"parent","weight_unit":"kg","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/device-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_read(client):
    """Test case for dcim_device_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/device-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_device_types_update(client):
    """Test case for dcim_device_types_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":0.5962133916683182,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","is_full_depth":True,"description":"description","weight":5.637376656633329,"url":"https://openapi-generator.tech","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"subdevice_role":"parent","weight_unit":"kg","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/device-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_bulk_delete(client):
    """Test case for dcim_devices_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/devices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_bulk_partial_update(client):
    """Test case for dcim_devices_bulk_partial_update

    
    """
    body = {"cluster":0,"config_context":"{}","primary_ip":"primary_ip","vc_priority":26,"description":"description","device_type":1,"platform":2,"id":5,"tenant":7,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"face":"front","site":4,"vc_position":31,"local_context_data":"{}","parent_device":{"display":"display","name":"name","id":1,"url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","location":5,"virtual_chassis":1,"position":1.206140124150311,"primary_ip6":3,"primary_ip4":9,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/devices/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_bulk_update(client):
    """Test case for dcim_devices_bulk_update

    
    """
    body = {"cluster":0,"config_context":"{}","primary_ip":"primary_ip","vc_priority":26,"description":"description","device_type":1,"platform":2,"id":5,"tenant":7,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"face":"front","site":4,"vc_position":31,"local_context_data":"{}","parent_device":{"display":"display","name":"name","id":1,"url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","location":5,"virtual_chassis":1,"position":1.206140124150311,"primary_ip6":3,"primary_ip4":9,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/devices/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_create(client):
    """Test case for dcim_devices_create

    
    """
    body = {"cluster":0,"config_context":"{}","primary_ip":"primary_ip","vc_priority":26,"description":"description","device_type":1,"platform":2,"id":5,"tenant":7,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"face":"front","site":4,"vc_position":31,"local_context_data":"{}","parent_device":{"display":"display","name":"name","id":1,"url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","location":5,"virtual_chassis":1,"position":1.206140124150311,"primary_ip6":3,"primary_ip4":9,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/devices/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_delete(client):
    """Test case for dcim_devices_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/devices/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_list(client):
    """Test case for dcim_devices_list

    
    """
    params = [('id', 'id_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('face', 'face_example'),
                    ('position', 'position_example'),
                    ('airflow', 'airflow_example'),
                    ('vc_position', 'vc_position_example'),
                    ('vc_priority', 'vc_priority_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('local_context_data', 'local_context_data_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('device_type', 'device_type_example'),
                    ('device_type_id', 'device_type_id_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('parent_device_id', 'parent_device_id_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('rack_id', 'rack_id_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('model', 'model_example'),
                    ('name', 'name_example'),
                    ('status', 'status_example'),
                    ('is_full_depth', 'is_full_depth_example'),
                    ('mac_address', 'mac_address_example'),
                    ('serial', 'serial_example'),
                    ('has_primary_ip', 'has_primary_ip_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis_member', 'virtual_chassis_member_example'),
                    ('console_ports', 'console_ports_example'),
                    ('console_server_ports', 'console_server_ports_example'),
                    ('power_ports', 'power_ports_example'),
                    ('power_outlets', 'power_outlets_example'),
                    ('interfaces', 'interfaces_example'),
                    ('pass_through_ports', 'pass_through_ports_example'),
                    ('module_bays', 'module_bays_example'),
                    ('device_bays', 'device_bays_example'),
                    ('primary_ip4_id', 'primary_ip4_id_example'),
                    ('primary_ip6_id', 'primary_ip6_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('asset_tag__empty', 'asset_tag__empty_example'),
                    ('face__n', 'face__n_example'),
                    ('position__n', 'position__n_example'),
                    ('position__lte', 'position__lte_example'),
                    ('position__lt', 'position__lt_example'),
                    ('position__gte', 'position__gte_example'),
                    ('position__gt', 'position__gt_example'),
                    ('airflow__n', 'airflow__n_example'),
                    ('vc_position__n', 'vc_position__n_example'),
                    ('vc_position__lte', 'vc_position__lte_example'),
                    ('vc_position__lt', 'vc_position__lt_example'),
                    ('vc_position__gte', 'vc_position__gte_example'),
                    ('vc_position__gt', 'vc_position__gt_example'),
                    ('vc_priority__n', 'vc_priority__n_example'),
                    ('vc_priority__lte', 'vc_priority__lte_example'),
                    ('vc_priority__lt', 'vc_priority__lt_example'),
                    ('vc_priority__gte', 'vc_priority__gte_example'),
                    ('vc_priority__gt', 'vc_priority__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('device_type__n', 'device_type__n_example'),
                    ('device_type_id__n', 'device_type_id__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('parent_device_id__n', 'parent_device_id__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('model__n', 'model__n_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('status__n', 'status__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('serial__n', 'serial__n_example'),
                    ('serial__ic', 'serial__ic_example'),
                    ('serial__nic', 'serial__nic_example'),
                    ('serial__iew', 'serial__iew_example'),
                    ('serial__niew', 'serial__niew_example'),
                    ('serial__isw', 'serial__isw_example'),
                    ('serial__nisw', 'serial__nisw_example'),
                    ('serial__ie', 'serial__ie_example'),
                    ('serial__nie', 'serial__nie_example'),
                    ('serial__empty', 'serial__empty_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('primary_ip4_id__n', 'primary_ip4_id__n_example'),
                    ('primary_ip6_id__n', 'primary_ip6_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/devices/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_napalm(client):
    """Test case for dcim_devices_napalm

    
    """
    params = [('method', 'method_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/devices/{id}/napalm'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_partial_update(client):
    """Test case for dcim_devices_partial_update

    
    """
    body = {"cluster":0,"config_context":"{}","primary_ip":"primary_ip","vc_priority":26,"description":"description","device_type":1,"platform":2,"id":5,"tenant":7,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"face":"front","site":4,"vc_position":31,"local_context_data":"{}","parent_device":{"display":"display","name":"name","id":1,"url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","location":5,"virtual_chassis":1,"position":1.206140124150311,"primary_ip6":3,"primary_ip4":9,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/devices/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_read(client):
    """Test case for dcim_devices_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/devices/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_update(client):
    """Test case for dcim_devices_update

    
    """
    body = {"cluster":0,"config_context":"{}","primary_ip":"primary_ip","vc_priority":26,"description":"description","device_type":1,"platform":2,"id":5,"tenant":7,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","airflow":"front-to-rear","display":"display","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"face":"front","site":4,"vc_position":31,"local_context_data":"{}","parent_device":{"display":"display","name":"name","id":1,"url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","location":5,"virtual_chassis":1,"position":1.206140124150311,"primary_ip6":3,"primary_ip4":9,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/devices/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_bulk_delete(client):
    """Test case for dcim_front_port_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/front-port-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_bulk_partial_update(client):
    """Test case for dcim_front_port_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","rear_port":5,"id":6,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/front-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_bulk_update(client):
    """Test case for dcim_front_port_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","rear_port":5,"id":6,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/front-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_create(client):
    """Test case for dcim_front_port_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","rear_port":5,"id":6,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/front-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_delete(client):
    """Test case for dcim_front_port_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/front-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_list(client):
    """Test case for dcim_front_port_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('color', 'color_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-port-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_partial_update(client):
    """Test case for dcim_front_port_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","rear_port":5,"id":6,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/front-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_read(client):
    """Test case for dcim_front_port_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_port_templates_update(client):
    """Test case for dcim_front_port_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","rear_port":5,"id":6,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/front-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_bulk_delete(client):
    """Test case for dcim_front_ports_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/front-ports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_bulk_partial_update(client):
    """Test case for dcim_front_ports_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","rear_port":5,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/front-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_bulk_update(client):
    """Test case for dcim_front_ports_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","rear_port":5,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/front-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_create(client):
    """Test case for dcim_front_ports_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","rear_port":5,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/front-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_delete(client):
    """Test case for dcim_front_ports_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/front-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_list(client):
    """Test case for dcim_front_ports_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('type', 'type_example'),
                    ('color', 'color_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-ports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_partial_update(client):
    """Test case for dcim_front_ports_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","rear_port":5,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/front-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_paths(client):
    """Test case for dcim_front_ports_paths

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-ports/{id}/paths'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_read(client):
    """Test case for dcim_front_ports_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_update(client):
    """Test case for dcim_front_ports_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","rear_port":5,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":577}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/front-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_bulk_delete(client):
    """Test case for dcim_interface_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/interface-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_bulk_partial_update(client):
    """Test case for dcim_interface_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","poe_mode":"pd","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"virtual","mgmt_only":True,"url":"https://openapi-generator.tech","poe_type":"type1-ieee802.3af","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/interface-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_bulk_update(client):
    """Test case for dcim_interface_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","poe_mode":"pd","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"virtual","mgmt_only":True,"url":"https://openapi-generator.tech","poe_type":"type1-ieee802.3af","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/interface-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_create(client):
    """Test case for dcim_interface_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","poe_mode":"pd","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"virtual","mgmt_only":True,"url":"https://openapi-generator.tech","poe_type":"type1-ieee802.3af","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/interface-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_delete(client):
    """Test case for dcim_interface_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/interface-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_list(client):
    """Test case for dcim_interface_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('mgmt_only', 'mgmt_only_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('poe_mode', 'poe_mode_example'),
                    ('poe_type', 'poe_type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('poe_mode__n', 'poe_mode__n_example'),
                    ('poe_type__n', 'poe_type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interface-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_partial_update(client):
    """Test case for dcim_interface_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","poe_mode":"pd","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"virtual","mgmt_only":True,"url":"https://openapi-generator.tech","poe_type":"type1-ieee802.3af","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/interface-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_read(client):
    """Test case for dcim_interface_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interface-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_update(client):
    """Test case for dcim_interface_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","poe_mode":"pd","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"virtual","mgmt_only":True,"url":"https://openapi-generator.tech","poe_type":"type1-ieee802.3af","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/interface-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_bulk_delete(client):
    """Test case for dcim_interfaces_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/interfaces/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_bulk_partial_update(client):
    """Test case for dcim_interfaces_bulk_partial_update

    
    """
    body = {"parent":3,"l2vpn_termination":"l2vpn_termination","connected_endpoints":["connected_endpoints","connected_endpoints"],"duplex":"half","type":"virtual","wwn":"wwn","mode":"access","tagged_vlans":[1,1],"lag":2,"mark_connected":True,"wireless_lans":[1,1],"wireless_link":4,"id":5,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"last_updated":"2000-01-23T04:56:07.000+00:00","untagged_vlan":1,"rf_role":"ap","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","module":7,"vdcs":[6,6],"connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","vrf":7,"count_fhrp_groups":6,"mtu":60958,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"poe_type":"type1-ieee802.3af","link_peers":["link_peers","link_peers"],"name":"name","rf_channel_frequency":2.027123023002322,"bridge":0,"device":5,"description":"description","rf_channel_width":4.145608029883936,"enabled":True,"mgmt_only":True,"speed":1586191969,"mac_address":"mac_address","_occupied":True,"connected_endpoints_reachable":True,"poe_mode":"pd","tx_power":13,"display":"display","label":"label","rf_channel":"2.4g-1-2412-22","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","count_ipaddresses":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_bulk_update(client):
    """Test case for dcim_interfaces_bulk_update

    
    """
    body = {"parent":3,"l2vpn_termination":"l2vpn_termination","connected_endpoints":["connected_endpoints","connected_endpoints"],"duplex":"half","type":"virtual","wwn":"wwn","mode":"access","tagged_vlans":[1,1],"lag":2,"mark_connected":True,"wireless_lans":[1,1],"wireless_link":4,"id":5,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"last_updated":"2000-01-23T04:56:07.000+00:00","untagged_vlan":1,"rf_role":"ap","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","module":7,"vdcs":[6,6],"connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","vrf":7,"count_fhrp_groups":6,"mtu":60958,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"poe_type":"type1-ieee802.3af","link_peers":["link_peers","link_peers"],"name":"name","rf_channel_frequency":2.027123023002322,"bridge":0,"device":5,"description":"description","rf_channel_width":4.145608029883936,"enabled":True,"mgmt_only":True,"speed":1586191969,"mac_address":"mac_address","_occupied":True,"connected_endpoints_reachable":True,"poe_mode":"pd","tx_power":13,"display":"display","label":"label","rf_channel":"2.4g-1-2412-22","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","count_ipaddresses":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_create(client):
    """Test case for dcim_interfaces_create

    
    """
    body = {"parent":3,"l2vpn_termination":"l2vpn_termination","connected_endpoints":["connected_endpoints","connected_endpoints"],"duplex":"half","type":"virtual","wwn":"wwn","mode":"access","tagged_vlans":[1,1],"lag":2,"mark_connected":True,"wireless_lans":[1,1],"wireless_link":4,"id":5,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"last_updated":"2000-01-23T04:56:07.000+00:00","untagged_vlan":1,"rf_role":"ap","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","module":7,"vdcs":[6,6],"connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","vrf":7,"count_fhrp_groups":6,"mtu":60958,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"poe_type":"type1-ieee802.3af","link_peers":["link_peers","link_peers"],"name":"name","rf_channel_frequency":2.027123023002322,"bridge":0,"device":5,"description":"description","rf_channel_width":4.145608029883936,"enabled":True,"mgmt_only":True,"speed":1586191969,"mac_address":"mac_address","_occupied":True,"connected_endpoints_reachable":True,"poe_mode":"pd","tx_power":13,"display":"display","label":"label","rf_channel":"2.4g-1-2412-22","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","count_ipaddresses":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_delete(client):
    """Test case for dcim_interfaces_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_list(client):
    """Test case for dcim_interfaces_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('type', 'type_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 'mtu_example'),
                    ('mgmt_only', 'mgmt_only_example'),
                    ('poe_mode', 'poe_mode_example'),
                    ('poe_type', 'poe_type_example'),
                    ('mode', 'mode_example'),
                    ('rf_role', 'rf_role_example'),
                    ('rf_channel', 'rf_channel_example'),
                    ('rf_channel_frequency', 'rf_channel_frequency_example'),
                    ('rf_channel_width', 'rf_channel_width_example'),
                    ('tx_power', 'tx_power_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('kind', 'kind_example'),
                    ('parent_id', 'parent_id_example'),
                    ('bridge_id', 'bridge_id_example'),
                    ('lag_id', 'lag_id_example'),
                    ('speed', 'speed_example'),
                    ('duplex', 'duplex_example'),
                    ('mac_address', 'mac_address_example'),
                    ('wwn', 'wwn_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan', 'vlan_example'),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('vdc_id', 'vdc_id_example'),
                    ('vdc_identifier', 'vdc_identifier_example'),
                    ('vdc', 'vdc_example'),
                    ('l2vpn_id', 'l2vpn_id_example'),
                    ('l2vpn', 'l2vpn_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('mtu__n', 'mtu__n_example'),
                    ('mtu__lte', 'mtu__lte_example'),
                    ('mtu__lt', 'mtu__lt_example'),
                    ('mtu__gte', 'mtu__gte_example'),
                    ('mtu__gt', 'mtu__gt_example'),
                    ('poe_mode__n', 'poe_mode__n_example'),
                    ('poe_type__n', 'poe_type__n_example'),
                    ('mode__n', 'mode__n_example'),
                    ('rf_role__n', 'rf_role__n_example'),
                    ('rf_channel__n', 'rf_channel__n_example'),
                    ('rf_channel_frequency__n', 'rf_channel_frequency__n_example'),
                    ('rf_channel_frequency__lte', 'rf_channel_frequency__lte_example'),
                    ('rf_channel_frequency__lt', 'rf_channel_frequency__lt_example'),
                    ('rf_channel_frequency__gte', 'rf_channel_frequency__gte_example'),
                    ('rf_channel_frequency__gt', 'rf_channel_frequency__gt_example'),
                    ('rf_channel_width__n', 'rf_channel_width__n_example'),
                    ('rf_channel_width__lte', 'rf_channel_width__lte_example'),
                    ('rf_channel_width__lt', 'rf_channel_width__lt_example'),
                    ('rf_channel_width__gte', 'rf_channel_width__gte_example'),
                    ('rf_channel_width__gt', 'rf_channel_width__gt_example'),
                    ('tx_power__n', 'tx_power__n_example'),
                    ('tx_power__lte', 'tx_power__lte_example'),
                    ('tx_power__lt', 'tx_power__lt_example'),
                    ('tx_power__gte', 'tx_power__gte_example'),
                    ('tx_power__gt', 'tx_power__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('bridge_id__n', 'bridge_id__n_example'),
                    ('lag_id__n', 'lag_id__n_example'),
                    ('speed__n', 'speed__n_example'),
                    ('speed__lte', 'speed__lte_example'),
                    ('speed__lt', 'speed__lt_example'),
                    ('speed__gte', 'speed__gte_example'),
                    ('speed__gt', 'speed__gt_example'),
                    ('duplex__n', 'duplex__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('wwn__n', 'wwn__n_example'),
                    ('wwn__ic', 'wwn__ic_example'),
                    ('wwn__nic', 'wwn__nic_example'),
                    ('wwn__iew', 'wwn__iew_example'),
                    ('wwn__niew', 'wwn__niew_example'),
                    ('wwn__isw', 'wwn__isw_example'),
                    ('wwn__nisw', 'wwn__nisw_example'),
                    ('wwn__ie', 'wwn__ie_example'),
                    ('wwn__nie', 'wwn__nie_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('vdc_id__n', 'vdc_id__n_example'),
                    ('vdc_identifier__n', 'vdc_identifier__n_example'),
                    ('vdc__n', 'vdc__n_example'),
                    ('l2vpn_id__n', 'l2vpn_id__n_example'),
                    ('l2vpn__n', 'l2vpn__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interfaces/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_partial_update(client):
    """Test case for dcim_interfaces_partial_update

    
    """
    body = {"parent":3,"l2vpn_termination":"l2vpn_termination","connected_endpoints":["connected_endpoints","connected_endpoints"],"duplex":"half","type":"virtual","wwn":"wwn","mode":"access","tagged_vlans":[1,1],"lag":2,"mark_connected":True,"wireless_lans":[1,1],"wireless_link":4,"id":5,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"last_updated":"2000-01-23T04:56:07.000+00:00","untagged_vlan":1,"rf_role":"ap","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","module":7,"vdcs":[6,6],"connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","vrf":7,"count_fhrp_groups":6,"mtu":60958,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"poe_type":"type1-ieee802.3af","link_peers":["link_peers","link_peers"],"name":"name","rf_channel_frequency":2.027123023002322,"bridge":0,"device":5,"description":"description","rf_channel_width":4.145608029883936,"enabled":True,"mgmt_only":True,"speed":1586191969,"mac_address":"mac_address","_occupied":True,"connected_endpoints_reachable":True,"poe_mode":"pd","tx_power":13,"display":"display","label":"label","rf_channel":"2.4g-1-2412-22","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","count_ipaddresses":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_read(client):
    """Test case for dcim_interfaces_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_trace(client):
    """Test case for dcim_interfaces_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interfaces/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_update(client):
    """Test case for dcim_interfaces_update

    
    """
    body = {"parent":3,"l2vpn_termination":"l2vpn_termination","connected_endpoints":["connected_endpoints","connected_endpoints"],"duplex":"half","type":"virtual","wwn":"wwn","mode":"access","tagged_vlans":[1,1],"lag":2,"mark_connected":True,"wireless_lans":[1,1],"wireless_link":4,"id":5,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"last_updated":"2000-01-23T04:56:07.000+00:00","untagged_vlan":1,"rf_role":"ap","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","module":7,"vdcs":[6,6],"connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","vrf":7,"count_fhrp_groups":6,"mtu":60958,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"poe_type":"type1-ieee802.3af","link_peers":["link_peers","link_peers"],"name":"name","rf_channel_frequency":2.027123023002322,"bridge":0,"device":5,"description":"description","rf_channel_width":4.145608029883936,"enabled":True,"mgmt_only":True,"speed":1586191969,"mac_address":"mac_address","_occupied":True,"connected_endpoints_reachable":True,"poe_mode":"pd","tx_power":13,"display":"display","label":"label","rf_channel":"2.4g-1-2412-22","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","count_ipaddresses":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_bulk_delete(client):
    """Test case for dcim_inventory_item_roles_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-item-roles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_bulk_partial_update(client):
    """Test case for dcim_inventory_item_roles_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":1,"name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-item-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_bulk_update(client):
    """Test case for dcim_inventory_item_roles_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":1,"name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-item-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_create(client):
    """Test case for dcim_inventory_item_roles_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":1,"name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/inventory-item-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_delete(client):
    """Test case for dcim_inventory_item_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-item-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_list(client):
    """Test case for dcim_inventory_item_roles_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-item-roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_partial_update(client):
    """Test case for dcim_inventory_item_roles_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":1,"name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-item-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_read(client):
    """Test case for dcim_inventory_item_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-item-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_roles_update(client):
    """Test case for dcim_inventory_item_roles_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":1,"name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-item-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_bulk_delete(client):
    """Test case for dcim_inventory_item_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-item-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_bulk_partial_update(client):
    """Test case for dcim_inventory_item_templates_bulk_partial_update

    
    """
    body = {"parent":2,"component_id":2147483647,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","display":"display","_depth":0,"description":"description","device_type":1,"label":"label","url":"https://openapi-generator.tech","manufacturer":5,"component_type":"component_type","component":"{}","name":"name","id":5,"part_id":"part_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-item-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_bulk_update(client):
    """Test case for dcim_inventory_item_templates_bulk_update

    
    """
    body = {"parent":2,"component_id":2147483647,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","display":"display","_depth":0,"description":"description","device_type":1,"label":"label","url":"https://openapi-generator.tech","manufacturer":5,"component_type":"component_type","component":"{}","name":"name","id":5,"part_id":"part_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-item-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_create(client):
    """Test case for dcim_inventory_item_templates_create

    
    """
    body = {"parent":2,"component_id":2147483647,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","display":"display","_depth":0,"description":"description","device_type":1,"label":"label","url":"https://openapi-generator.tech","manufacturer":5,"component_type":"component_type","component":"{}","name":"name","id":5,"part_id":"part_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/inventory-item-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_delete(client):
    """Test case for dcim_inventory_item_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-item-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_list(client):
    """Test case for dcim_inventory_item_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('part_id', 'part_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('parent_id', 'parent_id_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('component_type', 'component_type_example'),
                    ('component_id', 'component_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('part_id__n', 'part_id__n_example'),
                    ('part_id__ic', 'part_id__ic_example'),
                    ('part_id__nic', 'part_id__nic_example'),
                    ('part_id__iew', 'part_id__iew_example'),
                    ('part_id__niew', 'part_id__niew_example'),
                    ('part_id__isw', 'part_id__isw_example'),
                    ('part_id__nisw', 'part_id__nisw_example'),
                    ('part_id__ie', 'part_id__ie_example'),
                    ('part_id__nie', 'part_id__nie_example'),
                    ('part_id__empty', 'part_id__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('component_type__n', 'component_type__n_example'),
                    ('component_id__n', 'component_id__n_example'),
                    ('component_id__lte', 'component_id__lte_example'),
                    ('component_id__lt', 'component_id__lt_example'),
                    ('component_id__gte', 'component_id__gte_example'),
                    ('component_id__gt', 'component_id__gt_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-item-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_partial_update(client):
    """Test case for dcim_inventory_item_templates_partial_update

    
    """
    body = {"parent":2,"component_id":2147483647,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","display":"display","_depth":0,"description":"description","device_type":1,"label":"label","url":"https://openapi-generator.tech","manufacturer":5,"component_type":"component_type","component":"{}","name":"name","id":5,"part_id":"part_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-item-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_read(client):
    """Test case for dcim_inventory_item_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-item-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_item_templates_update(client):
    """Test case for dcim_inventory_item_templates_update

    
    """
    body = {"parent":2,"component_id":2147483647,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","display":"display","_depth":0,"description":"description","device_type":1,"label":"label","url":"https://openapi-generator.tech","manufacturer":5,"component_type":"component_type","component":"{}","name":"name","id":5,"part_id":"part_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-item-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_bulk_delete(client):
    """Test case for dcim_inventory_items_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-items/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_bulk_partial_update(client):
    """Test case for dcim_inventory_items_bulk_partial_update

    
    """
    body = {"asset_tag":"asset_tag","parent":2,"component_id":2147483647,"discovered":True,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","label":"label","url":"https://openapi-generator.tech","manufacturer":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"component_type":"component_type","component":"{}","serial":"serial","name":"name","id":5,"part_id":"part_id","device":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-items/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_bulk_update(client):
    """Test case for dcim_inventory_items_bulk_update

    
    """
    body = {"asset_tag":"asset_tag","parent":2,"component_id":2147483647,"discovered":True,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","label":"label","url":"https://openapi-generator.tech","manufacturer":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"component_type":"component_type","component":"{}","serial":"serial","name":"name","id":5,"part_id":"part_id","device":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-items/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_create(client):
    """Test case for dcim_inventory_items_create

    
    """
    body = {"asset_tag":"asset_tag","parent":2,"component_id":2147483647,"discovered":True,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","label":"label","url":"https://openapi-generator.tech","manufacturer":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"component_type":"component_type","component":"{}","serial":"serial","name":"name","id":5,"part_id":"part_id","device":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/inventory-items/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_delete(client):
    """Test case for dcim_inventory_items_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/inventory-items/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_list(client):
    """Test case for dcim_inventory_items_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('part_id', 'part_id_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('discovered', 'discovered_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('parent_id', 'parent_id_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('component_type', 'component_type_example'),
                    ('component_id', 'component_id_example'),
                    ('serial', 'serial_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('part_id__n', 'part_id__n_example'),
                    ('part_id__ic', 'part_id__ic_example'),
                    ('part_id__nic', 'part_id__nic_example'),
                    ('part_id__iew', 'part_id__iew_example'),
                    ('part_id__niew', 'part_id__niew_example'),
                    ('part_id__isw', 'part_id__isw_example'),
                    ('part_id__nisw', 'part_id__nisw_example'),
                    ('part_id__ie', 'part_id__ie_example'),
                    ('part_id__nie', 'part_id__nie_example'),
                    ('part_id__empty', 'part_id__empty_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('asset_tag__empty', 'asset_tag__empty_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('component_type__n', 'component_type__n_example'),
                    ('component_id__n', 'component_id__n_example'),
                    ('component_id__lte', 'component_id__lte_example'),
                    ('component_id__lt', 'component_id__lt_example'),
                    ('component_id__gte', 'component_id__gte_example'),
                    ('component_id__gt', 'component_id__gt_example'),
                    ('serial__n', 'serial__n_example'),
                    ('serial__ic', 'serial__ic_example'),
                    ('serial__nic', 'serial__nic_example'),
                    ('serial__iew', 'serial__iew_example'),
                    ('serial__niew', 'serial__niew_example'),
                    ('serial__isw', 'serial__isw_example'),
                    ('serial__nisw', 'serial__nisw_example'),
                    ('serial__ie', 'serial__ie_example'),
                    ('serial__nie', 'serial__nie_example'),
                    ('serial__empty', 'serial__empty_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-items/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_partial_update(client):
    """Test case for dcim_inventory_items_partial_update

    
    """
    body = {"asset_tag":"asset_tag","parent":2,"component_id":2147483647,"discovered":True,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","label":"label","url":"https://openapi-generator.tech","manufacturer":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"component_type":"component_type","component":"{}","serial":"serial","name":"name","id":5,"part_id":"part_id","device":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/inventory-items/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_read(client):
    """Test case for dcim_inventory_items_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/inventory-items/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_inventory_items_update(client):
    """Test case for dcim_inventory_items_update

    
    """
    body = {"asset_tag":"asset_tag","parent":2,"component_id":2147483647,"discovered":True,"last_updated":"2000-01-23T04:56:07.000+00:00","role":7,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","label":"label","url":"https://openapi-generator.tech","manufacturer":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"component_type":"component_type","component":"{}","serial":"serial","name":"name","id":5,"part_id":"part_id","device":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/inventory-items/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_bulk_delete(client):
    """Test case for dcim_locations_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/locations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_bulk_partial_update(client):
    """Test case for dcim_locations_bulk_partial_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rack_count":5,"site":2,"name":"name","id":1,"device_count":6,"slug":"slug","tenant":7,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/locations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_bulk_update(client):
    """Test case for dcim_locations_bulk_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rack_count":5,"site":2,"name":"name","id":1,"device_count":6,"slug":"slug","tenant":7,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/locations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_create(client):
    """Test case for dcim_locations_create

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rack_count":5,"site":2,"name":"name","id":1,"device_count":6,"slug":"slug","tenant":7,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/locations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_delete(client):
    """Test case for dcim_locations_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/locations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_list(client):
    """Test case for dcim_locations_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('status', 'status_example'),
                    ('description', 'description_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('status__n', 'status__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/locations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_partial_update(client):
    """Test case for dcim_locations_partial_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rack_count":5,"site":2,"name":"name","id":1,"device_count":6,"slug":"slug","tenant":7,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/locations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_read(client):
    """Test case for dcim_locations_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/locations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_locations_update(client):
    """Test case for dcim_locations_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rack_count":5,"site":2,"name":"name","id":1,"device_count":6,"slug":"slug","tenant":7,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/locations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_bulk_delete(client):
    """Test case for dcim_manufacturers_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/manufacturers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_bulk_partial_update(client):
    """Test case for dcim_manufacturers_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":5,"description":"description","devicetype_count":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"platform_count":5,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/manufacturers/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_bulk_update(client):
    """Test case for dcim_manufacturers_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":5,"description":"description","devicetype_count":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"platform_count":5,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/manufacturers/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_create(client):
    """Test case for dcim_manufacturers_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":5,"description":"description","devicetype_count":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"platform_count":5,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/manufacturers/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_delete(client):
    """Test case for dcim_manufacturers_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/manufacturers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_list(client):
    """Test case for dcim_manufacturers_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/manufacturers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_partial_update(client):
    """Test case for dcim_manufacturers_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":5,"description":"description","devicetype_count":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"platform_count":5,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/manufacturers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_read(client):
    """Test case for dcim_manufacturers_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/manufacturers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_manufacturers_update(client):
    """Test case for dcim_manufacturers_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","inventoryitem_count":5,"description":"description","devicetype_count":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"platform_count":5,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/manufacturers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_bulk_delete(client):
    """Test case for dcim_module_bay_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-bay-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_bulk_partial_update(client):
    """Test case for dcim_module_bay_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","position":"position","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_bulk_update(client):
    """Test case for dcim_module_bay_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","position":"position","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_create(client):
    """Test case for dcim_module_bay_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","position":"position","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/module-bay-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_delete(client):
    """Test case for dcim_module_bay_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-bay-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_list(client):
    """Test case for dcim_module_bay_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-bay-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_partial_update(client):
    """Test case for dcim_module_bay_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","position":"position","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-bay-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_read(client):
    """Test case for dcim_module_bay_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-bay-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bay_templates_update(client):
    """Test case for dcim_module_bay_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","description":"description","device_type":0,"id":6,"label":"label","position":"position","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-bay-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_bulk_delete(client):
    """Test case for dcim_module_bays_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-bays/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_bulk_partial_update(client):
    """Test case for dcim_module_bays_bulk_partial_update

    
    """
    body = {"installed_module":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","label":"label","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"position":"position","device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_bulk_update(client):
    """Test case for dcim_module_bays_bulk_update

    
    """
    body = {"installed_module":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","label":"label","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"position":"position","device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_create(client):
    """Test case for dcim_module_bays_create

    
    """
    body = {"installed_module":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","label":"label","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"position":"position","device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/module-bays/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_delete(client):
    """Test case for dcim_module_bays_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-bays/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_list(client):
    """Test case for dcim_module_bays_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-bays/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_partial_update(client):
    """Test case for dcim_module_bays_partial_update

    
    """
    body = {"installed_module":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","label":"label","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"position":"position","device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-bays/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_read(client):
    """Test case for dcim_module_bays_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-bays/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_bays_update(client):
    """Test case for dcim_module_bays_update

    
    """
    body = {"installed_module":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","label":"label","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"position":"position","device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-bays/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_bulk_delete(client):
    """Test case for dcim_module_types_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_bulk_partial_update(client):
    """Test case for dcim_module_types_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":1.4658129805029452,"url":"https://openapi-generator.tech","manufacturer":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"weight_unit":"kg","part_number":"part_number","model":"model","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_bulk_update(client):
    """Test case for dcim_module_types_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":1.4658129805029452,"url":"https://openapi-generator.tech","manufacturer":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"weight_unit":"kg","part_number":"part_number","model":"model","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_create(client):
    """Test case for dcim_module_types_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":1.4658129805029452,"url":"https://openapi-generator.tech","manufacturer":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"weight_unit":"kg","part_number":"part_number","model":"model","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/module-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_delete(client):
    """Test case for dcim_module_types_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/module-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_list(client):
    """Test case for dcim_module_types_list

    
    """
    params = [('id', 'id_example'),
                    ('model', 'model_example'),
                    ('part_number', 'part_number_example'),
                    ('weight', 'weight_example'),
                    ('weight_unit', 'weight_unit_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('console_ports', 'console_ports_example'),
                    ('console_server_ports', 'console_server_ports_example'),
                    ('power_ports', 'power_ports_example'),
                    ('power_outlets', 'power_outlets_example'),
                    ('interfaces', 'interfaces_example'),
                    ('pass_through_ports', 'pass_through_ports_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('model__n', 'model__n_example'),
                    ('model__ic', 'model__ic_example'),
                    ('model__nic', 'model__nic_example'),
                    ('model__iew', 'model__iew_example'),
                    ('model__niew', 'model__niew_example'),
                    ('model__isw', 'model__isw_example'),
                    ('model__nisw', 'model__nisw_example'),
                    ('model__ie', 'model__ie_example'),
                    ('model__nie', 'model__nie_example'),
                    ('model__empty', 'model__empty_example'),
                    ('part_number__n', 'part_number__n_example'),
                    ('part_number__ic', 'part_number__ic_example'),
                    ('part_number__nic', 'part_number__nic_example'),
                    ('part_number__iew', 'part_number__iew_example'),
                    ('part_number__niew', 'part_number__niew_example'),
                    ('part_number__isw', 'part_number__isw_example'),
                    ('part_number__nisw', 'part_number__nisw_example'),
                    ('part_number__ie', 'part_number__ie_example'),
                    ('part_number__nie', 'part_number__nie_example'),
                    ('part_number__empty', 'part_number__empty_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('weight_unit__n', 'weight_unit__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_partial_update(client):
    """Test case for dcim_module_types_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":1.4658129805029452,"url":"https://openapi-generator.tech","manufacturer":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"weight_unit":"kg","part_number":"part_number","model":"model","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/module-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_read(client):
    """Test case for dcim_module_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/module-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_module_types_update(client):
    """Test case for dcim_module_types_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":1.4658129805029452,"url":"https://openapi-generator.tech","manufacturer":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"weight_unit":"kg","part_number":"part_number","model":"model","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/module-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_bulk_delete(client):
    """Test case for dcim_modules_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/modules/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_bulk_partial_update(client):
    """Test case for dcim_modules_bulk_partial_update

    
    """
    body = {"module_bay":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"serial":"serial","id":6,"device":0,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/modules/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_bulk_update(client):
    """Test case for dcim_modules_bulk_update

    
    """
    body = {"module_bay":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"serial":"serial","id":6,"device":0,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/modules/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_create(client):
    """Test case for dcim_modules_create

    
    """
    body = {"module_bay":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"serial":"serial","id":6,"device":0,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/modules/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_delete(client):
    """Test case for dcim_modules_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/modules/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_list(client):
    """Test case for dcim_modules_list

    
    """
    params = [('id', 'id_example'),
                    ('status', 'status_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('module_type_id', 'module_type_id_example'),
                    ('module_type', 'module_type_example'),
                    ('module_bay_id', 'module_bay_id_example'),
                    ('device_id', 'device_id_example'),
                    ('serial', 'serial_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('status__n', 'status__n_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('asset_tag__empty', 'asset_tag__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('module_type_id__n', 'module_type_id__n_example'),
                    ('module_type__n', 'module_type__n_example'),
                    ('module_bay_id__n', 'module_bay_id__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('serial__n', 'serial__n_example'),
                    ('serial__ic', 'serial__ic_example'),
                    ('serial__nic', 'serial__nic_example'),
                    ('serial__iew', 'serial__iew_example'),
                    ('serial__niew', 'serial__niew_example'),
                    ('serial__isw', 'serial__isw_example'),
                    ('serial__nisw', 'serial__nisw_example'),
                    ('serial__ie', 'serial__ie_example'),
                    ('serial__nie', 'serial__nie_example'),
                    ('serial__empty', 'serial__empty_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/modules/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_partial_update(client):
    """Test case for dcim_modules_partial_update

    
    """
    body = {"module_bay":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"serial":"serial","id":6,"device":0,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/modules/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_read(client):
    """Test case for dcim_modules_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/modules/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_modules_update(client):
    """Test case for dcim_modules_update

    
    """
    body = {"module_bay":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"serial":"serial","id":6,"device":0,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/modules/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_bulk_delete(client):
    """Test case for dcim_platforms_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/platforms/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_bulk_partial_update(client):
    """Test case for dcim_platforms_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","napalm_driver":"napalm_driver","description":"description","url":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"napalm_args":"{}","name":"name","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/platforms/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_bulk_update(client):
    """Test case for dcim_platforms_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","napalm_driver":"napalm_driver","description":"description","url":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"napalm_args":"{}","name":"name","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/platforms/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_create(client):
    """Test case for dcim_platforms_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","napalm_driver":"napalm_driver","description":"description","url":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"napalm_args":"{}","name":"name","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/platforms/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_delete(client):
    """Test case for dcim_platforms_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/platforms/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_list(client):
    """Test case for dcim_platforms_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('napalm_driver', 'napalm_driver_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('napalm_driver__n', 'napalm_driver__n_example'),
                    ('napalm_driver__ic', 'napalm_driver__ic_example'),
                    ('napalm_driver__nic', 'napalm_driver__nic_example'),
                    ('napalm_driver__iew', 'napalm_driver__iew_example'),
                    ('napalm_driver__niew', 'napalm_driver__niew_example'),
                    ('napalm_driver__isw', 'napalm_driver__isw_example'),
                    ('napalm_driver__nisw', 'napalm_driver__nisw_example'),
                    ('napalm_driver__ie', 'napalm_driver__ie_example'),
                    ('napalm_driver__nie', 'napalm_driver__nie_example'),
                    ('napalm_driver__empty', 'napalm_driver__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/platforms/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_partial_update(client):
    """Test case for dcim_platforms_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","napalm_driver":"napalm_driver","description":"description","url":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"napalm_args":"{}","name":"name","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/platforms/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_read(client):
    """Test case for dcim_platforms_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/platforms/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_platforms_update(client):
    """Test case for dcim_platforms_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","napalm_driver":"napalm_driver","description":"description","url":"https://openapi-generator.tech","manufacturer":1,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"napalm_args":"{}","name":"name","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/platforms/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_bulk_delete(client):
    """Test case for dcim_power_feeds_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-feeds/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_bulk_partial_update(client):
    """Test case for dcim_power_feeds_bulk_partial_update

    
    """
    body = {"connected_endpoints":["connected_endpoints","connected_endpoints"],"description":"description","type":"primary","power_panel":5,"supply":"ac","amperage":2624,"max_utilization":15,"mark_connected":True,"_occupied":True,"connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"voltage":-17680,"link_peers":["link_peers","link_peers"],"name":"name","status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-feeds/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_bulk_update(client):
    """Test case for dcim_power_feeds_bulk_update

    
    """
    body = {"connected_endpoints":["connected_endpoints","connected_endpoints"],"description":"description","type":"primary","power_panel":5,"supply":"ac","amperage":2624,"max_utilization":15,"mark_connected":True,"_occupied":True,"connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"voltage":-17680,"link_peers":["link_peers","link_peers"],"name":"name","status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-feeds/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_create(client):
    """Test case for dcim_power_feeds_create

    
    """
    body = {"connected_endpoints":["connected_endpoints","connected_endpoints"],"description":"description","type":"primary","power_panel":5,"supply":"ac","amperage":2624,"max_utilization":15,"mark_connected":True,"_occupied":True,"connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"voltage":-17680,"link_peers":["link_peers","link_peers"],"name":"name","status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-feeds/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_delete(client):
    """Test case for dcim_power_feeds_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-feeds/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_list(client):
    """Test case for dcim_power_feeds_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('status', 'status_example'),
                    ('type', 'type_example'),
                    ('supply', 'supply_example'),
                    ('phase', 'phase_example'),
                    ('voltage', 'voltage_example'),
                    ('amperage', 'amperage_example'),
                    ('max_utilization', 'max_utilization_example'),
                    ('cable_end', 'cable_end_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('power_panel_id', 'power_panel_id_example'),
                    ('rack_id', 'rack_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('status__n', 'status__n_example'),
                    ('type__n', 'type__n_example'),
                    ('supply__n', 'supply__n_example'),
                    ('phase__n', 'phase__n_example'),
                    ('voltage__n', 'voltage__n_example'),
                    ('voltage__lte', 'voltage__lte_example'),
                    ('voltage__lt', 'voltage__lt_example'),
                    ('voltage__gte', 'voltage__gte_example'),
                    ('voltage__gt', 'voltage__gt_example'),
                    ('amperage__n', 'amperage__n_example'),
                    ('amperage__lte', 'amperage__lte_example'),
                    ('amperage__lt', 'amperage__lt_example'),
                    ('amperage__gte', 'amperage__gte_example'),
                    ('amperage__gt', 'amperage__gt_example'),
                    ('max_utilization__n', 'max_utilization__n_example'),
                    ('max_utilization__lte', 'max_utilization__lte_example'),
                    ('max_utilization__lt', 'max_utilization__lt_example'),
                    ('max_utilization__gte', 'max_utilization__gte_example'),
                    ('max_utilization__gt', 'max_utilization__gt_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('power_panel_id__n', 'power_panel_id__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-feeds/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_partial_update(client):
    """Test case for dcim_power_feeds_partial_update

    
    """
    body = {"connected_endpoints":["connected_endpoints","connected_endpoints"],"description":"description","type":"primary","power_panel":5,"supply":"ac","amperage":2624,"max_utilization":15,"mark_connected":True,"_occupied":True,"connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"voltage":-17680,"link_peers":["link_peers","link_peers"],"name":"name","status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-feeds/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_read(client):
    """Test case for dcim_power_feeds_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-feeds/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_trace(client):
    """Test case for dcim_power_feeds_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-feeds/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_update(client):
    """Test case for dcim_power_feeds_update

    
    """
    body = {"connected_endpoints":["connected_endpoints","connected_endpoints"],"description":"description","type":"primary","power_panel":5,"supply":"ac","amperage":2624,"max_utilization":15,"mark_connected":True,"_occupied":True,"connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"voltage":-17680,"link_peers":["link_peers","link_peers"],"name":"name","status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-feeds/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_bulk_delete(client):
    """Test case for dcim_power_outlet_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-outlet-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_bulk_partial_update(client):
    """Test case for dcim_power_outlet_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"iec-60320-c5","url":"https://openapi-generator.tech","name":"name","feed_leg":"A","id":6,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-outlet-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_bulk_update(client):
    """Test case for dcim_power_outlet_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"iec-60320-c5","url":"https://openapi-generator.tech","name":"name","feed_leg":"A","id":6,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-outlet-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_create(client):
    """Test case for dcim_power_outlet_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"iec-60320-c5","url":"https://openapi-generator.tech","name":"name","feed_leg":"A","id":6,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-outlet-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_delete(client):
    """Test case for dcim_power_outlet_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-outlet-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_list(client):
    """Test case for dcim_power_outlet_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('feed_leg', 'feed_leg_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('feed_leg__n', 'feed_leg__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-outlet-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_partial_update(client):
    """Test case for dcim_power_outlet_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"iec-60320-c5","url":"https://openapi-generator.tech","name":"name","feed_leg":"A","id":6,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-outlet-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_read(client):
    """Test case for dcim_power_outlet_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-outlet-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlet_templates_update(client):
    """Test case for dcim_power_outlet_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"label":"label","type":"iec-60320-c5","url":"https://openapi-generator.tech","name":"name","feed_leg":"A","id":6,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-outlet-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_bulk_delete(client):
    """Test case for dcim_power_outlets_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-outlets/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_bulk_partial_update(client):
    """Test case for dcim_power_outlets_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c5","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","feed_leg":"A","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-outlets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_bulk_update(client):
    """Test case for dcim_power_outlets_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c5","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","feed_leg":"A","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-outlets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_create(client):
    """Test case for dcim_power_outlets_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c5","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","feed_leg":"A","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-outlets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_delete(client):
    """Test case for dcim_power_outlets_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-outlets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_list(client):
    """Test case for dcim_power_outlets_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('feed_leg', 'feed_leg_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('type', 'type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('feed_leg__n', 'feed_leg__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-outlets/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_partial_update(client):
    """Test case for dcim_power_outlets_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c5","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","feed_leg":"A","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-outlets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_read(client):
    """Test case for dcim_power_outlets_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-outlets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_trace(client):
    """Test case for dcim_power_outlets_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-outlets/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_outlets_update(client):
    """Test case for dcim_power_outlets_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c5","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","feed_leg":"A","connected_endpoints_reachable":True,"id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-outlets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_bulk_delete(client):
    """Test case for dcim_power_panels_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-panels/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_bulk_partial_update(client):
    """Test case for dcim_power_panels_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","powerfeed_count":1,"location":6,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-panels/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_bulk_update(client):
    """Test case for dcim_power_panels_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","powerfeed_count":1,"location":6,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-panels/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_create(client):
    """Test case for dcim_power_panels_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","powerfeed_count":1,"location":6,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-panels/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_delete(client):
    """Test case for dcim_power_panels_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-panels/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_list(client):
    """Test case for dcim_power_panels_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-panels/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_partial_update(client):
    """Test case for dcim_power_panels_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","powerfeed_count":1,"location":6,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-panels/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_read(client):
    """Test case for dcim_power_panels_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-panels/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_panels_update(client):
    """Test case for dcim_power_panels_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","powerfeed_count":1,"location":6,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-panels/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_bulk_delete(client):
    """Test case for dcim_power_port_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-port-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_bulk_partial_update(client):
    """Test case for dcim_power_port_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":6,"label":"label","type":"iec-60320-c6","maximum_draw":19536,"url":"https://openapi-generator.tech","allocated_draw":2624,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_bulk_update(client):
    """Test case for dcim_power_port_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":6,"label":"label","type":"iec-60320-c6","maximum_draw":19536,"url":"https://openapi-generator.tech","allocated_draw":2624,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_create(client):
    """Test case for dcim_power_port_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":6,"label":"label","type":"iec-60320-c6","maximum_draw":19536,"url":"https://openapi-generator.tech","allocated_draw":2624,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_delete(client):
    """Test case for dcim_power_port_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_list(client):
    """Test case for dcim_power_port_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('maximum_draw', 'maximum_draw_example'),
                    ('allocated_draw', 'allocated_draw_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('maximum_draw__n', 'maximum_draw__n_example'),
                    ('maximum_draw__lte', 'maximum_draw__lte_example'),
                    ('maximum_draw__lt', 'maximum_draw__lt_example'),
                    ('maximum_draw__gte', 'maximum_draw__gte_example'),
                    ('maximum_draw__gt', 'maximum_draw__gt_example'),
                    ('allocated_draw__n', 'allocated_draw__n_example'),
                    ('allocated_draw__lte', 'allocated_draw__lte_example'),
                    ('allocated_draw__lt', 'allocated_draw__lt_example'),
                    ('allocated_draw__gte', 'allocated_draw__gte_example'),
                    ('allocated_draw__gt', 'allocated_draw__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-port-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_partial_update(client):
    """Test case for dcim_power_port_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":6,"label":"label","type":"iec-60320-c6","maximum_draw":19536,"url":"https://openapi-generator.tech","allocated_draw":2624,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_read(client):
    """Test case for dcim_power_port_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_port_templates_update(client):
    """Test case for dcim_power_port_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","module_type":5,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":6,"label":"label","type":"iec-60320-c6","maximum_draw":19536,"url":"https://openapi-generator.tech","allocated_draw":2624,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_bulk_delete(client):
    """Test case for dcim_power_ports_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-ports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_bulk_partial_update(client):
    """Test case for dcim_power_ports_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":5,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c6","link_peers_type":"link_peers_type","maximum_draw":19536,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"allocated_draw":2624,"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":1,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_bulk_update(client):
    """Test case for dcim_power_ports_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":5,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c6","link_peers_type":"link_peers_type","maximum_draw":19536,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"allocated_draw":2624,"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":1,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_create(client):
    """Test case for dcim_power_ports_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":5,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c6","link_peers_type":"link_peers_type","maximum_draw":19536,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"allocated_draw":2624,"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":1,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/power-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_delete(client):
    """Test case for dcim_power_ports_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/power-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_list(client):
    """Test case for dcim_power_ports_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('maximum_draw', 'maximum_draw_example'),
                    ('allocated_draw', 'allocated_draw_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('connected', 'connected_example'),
                    ('type', 'type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('maximum_draw__n', 'maximum_draw__n_example'),
                    ('maximum_draw__lte', 'maximum_draw__lte_example'),
                    ('maximum_draw__lt', 'maximum_draw__lt_example'),
                    ('maximum_draw__gte', 'maximum_draw__gte_example'),
                    ('maximum_draw__gt', 'maximum_draw__gt_example'),
                    ('allocated_draw__n', 'allocated_draw__n_example'),
                    ('allocated_draw__lte', 'allocated_draw__lte_example'),
                    ('allocated_draw__lt', 'allocated_draw__lt_example'),
                    ('allocated_draw__gte', 'allocated_draw__gte_example'),
                    ('allocated_draw__gt', 'allocated_draw__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-ports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_partial_update(client):
    """Test case for dcim_power_ports_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":5,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c6","link_peers_type":"link_peers_type","maximum_draw":19536,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"allocated_draw":2624,"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":1,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/power-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_read(client):
    """Test case for dcim_power_ports_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_trace(client):
    """Test case for dcim_power_ports_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-ports/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_ports_update(client):
    """Test case for dcim_power_ports_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","connected_endpoints":["connected_endpoints","connected_endpoints"],"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":5,"description":"description","connected_endpoints_type":"connected_endpoints_type","cable_end":"cable_end","label":"label","type":"iec-60320-c6","link_peers_type":"link_peers_type","maximum_draw":19536,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"allocated_draw":2624,"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","connected_endpoints_reachable":True,"id":1,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/power-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_bulk_delete(client):
    """Test case for dcim_rack_reservations_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rack-reservations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_bulk_partial_update(client):
    """Test case for dcim_rack_reservations_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack":6,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","units":[19536,19536],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":0,"user":5,"tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rack-reservations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_bulk_update(client):
    """Test case for dcim_rack_reservations_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack":6,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","units":[19536,19536],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":0,"user":5,"tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rack-reservations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_create(client):
    """Test case for dcim_rack_reservations_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack":6,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","units":[19536,19536],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":0,"user":5,"tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/rack-reservations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_delete(client):
    """Test case for dcim_rack_reservations_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rack-reservations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_list(client):
    """Test case for dcim_rack_reservations_list

    
    """
    params = [('id', 'id_example'),
                    ('created', 'created_example'),
                    ('description', 'description_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('rack_id', 'rack_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('user_id', 'user_id_example'),
                    ('user', 'user_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('user__n', 'user__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-reservations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_partial_update(client):
    """Test case for dcim_rack_reservations_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack":6,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","units":[19536,19536],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":0,"user":5,"tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rack-reservations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_read(client):
    """Test case for dcim_rack_reservations_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-reservations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_update(client):
    """Test case for dcim_rack_reservations_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack":6,"comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","units":[19536,19536],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":0,"user":5,"tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rack-reservations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_bulk_delete(client):
    """Test case for dcim_rack_roles_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rack-roles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_bulk_partial_update(client):
    """Test case for dcim_rack_roles_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack_count":1,"color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rack-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_bulk_update(client):
    """Test case for dcim_rack_roles_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack_count":1,"color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rack-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_create(client):
    """Test case for dcim_rack_roles_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack_count":1,"color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/rack-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_delete(client):
    """Test case for dcim_rack_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rack-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_list(client):
    """Test case for dcim_rack_roles_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_partial_update(client):
    """Test case for dcim_rack_roles_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack_count":1,"color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rack-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_read(client):
    """Test case for dcim_rack_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_roles_update(client):
    """Test case for dcim_rack_roles_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rack_count":1,"color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rack-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_bulk_delete(client):
    """Test case for dcim_racks_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/racks/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_bulk_partial_update(client):
    """Test case for dcim_racks_bulk_partial_update

    
    """
    body = {"role":3,"description":"description","type":"2-post-frame","mounting_depth":18471,"facility_id":"facility_id","outer_depth":7543,"id":6,"device_count":0,"tenant":4,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":74,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","weight":1.2315135367772556,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"max_weight":1280358508,"site":2,"weight_unit":"kg","serial":"serial","outer_width":23138,"name":"name","powerfeed_count":9,"width":1,"location":1,"outer_unit":"mm","status":"reserved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/racks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_bulk_update(client):
    """Test case for dcim_racks_bulk_update

    
    """
    body = {"role":3,"description":"description","type":"2-post-frame","mounting_depth":18471,"facility_id":"facility_id","outer_depth":7543,"id":6,"device_count":0,"tenant":4,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":74,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","weight":1.2315135367772556,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"max_weight":1280358508,"site":2,"weight_unit":"kg","serial":"serial","outer_width":23138,"name":"name","powerfeed_count":9,"width":1,"location":1,"outer_unit":"mm","status":"reserved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/racks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_create(client):
    """Test case for dcim_racks_create

    
    """
    body = {"role":3,"description":"description","type":"2-post-frame","mounting_depth":18471,"facility_id":"facility_id","outer_depth":7543,"id":6,"device_count":0,"tenant":4,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":74,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","weight":1.2315135367772556,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"max_weight":1280358508,"site":2,"weight_unit":"kg","serial":"serial","outer_width":23138,"name":"name","powerfeed_count":9,"width":1,"location":1,"outer_unit":"mm","status":"reserved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/racks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_delete(client):
    """Test case for dcim_racks_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/racks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_elevation(client):
    """Test case for dcim_racks_elevation

    
    """
    params = [('q', 'q_example'),
                    ('face', front),
                    ('render', json),
                    ('unit_width', 220),
                    ('unit_height', 22),
                    ('legend_width', 30),
                    ('margin_width', 15),
                    ('exclude', 56),
                    ('expand_devices', True),
                    ('include_images', True)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/racks/{id}/elevation'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_list(client):
    """Test case for dcim_racks_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('facility_id', 'facility_id_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('u_height', 'u_height_example'),
                    ('desc_units', 'desc_units_example'),
                    ('outer_width', 'outer_width_example'),
                    ('outer_depth', 'outer_depth_example'),
                    ('outer_unit', 'outer_unit_example'),
                    ('mounting_depth', 'mounting_depth_example'),
                    ('weight', 'weight_example'),
                    ('max_weight', 'max_weight_example'),
                    ('weight_unit', 'weight_unit_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('status', 'status_example'),
                    ('type', 'type_example'),
                    ('width', 'width_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('serial', 'serial_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('facility_id__n', 'facility_id__n_example'),
                    ('facility_id__ic', 'facility_id__ic_example'),
                    ('facility_id__nic', 'facility_id__nic_example'),
                    ('facility_id__iew', 'facility_id__iew_example'),
                    ('facility_id__niew', 'facility_id__niew_example'),
                    ('facility_id__isw', 'facility_id__isw_example'),
                    ('facility_id__nisw', 'facility_id__nisw_example'),
                    ('facility_id__ie', 'facility_id__ie_example'),
                    ('facility_id__nie', 'facility_id__nie_example'),
                    ('facility_id__empty', 'facility_id__empty_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('asset_tag__empty', 'asset_tag__empty_example'),
                    ('u_height__n', 'u_height__n_example'),
                    ('u_height__lte', 'u_height__lte_example'),
                    ('u_height__lt', 'u_height__lt_example'),
                    ('u_height__gte', 'u_height__gte_example'),
                    ('u_height__gt', 'u_height__gt_example'),
                    ('outer_width__n', 'outer_width__n_example'),
                    ('outer_width__lte', 'outer_width__lte_example'),
                    ('outer_width__lt', 'outer_width__lt_example'),
                    ('outer_width__gte', 'outer_width__gte_example'),
                    ('outer_width__gt', 'outer_width__gt_example'),
                    ('outer_depth__n', 'outer_depth__n_example'),
                    ('outer_depth__lte', 'outer_depth__lte_example'),
                    ('outer_depth__lt', 'outer_depth__lt_example'),
                    ('outer_depth__gte', 'outer_depth__gte_example'),
                    ('outer_depth__gt', 'outer_depth__gt_example'),
                    ('outer_unit__n', 'outer_unit__n_example'),
                    ('mounting_depth__n', 'mounting_depth__n_example'),
                    ('mounting_depth__lte', 'mounting_depth__lte_example'),
                    ('mounting_depth__lt', 'mounting_depth__lt_example'),
                    ('mounting_depth__gte', 'mounting_depth__gte_example'),
                    ('mounting_depth__gt', 'mounting_depth__gt_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('max_weight__n', 'max_weight__n_example'),
                    ('max_weight__lte', 'max_weight__lte_example'),
                    ('max_weight__lt', 'max_weight__lt_example'),
                    ('max_weight__gte', 'max_weight__gte_example'),
                    ('max_weight__gt', 'max_weight__gt_example'),
                    ('weight_unit__n', 'weight_unit__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('status__n', 'status__n_example'),
                    ('type__n', 'type__n_example'),
                    ('width__n', 'width__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('serial__n', 'serial__n_example'),
                    ('serial__ic', 'serial__ic_example'),
                    ('serial__nic', 'serial__nic_example'),
                    ('serial__iew', 'serial__iew_example'),
                    ('serial__niew', 'serial__niew_example'),
                    ('serial__isw', 'serial__isw_example'),
                    ('serial__nisw', 'serial__nisw_example'),
                    ('serial__ie', 'serial__ie_example'),
                    ('serial__nie', 'serial__nie_example'),
                    ('serial__empty', 'serial__empty_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/racks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_partial_update(client):
    """Test case for dcim_racks_partial_update

    
    """
    body = {"role":3,"description":"description","type":"2-post-frame","mounting_depth":18471,"facility_id":"facility_id","outer_depth":7543,"id":6,"device_count":0,"tenant":4,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":74,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","weight":1.2315135367772556,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"max_weight":1280358508,"site":2,"weight_unit":"kg","serial":"serial","outer_width":23138,"name":"name","powerfeed_count":9,"width":1,"location":1,"outer_unit":"mm","status":"reserved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/racks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_read(client):
    """Test case for dcim_racks_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/racks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_update(client):
    """Test case for dcim_racks_update

    
    """
    body = {"role":3,"description":"description","type":"2-post-frame","mounting_depth":18471,"facility_id":"facility_id","outer_depth":7543,"id":6,"device_count":0,"tenant":4,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":74,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","weight":1.2315135367772556,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"max_weight":1280358508,"site":2,"weight_unit":"kg","serial":"serial","outer_width":23138,"name":"name","powerfeed_count":9,"width":1,"location":1,"outer_unit":"mm","status":"reserved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/racks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_bulk_delete(client):
    """Test case for dcim_rear_port_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rear-port-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_bulk_partial_update(client):
    """Test case for dcim_rear_port_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"positions":610,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rear-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_bulk_update(client):
    """Test case for dcim_rear_port_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"positions":610,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rear-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_create(client):
    """Test case for dcim_rear_port_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"positions":610,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/rear-port-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_delete(client):
    """Test case for dcim_rear_port_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rear-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_list(client):
    """Test case for dcim_rear_port_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('color', 'color_example'),
                    ('positions', 'positions_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('devicetype_id', 'devicetype_id_example'),
                    ('moduletype_id', 'moduletype_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('positions__n', 'positions__n_example'),
                    ('positions__lte', 'positions__lte_example'),
                    ('positions__lt', 'positions__lt_example'),
                    ('positions__gte', 'positions__gte_example'),
                    ('positions__gt', 'positions__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
                    ('moduletype_id__n', 'moduletype_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-port-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_partial_update(client):
    """Test case for dcim_rear_port_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"positions":610,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rear-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_read(client):
    """Test case for dcim_rear_port_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-port-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_port_templates_update(client):
    """Test case for dcim_rear_port_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","module_type":1,"created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","device_type":0,"positions":610,"label":"label","type":"8p8c","url":"https://openapi-generator.tech","name":"name","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rear-port-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_bulk_delete(client):
    """Test case for dcim_rear_ports_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rear-ports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_bulk_partial_update(client):
    """Test case for dcim_rear_ports_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","positions":610,"cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rear-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_bulk_update(client):
    """Test case for dcim_rear_ports_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","positions":610,"cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rear-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_create(client):
    """Test case for dcim_rear_ports_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","positions":610,"cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/rear-ports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_delete(client):
    """Test case for dcim_rear_ports_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rear-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_list(client):
    """Test case for dcim_rear_ports_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('label', 'label_example'),
                    ('type', 'type_example'),
                    ('color', 'color_example'),
                    ('positions', 'positions_example'),
                    ('description', 'description_example'),
                    ('cable_end', 'cable_end_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('virtual_chassis', 'virtual_chassis_example'),
                    ('module_id', 'module_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('occupied', 'occupied_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('label__n', 'label__n_example'),
                    ('label__ic', 'label__ic_example'),
                    ('label__nic', 'label__nic_example'),
                    ('label__iew', 'label__iew_example'),
                    ('label__niew', 'label__niew_example'),
                    ('label__isw', 'label__isw_example'),
                    ('label__nisw', 'label__nisw_example'),
                    ('label__ie', 'label__ie_example'),
                    ('label__nie', 'label__nie_example'),
                    ('label__empty', 'label__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('positions__n', 'positions__n_example'),
                    ('positions__lte', 'positions__lte_example'),
                    ('positions__lt', 'positions__lt_example'),
                    ('positions__gte', 'positions__gte_example'),
                    ('positions__gt', 'positions__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('cable_end__n', 'cable_end__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('rack__n', 'rack__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('virtual_chassis__n', 'virtual_chassis__n_example'),
                    ('module_id__n', 'module_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-ports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_partial_update(client):
    """Test case for dcim_rear_ports_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","positions":610,"cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rear-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_paths(client):
    """Test case for dcim_rear_ports_paths

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-ports/{id}/paths'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_read(client):
    """Test case for dcim_rear_ports_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-ports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_update(client):
    """Test case for dcim_rear_ports_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","module":1,"description":"description","positions":610,"cable_end":"cable_end","label":"label","type":"8p8c","link_peers_type":"link_peers_type","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"link_peers":["link_peers","link_peers"],"mark_connected":True,"_occupied":True,"name":"name","id":6,"cable":{"display":"display","id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rear-ports/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_bulk_delete(client):
    """Test case for dcim_regions_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/regions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_bulk_partial_update(client):
    """Test case for dcim_regions_bulk_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/regions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_bulk_update(client):
    """Test case for dcim_regions_bulk_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/regions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_create(client):
    """Test case for dcim_regions_create

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/regions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_delete(client):
    """Test case for dcim_regions_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/regions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_list(client):
    """Test case for dcim_regions_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/regions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_partial_update(client):
    """Test case for dcim_regions_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/regions/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_read(client):
    """Test case for dcim_regions_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/regions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_regions_update(client):
    """Test case for dcim_regions_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/regions/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_bulk_delete(client):
    """Test case for dcim_site_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/site-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_bulk_partial_update(client):
    """Test case for dcim_site_groups_bulk_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/site-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_bulk_update(client):
    """Test case for dcim_site_groups_bulk_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/site-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_create(client):
    """Test case for dcim_site_groups_create

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/site-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_delete(client):
    """Test case for dcim_site_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/site-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_list(client):
    """Test case for dcim_site_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/site-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_partial_update(client):
    """Test case for dcim_site_groups_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/site-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_read(client):
    """Test case for dcim_site_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/site-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_site_groups_update(client):
    """Test case for dcim_site_groups_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/site-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_bulk_delete(client):
    """Test case for dcim_sites_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/sites/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_bulk_partial_update(client):
    """Test case for dcim_sites_bulk_partial_update

    
    """
    body = {"physical_address":"physical_address","circuit_count":6,"latitude":2.3021358869347655,"description":"description","vlan_count":1,"rack_count":3,"asns":[0,0],"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":4,"group":5,"longitude":7.061401241503109,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","time_zone":"time_zone","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","virtualmachine_count":7,"prefix_count":9,"region":2,"facility":"facility","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/sites/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_bulk_update(client):
    """Test case for dcim_sites_bulk_update

    
    """
    body = {"physical_address":"physical_address","circuit_count":6,"latitude":2.3021358869347655,"description":"description","vlan_count":1,"rack_count":3,"asns":[0,0],"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":4,"group":5,"longitude":7.061401241503109,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","time_zone":"time_zone","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","virtualmachine_count":7,"prefix_count":9,"region":2,"facility":"facility","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/sites/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_create(client):
    """Test case for dcim_sites_create

    
    """
    body = {"physical_address":"physical_address","circuit_count":6,"latitude":2.3021358869347655,"description":"description","vlan_count":1,"rack_count":3,"asns":[0,0],"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":4,"group":5,"longitude":7.061401241503109,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","time_zone":"time_zone","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","virtualmachine_count":7,"prefix_count":9,"region":2,"facility":"facility","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/sites/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_delete(client):
    """Test case for dcim_sites_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/sites/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_list(client):
    """Test case for dcim_sites_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('facility', 'facility_example'),
                    ('latitude', 'latitude_example'),
                    ('longitude', 'longitude_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('status', 'status_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('asn', 'asn_example'),
                    ('asn_id', 'asn_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('facility__n', 'facility__n_example'),
                    ('facility__ic', 'facility__ic_example'),
                    ('facility__nic', 'facility__nic_example'),
                    ('facility__iew', 'facility__iew_example'),
                    ('facility__niew', 'facility__niew_example'),
                    ('facility__isw', 'facility__isw_example'),
                    ('facility__nisw', 'facility__nisw_example'),
                    ('facility__ie', 'facility__ie_example'),
                    ('facility__nie', 'facility__nie_example'),
                    ('facility__empty', 'facility__empty_example'),
                    ('latitude__n', 'latitude__n_example'),
                    ('latitude__lte', 'latitude__lte_example'),
                    ('latitude__lt', 'latitude__lt_example'),
                    ('latitude__gte', 'latitude__gte_example'),
                    ('latitude__gt', 'latitude__gt_example'),
                    ('longitude__n', 'longitude__n_example'),
                    ('longitude__lte', 'longitude__lte_example'),
                    ('longitude__lt', 'longitude__lt_example'),
                    ('longitude__gte', 'longitude__gte_example'),
                    ('longitude__gt', 'longitude__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('status__n', 'status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('asn__n', 'asn__n_example'),
                    ('asn_id__n', 'asn_id__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/sites/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_partial_update(client):
    """Test case for dcim_sites_partial_update

    
    """
    body = {"physical_address":"physical_address","circuit_count":6,"latitude":2.3021358869347655,"description":"description","vlan_count":1,"rack_count":3,"asns":[0,0],"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":4,"group":5,"longitude":7.061401241503109,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","time_zone":"time_zone","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","virtualmachine_count":7,"prefix_count":9,"region":2,"facility":"facility","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/sites/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_read(client):
    """Test case for dcim_sites_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/sites/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_sites_update(client):
    """Test case for dcim_sites_update

    
    """
    body = {"physical_address":"physical_address","circuit_count":6,"latitude":2.3021358869347655,"description":"description","vlan_count":1,"rack_count":3,"asns":[0,0],"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":4,"group":5,"longitude":7.061401241503109,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","time_zone":"time_zone","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","virtualmachine_count":7,"prefix_count":9,"region":2,"facility":"facility","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/sites/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_bulk_delete(client):
    """Test case for dcim_virtual_chassis_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/virtual-chassis/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_bulk_partial_update(client):
    """Test case for dcim_virtual_chassis_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","master":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"domain":"domain","name":"name","id":0,"member_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/virtual-chassis/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_bulk_update(client):
    """Test case for dcim_virtual_chassis_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","master":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"domain":"domain","name":"name","id":0,"member_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/virtual-chassis/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_create(client):
    """Test case for dcim_virtual_chassis_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","master":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"domain":"domain","name":"name","id":0,"member_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/virtual-chassis/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_delete(client):
    """Test case for dcim_virtual_chassis_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/virtual-chassis/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_list(client):
    """Test case for dcim_virtual_chassis_list

    
    """
    params = [('id', 'id_example'),
                    ('domain', 'domain_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('master_id', 'master_id_example'),
                    ('master', 'master_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('domain__n', 'domain__n_example'),
                    ('domain__ic', 'domain__ic_example'),
                    ('domain__nic', 'domain__nic_example'),
                    ('domain__iew', 'domain__iew_example'),
                    ('domain__niew', 'domain__niew_example'),
                    ('domain__isw', 'domain__isw_example'),
                    ('domain__nisw', 'domain__nisw_example'),
                    ('domain__ie', 'domain__ie_example'),
                    ('domain__nie', 'domain__nie_example'),
                    ('domain__empty', 'domain__empty_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('master_id__n', 'master_id__n_example'),
                    ('master__n', 'master__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/virtual-chassis/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_partial_update(client):
    """Test case for dcim_virtual_chassis_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","master":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"domain":"domain","name":"name","id":0,"member_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/virtual-chassis/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_read(client):
    """Test case for dcim_virtual_chassis_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/virtual-chassis/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_chassis_update(client):
    """Test case for dcim_virtual_chassis_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","master":6,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"domain":"domain","name":"name","id":0,"member_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/virtual-chassis/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_bulk_delete(client):
    """Test case for dcim_virtual_device_contexts_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/virtual-device-contexts/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_bulk_partial_update(client):
    """Test case for dcim_virtual_device_contexts_bulk_partial_update

    
    """
    body = {"identifier":4803,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","primary_ip":"primary_ip","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"device":0,"primary_ip6":2,"tenant":7,"interface_count":5,"primary_ip4":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/virtual-device-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_bulk_update(client):
    """Test case for dcim_virtual_device_contexts_bulk_update

    
    """
    body = {"identifier":4803,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","primary_ip":"primary_ip","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"device":0,"primary_ip6":2,"tenant":7,"interface_count":5,"primary_ip4":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/virtual-device-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_create(client):
    """Test case for dcim_virtual_device_contexts_create

    
    """
    body = {"identifier":4803,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","primary_ip":"primary_ip","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"device":0,"primary_ip6":2,"tenant":7,"interface_count":5,"primary_ip4":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/virtual-device-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_delete(client):
    """Test case for dcim_virtual_device_contexts_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/virtual-device-contexts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_list(client):
    """Test case for dcim_virtual_device_contexts_list

    
    """
    params = [('id', 'id_example'),
                    ('device', 'device_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('device_id', 'device_id_example'),
                    ('status', 'status_example'),
                    ('has_primary_ip', 'has_primary_ip_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('device__n', 'device__n_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('status__n', 'status__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/virtual-device-contexts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_partial_update(client):
    """Test case for dcim_virtual_device_contexts_partial_update

    
    """
    body = {"identifier":4803,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","primary_ip":"primary_ip","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"device":0,"primary_ip6":2,"tenant":7,"interface_count":5,"primary_ip4":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/virtual-device-contexts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_read(client):
    """Test case for dcim_virtual_device_contexts_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/virtual-device-contexts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_virtual_device_contexts_update(client):
    """Test case for dcim_virtual_device_contexts_update

    
    """
    body = {"identifier":4803,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","primary_ip":"primary_ip","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":6,"device":0,"primary_ip6":2,"tenant":7,"interface_count":5,"primary_ip4":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/virtual-device-contexts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

