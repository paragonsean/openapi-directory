# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.windows_cluster_detail import WindowsClusterDetail
from openapi_server.models.windows_cluster_summary_list_response import WindowsClusterSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_get_windows_cluster(client):
    """Test case for get_windows_cluster

    Get detailed information for a Windows cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/windows_cluster/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_windows_cluster(client):
    """Test case for query_windows_cluster

    Get summary information for Windows clusters
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('is_agentless', True),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/windows_cluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

