# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_validation import UserValidation


pytestmark = pytest.mark.asyncio

async def test_validate_name_name_get(client):
    """Test case for validate_name_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
    }
    response = await client.request(
        method='GET',
        path='/validate/name/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_uuid_uuid_get(client):
    """Test case for validate_uuid_uuid_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
    }
    response = await client.request(
        method='GET',
        path='/validate/uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

