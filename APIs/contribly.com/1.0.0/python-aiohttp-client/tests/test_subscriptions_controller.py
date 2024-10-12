# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_submission import SubscriptionSubmission
from openapi_server.models.subscription_type import SubscriptionType


pytestmark = pytest.mark.asyncio

async def test_subscription_types_get(client):
    """Test case for subscription_types_get

    Subscription types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/subscription-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    List subscriptions for the authorised user.
    """
    body = {"types":["types","types"],"includeBody":True,"assignment":"assignment","slackChannel":"slackChannel","includeThumbenail":True,"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_id_delete(client):
    """Test case for subscriptions_id_delete

    Delete a subscription.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/1/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

