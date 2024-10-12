# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_detail_settings import EventDetailSettings
from openapi_server.models.event_detail_settings_url import EventDetailSettingsUrl


pytestmark = pytest.mark.asyncio

async def test_get_marketing_v3_marketing_events_app_id_settings_get_all(client):
    """Test case for get_marketing_v3_marketing_events_app_id_settings_get_all

    Retrieve the application settings
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketing/v3/marketing-events/{app_id}/settings'.format(app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_app_id_settings_create(client):
    """Test case for post_marketing_v3_marketing_events_app_id_settings_create

    Update the application settings
    """
    body = {"eventDetailsUrl":"eventDetailsUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/{app_id}/settings'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

