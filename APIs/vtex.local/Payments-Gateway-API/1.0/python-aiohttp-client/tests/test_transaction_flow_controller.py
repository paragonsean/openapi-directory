# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancelthetransaction_request import CancelthetransactionRequest
from openapi_server.models.refundthetransaction_request import RefundthetransactionRequest
from openapi_server.models.settle_response import SettleResponse
from openapi_server.models.settlethetransaction_request import SettlethetransactionRequest


pytestmark = pytest.mark.asyncio

async def test_cancelthetransaction(client):
    """Test case for cancelthetransaction

    Cancel the transaction
    """
    body = {"value":1,"minicart":{"freight":0,"tax":6,"items":["",""]}}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/cancellation-request'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refundthetransaction(client):
    """Test case for refundthetransaction

    Refund the transaction
    """
    body = {"value":0,"minicart":{"freight":0,"tax":6,"items":["",""]}}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/refunding-request'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settlethetransaction(client):
    """Test case for settlethetransaction

    Settle the transaction
    """
    body = {"value":100}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/settlement-request'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

