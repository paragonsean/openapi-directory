# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get_product_info200_response import GetProductInfo200Response


pytestmark = pytest.mark.asyncio

async def test_get_product_info(client):
    """Test case for get_product_info

    Retrieve product info for a particular barcode number (UPC, EAN, or ISBN).
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/code/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

