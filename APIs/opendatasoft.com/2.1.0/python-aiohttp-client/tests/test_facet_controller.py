# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response


pytestmark = pytest.mark.asyncio

async def test_get_datasets_facets_0(client):
    """Test case for get_datasets_facets_0

    
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

async def test_get_records_facets_0(client):
    """Test case for get_records_facets_0

    
    """
    params = [('where', ['where_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('search', ['search_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/facets'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

