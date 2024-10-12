# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_collection import ErrorCollection


pytestmark = pytest.mark.asyncio

async def test_get_valid_project_key(client):
    """Test case for get_valid_project_key

    Get valid project key
    """
    params = [('key', 'HSP')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/projectvalidate/validProjectKey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_valid_project_name(client):
    """Test case for get_valid_project_name

    Get valid project name
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/projectvalidate/validProjectName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_project_key(client):
    """Test case for validate_project_key

    Validate project key
    """
    params = [('key', 'HSP')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/projectvalidate/key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

