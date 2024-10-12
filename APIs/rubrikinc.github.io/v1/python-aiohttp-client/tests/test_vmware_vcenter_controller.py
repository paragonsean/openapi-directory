# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.hot_add_bandwidth_info import HotAddBandwidthInfo
from openapi_server.models.hot_add_network_config_with_id import HotAddNetworkConfigWithId
from openapi_server.models.hot_add_network_config_with_name import HotAddNetworkConfigWithName
from openapi_server.models.hot_add_proxies_needed_info import HotAddProxiesNeededInfo
from openapi_server.models.hot_add_proxy_vm_info_list_response import HotAddProxyVmInfoListResponse
from openapi_server.models.network_info_list_response import NetworkInfoListResponse
from openapi_server.models.vcenter_config import VcenterConfig
from openapi_server.models.vcenter_detail import VcenterDetail
from openapi_server.models.vcenter_patch import VcenterPatch
from openapi_server.models.vcenter_summary import VcenterSummary
from openapi_server.models.vcenter_summary_list_response import VcenterSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_refresh(client):
    """Test case for create_refresh

    Refresh vCenter Server metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vcenter/{id}/refresh'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_refresh_vm_v1(client):
    """Test case for create_refresh_vm_v1

    Refresh single virtual machine metadata in a vcenter
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vcenter/{id}/refresh_vm'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vcenter(client):
    """Test case for create_vcenter

    Add vCenter Server
    """
    body = {"hostname":"hostname","password":"password","computeVisibilityFilter":[{"hostGroupFilter":["hostGroupFilter","hostGroupFilter"],"id":"id"},{"hostGroupFilter":["hostGroupFilter","hostGroupFilter"],"id":"id"}],"conflictResolutionAuthz":"AllowAutoConflictResolution","caCerts":"caCerts","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vcenter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vcenter(client):
    """Test case for delete_vcenter

    Remove vCenter Server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vmware/vcenter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hot_add_bandwidth(client):
    """Test case for get_hot_add_bandwidth

    Get the ingest and export bandwidth limits for HotAdd with the vCenter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/{id}/hotadd/bandwidth'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hot_add_network(client):
    """Test case for get_hot_add_network

    Retrieve the user-configured network for HotAdd operations
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/{id}/hotadd/network'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_networks(client):
    """Test case for get_networks

    Get the user-configured networks in the vCenter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/{id}/networks'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_num_proxies_needed(client):
    """Test case for get_num_proxies_needed

    Get the number of HotAdd proxies needed for the vCenter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/{id}/hotadd/needed'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcenter(client):
    """Test case for get_vcenter

    Get the details of a vCenter Server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcenter_async_request_status(client):
    """Test case for get_vcenter_async_request_status

    Get vCenter Server async request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_vcenter(client):
    """Test case for patch_vcenter

    Update the SLA Domain for a vCenter Server
    """
    body = {"configuredSlaDomainId":"configuredSlaDomainId","caCerts":"caCerts"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/vcenter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_hot_add_proxy_vm(client):
    """Test case for query_hot_add_proxy_vm

    Get a list of HotAdd proxy virtual machines
    """
    params = [('name', 'name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter/hotadd/vm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vcenter(client):
    """Test case for query_vcenter

    Get list of vCenters
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('snappable_status', 'snappable_status_example'),
                    ('ignore_connection_status', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vcenter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_hot_add_bandwidth(client):
    """Test case for set_hot_add_bandwidth

    Set the ingest and export bandwidth limits for HotAdd with the vCenter
    """
    body = {"exportLimit":0,"ingestLimit":6}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vcenter/{id}/hotadd/bandwidth'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_hot_add_network(client):
    """Test case for set_hot_add_network

    Set the user-configured network for HotAdd backup and recovery
    """
    body = {"network_id":"network_id","static_ip_info":{"ip_addresses":["ip_addresses","ip_addresses"],"subnet_mask":"subnet_mask","gateway":"gateway","dns_servers":["dns_servers","dns_servers"]}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vcenter/{id}/hotadd/network'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vcenter(client):
    """Test case for update_vcenter

    Update vCenter Server
    """
    body = {"hostname":"hostname","password":"password","computeVisibilityFilter":[{"hostGroupFilter":["hostGroupFilter","hostGroupFilter"],"id":"id"},{"hostGroupFilter":["hostGroupFilter","hostGroupFilter"],"id":"id"}],"conflictResolutionAuthz":"AllowAutoConflictResolution","caCerts":"caCerts","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/vmware/vcenter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

