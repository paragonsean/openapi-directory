# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_gift_card_transaction_request import CancelGiftCardTransactionRequest
from openapi_server.models.create_gift_card_transaction_request import CreateGiftCardTransactionRequest
from openapi_server.models.response3 import Response3
from openapi_server.models.response5 import Response5
from openapi_server.models.response6 import Response6
from openapi_server.models.response7 import Response7
from openapi_server.models.settle_gift_card_transaction_request import SettleGiftCardTransactionRequest


pytestmark = pytest.mark.asyncio

async def test_cancel_gift_card_transaction(client):
    """Test case for cancel_gift_card_transaction

    Cancel GiftCard Transaction
    """
    body = {"requestId":"requestId","value":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}/cancellations'.format(gift_card_id='6', transaction_id='b476900c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_gift_card_transaction(client):
    """Test case for create_gift_card_transaction

    Create GiftCard Transaction
    """
    body = {"description":"GiftCardHub","operation":"Debit","orderInfo":{"cart":{"discounts":-7.5,"grandTotal":0,"items":[{"discount":-7.5,"id":"2001023","name":"Vaporizador Des. ColC4nia Branco","price":14.99,"priceTags":[{"name":"discount@price-discount_store_183#4911bf6f-22a2-4af1-a365-cce895c3df2c","value":0}],"productId":"2000492","quantity":1,"refId":"35994","shippingDiscount":0,"value":14.99}],"itemsTotal":14.99,"shipping":7.27,"taxes":0},"clientProfile":{"birthDate":"0001-01-01T00:00:00","document":"02906792063","email":"miguel.scott96@yahoo.com.br","firstName":"miguel","isCorporate":False,"lastName":"scott","phone":"+551111111111"},"orderId":"v5006128str","sequence":5006128,"shipping":{"city":"Rio de Janeiro","complement":null,"country":"BRA","neighborhood":"Botafogo","number":"111","postalCode":"22250040","receiverName":"miguel scott","reference":null,"state":"RJ","street":"Praia de Botafogo"}},"redemptionCode":"","redemptionToken":"b2dac6f2-f365-48cd-82a9-0b376a55557a","requestId":"B56CBE231DEE4E1A859183C1030CE926","value":3}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcards/{gift_card_id}/transactions'.format(gift_card_id='7'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_card_transactionby_id(client):
    """Test case for get_gift_card_transactionby_id

    Get GiftCard Transaction by ID
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}'.format(gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_card_transactions(client):
    """Test case for get_gift_card_transactions

    Get GiftCard Transactions
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}/transactions'.format(gift_card_id='2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_authorizations(client):
    """Test case for get_transaction_authorizations

    Get Transaction Authorizations
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}/authorization'.format(gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_cancellations(client):
    """Test case for get_transaction_cancellations

    Get Transaction Cancellations
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}/cancellations'.format(gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_settlements(client):
    """Test case for get_transaction_settlements

    Get Transaction Settlements
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}/settlements'.format(gift_card_id='7', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settle_gift_card_transaction(client):
    """Test case for settle_gift_card_transaction

    Settle GiftCard Transaction
    """
    body = {"requestId":"requestId","value":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcards/{gift_card_id}/transactions/{transaction_id}/settlements'.format(gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

