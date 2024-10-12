# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transfer_entry import TransferEntry


pytestmark = pytest.mark.asyncio

async def test_credit_transfer_post(client):
    """Test case for credit_transfer_post

    Transfer credits to another account
    """
    body = {"commentOnFrom":"Tranfer to Bobby","credits":2345,"commentOnTo":"Tranfer from Danny","toUsername":"roboto","toUserId":2345}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/credit/transfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

