# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_errors import AccountErrors


pytestmark = pytest.mark.asyncio

async def test_set_lost_stolen_4(client):
    """Test case for set_lost_stolen_4

    Sets a customer's plus card as Lost/Stolen
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/account/plusCard/lostStolen',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

