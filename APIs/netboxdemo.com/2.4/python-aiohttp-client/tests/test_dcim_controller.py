# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_dcim_choices_list(client):
    """Test case for dcim_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_choices_read(client):
    """Test case for dcim_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/_choices/{id}'.format(id='id_example'),
        headers=headers,
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
                    ('device', 'device_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    params = [('name', 'name_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"cs_port":0,"connection_status":True,"name":"name","id":1,"device":6,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
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
    body = {"cs_port":0,"connection_status":True,"name":"name","id":1,"device":6,"tags":["tags","tags"]}
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

async def test_dcim_console_ports_update(client):
    """Test case for dcim_console_ports_update

    
    """
    body = {"cs_port":0,"connection_status":True,"name":"name","id":1,"device":6,"tags":["tags","tags"]}
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
    body = {"name":"name","device_type":0,"id":6}
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
    params = [('name', 'name_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"connected_console":"connected_console","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
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
    body = {"connected_console":"connected_console","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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

async def test_dcim_console_server_ports_update(client):
    """Test case for dcim_console_server_ports_update

    
    """
    body = {"connected_console":"connected_console","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"installed_device":1,"name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
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
    body = {"installed_device":1,"name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    body = {"installed_device":1,"name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    body = {"vm_role":True,"color":"color","name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
                    ('vm_role', 'vm_role_example'),
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
    body = {"vm_role":True,"color":"color","name":"name","id":6,"slug":"slug"}
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
    body = {"vm_role":True,"color":"color","name":"name","id":6,"slug":"slug"}
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
    body = {"is_pdu":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":18471,"is_console_server":True,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"is_network_device":True,"manufacturer":5,"tags":["tags","tags"],"subdevice_role":True,"part_number":"part_number","model":"model","id":0,"interface_ordering":1,"instance_count":6,"slug":"slug"}
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
    params = [('model', 'model_example'),
                    ('slug', 'slug_example'),
                    ('part_number', 'part_number_example'),
                    ('u_height', 3.4),
                    ('is_full_depth', 'is_full_depth_example'),
                    ('is_console_server', 'is_console_server_example'),
                    ('is_pdu', 'is_pdu_example'),
                    ('is_network_device', 'is_network_device_example'),
                    ('subdevice_role', 'subdevice_role_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('tag', 'tag_example'),
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
    body = {"is_pdu":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":18471,"is_console_server":True,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"is_network_device":True,"manufacturer":5,"tags":["tags","tags"],"subdevice_role":True,"part_number":"part_number","model":"model","id":0,"interface_ordering":1,"instance_count":6,"slug":"slug"}
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
    body = {"is_pdu":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","u_height":18471,"is_console_server":True,"created":"2000-01-23","custom_fields":"{}","is_full_depth":True,"is_network_device":True,"manufacturer":5,"tags":["tags","tags"],"subdevice_role":True,"part_number":"part_number","model":"model","id":0,"interface_ordering":1,"instance_count":6,"slug":"slug"}
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
    body = {"cluster":0,"primary_ip":"primary_ip","vc_priority":37,"device_type":1,"platform":2,"id":5,"tenant":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":5,"site":4,"vc_position":26,"local_context_data":"local_context_data","parent_device":"parent_device","serial":"serial","device_role":6,"name":"name","virtual_chassis":6,"position":23138,"primary_ip6":3,"primary_ip4":9,"status":7}
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
    params = [('serial', 'serial_example'),
                    ('position', 3.4),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('device_type_id', 'device_type_id_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('name', 'name_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('region_id', 3.4),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('rack_group_id', 'rack_group_id_example'),
                    ('rack_id', 'rack_id_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('model', 'model_example'),
                    ('status', 'status_example'),
                    ('is_full_depth', 'is_full_depth_example'),
                    ('is_console_server', 'is_console_server_example'),
                    ('is_pdu', 'is_pdu_example'),
                    ('is_network_device', 'is_network_device_example'),
                    ('mac_address', 'mac_address_example'),
                    ('has_primary_ip', 'has_primary_ip_example'),
                    ('virtual_chassis_id', 'virtual_chassis_id_example'),
                    ('tag', 'tag_example'),
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
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/devices/{id}/napalm'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_devices_partial_update(client):
    """Test case for dcim_devices_partial_update

    
    """
    body = {"cluster":0,"primary_ip":"primary_ip","vc_priority":37,"device_type":1,"platform":2,"id":5,"tenant":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":5,"site":4,"vc_position":26,"local_context_data":"local_context_data","parent_device":"parent_device","serial":"serial","device_role":6,"name":"name","virtual_chassis":6,"position":23138,"primary_ip6":3,"primary_ip4":9,"status":7}
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
    body = {"cluster":0,"primary_ip":"primary_ip","vc_priority":37,"device_type":1,"platform":2,"id":5,"tenant":1,"asset_tag":"asset_tag","last_updated":"2000-01-23T04:56:07.000+00:00","rack":2,"comments":"comments","created":"2000-01-23","custom_fields":"{}","display_name":"display_name","tags":["tags","tags"],"face":5,"site":4,"vc_position":26,"local_context_data":"local_context_data","parent_device":"parent_device","serial":"serial","device_role":6,"name":"name","virtual_chassis":6,"position":23138,"primary_ip6":3,"primary_ip4":9,"status":7}
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

async def test_dcim_interface_connections_create(client):
    """Test case for dcim_interface_connections_create

    
    """
    body = {"interface_b":1,"interface_a":6,"connection_status":True,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dcim/interface-connections/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_connections_delete(client):
    """Test case for dcim_interface_connections_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dcim/interface-connections/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_connections_list(client):
    """Test case for dcim_interface_connections_list

    
    """
    params = [('connection_status', 'connection_status_example'),
                    ('site', 'site_example'),
                    ('device', 'device_example'),
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

async def test_dcim_interface_connections_partial_update(client):
    """Test case for dcim_interface_connections_partial_update

    
    """
    body = {"interface_b":1,"interface_a":6,"connection_status":True,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dcim/interface-connections/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_connections_read(client):
    """Test case for dcim_interface_connections_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/interface-connections/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_connections_update(client):
    """Test case for dcim_interface_connections_update

    
    """
    body = {"interface_b":1,"interface_a":6,"connection_status":True,"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dcim/interface-connections/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_interface_templates_create(client):
    """Test case for dcim_interface_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":1,"form_factor":6,"mgmt_only":True}
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
    params = [('name', 'name_example'),
                    ('form_factor', 'form_factor_example'),
                    ('mgmt_only', 'mgmt_only_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"name":"name","device_type":0,"id":1,"form_factor":6,"mgmt_only":True}
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
    body = {"name":"name","device_type":0,"id":1,"form_factor":6,"mgmt_only":True}
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
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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
    params = [('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 3.4),
                    ('mgmt_only', 'mgmt_only_example'),
                    ('device', 'device_example'),
                    ('device_id', 3.4),
                    ('type', 'type_example'),
                    ('lag_id', 'lag_id_example'),
                    ('mac_address', 'mac_address_example'),
                    ('tag', 'tag_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan', 'vlan_example'),
                    ('form_factor', 'form_factor_example'),
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
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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

async def test_dcim_interfaces_update(client):
    """Test case for dcim_interfaces_update

    
    """
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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
    params = [('name', 'name_example'),
                    ('part_id', 'part_id_example'),
                    ('serial', 'serial_example'),
                    ('asset_tag', 'asset_tag_example'),
                    ('discovered', 'discovered_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('q', 'q_example'),
                    ('parent_id', 'parent_id_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","rpc_client":"juniper-junos","id":0,"slug":"slug","manufacturer":6}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('manufacturer_id', 'manufacturer_id_example'),
                    ('manufacturer', 'manufacturer_example'),
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
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","rpc_client":"juniper-junos","id":0,"slug":"slug","manufacturer":6}
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
    body = {"napalm_args":"napalm_args","name":"name","napalm_driver":"napalm_driver","rpc_client":"juniper-junos","id":0,"slug":"slug","manufacturer":6}
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
                    ('device', 'device_example'),
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

async def test_dcim_power_outlet_templates_create(client):
    """Test case for dcim_power_outlet_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6}
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
    params = [('name', 'name_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"connected_port":"connected_port","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
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
    body = {"connected_port":"connected_port","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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

async def test_dcim_power_outlets_update(client):
    """Test case for dcim_power_outlets_update

    
    """
    body = {"connected_port":"connected_port","name":"name","id":6,"device":0,"tags":["tags","tags"]}
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

async def test_dcim_power_port_templates_create(client):
    """Test case for dcim_power_port_templates_create

    
    """
    body = {"name":"name","device_type":0,"id":6}
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
    params = [('name', 'name_example'),
                    ('devicetype_id', 'devicetype_id_example'),
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"name":"name","device_type":0,"id":6}
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
    body = {"connection_status":True,"name":"name","id":6,"power_outlet":1,"device":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
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
    body = {"connection_status":True,"name":"name","id":6,"power_outlet":1,"device":0,"tags":["tags","tags"]}
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

async def test_dcim_power_ports_update(client):
    """Test case for dcim_power_ports_update

    
    """
    body = {"connection_status":True,"name":"name","id":6,"power_outlet":1,"device":0,"tags":["tags","tags"]}
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    params = [('site_id', 'site_id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('q', 'q_example'),
                    ('site', 'site_example'),
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    params = [('created', 'created_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('rack_id', 'rack_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('user_id', 'user_id_example'),
                    ('user', 'user_example'),
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
    body = {"color":"color","name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
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
    body = {"color":"color","name":"name","id":6,"slug":"slug"}
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
    body = {"color":"color","name":"name","id":6,"slug":"slug"}
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
    body = {"desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"u_height":70,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","type":2,"tags":["tags","tags"],"site":5,"serial":"serial","name":"name","width":9,"facility_id":"facility_id","id":6,"tenant":5,"group":0}
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

async def test_dcim_racks_list(client):
    """Test case for dcim_racks_list

    
    """
    params = [('name', 'name_example'),
                    ('serial', 'serial_example'),
                    ('type', 'type_example'),
                    ('width', 'width_example'),
                    ('u_height', 3.4),
                    ('desc_units', 'desc_units_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('facility_id', 'facility_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('tag', 'tag_example'),
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
    body = {"desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"u_height":70,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","type":2,"tags":["tags","tags"],"site":5,"serial":"serial","name":"name","width":9,"facility_id":"facility_id","id":6,"tenant":5,"group":0}
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

async def test_dcim_racks_units(client):
    """Test case for dcim_racks_units

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dcim/racks/{id}/units'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dcim_racks_update(client):
    """Test case for dcim_racks_update

    
    """
    body = {"desc_units":True,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"u_height":70,"created":"2000-01-23","custom_fields":"{}","display_name":"display_name","type":2,"tags":["tags","tags"],"site":5,"serial":"serial","name":"name","width":9,"facility_id":"facility_id","id":6,"tenant":5,"group":0}
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

async def test_dcim_regions_create(client):
    """Test case for dcim_regions_create

    
    """
    body = {"parent":6,"name":"name","id":0,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('q', 'q_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
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
    body = {"parent":6,"name":"name","id":0,"slug":"slug"}
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
    body = {"parent":6,"name":"name","id":0,"slug":"slug"}
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
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","latitude":"latitude","description":"description","contact_email":"contact_email","count_prefixes":5,"id":7,"shipping_address":"shipping_address","slug":"slug","tenant":2,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"count_circuits":6,"count_vlans":2,"count_racks":5,"name":"name","count_devices":1,"region":9,"asn":343953089,"facility":"facility","status":3}
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
    params = [('q', 'q_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('facility', 'facility_example'),
                    ('asn', 3.4),
                    ('contact_name', 'contact_name_example'),
                    ('contact_phone', 'contact_phone_example'),
                    ('contact_email', 'contact_email_example'),
                    ('id__in', 'id__in_example'),
                    ('status', 'status_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('tag', 'tag_example'),
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
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","latitude":"latitude","description":"description","contact_email":"contact_email","count_prefixes":5,"id":7,"shipping_address":"shipping_address","slug":"slug","tenant":2,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"count_circuits":6,"count_vlans":2,"count_racks":5,"name":"name","count_devices":1,"region":9,"asn":343953089,"facility":"facility","status":3}
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
    body = {"physical_address":"physical_address","contact_phone":"contact_phone","latitude":"latitude","description":"description","contact_email":"contact_email","count_prefixes":5,"id":7,"shipping_address":"shipping_address","slug":"slug","tenant":2,"longitude":"longitude","contact_name":"contact_name","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","time_zone":"time_zone","tags":["tags","tags"],"count_circuits":6,"count_vlans":2,"count_racks":5,"name":"name","count_devices":1,"region":9,"asn":343953089,"facility":"facility","status":3}
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
    body = {"domain":"domain","id":0,"master":6,"tags":["tags","tags"]}
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
    params = [('limit', 56),
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
    body = {"domain":"domain","id":0,"master":6,"tags":["tags","tags"]}
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
    body = {"domain":"domain","id":0,"master":6,"tags":["tags","tags"]}
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

