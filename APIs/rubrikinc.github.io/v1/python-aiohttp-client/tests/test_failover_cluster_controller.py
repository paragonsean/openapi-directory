# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failover_cluster_config import FailoverClusterConfig
from openapi_server.models.failover_cluster_detail import FailoverClusterDetail
from openapi_server.models.failover_cluster_summary_list_response import FailoverClusterSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_failover_cluster(client):
    """Test case for bulk_delete_failover_cluster

    Delete the provided failover clusters
    """
    params = [('ids', ['ids_example']),
                    ('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/failover_cluster/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_failover_cluster(client):
    """Test case for create_failover_cluster

    Create a failover cluster
    """
    body = {"name":"name","configuredSlaDomainId":"configuredSlaDomainId","hostIds":["hostIds","hostIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/failover_cluster',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_failover_cluster(client):
    """Test case for delete_failover_cluster

    Delete a failover cluster
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/failover_cluster/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_failover_cluster(client):
    """Test case for get_failover_cluster

    Get details of a failover cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_failover_cluster(client):
    """Test case for query_failover_cluster

    Get a summary of all failover clusters
    """
    params = [('name', 'name_example'),
                    ('operating_system_type', 'operating_system_type_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_failover_cluster(client):
    """Test case for update_failover_cluster

    Update a failover cluster
    """
    body = {"name":"name","configuredSlaDomainId":"configuredSlaDomainId","hostIds":["hostIds","hostIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/failover_cluster/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

