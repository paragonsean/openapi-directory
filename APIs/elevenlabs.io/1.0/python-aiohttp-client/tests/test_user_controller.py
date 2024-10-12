# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.extended_subscription_response_model import ExtendedSubscriptionResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.user_response_model import UserResponseModel


pytestmark = pytest.mark.asyncio

async def test_get_user_info_v1_user_get(client):
    """Test case for get_user_info_v1_user_get

    Get User Info
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_subscription_info_v1_user_subscription_get(client):
    """Test case for get_user_subscription_info_v1_user_subscription_get

    Get User Subscription Info
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/subscription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

