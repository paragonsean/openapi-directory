# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_my_details200_response import GetMyDetails200Response
from openapi_server.models.get_user_details200_response import GetUserDetails200Response
from openapi_server.models.modify_project_notification_settings_request import ModifyProjectNotificationSettingsRequest
from openapi_server.models.org_org_id_notification_settings_get200_response import OrgOrgIdNotificationSettingsGet200Response
from openapi_server.models.set_notification_settings_request import SetNotificationSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_my_details(client):
    """Test case for get_my_details

    Get My Details
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_notification_settings(client):
    """Test case for get_organization_notification_settings

    Get organization notification settings
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/me/notification-settings/org/{org_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_notification_settings(client):
    """Test case for get_project_notification_settings

    Get project notification settings
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/me/notification-settings/org/{org_id}/project/{project_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_details(client):
    """Test case for get_user_details

    Get User Details
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/{user_id}'.format(user_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modify_organization_notification_settings(client):
    """Test case for modify_organization_notification_settings

    Modify organization notification settings
    """
    body = openapi_server.SetNotificationSettingsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/user/me/notification-settings/org/{org_id}'.format(org_id='org_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modify_project_notification_settings(client):
    """Test case for modify_project_notification_settings

    Modify project notification settings
    """
    body = openapi_server.ModifyProjectNotificationSettingsRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/user/me/notification-settings/org/{org_id}/project/{project_id}'.format(org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

