# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bug_tracker_get_repo_issue_from_crash200_response import BugTrackerGetRepoIssueFromCrash200Response
from openapi_server.models.bugtracker_get_settings200_response import BugtrackerGetSettings200Response
from openapi_server.models.bugtracker_get_settings_default_response import BugtrackerGetSettingsDefaultResponse
from openapi_server.models.notifications_get_app_email_settings200_response import NotificationsGetAppEmailSettings200Response
from openapi_server.models.notifications_get_user_email_settings200_response import NotificationsGetUserEmailSettings200Response
from openapi_server.models.webhooks_list200_response import WebhooksList200Response


pytestmark = pytest.mark.asyncio

async def test_bug_tracker_get_repo_issue_from_crash(client):
    """Test case for bug_tracker_get_repo_issue_from_crash

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/bugtracker/crashGroup/{crash_group_id}'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bugtracker_get_settings(client):
    """Test case for bugtracker_get_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/bugtracker'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_get_app_email_settings(client):
    """Test case for notifications_get_app_email_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/notifications/emailSettings'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_get_user_email_settings(client):
    """Test case for notifications_get_user_email_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/notifications/emailSettings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_list(client):
    """Test case for webhooks_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/webhooks'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

