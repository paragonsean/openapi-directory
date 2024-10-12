# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors


pytestmark = pytest.mark.asyncio

async def test_configuration_delete(client):
    """Test case for configuration_delete

    Delete a configuration item.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/system/configuration/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_get(client):
    """Test case for configuration_get

    Get the value of a configuration item.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/system/configuration/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_list(client):
    """Test case for configuration_list

    Get the current system configuration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/system/configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

