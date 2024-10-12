# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.product_group import ProductGroup
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_list import SubscriptionList
from openapi_server.models.subscription_update import SubscriptionUpdate


pytestmark = pytest.mark.asyncio

async def test_cancel(client):
    """Test case for cancel

    Cancel the specified Subscription
    """
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Retrieve details for the specified Subscription
    """
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    Retrieve a list of Subscriptions for the specified Shopper
    """
    params = [('productGroupKeys', ['product_group_keys_example']),
                    ('includes', ['includes_example']),
                    ('offset', 0),
                    ('limit', 25),
                    ('sort', -expiresAt)]
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_groups(client):
    """Test case for product_groups

    Retrieve a list of ProductGroups for the specified Shopper
    """
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions/productGroups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update(client):
    """Test case for update

    Update details for the specified Subscription
    """
    body = {"paymentProfileId":0,"renewAuto":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

