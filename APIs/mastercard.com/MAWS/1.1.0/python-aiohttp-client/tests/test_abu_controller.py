# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.abu import ABU
from openapi_server.models.abu_response import AbuResponse


pytestmark = pytest.mark.asyncio

async def test_abu_post(client):
    """Test case for abu_post

    Access methods for merchants to ABU program.
    """
    abu_request = {"method":"abu","id":"a1234567890","jsonrpc":"2.0","params":{"subMerchantId":"000000000000001","oldAccountNumber":"5573491171027312","merchantId":"000111222333456","subscribe":"subscribe","ica":"1111","discretionaryData":"RandomData","oldExpirationDate":"0714"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/maws/v1/maws',
        headers=headers,
        json=abu_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

