# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_field_bean import AddFieldBean
from openapi_server.models.move_field_bean import MoveFieldBean
from openapi_server.models.screenable_field import ScreenableField


pytestmark = pytest.mark.asyncio

async def test_add_screen_tab_field(client):
    """Test case for add_screen_tab_field

    Add screen tab field
    """
    body = {"fieldId":"fieldId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields'.format(screen_id=56, tab_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_screen_tab_fields(client):
    """Test case for get_all_screen_tab_fields

    Get all screen tab fields
    """
    params = [('projectKey', 'project_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields'.format(screen_id=56, tab_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_screen_tab_field(client):
    """Test case for move_screen_tab_field

    Move screen tab field
    """
    body = {"after":"https://openapi-generator.tech","position":"Earlier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id}/move'.format(screen_id=56, tab_id=56, id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_screen_tab_field(client):
    """Test case for remove_screen_tab_field

    Remove screen tab field
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id}'.format(screen_id=56, tab_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

