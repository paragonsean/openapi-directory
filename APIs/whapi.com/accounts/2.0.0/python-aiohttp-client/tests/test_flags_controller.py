# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_errors import AccountErrors
from openapi_server.models.account_flags_set import AccountFlagsSet
from openapi_server.models.flags_inner import FlagsInner


pytestmark = pytest.mark.asyncio

async def test_set_account_flags(client):
    """Test case for set_account_flags

    Sets a flag based on name to value provided for the user.
    """
    flags = [openapi_server.FlagsInner()]
    params = [('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
        'api_country_code': 'GB',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/account/flags',
        headers=headers,
        json=flags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

