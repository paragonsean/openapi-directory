# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_rns_pub_subscriptions_subscription_id_conversation_message_get200_response_inner import ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner
from openapi_server.models.simulate_response_vo import SimulateResponseVO
from openapi_server.models.subscription_group_request import SubscriptionGroupRequest
from openapi_server.models.subscription_group_response import SubscriptionGroupResponse
from openapi_server.models.subscription_thin_item_request import SubscriptionThinItemRequest
from openapi_server.models.subscription_update_request_v3 import SubscriptionUpdateRequestV3
from openapi_server.models.update_item_input import UpdateItemInput


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_subscriptions_get(client):
    """Test case for api_rns_pub_subscriptions_get

    List subscriptions
    """
    params = [('customerEmail', 'customer_email_example'),
                    ('status', 'status_example'),
                    ('addressId', 'address_id_example'),
                    ('paymentId', 'payment_id_example'),
                    ('planId', 'plan_id_example'),
                    ('nextPurchaseDate', 'next_purchase_date_example'),
                    ('originalOrderId', 'original_order_id_example'),
                    ('page', 1),
                    ('size', 15)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pub/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_subscriptions_id_get(client):
    """Test case for api_rns_pub_subscriptions_id_get

    Get subscription details
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pub/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_subscriptions_id_items_item_id_delete(client):
    """Test case for api_rns_pub_subscriptions_id_items_item_id_delete

    Remove items from a subscription.
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rns/pub/subscriptions/{id}/items/{item_id}'.format(id='id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rns_pub_subscriptions_id_items_item_id_patch(client):
    """Test case for api_rns_pub_subscriptions_id_items_item_id_patch

    Edit items on a subscription.
    """
    body = {"quantity":5,"isSkipped":True,"manualPrice":40,"status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rns/pub/subscriptions/{id}/items/{item_id}'.format(id='id_example', item_id='item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rns_pub_subscriptions_id_items_post(client):
    """Test case for api_rns_pub_subscriptions_id_items_post

    Add item to subscription
    """
    body = {"quantity":5,"manualPrice":40,"skuId":"12"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pub/subscriptions/{id}/items'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rns_pub_subscriptions_id_patch(client):
    """Test case for api_rns_pub_subscriptions_id_patch

    Update subscription
    """
    body = {"purchaseSettings":{"paymentMethod":{"paymentSystem":"4","paymentAccountId":"340357032569595","installments":3},"salesChannel":"1"},"isSkipped":False,"shippingAddress":{"addressType":"residential","addressId":"8109266555005"},"title":"catFood","plan":{"purchaseDay":"15","id":"store.subscription","validity":{"end":"2023-06-10T00:00:00","begin":"2022-06-10T00:00:00"},"frequency":{"periodicity":"MONTHLY","interval":3}},"status":"ACTIVE"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rns/pub/subscriptions/{id}'.format(id='4002961'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_subscriptions_id_simulate_post(client):
    """Test case for api_rns_pub_subscriptions_id_simulate_post

    Calculate the current prices for a specific subscription
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pub/subscriptions/{id}/simulate'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rns_pub_subscriptions_post(client):
    """Test case for api_rns_pub_subscriptions_post

    Create subscription
    """
    body = {"purchaseSettings":{"paymentMethod":{"paymentSystem":"4","paymentAccountId":"340357032569595","installments":3},"salesChannel":"1"},"customerEmail":"customerEmail","shippingAddress":{"addressType":"residential","addressId":"8109266555005"},"catalogAttachment":"catalogAttachment","title":"title","items":[{"quantity":5,"manualPrice":40,"skuId":"12"},{"quantity":5,"manualPrice":40,"skuId":"12"}],"plan":{"purchaseDay":"15","id":"store.subscription","validity":{"end":"2023-06-10T00:00:00","begin":"2022-06-10T00:00:00"},"frequency":{"periodicity":"MONTHLY","interval":3}},"nextPurchaseDate":"2000-01-23T04:56:07.000+00:00","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pub/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rns_pub_subscriptions_simulate_post(client):
    """Test case for api_rns_pub_subscriptions_simulate_post

    Calculate the current prices for the provided subscription template
    """
    body = {"purchaseSettings":{"paymentMethod":{"paymentSystem":"4","paymentAccountId":"340357032569595","installments":3},"salesChannel":"1"},"customerEmail":"customerEmail","shippingAddress":{"addressType":"residential","addressId":"8109266555005"},"catalogAttachment":"catalogAttachment","title":"title","items":[{"quantity":5,"manualPrice":40,"skuId":"12"},{"quantity":5,"manualPrice":40,"skuId":"12"}],"plan":{"purchaseDay":"15","id":"store.subscription","validity":{"end":"2023-06-10T00:00:00","begin":"2022-06-10T00:00:00"},"frequency":{"periodicity":"MONTHLY","interval":3}},"nextPurchaseDate":"2000-01-23T04:56:07.000+00:00","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pub/subscriptions/simulate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_subscriptions_subscription_id_conversation_message_get(client):
    """Test case for api_rns_pub_subscriptions_subscription_id_conversation_message_get

    Get conversation messages
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pub/subscriptions/{subscription_id}/conversation-message'.format(subscription_id='123456789abc'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

