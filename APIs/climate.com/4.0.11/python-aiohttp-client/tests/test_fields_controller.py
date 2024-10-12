# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.fields import Fields
from openapi_server.models.model_field import ModelField


pytestmark = pytest.mark.asyncio

async def test_fetch_all_fields(client):
    """Test case for fetch_all_fields

    Retrieve list of all Fields the user has access to.
    """
    params = [('fieldName', 'field_name_example')]
    headers = { 
        'Accept': 'application/json',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/fields/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_field_by_id(client):
    """Test case for fetch_field_by_id

    Retrieve a specific Field by ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/fields/{field_id}'.format(field_id='field_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_fields(client):
    """Test case for fetch_fields

    Retrieve list of Fields
    """
    params = [('fieldName', 'field_name_example')]
    headers = { 
        'Accept': 'application/json',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

