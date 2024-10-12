# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.vcd_cluster_config import VcdClusterConfig
from openapi_server.models.vcd_cluster_detail import VcdClusterDetail
from openapi_server.models.vcd_cluster_patch import VcdClusterPatch
from openapi_server.models.vcd_cluster_summary_list_response import VcdClusterSummaryListResponse
from openapi_server.models.vimserver_summary_list_response import VimserverSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_vcd_cluster_v1(client):
    """Test case for create_vcd_cluster_v1

    Add a vCD Cluster
    """
    body = {"hostname":"hostname","password":"password","caCerts":"caCerts","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/cluster',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vcd_cluster_v1(client):
    """Test case for delete_vcd_cluster_v1

    Remove vCD Cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vcd/cluster/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcd_cluster_async_request_status_v1(client):
    """Test case for get_vcd_cluster_async_request_status_v1

    Get vCD Cluster job status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/cluster/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcd_cluster_v1(client):
    """Test case for get_vcd_cluster_v1

    Get vCD Cluster details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/cluster/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vcd_cluster_v1(client):
    """Test case for query_vcd_cluster_v1

    Get summary for all vCD Clusters
    """
    params = [('name', 'name_example'),
                    ('status', 'status_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/cluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vcd_vim_server_v1(client):
    """Test case for query_vcd_vim_server_v1

    Get VimServers of a vCD Cluster
    """
    params = [('sort_by', 'sort_by_example'),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/cluster/{id}/vimserver'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_vcd_cluster_v1(client):
    """Test case for refresh_vcd_cluster_v1

    Refresh a vCD Cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/cluster/{id}/refresh'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vcd_cluster_v1(client):
    """Test case for update_vcd_cluster_v1

    Change vCD Cluster object
    """
    body = {"hostname":"hostname","password":"password","configuredSlaDomainId":"configuredSlaDomainId","caCerts":"caCerts","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vcd/cluster/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

