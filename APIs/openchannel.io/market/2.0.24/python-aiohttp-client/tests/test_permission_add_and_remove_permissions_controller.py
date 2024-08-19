# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access import Access


pytestmark = pytest.mark.asyncio

async def test_permission_apps_app_id_delete(client):
    """Test case for permission_apps_app_id_delete

    Removes permission that allows the app to access this user's data
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/permission/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permission_apps_app_id_get(client):
    """Test case for permission_apps_app_id_get

    Returns permission that allows the app to access this user's data
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/permission/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permission_apps_app_id_post(client):
    """Test case for permission_apps_app_id_post

    Adds permission to allow the app to access this user's data
    """
    params = [('userId', 'user_id_example'),
                    ('date', 56),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/permission/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

