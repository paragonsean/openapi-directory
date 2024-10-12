# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.action_notification_export_entity import ActionNotificationExportEntity


pytestmark = pytest.mark.asyncio

async def test_get_action_notification_exports_id(client):
    """Test case for get_action_notification_exports_id

    Show Action Notification Export
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/action_notification_exports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_action_notification_exports(client):
    """Test case for post_action_notification_exports

    Create Action Notification Export
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('end_at', '2013-10-20T19:20:30+01:00')
    data.add_field('query_folder', 'query_folder_example')
    data.add_field('query_message', 'query_message_example')
    data.add_field('query_path', 'query_path_example')
    data.add_field('query_request_method', 'query_request_method_example')
    data.add_field('query_request_url', 'query_request_url_example')
    data.add_field('query_status', 'query_status_example')
    data.add_field('query_success', True)
    data.add_field('start_at', '2013-10-20T19:20:30+01:00')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/action_notification_exports',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

