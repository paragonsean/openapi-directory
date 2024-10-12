# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar_list import CalendarList
from openapi_server.models.calendar_list_entry import CalendarListEntry
from openapi_server.models.channel import Channel


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_delete(client):
    """Test case for calendar_calendar_list_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/calendar/v3/users/me/calendarList/{calendar_id}'.format(calendar_id='calendar_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_get(client):
    """Test case for calendar_calendar_list_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/users/me/calendarList/{calendar_id}'.format(calendar_id='calendar_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_insert(client):
    """Test case for calendar_calendar_list_insert

    
    """
    body = {"conferenceProperties":{"allowedConferenceSolutionTypes":["allowedConferenceSolutionTypes","allowedConferenceSolutionTypes"]},"summary":"summary","backgroundColor":"backgroundColor","hidden":False,"colorId":"colorId","kind":"calendar#calendarListEntry","description":"description","timeZone":"timeZone","foregroundColor":"foregroundColor","notificationSettings":{"notifications":[{"method":"method","type":"type"},{"method":"method","type":"type"}]},"deleted":False,"summaryOverride":"summaryOverride","defaultReminders":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"accessRole":"accessRole","etag":"etag","location":"location","id":"id","selected":False,"primary":False}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('colorRgbFormat', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/users/me/calendarList',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_list(client):
    """Test case for calendar_calendar_list_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('minAccessRole', 'min_access_role_example'),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True),
                    ('showHidden', True),
                    ('syncToken', 'sync_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/users/me/calendarList',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_patch(client):
    """Test case for calendar_calendar_list_patch

    
    """
    body = {"conferenceProperties":{"allowedConferenceSolutionTypes":["allowedConferenceSolutionTypes","allowedConferenceSolutionTypes"]},"summary":"summary","backgroundColor":"backgroundColor","hidden":False,"colorId":"colorId","kind":"calendar#calendarListEntry","description":"description","timeZone":"timeZone","foregroundColor":"foregroundColor","notificationSettings":{"notifications":[{"method":"method","type":"type"},{"method":"method","type":"type"}]},"deleted":False,"summaryOverride":"summaryOverride","defaultReminders":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"accessRole":"accessRole","etag":"etag","location":"location","id":"id","selected":False,"primary":False}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('colorRgbFormat', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/calendar/v3/users/me/calendarList/{calendar_id}'.format(calendar_id='calendar_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_update(client):
    """Test case for calendar_calendar_list_update

    
    """
    body = {"conferenceProperties":{"allowedConferenceSolutionTypes":["allowedConferenceSolutionTypes","allowedConferenceSolutionTypes"]},"summary":"summary","backgroundColor":"backgroundColor","hidden":False,"colorId":"colorId","kind":"calendar#calendarListEntry","description":"description","timeZone":"timeZone","foregroundColor":"foregroundColor","notificationSettings":{"notifications":[{"method":"method","type":"type"},{"method":"method","type":"type"}]},"deleted":False,"summaryOverride":"summaryOverride","defaultReminders":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"accessRole":"accessRole","etag":"etag","location":"location","id":"id","selected":False,"primary":False}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('colorRgbFormat', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/calendar/v3/users/me/calendarList/{calendar_id}'.format(calendar_id='calendar_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_calendar_list_watch(client):
    """Test case for calendar_calendar_list_watch

    
    """
    body = {"resourceId":"resourceId","address":"address","payload":True,"kind":"api#channel","expiration":"expiration","id":"id","resourceUri":"resourceUri","params":{"key":"params"},"type":"type","token":"token"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('minAccessRole', 'min_access_role_example'),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True),
                    ('showHidden', True),
                    ('syncToken', 'sync_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/users/me/calendarList/watch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

