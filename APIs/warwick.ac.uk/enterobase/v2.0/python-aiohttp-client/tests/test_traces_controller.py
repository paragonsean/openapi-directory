# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v20_database_traces_barcode_get_request import ApiV20DatabaseTracesBarcodeGetRequest


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_traces_barcode_get(client):
    """Test case for api_v20_database_traces_barcode_get

    
    """
    body = openapi_server.ApiV20DatabaseTracesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/traces/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_traces_barcode_post(client):
    """Test case for api_v20_database_traces_barcode_post

    
    """
    body = openapi_server.ApiV20DatabaseTracesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.0/{database}/traces/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_traces_barcode_put(client):
    """Test case for api_v20_database_traces_barcode_put

    
    """
    body = openapi_server.ApiV20DatabaseTracesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2.0/{database}/traces/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_traces_get(client):
    """Test case for api_v20_database_traces_get

    
    """
    params = [('barcode', ['barcode_example']),
                    ('orderby', 'barcode'),
                    ('offset', 0),
                    ('only_fields', ['only_fields_example']),
                    ('sortorder', 'asc'),
                    ('limit', 50)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/traces'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

