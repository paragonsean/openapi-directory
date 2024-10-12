# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response
from openapi_server.models.get_datasets200_response import GetDatasets200Response
from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response
from openapi_server.models.get_root200_response import GetRoot200Response


pytestmark = pytest.mark.asyncio

async def test_aggregate_datasets(client):
    """Test case for aggregate_datasets

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('group_by', 'group_by_example'),
                    ('order_by', ['order_by_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/aggregates'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets(client):
    """Test case for get_datasets

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('group_by', 'group_by_example'),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('pretty', False),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets_facets(client):
    """Test case for get_datasets_facets

    
    """
    params = [('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('where', ['where_example']),
                    ('search', ['search_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/facets'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source(client):
    """Test case for get_source

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}'.format(source=catalog),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

