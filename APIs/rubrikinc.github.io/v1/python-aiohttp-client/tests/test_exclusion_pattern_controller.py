# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exclusion_pattern_create_config import ExclusionPatternCreateConfig
from openapi_server.models.exclusion_pattern_detail import ExclusionPatternDetail
from openapi_server.models.exclusion_pattern_detail_list import ExclusionPatternDetailList
from openapi_server.models.exclusion_pattern_detail_list_response import ExclusionPatternDetailListResponse
from openapi_server.models.exclusion_pattern_update_config import ExclusionPatternUpdateConfig


pytestmark = pytest.mark.asyncio

async def test_bulk_create_exclusion_pattern(client):
    """Test case for bulk_create_exclusion_pattern

    Bulk create exclusion patterns
    """
    body = {"sourceId":"sourceId","pattern":"pattern"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/exclusion_pattern/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_exclusion_pattern(client):
    """Test case for bulk_delete_exclusion_pattern

    Bulk delete the provided mutable exclusion patterns
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/exclusion_pattern/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_exclusion_pattern(client):
    """Test case for create_exclusion_pattern

    Create an exclusion pattern
    """
    body = {"sourceId":"sourceId","pattern":"pattern"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/exclusion_pattern',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_exclusion_pattern(client):
    """Test case for delete_exclusion_pattern

    Delete a mutable exclusion pattern
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/exclusion_pattern/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_exclusion_pattern(client):
    """Test case for get_exclusion_pattern

    Get details of a exclusion pattern
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/exclusion_pattern/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_exclusion_pattern(client):
    """Test case for query_exclusion_pattern

    Get a summary of all exclusion patterns
    """
    params = [('pattern', 'pattern_example'),
                    ('is_mutable', True),
                    ('source_id', 'source_id_example'),
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
        path='/api/v1/exclusion_pattern',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_exclusion_pattern(client):
    """Test case for update_exclusion_pattern

    Update a mutable exclusion pattern
    """
    body = {"isMutable":True,"pattern":"pattern","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/exclusion_pattern/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

