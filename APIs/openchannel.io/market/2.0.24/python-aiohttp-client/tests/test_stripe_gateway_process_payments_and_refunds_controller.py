# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts import Accounts
from openapi_server.models.cards import Cards
from openapi_server.models.developer_token import DeveloperToken


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_developer_developer_id_accounts_get(client):
    """Test case for stripe_gateway_developer_developer_id_accounts_get

    Returns a developers connected Stripe accounts
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/stripe-gateway/developer/{developer_id}/accounts'.format(developer_id='developer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_developer_developer_id_accounts_post(client):
    """Test case for stripe_gateway_developer_developer_id_accounts_post

    Generate a temporary URL to allow a developer to connect their Stripe account
    """
    params = [('redirectUrl', 'redirect_url_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/stripe-gateway/developer/{developer_id}/accounts'.format(developer_id='developer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_developer_developer_id_accounts_stripe_id_delete(client):
    """Test case for stripe_gateway_developer_developer_id_accounts_stripe_id_delete

    Disconnects a developer's Stripe account
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/stripe-gateway/developer/{developer_id}/accounts/{stripe_id}'.format(developer_id='developer_id_example', stripe_id='stripe_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_user_user_id_cards_card_id_delete(client):
    """Test case for stripe_gateway_user_user_id_cards_card_id_delete

    Removes a credit card for a user
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/stripe-gateway/user/{user_id}/cards/{card_id}'.format(user_id='user_id_example', card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_user_user_id_cards_card_id_post(client):
    """Test case for stripe_gateway_user_user_id_cards_card_id_post

    Updates a credit card for this user
    """
    params = [('isDefault', True),
                    ('address_city', 'address_city_example'),
                    ('address_country', 'address_country_example'),
                    ('address_line1', 'address_line1_example'),
                    ('address_line2', 'address_line2_example'),
                    ('address_state', 'address_state_example'),
                    ('address_zip', 'address_zip_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/stripe-gateway/user/{user_id}/cards/{card_id}'.format(user_id='user_id_example', card_id='card_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_user_user_id_cards_get(client):
    """Test case for stripe_gateway_user_user_id_cards_get

    Returns credit cards for this user
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/stripe-gateway/user/{user_id}/cards'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_gateway_user_user_id_cards_post(client):
    """Test case for stripe_gateway_user_user_id_cards_post

    Adds credit card for this user
    """
    params = [('token', 'token_example'),
                    ('isDefault', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/stripe-gateway/user/{user_id}/cards'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

