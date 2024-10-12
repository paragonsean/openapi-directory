# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vmware_host_datastore_detail import VmwareHostDatastoreDetail
from openapi_server.models.vmware_host_detail import VmwareHostDetail
from openapi_server.models.vmware_host_summary_list_response import VmwareHostSummaryListResponse
from openapi_server.models.vmware_host_update import VmwareHostUpdate


pytestmark = pytest.mark.asyncio

async def test_get_vmware_host(client):
    """Test case for get_vmware_host

    Get details of a ESXi hypervisor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/host/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_host_datastore(client):
    """Test case for get_vmware_host_datastore

    Get details of datastores in a ESXi hypervisor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/host/{id}/datastore'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vmware_host(client):
    """Test case for query_vmware_host

    Get summary of all the ESXi hypervisor
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('compute_cluster_id', 'compute_cluster_id_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/host',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vmware_host(client):
    """Test case for update_vmware_host

    Update the SLA Domain for an ESXi hypervisor
    """
    body = {"configuredSlaDomainId":"configuredSlaDomainId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/host/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

