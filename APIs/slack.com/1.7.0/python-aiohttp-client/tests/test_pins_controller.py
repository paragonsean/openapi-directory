# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pins_add_error_schema import PinsAddErrorSchema
from openapi_server.models.pins_add_schema import PinsAddSchema
from openapi_server.models.pins_list_error_schema import PinsListErrorSchema
from openapi_server.models.pins_list_success_schema_inner import PinsListSuccessSchemaInner
from openapi_server.models.pins_remove_error_schema import PinsRemoveErrorSchema
from openapi_server.models.pins_remove_schema import PinsRemoveSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_pins_add(client):
    """Test case for pins_add

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/pins.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pins_list(client):
    """Test case for pins_list

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pins.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_pins_remove(client):
    """Test case for pins_remove

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/pins.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

