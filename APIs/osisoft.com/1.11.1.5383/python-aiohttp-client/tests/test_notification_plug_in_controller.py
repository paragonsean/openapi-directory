# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_plug_in import NotificationPlugIn


pytestmark = pytest.mark.asyncio

async def test_notification_plug_in_get(client):
    """Test case for notification_plug_in_get

    Retrieve a notification plugin.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationplugins/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_plug_in_get_by_path(client):
    """Test case for notification_plug_in_get_by_path

    Retrieve a notification plugin by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationplugIns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

