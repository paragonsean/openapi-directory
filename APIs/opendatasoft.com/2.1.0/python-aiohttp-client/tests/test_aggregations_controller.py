# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response


pytestmark = pytest.mark.asyncio

async def test_aggregate_datasets_0(client):
    """Test case for aggregate_datasets_0

    
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

async def test_aggregate_records_0(client):
    """Test case for aggregate_records_0

    
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
        path='/api/v2/{source}/datasets/{dataset_id}/aggregates'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

