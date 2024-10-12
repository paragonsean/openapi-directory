# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clear_address import ClearAddress
from openapi_server.models.clear_address_request import ClearAddressRequest
from openapi_server.models.send_ethereum import SendEthereum
from openapi_server.models.send_ethereum_request import SendEthereumRequest
from openapi_server.models.send_token import SendToken
from openapi_server.models.send_token_request import SendTokenRequest


pytestmark = pytest.mark.asyncio

async def test_clear_address(client):
    """Test case for clear_address

    clearAddress
    """
    body = {"ethereumaddress":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","newaddress":"0xef4943d727e34280a2efa0b3352dfd61f508ee48","password":"padN39QkRA2hJ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/clearAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_ethereum(client):
    """Test case for send_ethereum

    sendEthereum
    """
    body = {"amount":0.01,"from":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","password":"padN39QkRA2hJ","to":"0xef4943d727e34280a2efa0b3352dfd61f508ee48"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/sendEthereum',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_token(client):
    """Test case for send_token

    sendToken
    """
    body = {"amount":5,"contractaddress":"0xdac17f958d2ee523a2206206994597c13d831ec7","from":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","identifier":"CN562","password":"padN39QkRA2hJ","to":"0xef4943d727e34280a2efa0b3352dfd61f508ee48"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/sendToken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

