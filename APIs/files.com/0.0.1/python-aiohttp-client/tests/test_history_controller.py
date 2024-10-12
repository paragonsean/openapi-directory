# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_entity import ActionEntity


pytestmark = pytest.mark.asyncio

async def test_history_list(client):
    """Test case for history_list

    List site full action history.
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('display', 'display_example'),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_list_for_file(client):
    """Test case for history_list_for_file

    List history for specific file.
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('display', 'display_example'),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history/files/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_list_for_folder(client):
    """Test case for history_list_for_folder

    List history for specific folder.
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('display', 'display_example'),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history/folders/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_list_for_user(client):
    """Test case for history_list_for_user

    List history for specific user.
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('display', 'display_example'),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history/users/{user_id}'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_list_logins(client):
    """Test case for history_list_logins

    List site login history.
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('display', 'display_example'),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

