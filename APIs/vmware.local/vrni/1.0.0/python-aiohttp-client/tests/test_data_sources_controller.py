# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.arista_switch_data_source import AristaSwitchDataSource
from openapi_server.models.arista_switch_data_source_request import AristaSwitchDataSourceRequest
from openapi_server.models.brocade_switch_data_source import BrocadeSwitchDataSource
from openapi_server.models.brocade_switch_data_source_request import BrocadeSwitchDataSourceRequest
from openapi_server.models.checkpoint_firewall_data_source import CheckpointFirewallDataSource
from openapi_server.models.checkpoint_firewall_data_source_request import CheckpointFirewallDataSourceRequest
from openapi_server.models.cisco_switch_data_source import CiscoSwitchDataSource
from openapi_server.models.cisco_switch_data_source_request import CiscoSwitchDataSourceRequest
from openapi_server.models.data_source_list_response import DataSourceListResponse
from openapi_server.models.dell_switch_data_source import DellSwitchDataSource
from openapi_server.models.dell_switch_data_source_request import DellSwitchDataSourceRequest
from openapi_server.models.hp_one_view_manager_data_source import HPOneViewManagerDataSource
from openapi_server.models.hp_one_view_manager_data_source_request import HPOneViewManagerDataSourceRequest
from openapi_server.models.hpvc_manager_data_source import HPVCManagerDataSource
from openapi_server.models.hpvc_manager_data_source_request import HPVCManagerDataSourceRequest
from openapi_server.models.juniper_switch_data_source import JuniperSwitchDataSource
from openapi_server.models.juniper_switch_data_source_request import JuniperSwitchDataSourceRequest
from openapi_server.models.nsx_controller_data_collection import NSXControllerDataCollection
from openapi_server.models.nsxv_manager_data_source import NSXVManagerDataSource
from openapi_server.models.nsxv_manager_data_source_request import NSXVManagerDataSourceRequest
from openapi_server.models.pan_firewall_data_source import PanFirewallDataSource
from openapi_server.models.pan_firewall_data_source_request import PanFirewallDataSourceRequest
from openapi_server.models.snmp_config import SNMPConfig
from openapi_server.models.ucs_manager_data_source import UCSManagerDataSource
from openapi_server.models.ucs_manager_data_source_request import UCSManagerDataSourceRequest
from openapi_server.models.v_center_data_source import VCenterDataSource
from openapi_server.models.v_center_data_source_request import VCenterDataSourceRequest


pytestmark = pytest.mark.asyncio

