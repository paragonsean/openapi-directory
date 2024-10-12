# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_exchange_ticket(client):
    """Test case for exchange_ticket

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/oauth/tickets/{ticket_id}/exchange'.format(ticket_id='ticket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

