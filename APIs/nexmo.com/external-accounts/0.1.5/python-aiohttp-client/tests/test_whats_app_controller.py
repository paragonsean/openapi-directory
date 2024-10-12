# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model401_response import Model401Response
from openapi_server.models.wa_account_response import WAAccountResponse


pytestmark = pytest.mark.asyncio

async def test_get_wa_account(client):
    """Test case for get_wa_account

    Retrieve a Whatsapp account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/beta/chatapp-accounts/whatsapp/{external_id}'.format(external_id='external_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

