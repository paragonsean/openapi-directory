# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capture_transaction_response import CaptureTransactionResponse
from openapi_server.models.charge_request import ChargeRequest
from openapi_server.models.charge_response import ChargeResponse
from openapi_server.models.create_refund_request import CreateRefundRequest
from openapi_server.models.create_refund_response import CreateRefundResponse
from openapi_server.models.list_refunds_response import ListRefundsResponse
from openapi_server.models.list_transactions_response import ListTransactionsResponse
from openapi_server.models.retrieve_transaction_response import RetrieveTransactionResponse
from openapi_server.models.void_transaction_response import VoidTransactionResponse


pytestmark = pytest.mark.asyncio

async def test_capture_transaction(client):
    """Test case for capture_transaction

    CaptureTransaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations/{location_id}/transactions/{transaction_id}/capture'.format(location_id='location_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charge(client):
    """Test case for charge

    Charge
    """
    body = {"request_body":{"additional_recipients":[{"amount_money":{"amount":20,"currency":"USD"},"description":"Application fees","location_id":"057P5VYJ4A5X1"}],"amount_money":{"amount":200,"currency":"USD"},"billing_address":{"address_line_1":"500 Electric Ave","address_line_2":"Suite 600","administrative_district_level_1":"NY","country":"US","locality":"New York","postal_code":"10003"},"card_nonce":"card_nonce_from_square_123","delay_capture":False,"idempotency_key":"74ae1696-b1e3-4328-af6d-f1e04d947a13","note":"some optional note","reference_id":"some optional reference id","shipping_address":{"address_line_1":"123 Main St","administrative_district_level_1":"CA","country":"US","locality":"San Francisco","postal_code":"94114"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations/{location_id}/transactions'.format(location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transactions(client):
    """Test case for list_transactions

    ListTransactions
    """
    params = [('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('sort_order', 'sort_order_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/{location_id}/transactions'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_transaction(client):
    """Test case for retrieve_transaction

    RetrieveTransaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/{location_id}/transactions/{transaction_id}'.format(location_id='location_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_locations_location_id_refunds_get(client):
    """Test case for v2_locations_location_id_refunds_get

    ListRefunds
    """
    params = [('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('sort_order', 'sort_order_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/{location_id}/refunds'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_locations_location_id_transactions_transaction_id_refund_post(client):
    """Test case for v2_locations_location_id_transactions_transaction_id_refund_post

    CreateRefund
    """
    body = {"request_body":{"amount_money":{"amount":100,"currency":"USD"},"idempotency_key":"86ae1696-b1e3-4328-af6d-f1e04d947ad2","reason":"a reason","tender_id":"MtZRYYdDrYNQbOvV7nbuBvMF"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations/{location_id}/transactions/{transaction_id}/refund'.format(location_id='location_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_void_transaction(client):
    """Test case for void_transaction

    VoidTransaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations/{location_id}/transactions/{transaction_id}/void'.format(location_id='location_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

