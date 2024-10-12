# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_dcim_cables_create(client):
    """Test case for dcim_cables_create

    
    """
    body = {"color":"color","length":19750,"termination_b":{"key":"termination_b"},"termination_b_id":1280358508,"termination_a":{"key":"termination_a"},"label":"label","termination_b_type":"termination_b_type","type":"cat3","length_unit":"m","termination_a_id":314780940,"termination_a_type":"termination_a_type","id":0,"status":"connected"}
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
                    ('q', 'q_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('color', 'color_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('rack_id', 'rack_id_example'),
                    ('rack', 'rack_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
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
                    ('length__n', 'length__n_example'),
                    ('length__lte', 'length__lte_example'),
                    ('length__lt', 'length__lt_example'),
                    ('length__gte', 'length__gte_example'),
                    ('length__gt', 'length__gt_example'),
                    ('length_unit__n', 'length_unit__n_example'),
                    ('type__n', 'type__n_example'),
                    ('status__n', 'status__n_example'),
                    ('color__n', 'color__n_example'),
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
    body = {"color":"color","length":19750,"termination_b":{"key":"termination_b"},"termination_b_id":1280358508,"termination_a":{"key":"termination_a"},"label":"label","termination_b_type":"termination_b_type","type":"cat3","length_unit":"m","termination_a_id":314780940,"termination_a_type":"termination_a_type","id":0,"status":"connected"}
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
    body = {"color":"color","length":19750,"termination_b":{"key":"termination_b"},"termination_b_id":1280358508,"termination_a":{"key":"termination_a"},"label":"label","termination_b_type":"termination_b_type","type":"cat3","length_unit":"m","termination_a_id":314780940,"termination_a_type":"termination_a_type","id":0,"status":"connected"}
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

async def test_dcim_console_connections_list(client):
    """Test case for dcim_console_connections_list

    
    """
    params = [('name', 'name_example'),
                    ('connection_status', 'connection_status_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('connection_status__n', 'connection_status__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/console-connections/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_console_port_templates_create(client):
    """Test case for dcim_console_port_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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
                    ('type__n', 'type__n_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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

async def test_dcim_console_ports_create(client):
    """Test case for dcim_console_ports_create

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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
                    ('description', 'description_example'),
                    ('connection_status', 'connection_status_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
                    ('cabled', 'cabled_example'),
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
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('connection_status__n', 'connection_status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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

async def test_dcim_console_server_port_templates_create(client):
    """Test case for dcim_console_server_port_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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
                    ('type__n', 'type__n_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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
    body = {"name":"name","device_type":0,"id":6,"type":"de-9"}
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

async def test_dcim_console_server_ports_create(client):
    """Test case for dcim_console_server_ports_create

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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
                    ('description', 'description_example'),
                    ('connection_status', 'connection_status_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
                    ('cabled', 'cabled_example'),
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
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('connection_status__n', 'connection_status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":6,"type":"de-9","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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

async def test_dcim_device_bay_templates_create(client):
    """Test case for dcim_device_bay_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6}
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
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"name":"name","device_type":0,"id":6}
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

async def test_dcim_device_bays_create(client):
    """Test case for dcim_device_bays_create

    
    """
    body = {"installed_device":1,"name":"name","description":"description","id":6,"device":0,"tags":["tags","tags"]}
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
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
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
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"installed_device":1,"name":"name","description":"description","id":6,"device":0,"tags":["tags","tags"]}
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
    body = {"installed_device":1,"name":"name","description":"description","id":6,"device":0,"tags":["tags","tags"]}
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

async def test_dcim_device_roles_create(client):
    """Test case for dcim_device_roles_create

    
    """
    body = {"vm_role":True,"color":"color","name":"name","description":"description","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
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
                    ('q', 'q_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
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
    body = {"vm_role":True,"color":"color","name":"name","description":"description","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
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
    body = {"vm_role":True,"color":"color","name":"name","description":"description","virtualmachine_count":5,"id":1,"device_count":6,"slug":"slug"}
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

async def test_dcim_device_types_create(client):
    """Test case for dcim_device_types_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":19536,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"display_name":"display_name","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":["tags","tags"],"subdevice_role":"parent","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
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
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('console_ports', 'console_ports_example'),
                    ('console_server_ports', 'console_server_ports_example'),
                    ('power_ports', 'power_ports_example'),
                    ('power_outlets', 'power_outlets_example'),
                    ('interfaces', 'interfaces_example'),
                    ('pass_through_ports', 'pass_through_ports_example'),
                    ('device_bays', 'device_bays_example'),
                    ('tag', 'tag_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('part_number__n', 'part_number__n_example'),
                    ('part_number__ic', 'part_number__ic_example'),
                    ('part_number__nic', 'part_number__nic_example'),
                    ('part_number__iew', 'part_number__iew_example'),
                    ('part_number__niew', 'part_number__niew_example'),
                    ('part_number__isw', 'part_number__isw_example'),
                    ('part_number__nisw', 'part_number__nisw_example'),
                    ('part_number__ie', 'part_number__ie_example'),
                    ('part_number__nie', 'part_number__nie_example'),
                    ('u_height__n', 'u_height__n_example'),
                    ('u_height__lte', 'u_height__lte_example'),
                    ('u_height__lt', 'u_height__lt_example'),
                    ('u_height__gte', 'u_height__gte_example'),
                    ('u_height__gt', 'u_height__gt_example'),
                    ('subdevice_role__n', 'subdevice_role__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":19536,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"display_name":"display_name","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":["tags","tags"],"subdevice_role":"parent","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","rear_image":"https://openapi-generator.tech","u_height":19536,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"display_name":"display_name","front_image":"https://openapi-generator.tech","manufacturer":1,"tags":["tags","tags"],"subdevice_role":"parent","part_number":"part_number","model":"model","id":6,"device_count":0,"slug":"slug"}
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

async def test_dcim_devices_create(client):
    """Test case for dcim_devices_create

    
    """
    body = {"cluster":0,"config_context":{"key":"config_context"},"primary_ip":"primary_ip","vc_priority":31,"device_type":1,"platform":5,"id":5,"tenant":4,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":3,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":"front","site":2,"vc_position":188,"local_context_data":"local_context_data","parent_device":{"name":"name","id":9,"display_name":"display_name","url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","virtual_chassis":1,"position":7544,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
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

async def test_dcim_devices_graphs(client):
    """Test case for dcim_devices_graphs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/devices/{id}/graphs'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_list(client):
    """Test case for dcim_devices_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('face', 'face_example'),
                    ('position', 'position_example'),
                    ('vc_position', 'vc_position_example'),
                    ('vc_priority', 'vc_priority_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('local_context_data', 'local_context_data_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('device_type_id', 'device_type_id_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('rack_group_id', 'rack_group_id_example'),
                    ('rack_id', 'rack_id_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('model', 'model_example'),
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
                    ('device_bays', 'device_bays_example'),
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
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('face__n', 'face__n_example'),
                    ('position__n', 'position__n_example'),
                    ('position__lte', 'position__lte_example'),
                    ('position__lt', 'position__lt_example'),
                    ('position__gte', 'position__gte_example'),
                    ('position__gt', 'position__gt_example'),
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
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
                    ('device_type_id__n', 'device_type_id__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('rack_group_id__n', 'rack_group_id__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('model__n', 'model__n_example'),
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
                    ('virtual_chassis_id__n', 'virtual_chassis_id__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"cluster":0,"config_context":{"key":"config_context"},"primary_ip":"primary_ip","vc_priority":31,"device_type":1,"platform":5,"id":5,"tenant":4,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":3,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":"front","site":2,"vc_position":188,"local_context_data":"local_context_data","parent_device":{"name":"name","id":9,"display_name":"display_name","url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","virtual_chassis":1,"position":7544,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
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
    body = {"cluster":0,"config_context":{"key":"config_context"},"primary_ip":"primary_ip","vc_priority":31,"device_type":1,"platform":5,"id":5,"tenant":4,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":3,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":"front","site":2,"vc_position":188,"local_context_data":"local_context_data","parent_device":{"name":"name","id":9,"display_name":"display_name","url":"https://openapi-generator.tech"},"serial":"serial","device_role":6,"name":"name","virtual_chassis":1,"position":7544,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
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

async def test_dcim_front_port_templates_create(client):
    """Test case for dcim_front_port_templates_create

    
    """
    body = {"name":"name","rear_port":1,"device_type":0,"id":6,"type":"8p8c","rear_port_position":38}
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
                    ('type__n', 'type__n_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","rear_port":1,"device_type":0,"id":6,"type":"8p8c","rear_port_position":38}
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
    body = {"name":"name","rear_port":1,"device_type":0,"id":6,"type":"8p8c","rear_port_position":38}
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

async def test_dcim_front_ports_create(client):
    """Test case for dcim_front_ports_create

    
    """
    body = {"name":"name","rear_port":1,"description":"description","id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":38,"tags":["tags","tags"]}
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
                    ('type', 'type_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
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
                    ('type__n', 'type__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"name":"name","rear_port":1,"description":"description","id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":38,"tags":["tags","tags"]}
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

async def test_dcim_front_ports_trace(client):
    """Test case for dcim_front_ports_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/front-ports/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_front_ports_update(client):
    """Test case for dcim_front_ports_update

    
    """
    body = {"name":"name","rear_port":1,"description":"description","id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"rear_port_position":38,"tags":["tags","tags"]}
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

async def test_dcim_interface_connections_list(client):
    """Test case for dcim_interface_connections_list

    
    """
    params = [('connection_status', 'connection_status_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('connection_status__n', 'connection_status__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interface-connections/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_create(client):
    """Test case for dcim_interface_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6,"type":"virtual","mgmt_only":True}
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
                    ('type__n', 'type__n_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","device_type":0,"id":6,"type":"virtual","mgmt_only":True}
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
    body = {"name":"name","device_type":0,"id":6,"type":"virtual","mgmt_only":True}
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

async def test_dcim_interfaces_create(client):
    """Test case for dcim_interfaces_create

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"untagged_vlan":7,"connection_status":True,"description":"description","type":"virtual","enabled":True,"mgmt_only":True,"mtu":36945,"tags":["tags","tags"],"mode":"access","tagged_vlans":[2,2],"lag":5,"count_ipaddresses":0,"mac_address":"mac_address","name":"name","id":1,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
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

async def test_dcim_interfaces_graphs(client):
    """Test case for dcim_interfaces_graphs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interfaces/{id}/graphs'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interfaces_list(client):
    """Test case for dcim_interfaces_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('connection_status', 'connection_status_example'),
                    ('type', 'type_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 'mtu_example'),
                    ('mgmt_only', 'mgmt_only_example'),
                    ('mode', 'mode_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
                    ('kind', 'kind_example'),
                    ('lag_id', 'lag_id_example'),
                    ('mac_address', 'mac_address_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan', 'vlan_example'),
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
                    ('connection_status__n', 'connection_status__n_example'),
                    ('type__n', 'type__n_example'),
                    ('mtu__n', 'mtu__n_example'),
                    ('mtu__lte', 'mtu__lte_example'),
                    ('mtu__lt', 'mtu__lt_example'),
                    ('mtu__gte', 'mtu__gte_example'),
                    ('mtu__gt', 'mtu__gt_example'),
                    ('mode__n', 'mode__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('lag_id__n', 'lag_id__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"untagged_vlan":7,"connection_status":True,"description":"description","type":"virtual","enabled":True,"mgmt_only":True,"mtu":36945,"tags":["tags","tags"],"mode":"access","tagged_vlans":[2,2],"lag":5,"count_ipaddresses":0,"mac_address":"mac_address","name":"name","id":1,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"untagged_vlan":7,"connection_status":True,"description":"description","type":"virtual","enabled":True,"mgmt_only":True,"mtu":36945,"tags":["tags","tags"],"mode":"access","tagged_vlans":[2,2],"lag":5,"count_ipaddresses":0,"mac_address":"mac_address","name":"name","id":1,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6}
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

async def test_dcim_inventory_items_create(client):
    """Test case for dcim_inventory_items_create

    
    """
    body = {"asset_tag":"asset_tag","parent":5,"discovered":True,"serial":"serial","name":"name","description":"description","id":6,"part_id":"part_id","device":0,"manufacturer":1,"tags":["tags","tags"]}
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
                    ('part_id', 'part_id_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('discovered', 'discovered_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('parent_id', 'parent_id_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
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
                    ('part_id__n', 'part_id__n_example'),
                    ('part_id__ic', 'part_id__ic_example'),
                    ('part_id__nic', 'part_id__nic_example'),
                    ('part_id__iew', 'part_id__iew_example'),
                    ('part_id__niew', 'part_id__niew_example'),
                    ('part_id__isw', 'part_id__isw_example'),
                    ('part_id__nisw', 'part_id__nisw_example'),
                    ('part_id__ie', 'part_id__ie_example'),
                    ('part_id__nie', 'part_id__nie_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
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
    body = {"asset_tag":"asset_tag","parent":5,"discovered":True,"serial":"serial","name":"name","description":"description","id":6,"part_id":"part_id","device":0,"manufacturer":1,"tags":["tags","tags"]}
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
    body = {"asset_tag":"asset_tag","parent":5,"discovered":True,"serial":"serial","name":"name","description":"description","id":6,"part_id":"part_id","device":0,"manufacturer":1,"tags":["tags","tags"]}
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

async def test_dcim_manufacturers_create(client):
    """Test case for dcim_manufacturers_create

    
    """
    body = {"inventoryitem_count":5,"name":"name","description":"description","id":1,"platform_count":5,"devicetype_count":6,"slug":"slug"}
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
                    ('q', 'q_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
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
    body = {"inventoryitem_count":5,"name":"name","description":"description","id":1,"platform_count":5,"devicetype_count":6,"slug":"slug"}
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
    body = {"inventoryitem_count":5,"name":"name","description":"description","id":1,"platform_count":5,"devicetype_count":6,"slug":"slug"}
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

async def test_dcim_platforms_create(client):
    """Test case for dcim_platforms_create

    
    """
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","description":"description","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug","manufacturer":1}
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
                    ('q', 'q_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('napalm_driver__n', 'napalm_driver__n_example'),
                    ('napalm_driver__ic', 'napalm_driver__ic_example'),
                    ('napalm_driver__nic', 'napalm_driver__nic_example'),
                    ('napalm_driver__iew', 'napalm_driver__iew_example'),
                    ('napalm_driver__niew', 'napalm_driver__niew_example'),
                    ('napalm_driver__isw', 'napalm_driver__isw_example'),
                    ('napalm_driver__nisw', 'napalm_driver__nisw_example'),
                    ('napalm_driver__ie', 'napalm_driver__ie_example'),
                    ('napalm_driver__nie', 'napalm_driver__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('manufacturer_id__n', 'manufacturer_id__n_example'),
                    ('manufacturer__n', 'manufacturer__n_example'),
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
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","description":"description","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug","manufacturer":1}
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
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","description":"description","virtualmachine_count":5,"id":6,"device_count":0,"slug":"slug","manufacturer":1}
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

async def test_dcim_power_connections_list(client):
    """Test case for dcim_power_connections_list

    
    """
    params = [('name', 'name_example'),
                    ('connection_status', 'connection_status_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('connection_status__n', 'connection_status__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/power-connections/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_power_feeds_create(client):
    """Test case for dcim_power_feeds_create

    
    """
    body = {"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23","custom_fields":"{}","type":"primary","power_panel":5,"supply":"ac","tags":["tags","tags"],"voltage":-17680,"amperage":2624,"max_utilization":15,"name":"name","id":6,"status":"offline"}
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
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('power_panel_id', 'power_panel_id_example'),
                    ('rack_id', 'rack_id_example'),
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
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('power_panel_id__n', 'power_panel_id__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23","custom_fields":"{}","type":"primary","power_panel":5,"supply":"ac","tags":["tags","tags"],"voltage":-17680,"amperage":2624,"max_utilization":15,"name":"name","id":6,"status":"offline"}
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

async def test_dcim_power_feeds_update(client):
    """Test case for dcim_power_feeds_update

    
    """
    body = {"phase":"single-phase","last_updated":"2000-01-23T04:56:07.000+00:00","rack":5,"comments":"comments","created":"2000-01-23","custom_fields":"{}","type":"primary","power_panel":5,"supply":"ac","tags":["tags","tags"],"voltage":-17680,"amperage":2624,"max_utilization":15,"name":"name","id":6,"status":"offline"}
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

async def test_dcim_power_outlet_templates_create(client):
    """Test case for dcim_power_outlet_templates_create

    
    """
    body = {"name":"name","feed_leg":"A","device_type":0,"id":6,"type":"iec-60320-c5","power_port":1}
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
                    ('type__n', 'type__n_example'),
                    ('feed_leg__n', 'feed_leg__n_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","feed_leg":"A","device_type":0,"id":6,"type":"iec-60320-c5","power_port":1}
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
    body = {"name":"name","feed_leg":"A","device_type":0,"id":6,"type":"iec-60320-c5","power_port":1}
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

async def test_dcim_power_outlets_create(client):
    """Test case for dcim_power_outlets_create

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","feed_leg":"A","id":6,"type":"iec-60320-c5","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":1,"tags":["tags","tags"]}
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
                    ('feed_leg', 'feed_leg_example'),
                    ('description', 'description_example'),
                    ('connection_status', 'connection_status_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
                    ('cabled', 'cabled_example'),
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
                    ('connection_status__n', 'connection_status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","feed_leg":"A","id":6,"type":"iec-60320-c5","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":1,"tags":["tags","tags"]}
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
    body = {"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","feed_leg":"A","id":6,"type":"iec-60320-c5","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"power_port":1,"tags":["tags","tags"]}
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

async def test_dcim_power_panels_create(client):
    """Test case for dcim_power_panels_create

    
    """
    body = {"site":5,"name":"name","powerfeed_count":6,"rack_group":1,"id":0}
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
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('rack_group_id', 'rack_group_id_example'),
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
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('rack_group_id__n', 'rack_group_id__n_example'),
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
    body = {"site":5,"name":"name","powerfeed_count":6,"rack_group":1,"id":0}
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
    body = {"site":5,"name":"name","powerfeed_count":6,"rack_group":1,"id":0}
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

async def test_dcim_power_port_templates_create(client):
    """Test case for dcim_power_port_templates_create

    
    """
    body = {"allocated_draw":2624,"name":"name","device_type":6,"id":1,"type":"iec-60320-c6","maximum_draw":19536}
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
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"allocated_draw":2624,"name":"name","device_type":6,"id":1,"type":"iec-60320-c6","maximum_draw":19536}
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
    body = {"allocated_draw":2624,"name":"name","device_type":6,"id":1,"type":"iec-60320-c6","maximum_draw":19536}
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

async def test_dcim_power_ports_create(client):
    """Test case for dcim_power_ports_create

    
    """
    body = {"allocated_draw":2624,"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":1,"type":"iec-60320-c6","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6,"maximum_draw":19536,"tags":["tags","tags"]}
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
                    ('maximum_draw', 'maximum_draw_example'),
                    ('allocated_draw', 'allocated_draw_example'),
                    ('description', 'description_example'),
                    ('connection_status', 'connection_status_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
                    ('cabled', 'cabled_example'),
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
                    ('connection_status__n', 'connection_status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('type__n', 'type__n_example'),
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
    body = {"allocated_draw":2624,"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":1,"type":"iec-60320-c6","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6,"maximum_draw":19536,"tags":["tags","tags"]}
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
    body = {"allocated_draw":2624,"connected_endpoint_type":"connected_endpoint_type","connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"name":"name","description":"description","id":1,"type":"iec-60320-c6","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":6,"maximum_draw":19536,"tags":["tags","tags"]}
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

async def test_dcim_rack_groups_create(client):
    """Test case for dcim_rack_groups_create

    
    """
    body = {"parent":6,"rack_count":1,"site":5,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/rack-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_groups_delete(client):
    """Test case for dcim_rack_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/rack-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_groups_list(client):
    """Test case for dcim_rack_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_groups_partial_update(client):
    """Test case for dcim_rack_groups_partial_update

    
    """
    body = {"parent":6,"rack_count":1,"site":5,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/rack-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_groups_read(client):
    """Test case for dcim_rack_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rack-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_groups_update(client):
    """Test case for dcim_rack_groups_update

    
    """
    body = {"parent":6,"rack_count":1,"site":5,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/rack-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rack_reservations_create(client):
    """Test case for dcim_rack_reservations_create

    
    """
    body = {"rack":6,"created":"2000-01-23","description":"description","id":0,"units":[19536,19536],"user":5,"tenant":1}
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
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('q', 'q_example'),
                    ('rack_id', 'rack_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
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
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('rack_id__n', 'rack_id__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('user__n', 'user__n_example'),
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
    body = {"rack":6,"created":"2000-01-23","description":"description","id":0,"units":[19536,19536],"user":5,"tenant":1}
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
    body = {"rack":6,"created":"2000-01-23","description":"description","id":0,"units":[19536,19536],"user":5,"tenant":1}
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

async def test_dcim_rack_roles_create(client):
    """Test case for dcim_rack_roles_create

    
    """
    body = {"rack_count":1,"color":"color","name":"name","description":"description","id":6,"slug":"slug"}
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
                    ('q', 'q_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
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
    body = {"rack_count":1,"color":"color","name":"name","description":"description","id":6,"slug":"slug"}
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
    body = {"rack_count":1,"color":"color","name":"name","description":"description","id":6,"slug":"slug"}
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

async def test_dcim_racks_create(client):
    """Test case for dcim_racks_create

    
    """
    body = {"role":7,"type":"2-post-frame","facility_id":"facility_id","outer_depth":19536,"id":1,"device_count":0,"tenant":3,"group":6,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":21,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"site":9,"serial":"serial","outer_width":18471,"name":"name","powerfeed_count":2,"width":4,"outer_unit":"mm","status":"reserved"}
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
                    ('type', 'type_example'),
                    ('width', 'width_example'),
                    ('u_height', 'u_height_example'),
                    ('desc_units', 'desc_units_example'),
                    ('outer_width', 'outer_width_example'),
                    ('outer_depth', 'outer_depth_example'),
                    ('outer_unit', 'outer_unit_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('status', 'status_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('serial', 'serial_example'),
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
                    ('facility_id__n', 'facility_id__n_example'),
                    ('facility_id__ic', 'facility_id__ic_example'),
                    ('facility_id__nic', 'facility_id__nic_example'),
                    ('facility_id__iew', 'facility_id__iew_example'),
                    ('facility_id__niew', 'facility_id__niew_example'),
                    ('facility_id__isw', 'facility_id__isw_example'),
                    ('facility_id__nisw', 'facility_id__nisw_example'),
                    ('facility_id__ie', 'facility_id__ie_example'),
                    ('facility_id__nie', 'facility_id__nie_example'),
                    ('asset_tag__n', 'asset_tag__n_example'),
                    ('asset_tag__ic', 'asset_tag__ic_example'),
                    ('asset_tag__nic', 'asset_tag__nic_example'),
                    ('asset_tag__iew', 'asset_tag__iew_example'),
                    ('asset_tag__niew', 'asset_tag__niew_example'),
                    ('asset_tag__isw', 'asset_tag__isw_example'),
                    ('asset_tag__nisw', 'asset_tag__nisw_example'),
                    ('asset_tag__ie', 'asset_tag__ie_example'),
                    ('asset_tag__nie', 'asset_tag__nie_example'),
                    ('type__n', 'type__n_example'),
                    ('width__n', 'width__n_example'),
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
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('status__n', 'status__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"role":7,"type":"2-post-frame","facility_id":"facility_id","outer_depth":19536,"id":1,"device_count":0,"tenant":3,"group":6,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":21,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"site":9,"serial":"serial","outer_width":18471,"name":"name","powerfeed_count":2,"width":4,"outer_unit":"mm","status":"reserved"}
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
    body = {"role":7,"type":"2-post-frame","facility_id":"facility_id","outer_depth":19536,"id":1,"device_count":0,"tenant":3,"group":6,"asset_tag":"asset_tag","desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":21,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"site":9,"serial":"serial","outer_width":18471,"name":"name","powerfeed_count":2,"width":4,"outer_unit":"mm","status":"reserved"}
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

async def test_dcim_rear_port_templates_create(client):
    """Test case for dcim_rear_port_templates_create

    
    """
    body = {"name":"name","device_type":0,"positions":10,"id":6,"type":"8p8c"}
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
                    ('positions', 'positions_example'),
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
                    ('type__n', 'type__n_example'),
                    ('positions__n', 'positions__n_example'),
                    ('positions__lte', 'positions__lte_example'),
                    ('positions__lt', 'positions__lt_example'),
                    ('positions__gte', 'positions__gte_example'),
                    ('positions__gt', 'positions__gt_example'),
                    ('devicetype_id__n', 'devicetype_id__n_example'),
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
    body = {"name":"name","device_type":0,"positions":10,"id":6,"type":"8p8c"}
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
    body = {"name":"name","device_type":0,"positions":10,"id":6,"type":"8p8c"}
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

async def test_dcim_rear_ports_create(client):
    """Test case for dcim_rear_ports_create

    
    """
    body = {"name":"name","description":"description","positions":10,"id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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
                    ('type', 'type_example'),
                    ('positions', 'positions_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('cabled', 'cabled_example'),
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
                    ('type__n', 'type__n_example'),
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
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"name":"name","description":"description","positions":10,"id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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

async def test_dcim_rear_ports_trace(client):
    """Test case for dcim_rear_ports_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/rear-ports/{id}/trace'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_rear_ports_update(client):
    """Test case for dcim_rear_ports_update

    
    """
    body = {"name":"name","description":"description","positions":10,"id":6,"type":"8p8c","cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"},"device":0,"tags":["tags","tags"]}
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

async def test_dcim_regions_create(client):
    """Test case for dcim_regions_create

    
    """
    body = {"parent":6,"site_count":1,"name":"name","description":"description","id":0,"slug":"slug"}
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
                    ('q', 'q_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
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
    body = {"parent":6,"site_count":1,"name":"name","description":"description","id":0,"slug":"slug"}
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
    body = {"parent":6,"site_count":1,"name":"name","description":"description","id":0,"slug":"slug"}
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

async def test_dcim_sites_create(client):
    """Test case for dcim_sites_create

    
    """
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","circuit_count":6,"latitude":"latitude","description":"description","contact_email":"contact_email","vlan_count":2,"rack_count":2,"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":9,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"name":"name","virtualmachine_count":3,"prefix_count":5,"region":7,"asn":343953089,"facility":"facility","status":"active"}
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

async def test_dcim_sites_graphs(client):
    """Test case for dcim_sites_graphs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/sites/{id}/graphs'.format(id=56),
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
                    ('asn', 'asn_example'),
                    ('latitude', 'latitude_example'),
                    ('longitude', 'longitude_example'),
                    ('contact_name', 'contact_name_example'),
                    ('contact_phone', 'contact_phone_example'),
                    ('contact_email', 'contact_email_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('status', 'status_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
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
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('facility__n', 'facility__n_example'),
                    ('facility__ic', 'facility__ic_example'),
                    ('facility__nic', 'facility__nic_example'),
                    ('facility__iew', 'facility__iew_example'),
                    ('facility__niew', 'facility__niew_example'),
                    ('facility__isw', 'facility__isw_example'),
                    ('facility__nisw', 'facility__nisw_example'),
                    ('facility__ie', 'facility__ie_example'),
                    ('facility__nie', 'facility__nie_example'),
                    ('asn__n', 'asn__n_example'),
                    ('asn__lte', 'asn__lte_example'),
                    ('asn__lt', 'asn__lt_example'),
                    ('asn__gte', 'asn__gte_example'),
                    ('asn__gt', 'asn__gt_example'),
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
                    ('contact_name__n', 'contact_name__n_example'),
                    ('contact_name__ic', 'contact_name__ic_example'),
                    ('contact_name__nic', 'contact_name__nic_example'),
                    ('contact_name__iew', 'contact_name__iew_example'),
                    ('contact_name__niew', 'contact_name__niew_example'),
                    ('contact_name__isw', 'contact_name__isw_example'),
                    ('contact_name__nisw', 'contact_name__nisw_example'),
                    ('contact_name__ie', 'contact_name__ie_example'),
                    ('contact_name__nie', 'contact_name__nie_example'),
                    ('contact_phone__n', 'contact_phone__n_example'),
                    ('contact_phone__ic', 'contact_phone__ic_example'),
                    ('contact_phone__nic', 'contact_phone__nic_example'),
                    ('contact_phone__iew', 'contact_phone__iew_example'),
                    ('contact_phone__niew', 'contact_phone__niew_example'),
                    ('contact_phone__isw', 'contact_phone__isw_example'),
                    ('contact_phone__nisw', 'contact_phone__nisw_example'),
                    ('contact_phone__ie', 'contact_phone__ie_example'),
                    ('contact_phone__nie', 'contact_phone__nie_example'),
                    ('contact_email__n', 'contact_email__n_example'),
                    ('contact_email__ic', 'contact_email__ic_example'),
                    ('contact_email__nic', 'contact_email__nic_example'),
                    ('contact_email__iew', 'contact_email__iew_example'),
                    ('contact_email__niew', 'contact_email__niew_example'),
                    ('contact_email__isw', 'contact_email__isw_example'),
                    ('contact_email__nisw', 'contact_email__nisw_example'),
                    ('contact_email__ie', 'contact_email__ie_example'),
                    ('contact_email__nie', 'contact_email__nie_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('status__n', 'status__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","circuit_count":6,"latitude":"latitude","description":"description","contact_email":"contact_email","vlan_count":2,"rack_count":2,"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":9,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"name":"name","virtualmachine_count":3,"prefix_count":5,"region":7,"asn":343953089,"facility":"facility","status":"active"}
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
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","circuit_count":6,"latitude":"latitude","description":"description","contact_email":"contact_email","vlan_count":2,"rack_count":2,"id":5,"shipping_address":"shipping_address","device_count":1,"slug":"slug","tenant":9,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"name":"name","virtualmachine_count":3,"prefix_count":5,"region":7,"asn":343953089,"facility":"facility","status":"active"}
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

async def test_dcim_virtual_chassis_create(client):
    """Test case for dcim_virtual_chassis_create

    
    """
    body = {"domain":"domain","id":0,"member_count":1,"master":6,"tags":["tags","tags"]}
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
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('tag', 'tag_example'),
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
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('tag__n', 'tag__n_example'),
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
    body = {"domain":"domain","id":0,"member_count":1,"master":6,"tags":["tags","tags"]}
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
    body = {"domain":"domain","id":0,"member_count":1,"master":6,"tags":["tags","tags"]}
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

