# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_consents_raw_ok_body import PostPaymentsConsentsRawOKBody
from openapi_server.models.post_payments_consents_raw_params_body import PostPaymentsConsentsRawParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_consents_raw_post(client):
    """Test case for payments_consents_raw_post

    Extracts the original raw consent given by the aspsp
    """
    body = openapi_server.PostPaymentsConsentsRawParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/consents/raw',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

