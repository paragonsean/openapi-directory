# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_all_accounts200_response import GetAllAccounts200Response
from openapi_server.models.model401_response import Model401Response


pytestmark = pytest.mark.asyncio

async def test_get_all_accounts(client):
    """Test case for get_all_accounts

    Retrieve all accounts you own
    """
    params = [('provider', 'provider_example'),
                    ('page_number', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/beta/chatapp-accounts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

