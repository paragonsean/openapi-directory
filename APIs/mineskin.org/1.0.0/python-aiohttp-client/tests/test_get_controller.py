# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_delay_get200_response import GetDelayGet200Response
from openapi_server.models.get_list_page_get200_response import GetListPageGet200Response
from openapi_server.models.skin_info import SkinInfo


pytestmark = pytest.mark.asyncio

async def test_get_delay_get(client):
    """Test case for get_delay_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
        'apiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/get/delay',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_id_id_get(client):
    """Test case for get_id_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
    }
    response = await client.request(
        method='GET',
        path='/get/id/{id}'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_page_get(client):
    """Test case for get_list_page_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
    }
    response = await client.request(
        method='GET',
        path='/get/list/{page}'.format(page=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_uuid_uuid_get(client):
    """Test case for get_uuid_uuid_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
    }
    response = await client.request(
        method='GET',
        path='/get/uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

