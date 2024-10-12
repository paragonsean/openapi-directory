# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_cycle_device_switch_ports_1(client):
    """Test case for cycle_device_switch_ports_1

    Cycle a set of switch ports
    """
    body = openapi_server.CycleDeviceSwitchPortsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/switch/ports/cycle'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_port_1(client):
    """Test case for get_device_switch_port_1

    Return a switch port
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/{port_id}'.format(serial='serial_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports_1(client):
    """Test case for get_device_switch_ports_1

    List the switch ports for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports_statuses_1(client):
    """Test case for get_device_switch_ports_statuses_1

    Return the status for all the ports of a switch
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/statuses'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports_statuses_packets_1(client):
    """Test case for get_device_switch_ports_statuses_packets_1

    Return the packet counters for all the ports of a switch
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/statuses/packets'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_port_1(client):
    """Test case for get_network_appliance_port_1

    Return per-port VLAN settings for a single MX port.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/ports/{port_id}'.format(network_id='network_id_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_ports_1(client):
    """Test case for get_network_appliance_ports_1

    List per-port VLAN settings for all ports of a MX.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/ports'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_port_3(client):
    """Test case for get_organization_config_template_switch_profile_port_3

    Return a switch profile port
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_ports_3(client):
    """Test case for get_organization_config_template_switch_profile_ports_3

    Return all the ports of a switch profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_switch_ports_by_switch_1(client):
    """Test case for get_organization_switch_ports_by_switch_1

    List the switchports in an organization by switch
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('portProfileIds', ['port_profile_ids_example']),
                    ('name', 'name_example'),
                    ('mac', 'mac_example'),
                    ('macs', ['macs_example']),
                    ('serial', 'serial_example'),
                    ('serials', ['serials_example']),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/switch/ports/bySwitch'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_port_1(client):
    """Test case for update_device_switch_port_1

    Update a switch port
    """
    body = openapi_server.UpdateDeviceSwitchPortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/ports/{port_id}'.format(serial='serial_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_port_1(client):
    """Test case for update_network_appliance_port_1

    Update the per-port VLAN settings for a single MX port.
    """
    body = openapi_server.UpdateNetworkAppliancePortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/ports/{port_id}'.format(network_id='network_id_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_config_template_switch_profile_port_3(client):
    """Test case for update_organization_config_template_switch_profile_port_3

    Update a switch profile port
    """
    body = openapi_server.UpdateOrganizationConfigTemplateSwitchProfilePortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

