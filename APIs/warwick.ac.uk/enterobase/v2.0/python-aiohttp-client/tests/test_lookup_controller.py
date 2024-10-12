# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v20_lookup_barcode_post_request import ApiV20LookupBarcodePostRequest


pytestmark = pytest.mark.asyncio

async def test_api_v20_lookup_barcode_get(client):
    """Test case for api_v20_lookup_barcode_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/lookup/{barcode}'.format(barcode='barcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_lookup_barcode_post(client):
    """Test case for api_v20_lookup_barcode_post

    
    """
    body = openapi_server.ApiV20LookupBarcodePostRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.0/lookup/{barcode}'.format(barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_lookup_get(client):
    """Test case for api_v20_lookup_get

    
    """
    params = [('barcode', 'barcode_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

