# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_gift_card_activity_request import CreateGiftCardActivityRequest
from openapi_server.models.create_gift_card_activity_response import CreateGiftCardActivityResponse
from openapi_server.models.list_gift_card_activities_response import ListGiftCardActivitiesResponse


pytestmark = pytest.mark.asyncio

async def test_create_gift_card_activity(client):
    """Test case for create_gift_card_activity

    CreateGiftCardActivity
    """
    body = {"request_body":{"gift_card_activity":{"activate_activity_details":{"line_item_uid":"eIWl7X0nMuO9Ewbh0ChIx","order_id":"jJNGHm4gLI6XkFbwtiSLqK72KkAZY"},"gift_card_id":"gftc:6d55a72470d940c6ba09c0ab8ad08d20","location_id":"81FN9BNFZTKS4","type":"ACTIVATE"},"idempotency_key":"U16kfr-kA70er-q4Rsym-7U7NnY"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/gift-cards/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_gift_card_activities(client):
    """Test case for list_gift_card_activities

    ListGiftCardActivities
    """
    params = [('gift_card_id', 'gift_card_id_example'),
                    ('type', 'type_example'),
                    ('location_id', 'location_id_example'),
                    ('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/gift-cards/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

