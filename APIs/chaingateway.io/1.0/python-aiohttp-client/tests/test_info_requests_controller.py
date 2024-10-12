# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_block import GetBlock
from openapi_server.models.get_block_request import GetBlockRequest
from openapi_server.models.get_ethereum_balance import GetEthereumBalance
from openapi_server.models.get_ethereum_balance_request import GetEthereumBalanceRequest
from openapi_server.models.get_exchange_rate import GetExchangeRate
from openapi_server.models.get_exchange_rate_request import GetExchangeRateRequest
from openapi_server.models.get_gas_price import GetGasPrice
from openapi_server.models.get_last_block_number import GetLastBlockNumber
from openapi_server.models.get_token import GetToken
from openapi_server.models.get_token_balance import GetTokenBalance
from openapi_server.models.get_token_balance_request import GetTokenBalanceRequest
from openapi_server.models.get_token_request import GetTokenRequest
from openapi_server.models.get_transactions import GetTransactions
from openapi_server.models.get_transactions_request import GetTransactionsRequest


pytestmark = pytest.mark.asyncio

async def test_get_block(client):
    """Test case for get_block

    getBlock
    """
    body = {"block":"5000000"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getBlock',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ethereum_balance(client):
    """Test case for get_ethereum_balance

    getEthereumBalance
    """
    body = {"ethereumaddress":"0xa1f36016221d48ce7f15cde7b826a4fbe09bacce"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getEthereumBalance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_exchange_rate(client):
    """Test case for get_exchange_rate

    getExchangeRate
    """
    body = {"currency":"eur"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getExchangeRate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gas_price(client):
    """Test case for get_gas_price

    getGasPrice
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getGasPrice',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_block_number(client):
    """Test case for get_last_block_number

    getLastBlockNumber
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getLastBlockNumber',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token(client):
    """Test case for get_token

    getToken
    """
    body = {"contractaddress":"0x5b86a33f0c232fe909eb4602a9d039072869d915"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getToken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_balance(client):
    """Test case for get_token_balance

    getTokenBalance
    """
    body = {"contractaddress":"0x5b86a33f0c232fe909eb4602a9d039072869d915","ethereumaddress":"0xa1f36016221d48ce7f15cde7b826a4fbe09bacce"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getTokenBalance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions(client):
    """Test case for get_transactions

    getTransactions
    """
    body = {"txid":"0x8ab5543bc103bdd908681da501d03c2c495afd7fde5ed104935ba97b1550d65b"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/getTransactions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

