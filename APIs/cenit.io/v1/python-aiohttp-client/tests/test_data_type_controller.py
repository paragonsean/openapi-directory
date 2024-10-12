# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_type import DataType


pytestmark = pytest.mark.asyncio

async def test_setup_data_type_get(client):
    """Test case for setup_data_type_get

    Returns a list of data types
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/data_type/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_data_type_id_delete(client):
    """Test case for setup_data_type_id_delete

    Delete a data type
    """
    headers = { 
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/setup/data_type/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_data_type_id_get(client):
    """Test case for setup_data_type_id_get

    Retrieve a data type
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/data_type/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_data_type_post(client):
    """Test case for setup_data_type_post

    Create or update a data type
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/setup/data_type/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

