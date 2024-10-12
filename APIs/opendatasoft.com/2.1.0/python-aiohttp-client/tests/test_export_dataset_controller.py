# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_export_records_csv(client):
    """Test case for export_records_csv

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('delimiter', ;)]
    headers = { 
        'Accept': 'text/csv',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/csv'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_geojson(client):
    """Test case for export_records_geojson

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('pretty', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/geojson'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_ical(client):
    """Test case for export_records_ical

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/ical'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_json(client):
    """Test case for export_records_json

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('pretty', False),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/json'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_ov2(client):
    """Test case for export_records_ov2

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/ov2'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_shp(client):
    """Test case for export_records_shp

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'application/zip',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/shp'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_records_xls(client):
    """Test case for export_records_xls

    
    """
    params = [('select', 'select_example'),
                    ('where', ['where_example']),
                    ('sort', ['sort_example']),
                    ('order_by', ['order_by_example']),
                    ('limit', -1),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC')]
    headers = { 
        'Accept': 'xls',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/datasets/{dataset_id}/exports/xls'.format(source=catalog, dataset_id='dataset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

