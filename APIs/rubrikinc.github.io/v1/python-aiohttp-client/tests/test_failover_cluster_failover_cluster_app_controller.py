# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failover_cluster_app_config import FailoverClusterAppConfig
from openapi_server.models.failover_cluster_app_detail import FailoverClusterAppDetail
from openapi_server.models.failover_cluster_app_summary import FailoverClusterAppSummary
from openapi_server.models.failover_cluster_app_summary_list_response import FailoverClusterAppSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_failover_cluster_app(client):
    """Test case for bulk_delete_failover_cluster_app

    Delete failover cluster applications
    """
    params = [('ids', ['ids_example']),
                    ('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/failover_cluster/failover_cluster_app/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_failover_cluster_app(client):
    """Test case for create_failover_cluster_app

    Create a failover cluster app
    """
    body = {"failoverClusterId":"failoverClusterId","name":"name","configuredSlaDomainId":"configuredSlaDomainId","failoverClusterType":"Windows","failoverClusterAppSource":{"virtualIps":["virtualIps","virtualIps"],"nodeOrders":[{"nodeName":"nodeName","nodeId":"nodeId","order":0},{"nodeName":"nodeName","nodeId":"nodeId","order":0}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/failover_cluster/failover_cluster_app',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_failover_cluster_app(client):
    """Test case for delete_failover_cluster_app

    Delete a failover cluster app
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/failover_cluster/failover_cluster_app/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_failover_cluster_app(client):
    """Test case for get_failover_cluster_app

    Get details of a failover cluster app
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster/failover_cluster_app/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_failover_cluster_app(client):
    """Test case for query_failover_cluster_app

    Get a summary of all failover cluster apps
    """
    params = [('name', 'name_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('operating_system_type', 'operating_system_type_example'),
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
        path='/api/v1/failover_cluster/failover_cluster_app',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_failover_cluster_app(client):
    """Test case for update_failover_cluster_app

    Update a failover cluster app
    """
    body = {"failoverClusterId":"failoverClusterId","name":"name","configuredSlaDomainId":"configuredSlaDomainId","failoverClusterType":"Windows","failoverClusterAppSource":{"virtualIps":["virtualIps","virtualIps"],"nodeOrders":[{"nodeName":"nodeName","nodeId":"nodeId","order":0},{"nodeName":"nodeName","nodeId":"nodeId","order":0}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/failover_cluster/failover_cluster_app/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

