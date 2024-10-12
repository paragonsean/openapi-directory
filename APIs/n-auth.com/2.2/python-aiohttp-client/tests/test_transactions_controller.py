# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_id import TransactionId
from openapi_server.models.transaction_result import TransactionResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_transaction(client):
    """Test case for create_transaction

    Create a transaction to be approved within the current session.
    """
    msg = openapi_server.Transaction()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/transactions'.format(serverid='serverid_example'),
        headers=headers,
        json=msg,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_result(client):
    """Test case for get_transaction_result

    Get transaction result for a given transaction.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/transactions/{transactionid}'.format(serverid='serverid_example', transactionid='transactionid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

