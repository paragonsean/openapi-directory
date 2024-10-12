# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_editable import UserEditable


pytestmark = pytest.mark.asyncio

async def test_account_patch(client):
    """Test case for account_patch

    Update account
    """
    user = {"screen_name":"billhicks","about":"The comedian","name":"Bill Hicks","header":"<BASE_64_ENCODED_STRING>","language":"en","location":"Little Rock, Arkansas","time_zone":"Pacific Time (US & Canada)","picture":"<BASE_64_ENCODED_STRING>","url":"http://www.billhicks.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/account',
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

