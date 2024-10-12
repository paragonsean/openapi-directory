# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_barcode_decode_post(client):
    """Test case for barcode_decode_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    data = {
        'barimage': '/path/to/file'
        }
    response = await client.request(
        method='POST',
        path='/barcode/decode',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_barcode_decode_types_get(client):
    """Test case for barcode_decode_types_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode/decode/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_barcode_encode_get(client):
    """Test case for barcode_encode_get

    
    """
    params = [('number', 'number_example'),
                    ('barcodeformat', 'barcodeformat_example'),
                    ('outputformat', 'outputformat_example'),
                    ('widthfactor', 56),
                    ('totalheight', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode/encode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_barcode_encode_types_get(client):
    """Test case for barcode_encode_types_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode/encode/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

