# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.variable import Variable
from openapi_server.models.variable_collection import VariableCollection


pytestmark = pytest.mark.asyncio

async def test_delete_variable(client):
    """Test case for delete_variable

    Delete a variable
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/variables/{variable_key}'.format(variable_key='variable_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variable(client):
    """Test case for get_variable

    Get a variable
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/variables/{variable_key}'.format(variable_key='variable_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables(client):
    """Test case for get_variables

    List variables
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/variables',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_variable(client):
    """Test case for patch_variable

    Update a variable
    """
    body = {"description":"description","value":"value","key":"key"}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/variables/{variable_key}'.format(variable_key='variable_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_variables(client):
    """Test case for post_variables

    Create a variable
    """
    body = {"description":"description","value":"value","key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/variables',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

