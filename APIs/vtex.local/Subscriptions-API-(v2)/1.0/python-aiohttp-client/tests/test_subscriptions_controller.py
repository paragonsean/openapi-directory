# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insert_addressesfor_subscription_request import InsertAddressesforSubscriptionRequest
from openapi_server.models.update_subscriptionsby_subscription_id_request import UpdateSubscriptionsbySubscriptionIdRequest


pytestmark = pytest.mark.asyncio

async def test_cancel_subscriptionsby_subscription_id(client):
    """Test case for cancel_subscriptionsby_subscription_id

    Cancel Subscriptions by SubscriptionId
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/cancel'.format(subscription_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_list(client):
    """Test case for get_subscription_list

    Get Subscription List
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getfrequencyoptionsbysubscription_id(client):
    """Test case for getfrequencyoptionsbysubscription_id

    Get frequency options by subscriptionId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/frequency-options'.format(subscription_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getsubscriptionby_id(client):
    """Test case for getsubscriptionby_id

    Retrieve subscription by ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}'.format(subscription_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getsubscriptionstocustomer(client):
    """Test case for getsubscriptionstocustomer

    Retrieve customer's subscriptions
    """
    params = [('customerId', 'user@vtex.com.br')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insert_addressesfor_subscription(client):
    """Test case for insert_addressesfor_subscription

    Insert Addresses for Subscription
    """
    body = {"additionalComponents":null,"addressId":"1234567890","addressName":"xt5353818181nhshs","addressType":"residential","city":"Rio de Janeiro","complement":null,"country":"BRA","formattedAddress":null,"geoCoordinate":null,"neighborhood":"Barra da Tijuca","number":"1","postalCode":"22204-004","receiverName":"Fulano","reference":null,"state":"RJ","street":"Avenida do Estado"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/addresses'.format(subscription_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscriptionsby_subscription_id(client):
    """Test case for update_subscriptionsby_subscription_id

    Update Subscriptions by SubscriptionId
    """
    body = {"isSkipped":True,"item":{"endpoint":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"}},"metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"plan":{"frequency":{"interval":0,"periodicity":"string"},"type":"string","validity":{"begin":"2019-07-04T14:40:30.819Z","end":"2019-07-04T14:40:30.819Z"}},"purchaseSettings":{"currencyCode":"string","paymentMethod":{"paymentAccountId":"string","paymentSystem":"string"},"purchaseDay":"string","salesChannel":"string","selectedSla":"string","seller":"string"},"shippingAddress":{"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"},"status":"string"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}'.format(subscription_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

