# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_count import NotificationCount
from openapi_server.models.notification_thread import NotificationThread


pytestmark = pytest.mark.asyncio

async def test_notify_get_list(client):
    """Test case for notify_get_list

    List users's notification threads
    """
    params = [('all', True),
                    ('status-types', ['status_types_example']),
                    ('subject-type', ['subject_type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_get_repo_list(client):
    """Test case for notify_get_repo_list

    List users's notification threads on a specific repo
    """
    params = [('all', True),
                    ('status-types', ['status_types_example']),
                    ('subject-type', ['subject_type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/repos/{owner}/{repo}/notifications'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_get_thread(client):
    """Test case for notify_get_thread

    Get notification thread by ID
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/notifications/threads/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_new_available(client):
    """Test case for notify_new_available

    Check if unread notifications exist
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/notifications/new',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_read_list(client):
    """Test case for notify_read_list

    Mark notification threads as read, pinned or unread
    """
    params = [('last_read_at', '2013-10-20T19:20:30+01:00'),
                    ('all', 'all_example'),
                    ('status-types', ['status_types_example']),
                    ('to-status', 'to_status_example')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_read_repo_list(client):
    """Test case for notify_read_repo_list

    Mark notification threads as read, pinned or unread on a specific repo
    """
    params = [('all', 'all_example'),
                    ('status-types', ['status_types_example']),
                    ('to-status', 'to_status_example'),
                    ('last_read_at', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/repos/{owner}/{repo}/notifications'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_read_thread(client):
    """Test case for notify_read_thread

    Mark notification thread as read by ID
    """
    params = [('to-status', 'read')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/notifications/threads/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

