# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_export_datasets_csv(client):
    """Test case for export_datasets_csv

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False),
                    ('delimiter', ;)]
    headers = { 
        'Accept': 'text/csv',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/csv'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_json(client):
    """Test case for export_datasets_json

    
    """
    params = [('where', ['where_example']),
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
        path='/api/v2/{source}/exports/json'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_rdf(client):
    """Test case for export_datasets_rdf

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'application/rdf+xml',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/rdf'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_rss(client):
    """Test case for export_datasets_rss

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'text/xml',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/rss'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_ttl(client):
    """Test case for export_datasets_ttl

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'text/turtle',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/ttl'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_datasets_xls(client):
    """Test case for export_datasets_xls

    
    """
    params = [('where', ['where_example']),
                    ('limit', 10),
                    ('offset', 0),
                    ('search', ['search_example']),
                    ('facet', ['facet_example']),
                    ('refine', ['refine_example']),
                    ('exclude', ['exclude_example']),
                    ('timezone', 'UTC'),
                    ('include_app_metas', False)]
    headers = { 
        'Accept': 'xls',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/exports/xls'.format(source=catalog),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

