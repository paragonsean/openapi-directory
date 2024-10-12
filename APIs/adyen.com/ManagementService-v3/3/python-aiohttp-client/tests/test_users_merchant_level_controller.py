# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_merchant_user_request import CreateMerchantUserRequest
from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.list_merchant_users_response import ListMerchantUsersResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_merchant_user_request import UpdateMerchantUserRequest
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_users(client):
    """Test case for get_merchants_merchant_id_users

    Get a list of users
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/users'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_users_user_id(client):
    """Test case for get_merchants_merchant_id_users_user_id

    Get user details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/users/{user_id}'.format(merchant_id='merchant_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_users_user_id(client):
    """Test case for patch_merchants_merchant_id_users_user_id

    Update a user
    """
    body = {"timeZoneCode":"timeZoneCode","roles":["roles","roles"],"name":{"firstName":"firstName","lastName":"lastName"},"active":True,"accountGroups":["accountGroups","accountGroups"],"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/users/{user_id}'.format(merchant_id='merchant_id_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_users(client):
    """Test case for post_merchants_merchant_id_users

    Create a new user
    """
    body = {"timeZoneCode":"timeZoneCode","roles":["roles","roles"],"name":{"firstName":"firstName","lastName":"lastName"},"accountGroups":["accountGroups","accountGroups"],"email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/users'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