async def test_add_arista_switch(client):
    """Test case for add_arista_switch

    Create an arista switch data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/arista-switches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_brocade_switch(client):
    """Test case for add_brocade_switch

    Create a brocade switch data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/brocade-switches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_checkpoint_firewall(client):
    """Test case for add_checkpoint_firewall

    Create a checkpoint firewall
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/checkpoint-firewalls',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cisco_switch(client):
    """Test case for add_cisco_switch

    Create a cisco switch data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True,"switch_type":"CATALYST_3000"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/cisco-switches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_dell_switch(client):
    """Test case for add_dell_switch

    Create a dell switch data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True,"switch_type":"FORCE_10_MXL_10"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/dell-switches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_hpov_manager(client):
    """Test case for add_hpov_manager

    Create a hp oneview manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpov-managers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_hpvc_manager(client):
    """Test case for add_hpvc_manager

    Create a hpvc manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpvc-managers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_juniper_switch(client):
    """Test case for add_juniper_switch

    Add a juniper switch as data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/juniper-switches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_nsxv_manager_datasource(client):
    """Test case for add_nsxv_manager_datasource

    Create a nsx-v manager data source
    """
    body = {"notes":"notes","vcenter_id":"vcenter_id","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","ipfix_enabled":False,"nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True,"central_cli_enabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/nsxv-managers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_panorama_firewall(client):
    """Test case for add_panorama_firewall

    Create panorama firewall data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/panorama-firewalls',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_ucs_manager(client):
    """Test case for add_ucs_manager

    Create an ucs manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/ucs-managers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_vcenter_datasource(client):
    """Test case for add_vcenter_datasource

    Create a vCenter data source
    """
    body = {"notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/vcenters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_arista_switch(client):
    """Test case for delete_arista_switch

    Delete an arista switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/arista-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_brocade_switch(client):
    """Test case for delete_brocade_switch

    Delete a brocade switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/brocade-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_checkpoint_firewall(client):
    """Test case for delete_checkpoint_firewall

    Delete a checkpoint firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/checkpoint-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cisco_switch(client):
    """Test case for delete_cisco_switch

    Delete a cisco switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/cisco-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dell_switch(client):
    """Test case for delete_dell_switch

    Delete a dell switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/dell-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hpov_manager(client):
    """Test case for delete_hpov_manager

    Delete a hp oneview data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/hpov-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hpvc_manager(client):
    """Test case for delete_hpvc_manager

    Delete a hpvc manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/hpvc-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_juniper_switch(client):
    """Test case for delete_juniper_switch

    Delete a juniper switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/juniper-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_nsxv_manager(client):
    """Test case for delete_nsxv_manager

    Delete a nsx-v manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/nsxv-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_panorama_firewall(client):
    """Test case for delete_panorama_firewall

    Delete a panorama firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/panorama-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ucs_manager(client):
    """Test case for delete_ucs_manager

    Delete an ucs manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/ucs-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vcenter(client):
    """Test case for delete_vcenter

    Delete a vCenter data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/data-sources/vcenters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_arista_switch(client):
    """Test case for disable_arista_switch

    Disable an arista switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/arista-switches/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_brocade_switch(client):
    """Test case for disable_brocade_switch

    Disable a brocade switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/brocade-switches/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_checkpoint_firewall(client):
    """Test case for disable_checkpoint_firewall

    Disable a checkpoint firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/checkpoint-firewalls/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_cisco_switch(client):
    """Test case for disable_cisco_switch

    Disable a cisco switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/cisco-switches/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_dell_switch(client):
    """Test case for disable_dell_switch

    Disable a dell switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/dell-switches/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_hpov_manager(client):
    """Test case for disable_hpov_manager

    Disable a hp oneview data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpov-managers/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_hpvc_manager(client):
    """Test case for disable_hpvc_manager

    Disable a hpvc manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpvc-managers/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_juniper_switch(client):
    """Test case for disable_juniper_switch

    Disable a juniper switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/juniper-switches/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_nsxv_manager(client):
    """Test case for disable_nsxv_manager

    Disable a nsx-v manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/nsxv-managers/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_panorama_firewall(client):
    """Test case for disable_panorama_firewall

    Disable a panorama firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/panorama-firewalls/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_ucs_manager(client):
    """Test case for disable_ucs_manager

    Disable an ucs manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/ucs-managers/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_vcenter(client):
    """Test case for disable_vcenter

    Disable a vCenter data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/vcenters/{id}/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_arista_switch(client):
    """Test case for enable_arista_switch

    Enable an arista switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/arista-switches/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_brocade_switch(client):
    """Test case for enable_brocade_switch

    Enable a brocade switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/brocade-switches/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_checkpoint_firewall(client):
    """Test case for enable_checkpoint_firewall

    Enable a checkpoint firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/checkpoint-firewalls/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_cisco_switch(client):
    """Test case for enable_cisco_switch

    Enable a cisco switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/cisco-switches/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_dell_switch(client):
    """Test case for enable_dell_switch

    Enable a dell switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/dell-switches/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_hpov_manager(client):
    """Test case for enable_hpov_manager

    Enable a hp oneview data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpov-managers/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_hpvc_manager(client):
    """Test case for enable_hpvc_manager

    Enable a hpvc manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/hpvc-managers/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_juniper_switch(client):
    """Test case for enable_juniper_switch

    Enable a juniper switch data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/juniper-switches/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_nsxv_manager(client):
    """Test case for enable_nsxv_manager

    Enable a nsx-v manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/nsxv-managers/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_panorama_firewall(client):
    """Test case for enable_panorama_firewall

    Enable a panorama firewall data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/panorama-firewalls/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_ucs_manager(client):
    """Test case for enable_ucs_manager

    Enable an ucs manager data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/ucs-managers/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_vcenter(client):
    """Test case for enable_vcenter

    Enable a vCenter data source
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/data-sources/vcenters/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_arista_switch(client):
    """Test case for get_arista_switch

    Show arista switch data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/arista-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_arista_switch_snmp_config(client):
    """Test case for get_arista_switch_snmp_config

    Show snmp config for arista switch data source
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/arista-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_brocade_switch(client):
    """Test case for get_brocade_switch

    Show brocade switch data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/brocade-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_brocade_switch_snmp_config(client):
    """Test case for get_brocade_switch_snmp_config

    Show snmp config for brocade switch data source
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/brocade-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checkpoint_firewall(client):
    """Test case for get_checkpoint_firewall

    Show checkpoint firewall data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/checkpoint-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cisco_switch(client):
    """Test case for get_cisco_switch

    Show cisco switch data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/cisco-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cisco_switch_snmp_config(client):
    """Test case for get_cisco_switch_snmp_config

    Show snmp config for cisco switch data source
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/cisco-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dell_switch(client):
    """Test case for get_dell_switch

    Show dell switch data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/dell-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dell_switch_snmp_config(client):
    """Test case for get_dell_switch_snmp_config

    Show snmp config for dell switch data source
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/dell-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hpov_manager(client):
    """Test case for get_hpov_manager

    Show hp oneview data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/hpov-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hpvc_manager(client):
    """Test case for get_hpvc_manager

    Show hpvc data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/hpvc-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_juniper_switch(client):
    """Test case for get_juniper_switch

    Show juniper switch data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/juniper-switches/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_juniper_switch_snmp_config(client):
    """Test case for get_juniper_switch_snmp_config

    Show snmp config for juniper switch data source
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/juniper-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nsxv_controller_cluster(client):
    """Test case for get_nsxv_controller_cluster

    Show nsx controller-cluster details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/nsxv-managers/{id}/controller-cluster'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nsxv_manager(client):
    """Test case for get_nsxv_manager

    Show nsx-v manager data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/nsxv-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_panorama_firewall(client):
    """Test case for get_panorama_firewall

    Show panorama firewall data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/panorama-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ucs_manager(client):
    """Test case for get_ucs_manager

    Show ucs manager data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/ucs-managers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ucs_snmp_config(client):
    """Test case for get_ucs_snmp_config

    Show snmp config for ucs fabric interconnects
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/ucs-managers/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcenter(client):
    """Test case for get_vcenter

    Show vCenter data source details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/vcenters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_arista_switches(client):
    """Test case for list_arista_switches

    List arista switch data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/arista-switches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_brocade_switches(client):
    """Test case for list_brocade_switches

    List brocade switch data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/brocade-switches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_checkpoint_firewalls(client):
    """Test case for list_checkpoint_firewalls

    List checkpoint firewall data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/checkpoint-firewalls',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cisco_switches(client):
    """Test case for list_cisco_switches

    List cisco switch data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/cisco-switches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_dell_switches(client):
    """Test case for list_dell_switches

    List dell switch data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/dell-switches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hpov_managers(client):
    """Test case for list_hpov_managers

    List hp oneview manager data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/hpov-managers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hpvc_managers(client):
    """Test case for list_hpvc_managers

    List hpvc manager data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/hpvc-managers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_juniper_switches(client):
    """Test case for list_juniper_switches

    List juniper switch data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/juniper-switches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_nsxv_managers(client):
    """Test case for list_nsxv_managers

    List nsx-v manager data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/nsxv-managers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_panorama_firewalls(client):
    """Test case for list_panorama_firewalls

    List panorama firewall data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/panorama-firewalls',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ucs_managers(client):
    """Test case for list_ucs_managers

    List ucs manager data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/ucs-managers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vcenters(client):
    """Test case for list_vcenters

    List vCenter data sources
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/data-sources/vcenters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_arista_switch(client):
    """Test case for update_arista_switch

    Update an arista switch data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/arista-switches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_arista_switch_snmp_config(client):
    """Test case for update_arista_switch_snmp_config

    Update snmp config for arista switch data source
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/arista-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_brocade_switch(client):
    """Test case for update_brocade_switch

    Update a brocade switch data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/brocade-switches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_brocade_switch_snmp_config(client):
    """Test case for update_brocade_switch_snmp_config

    Update snmp config for brocade switch data source
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/brocade-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_checkpoint_firewall(client):
    """Test case for update_checkpoint_firewall

    Update a checkpoint firewall data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/checkpoint-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cisco_switch(client):
    """Test case for update_cisco_switch

    Update a cisco switch data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True,"switch_type":"CATALYST_3000"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/cisco-switches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cisco_switch_snmp_config(client):
    """Test case for update_cisco_switch_snmp_config

    Update snmp config for cisco switch data source
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/cisco-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dell_switch(client):
    """Test case for update_dell_switch

    Update a dell switch data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True,"switch_type":"FORCE_10_MXL_10"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/dell-switches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dell_switch_snmp_config(client):
    """Test case for update_dell_switch_snmp_config

    Update snmp config for dell switch data source
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/dell-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_hpov_manager(client):
    """Test case for update_hpov_manager

    Update a hp oneview data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/hpov-managers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_hpvc_manager(client):
    """Test case for update_hpvc_manager

    Update a hpvc manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/hpvc-managers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_juniper_switch(client):
    """Test case for update_juniper_switch

    Update a juniper switch data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/juniper-switches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_juniper_switch_snmp_config(client):
    """Test case for update_juniper_switch_snmp_config

    Update snmp config for a juniper switch data source
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/juniper-switches/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_nsxv_controller_cluster(client):
    """Test case for update_nsxv_controller_cluster

    Update nsx controller-cluster details
    """
    body = {"controller_password":"controller_password","enabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/nsxv-managers/{id}/controller-cluster'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_nsxv_manager(client):
    """Test case for update_nsxv_manager

    Update a nsx-v manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","vcenter_id":"vcenter_id","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","ipfix_enabled":False,"nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True,"central_cli_enabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/nsxv-managers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_panorama_firewall(client):
    """Test case for update_panorama_firewall

    Update a panorama firewall data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/panorama-firewalls/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ucs_manager(client):
    """Test case for update_ucs_manager

    Update an ucs manager data source
    """
    body = {"entity_type":"CiscoSwitchDataSource","notes":"notes","fqdn":"your.domain.com","credentials":{"password":"password","username":"username"},"ip":"192.168.10.1","nickname":"vc1","proxy_id":"1000:104:12313412","entity_id":"entity_id","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/ucs-managers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ucs_snmp_config(client):
    """Test case for update_ucs_snmp_config

    Update snmp config for ucs fabric interconnects
    """
    body = {"config_snmp_2c":{"community_string":"community_string"},"snmp_enabled":False,"snmp_version":"v2c","config_snmp_3":{"authentication_password":"authentication_password","privacy_type":"AES","context_name":"context_name","privacy_password":"privacy_password","authentication_type":"NO_AUTH","username":"username"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/ucs-managers/{id}/snmp-config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vcenter(client):
    """Test case for update_vcenter

    Update a vCenter data source.
    """
    body = {"credentials":{"password":"thePassword","username":"admin@vsphere.local"},"enabled":True,"entity_type":"VCenterDataSource","fqdn":"go.vc.org","id":"1000:33:12890123","ip":"192.168.10.1","nickname":"vc1","notes":"VC 1","proxy_id":"1000:104:12313412"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/data-sources/vcenters/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

