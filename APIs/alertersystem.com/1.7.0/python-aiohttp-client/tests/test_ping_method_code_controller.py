# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_ping_method_code_get_collection200_response import ApiPingMethodCodeGetCollection200Response
from openapi_server.models.ping_method_code_get import PingMethodCodeGet
from openapi_server.models.ping_method_code_jsonld_get import PingMethodCodeJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_ping_method_code_get_collection(client):
    """Test case for api_ping_method_code_get_collection

    Retrieves the collection of PingMethodCode resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ping-method-code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_ping_method_code_id_get(client):
    """Test case for api_ping_method_code_id_get

    Retrieves a PingMethodCode resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ping-method-code/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

