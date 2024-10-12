# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_price_info import ChannelPriceInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.subscription_feature import SubscriptionFeature
from openapi_server.models.subscription_info import SubscriptionInfo
from openapi_server.models.subscription_profile import SubscriptionProfile
from openapi_server.models.user_license_info import UserLicenseInfo


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    Get infos of all available/managed subscriptions.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_channel_prices_get(client):
    """Test case for subscriptions_subscription_id_channel_prices_get

    Returns the subscription's channel price information.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/channelPrices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_features_get(client):
    """Test case for subscriptions_subscription_id_features_get

    Returns the features of a specified subscription.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/features'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_get(client):
    """Test case for subscriptions_subscription_id_get

    Get infos of a specific subscription.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_subscriptions_subscription_id_profile_put(client):
    """Test case for subscriptions_subscription_id_profile_put

    Updates a subscriptions profile.
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/subscriptions/{subscription_id}/profile'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_user_licenses_get(client):
    """Test case for subscriptions_subscription_id_user_licenses_get

    Gets a subscription's user licenses.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/userLicenses'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

