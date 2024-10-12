# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_bean_screen import PageBeanScreen
from openapi_server.models.page_bean_screen_with_tab import PageBeanScreenWithTab
from openapi_server.models.screen import Screen
from openapi_server.models.screen_details import ScreenDetails
from openapi_server.models.screenable_field import ScreenableField
from openapi_server.models.update_screen_details import UpdateScreenDetails


pytestmark = pytest.mark.asyncio

async def test_add_field_to_default_screen(client):
    """Test case for add_field_to_default_screen

    Add field to default screen
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/screens/addToDefault/{field_id}'.format(field_id='field_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_screen(client):
    """Test case for create_screen

    Create screen
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/screens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_screen(client):
    """Test case for delete_screen

    Delete screen
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/screens/{screen_id}'.format(screen_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_screen_fields(client):
    """Test case for get_available_screen_fields

    Get available screen fields
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/screens/{screen_id}/availableFields'.format(screen_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_screens(client):
    """Test case for get_screens

    Get screens
    """
    params = [('startAt', 0),
                    ('maxResults', 100),
                    ('id', [56]),
                    ('queryString', ''),
                    ('scope', ['scope_example']),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/screens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_screens_for_field(client):
    """Test case for get_screens_for_field

    Get screens for a field
    """
    params = [('startAt', 0),
                    ('maxResults', 100),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/screens'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_screen(client):
    """Test case for update_screen

    Update screen
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/screens/{screen_id}'.format(screen_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

