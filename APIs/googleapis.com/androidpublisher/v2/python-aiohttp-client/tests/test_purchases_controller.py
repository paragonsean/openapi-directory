# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_purchase import ProductPurchase
from openapi_server.models.subscription_purchase import SubscriptionPurchase
from openapi_server.models.subscription_purchases_defer_request import SubscriptionPurchasesDeferRequest
from openapi_server.models.subscription_purchases_defer_response import SubscriptionPurchasesDeferResponse
from openapi_server.models.voided_purchases_list_response import VoidedPurchasesListResponse


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_products_get(client):
    """Test case for androidpublisher_purchases_products_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/purchases/products/{product_id}/tokens/{token}'.format(package_name='package_name_example', product_id='product_id_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_subscriptions_cancel(client):
    """Test case for androidpublisher_purchases_subscriptions_cancel

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{tokencance}'.format(package_name='package_name_example', subscription_id='subscription_id_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_subscriptions_defer(client):
    """Test case for androidpublisher_purchases_subscriptions_defer

    
    """
    body = {"deferralInfo":{"expectedExpiryTimeMillis":"expectedExpiryTimeMillis","desiredExpiryTimeMillis":"desiredExpiryTimeMillis"}}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{tokendefe}'.format(package_name='package_name_example', subscription_id='subscription_id_example', token='token_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_subscriptions_get(client):
    """Test case for androidpublisher_purchases_subscriptions_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{token}'.format(package_name='package_name_example', subscription_id='subscription_id_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_subscriptions_refund(client):
    """Test case for androidpublisher_purchases_subscriptions_refund

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{tokenrefun}'.format(package_name='package_name_example', subscription_id='subscription_id_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_subscriptions_revoke(client):
    """Test case for androidpublisher_purchases_subscriptions_revoke

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{tokenrevok}'.format(package_name='package_name_example', subscription_id='subscription_id_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_purchases_voidedpurchases_list(client):
    """Test case for androidpublisher_purchases_voidedpurchases_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('endTime', 'end_time_example'),
                    ('maxResults', 56),
                    ('startIndex', 56),
                    ('startTime', 'start_time_example'),
                    ('token', 'token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/purchases/voidedpurchases'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

