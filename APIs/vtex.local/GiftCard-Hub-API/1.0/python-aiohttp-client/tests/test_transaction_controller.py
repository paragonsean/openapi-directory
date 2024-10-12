# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_gift_card_cancellation_transaction_request import CreateGiftCardCancellationTransactionRequest
from openapi_server.models.create_gift_card_settlement_transaction_request import CreateGiftCardSettlementTransactionRequest
from openapi_server.models.create_gift_card_transaction_request import CreateGiftCardTransactionRequest
from openapi_server.models.create_gift_cardin_gift_card_provider_request import CreateGiftCardinGiftCardProviderRequest
from openapi_server.models.get_gift_cardfrom_gift_card_provider_request import GetGiftCardfromGiftCardProviderRequest


pytestmark = pytest.mark.asyncio

async def test_create_gift_card_cancellation_transaction(client):
    """Test case for create_gift_card_cancellation_transaction

    Create GiftCard Cancellation Transaction
    """
    body = {"requestId":"12093812masoidj120398","value":12.1}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/vnd.vtex.giftcardproviders.v1+json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{t_id}/cancellations'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', t_id='b47690'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;utf-8 not supported by Connexion")
async def test_create_gift_card_settlement_transaction(client):
    """Test case for create_gift_card_settlement_transaction

    Create GiftCard Settlement Transaction
    """
    body = {"cart":{"discounts":-20,"grandTotal":182,"items":[{"id":"2000002","name":null,"price":200,"productId":"2000000","quantity":1,"refId":"MEV41"}],"itemsTotal":200,"redemptionCode":"FASD-ASDS-ASDA-ASDA","relationName":"loyalty-program","shipping":2,"taxes":0},"client":{"document":"42151783120","email":"convidadovtex@gmail.com","id":"3b1abc17-988e-4a14-8b7f-31fc6a5b955c"}}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json;charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{t_id}/settlements'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', t_id='b47690'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_gift_card_transaction(client):
    """Test case for create_gift_card_transaction

    Create GiftCard Transaction
    """
    body = {"description":"Order v2915869org-01","operation":"Credit","orderInfo":{"cart":{"discounts":0,"grandTotal":0,"items":[{"discount":0,"id":"2000330","name":"T-Shirt M","price":15,"priceTags":[],"productId":"2000196","quantity":1,"refId":null,"shippingDiscount":0,"value":15}],"itemsTotal":15,"shipping":0,"taxes":0},"clientProfile":{"birthDate":"0001-01-01T00:00:00","document":"10617764093","documentType":"cpf","email":"email@domain.com","firstName":"John","isCorporate":false,"lastName":"Smith","phone":"+5521993759875"},"orderId":"v2915869org-01","sequence":2915869,"shipping":{"city":"Leblon","complement":"address","country":"BRA","neighborhood":"address","number":"9678","postalCode":"24417-246","receiverName":"John Smith","reference":"address","state":"RJ","street":"Rua Aidea Barreto do Couto"}},"redemptionCode":null,"redemptionToken":null,"requestId":"v2915869org-01","value":28.4}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/vnd.vtex.giftcardproviders.v1+json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions'.format(gift_card_provider_id='insert identifier here', gift_card_id='6'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_gift_cardin_gift_card_provider(client):
    """Test case for create_gift_cardin_gift_card_provider

    Create GiftCard in GiftCard Provider
    """
    body = {"caption":"Loyalty Program","emissionDate":"2011-02-04T17:02:19.17","expiringDate":"2020-02-04T17:02:19.17","multipleCredits":true,"multipleRedemptions":true,"profileId":"92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff","relationName":"loyalty-program","restrictedToOwner":true}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/vnd.vtex.giftcardproviders.v1+json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards'.format(gift_card_provider_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_card_authorization_transaction(client):
    """Test case for get_gift_card_authorization_transaction

    Get GiftCard Authorization Transaction
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{transaction_id}/authorization'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_card_transactionby_id(client):
    """Test case for get_gift_card_transactionby_id

    Get GiftCard Transaction by ID
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{transaction_id}'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', transaction_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_cardfrom_gift_card_provider(client):
    """Test case for get_gift_cardfrom_gift_card_provider

    Get GiftCard from GiftCard Provider
    """
    body = {"cart":{"discounts":-20,"grandTotal":182,"items":[{"id":"2000002","name":null,"price":200,"productId":"2000000","quantity":1,"refId":"MEV41"}],"itemsTotal":200,"redemptionCode":null,"relationName":null,"shipping":2,"taxes":0},"client":{"document":"42151783120","email":"email@domain.com","id":"3b1abc17-988e-4a14-8b7f-31fc6a5b955c"}}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/vnd.vtex.giftcardproviders.v1+json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'rest_range': 'resources=0-49',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/_search'.format(gift_card_provider_id='insert example here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gift_cardfrom_gift_card_providerby_id(client):
    """Test case for get_gift_cardfrom_gift_card_providerby_id

    Get GiftCard from GiftCard Provider by ID
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}'.format(gift_card_provider_id='insert identifier here', gift_card_id='6'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_gift_card_cancellation_transactions(client):
    """Test case for list_all_gift_card_cancellation_transactions

    List All GiftCard Cancellation Transactions
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{t_id}/cancellations'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', t_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_gift_card_settlement_transactions(client):
    """Test case for list_all_gift_card_settlement_transactions

    List All GiftCard Settlement Transactions
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{t_id}/settlements'.format(gift_card_provider_id='insert identifier here', gift_card_id='6', t_id='b47690'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_gift_card_transactions(client):
    """Test case for list_all_gift_card_transactions

    List All GiftCard Transactions
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions'.format(gift_card_provider_id='insert identifier here', gift_card_id='6'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

