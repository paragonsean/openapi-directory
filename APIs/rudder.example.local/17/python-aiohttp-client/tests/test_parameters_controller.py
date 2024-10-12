# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_parameter200_response import CreateParameter200Response
from openapi_server.models.delete_parameter200_response import DeleteParameter200Response
from openapi_server.models.delete_parameter500_response import DeleteParameter500Response
from openapi_server.models.list_parameters200_response import ListParameters200Response
from openapi_server.models.parameter import Parameter
from openapi_server.models.parameter_details200_response import ParameterDetails200Response
from openapi_server.models.update_parameter200_response import UpdateParameter200Response


pytestmark = pytest.mark.asyncio

async def test_create_parameter(client):
    """Test case for create_parameter

    Create a new parameter
    """
    body = openapi_server.Parameter()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/parameters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_parameter(client):
    """Test case for delete_parameter

    Delete a parameter
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/parameters/{parameter_id}'.format(parameter_id='rudder_file_edit_header'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_parameters(client):
    """Test case for list_parameters

    List all global parameters
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/parameters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parameter_details(client):
    """Test case for parameter_details

    Get the value of a parameter
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/parameters/{parameter_id}'.format(parameter_id='rudder_file_edit_header'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_parameter(client):
    """Test case for update_parameter

    Update a parameter's value
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/parameters/{parameter_id}'.format(parameter_id='rudder_file_edit_header'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

