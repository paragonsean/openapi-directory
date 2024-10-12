# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedule_api_triggered_canvases_request import ScheduleApiTriggeredCanvasesRequest


pytestmark = pytest.mark.asyncio

async def test_get_upcoming_scheduled_campaigns_and_canvases(client):
    """Test case for get_upcoming_scheduled_campaigns_and_canvases

    Get Upcoming Scheduled Campaigns and Canvases
    """
    params = [('end_time', '2018-09-01T00:00:00-04:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/messages/scheduled_broadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_api_triggered_canvases(client):
    """Test case for schedule_api_triggered_canvases

    Schedule API Triggered Canvases
    """
    body = {"audience":{"AND":[{"custom_attribute":{"comparison":"equals","custom_attribute_name":"eye_color","value":"blue"}},{"custom_attribute":{"comparison":"includes_value","custom_attribute_name":"favorite_foods","value":"pizza"}},{"OR":[{"custom_attribute":{"comparison":"less_than_x_days_ago","custom_attribute_name":"last_purchase_time","value":2}},{"push_subscription_status":{"comparison":"is","value":"opted_in"}}]},{"email_subscription_status":{"comparison":"is_not","value":"subscribed"}},{"last_used_app":{"comparison":"after","value":"2019-07-22T13:17:55+0000"}}]},"broadcast":false,"canvas_entry_properties":{},"canvas_id":"canvas_identifier","recipients":[{"canvas_entry_properties":{},"external_user_id":"external_user_identifier","trigger_properties":"","user_alias":"example_alias"}],"schedule":{"at_optimal_time":false,"in_local_time":false,"time":""}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/canvas/trigger/schedule/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

