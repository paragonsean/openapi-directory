# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.additemsubscription_group_id_request import AdditemsubscriptionGroupIdRequest
from openapi_server.models.insert_addressesbygroup_id_request import InsertAddressesbygroupIdRequest
from openapi_server.models.update_subscriptionbygroup_id_request import UpdateSubscriptionbygroupIdRequest


pytestmark = pytest.mark.asyncio

async def test_additemsubscription_group_id(client):
    """Test case for additemsubscription_group_id

    Add Subscription item by groupId
    """
    body = {"endpoint":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"}}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions-group/{group_id}/additem'.format(group_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_subscriptionbygroup_id(client):
    """Test case for cancel_subscriptionbygroup_id

    Cancel Subscription by groupId
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions-group/{group_id}/cancel'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_allsubscriptiongroup(client):
    """Test case for get_allsubscriptiongroup

    List All subscription groups
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_configsubscriptionsgroup(client):
    """Test case for get_configsubscriptionsgroup

    List Subscription group's Configuration
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/config'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversation_messagebygroup_id(client):
    """Test case for get_conversation_messagebygroup_id

    Get Conversation Message by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/conversation-message'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nextpurchase(client):
    """Test case for get_nextpurchase

    Get Next purchase
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/nextPurchase/{date_str}'.format(date_str='date_str_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_simulatebysubscription_group(client):
    """Test case for get_simulatebysubscription_group

    Get Simulation by subscription-group
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/simulate/{group_id}'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscriptionbygroup_id(client):
    """Test case for get_subscriptionbygroup_id

    Get Subscription by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getaddressesbygroup_id(client):
    """Test case for getaddressesbygroup_id

    Get addresses by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/addresses'.format(group_id=''),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getfrequencyoptionsbygroup_id(client):
    """Test case for getfrequencyoptionsbygroup_id

    Get frequency options by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/frequency-options'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getpayment_systembygroup_id(client):
    """Test case for getpayment_systembygroup_id

    Get payment System by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/payment-systems'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getsubscriptiongrouplist(client):
    """Test case for getsubscriptiongrouplist

    Get subscription group list
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getwillcreatebygroup_id(client):
    """Test case for getwillcreatebygroup_id

    List 'Will create' by groupId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions-group/{group_id}/will-create'.format(group_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insert_addressesbygroup_id(client):
    """Test case for insert_addressesbygroup_id

    Insert Addresses by groupId
    """
    body = {"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions-group/{group_id}/addresses'.format(group_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrysubscriptionbygroup_id(client):
    """Test case for retrysubscriptionbygroup_id

    Retry subscription by groupId
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions-group/{groupid}/instances/{instance_id}/retry'.format(groupid='1', instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscriptionbygroup_id(client):
    """Test case for update_subscriptionbygroup_id

    Update Subscription by groupId
    """
    body = {"isSkipped":True,"item":[{"SubscriptionId":"string","createdAt":"2019-06-20T18:27:41.23Z","cycleCount":0,"endpoint":"string","isSkipped":True,"lastUpdate":"2019-06-20T18:27:41.23Z","metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"originalItemIndex":0,"originalOrderId":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"},"status":"ACTIVE"}],"metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"plan":{"frequency":{"interval":0,"periodicity":"string"},"type":"string","validity":{"begin":"2019-06-20T18:27:41.23Z","end":"2019-06-20T18:27:41.23Z"}},"purchaseSettings":{"currencyCode":"string","paymentMethod":{"paymentAccountId":"string","paymentSystem":"string"},"purchaseDay":"string","salesChannel":"string","selectedSla":"string","seller":"string"},"shippingAddress":{"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"},"status":"string"}
    headers = { 
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions-group/{group_id}'.format(group_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

