# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_bean_screen_scheme import PageBeanScreenScheme
from openapi_server.models.screen_scheme_details import ScreenSchemeDetails
from openapi_server.models.screen_scheme_id import ScreenSchemeId
from openapi_server.models.update_screen_scheme_details import UpdateScreenSchemeDetails


pytestmark = pytest.mark.asyncio

async def test_create_screen_scheme(client):
    """Test case for create_screen_scheme

    Create screen scheme
    """
    body = {"screens":"","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/screenscheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_screen_scheme(client):
    """Test case for delete_screen_scheme

    Delete screen scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/screenscheme/{screen_scheme_id}'.format(screen_scheme_id='screen_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_screen_schemes(client):
    """Test case for get_screen_schemes

    Get screen schemes
    """
    params = [('startAt', 0),
                    ('maxResults', 25),
                    ('id', [56]),
                    ('expand', ''),
                    ('queryString', ''),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/screenscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_screen_scheme(client):
    """Test case for update_screen_scheme

    Update screen scheme
    """
    body = {"screens":"","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/screenscheme/{screen_scheme_id}'.format(screen_scheme_id='screen_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

