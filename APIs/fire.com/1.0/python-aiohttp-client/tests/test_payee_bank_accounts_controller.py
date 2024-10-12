# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payee_bank_accounts import PayeeBankAccounts


pytestmark = pytest.mark.asyncio

async def test_get_payees(client):
    """Test case for get_payees

    List all Payee Bank Accounts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/payees',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

