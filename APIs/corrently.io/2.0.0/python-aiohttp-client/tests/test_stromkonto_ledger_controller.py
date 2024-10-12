# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance import Balance
from openapi_server.models.prepare_transaction_request import PrepareTransactionRequest
from openapi_server.models.quittung_create_request import QuittungCreateRequest
from openapi_server.models.stromkonto_login200_response import StromkontoLogin200Response
from openapi_server.models.stromkonto_register_request import StromkontoRegisterRequest


pytestmark = pytest.mark.asyncio

async def test_prepare_transaction(client):
    """Test case for prepare_transaction

    Prepare Transaction
    """
    body = openapi_server.PrepareTransactionRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/stromkonto/prepareTransaction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stromkonto_balances(client):
    """Test case for stromkonto_balances

    Balances
    """
    params = [('account', 'account_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/stromkonto/balances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stromkonto_choices(client):
    """Test case for stromkonto_choices

    Selectable Choices for customer
    """
    params = [('account', 'account_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/stromkonto/choices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stromkonto_login(client):
    """Test case for stromkonto_login

    Login (via Mail)
    """
    body = openapi_server.QuittungCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/stromkonto/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stromkonto_register(client):
    """Test case for stromkonto_register

    Register (new Stromkonto)
    """
    body = openapi_server.StromkontoRegisterRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/stromkonto/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

