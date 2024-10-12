# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_call_event_response import ListCallEventResponse


pytestmark = pytest.mark.asyncio

async def test_list_call_event(client):
    """Test case for list_call_event

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Events.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

