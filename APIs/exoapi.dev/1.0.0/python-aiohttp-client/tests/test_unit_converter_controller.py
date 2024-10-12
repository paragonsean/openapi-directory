# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.unit_converter_get200_response import UnitConverterGet200Response


pytestmark = pytest.mark.asyncio

async def test_unit_converter_get(client):
    """Test case for unit_converter_get

    
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('value', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/unit-converter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

