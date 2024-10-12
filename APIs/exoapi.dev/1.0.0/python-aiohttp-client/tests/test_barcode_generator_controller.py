# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.barcode_generator_post_request import BarcodeGeneratorPostRequest


pytestmark = pytest.mark.asyncio

async def test_barcode_generator_post(client):
    """Test case for barcode_generator_post

    
    """
    body = openapi_server.BarcodeGeneratorPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/barcode-generator',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

