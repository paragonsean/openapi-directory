# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_hal_response import UserHalResponse
from openapi_server.models.users_hal_response import UsersHalResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_user_ctrl_get_user_by_id(client):
    """Test case for user_ctrl_get_user_by_id

    Get user data by account ID and user ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/users/{user_id}'.format(account_id='451496', user_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_ctrl_get_users(client):
    """Test case for user_ctrl_get_users

    Get account users data by account ID
    """
    params = [('page_size', 10),
                    ('page', 10),
                    ('first_name', 'John'),
                    ('last_name', 'Smith'),
                    ('login_name', 'jsmith'),
                    ('email', 'john.smith@example.com')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/users'.format(account_id='451496'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

