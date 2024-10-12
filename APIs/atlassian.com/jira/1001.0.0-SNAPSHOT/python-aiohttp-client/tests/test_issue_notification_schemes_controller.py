# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_notifications_details import AddNotificationsDetails
from openapi_server.models.create_notification_scheme_details import CreateNotificationSchemeDetails
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.notification_scheme import NotificationScheme
from openapi_server.models.notification_scheme_id import NotificationSchemeId
from openapi_server.models.page_bean_notification_scheme import PageBeanNotificationScheme
from openapi_server.models.page_bean_notification_scheme_and_project_mapping_json_bean import PageBeanNotificationSchemeAndProjectMappingJsonBean
from openapi_server.models.update_notification_scheme_details import UpdateNotificationSchemeDetails


pytestmark = pytest.mark.asyncio

async def test_add_notifications(client):
    """Test case for add_notifications

    Add notifications to notification scheme
    """
    body = {"notificationSchemeEvents":[{"event":"","notifications":[{"parameter":"parameter","notificationType":"notificationType"},{"parameter":"parameter","notificationType":"notificationType"}]},{"event":"","notifications":[{"parameter":"parameter","notificationType":"notificationType"},{"parameter":"parameter","notificationType":"notificationType"}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/notificationscheme/{id}/notification'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_notification_scheme(client):
    """Test case for create_notification_scheme

    Create notification scheme
    """
    body = {"name":"name","description":"description","notificationSchemeEvents":[{"event":"","notifications":[{"parameter":"parameter","notificationType":"notificationType"},{"parameter":"parameter","notificationType":"notificationType"}]},{"event":"","notifications":[{"parameter":"parameter","notificationType":"notificationType"},{"parameter":"parameter","notificationType":"notificationType"}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/notificationscheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_notification_scheme(client):
    """Test case for delete_notification_scheme

    Delete notification scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/notificationscheme/{notification_scheme_id}'.format(notification_scheme_id='notification_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_scheme(client):
    """Test case for get_notification_scheme

    Get notification scheme
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/notificationscheme/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_scheme_to_project_mappings(client):
    """Test case for get_notification_scheme_to_project_mappings

    Get projects using notification schemes paginated
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('notificationSchemeId', ['notification_scheme_id_example']),
                    ('projectId', ['project_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/notificationscheme/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_schemes(client):
    """Test case for get_notification_schemes

    Get notification schemes paginated
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('id', ['id_example']),
                    ('projectId', ['project_id_example']),
                    ('onlyDefault', False),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/notificationscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_notification_from_notification_scheme(client):
    """Test case for remove_notification_from_notification_scheme

    Remove notification from notification scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}'.format(notification_scheme_id='notification_scheme_id_example', notification_id='notification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notification_scheme(client):
    """Test case for update_notification_scheme

    Update notification scheme
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
        path='/rest/api/3/notificationscheme/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

