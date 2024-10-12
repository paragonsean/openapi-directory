# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.developer import Developer
from openapi_server.models.developer_pages import DeveloperPages


pytestmark = pytest.mark.asyncio

async def test_developers_developer_id_delete(client):
    """Test case for developers_developer_id_delete

    Removes a single developer
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/developers/{developer_id}'.format(developer_id='developer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developers_developer_id_get(client):
    """Test case for developers_developer_id_get

    Returns a single developer
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/developers/{developer_id}'.format(developer_id='developer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developers_developer_id_patch(client):
    """Test case for developers_developer_id_patch

    Updates the developer fields
    """
    params = [('type', 'type_example'),
                    ('email', 'email_example'),
                    ('username', 'username_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/developers/{developer_id}'.format(developer_id='developer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developers_developer_id_post(client):
    """Test case for developers_developer_id_post

    Updates the developer record or adds the developer if it doesn't exist
    """
    params = [('type', 'type_example'),
                    ('email', 'email_example'),
                    ('username', 'username_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/developers/{developer_id}'.format(developer_id='developer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developers_get(client):
    """Test case for developers_get

    Returns a paginated list of developers
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/developers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

