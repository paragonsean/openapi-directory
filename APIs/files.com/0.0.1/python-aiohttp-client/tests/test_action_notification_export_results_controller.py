# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_notification_export_result_entity import ActionNotificationExportResultEntity


pytestmark = pytest.mark.asyncio

async def test_get_action_notification_export_results(client):
    """Test case for get_action_notification_export_results

    List Action Notification Export Results
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('action_notification_export_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/action_notification_export_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

