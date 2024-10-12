# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscriber_list200_response import SubscriberList200Response


pytestmark = pytest.mark.asyncio

async def test_subscriber_list(client):
    """Test case for subscriber_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('subscribed', True),
                    ('store_id', 'store_id_example'),
                    ('email', 'email_example'),
                    ('params', 'force_all'),
                    ('exclude', 'exclude_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('page_cursor', 'page_cursor_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/subscriber.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

