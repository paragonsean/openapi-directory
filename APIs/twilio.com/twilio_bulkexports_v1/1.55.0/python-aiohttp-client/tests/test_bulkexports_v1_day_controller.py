# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_day_instance import BulkexportsV1ExportDayInstance
from openapi_server.models.list_day_response import ListDayResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_day(client):
    """Test case for fetch_day

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/{resource_type}/Days/{day}'.format(resource_type='resource_type_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_day(client):
    """Test case for list_day

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/{resource_type}/Days'.format(resource_type='resource_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

