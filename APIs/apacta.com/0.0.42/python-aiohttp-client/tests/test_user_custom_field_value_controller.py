# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.users_user_id_user_custom_field_value_get200_response import UsersUserIdUserCustomFieldValueGet200Response
from openapi_server.models.users_user_id_user_custom_field_value_user_custom_field_value_id_get200_response import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response
from openapi_server.models.users_user_id_user_custom_field_value_user_custom_field_value_id_put200_response import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response


pytestmark = pytest.mark.asyncio

async def test_users_user_id_user_custom_field_value_get(client):
    """Test case for users_user_id_user_custom_field_value_get

    Get a list of user custom field values
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/user_custom_field_value'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_user_custom_field_value_user_custom_field_value_id_get(client):
    """Test case for users_user_id_user_custom_field_value_user_custom_field_value_id_get

    Get a single record of user custom field value
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/user_custom_field_value/{user_custom_field_value_id}'.format(user_id='user_id_example', user_custom_field_value_id='user_custom_field_value_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_user_custom_field_value_user_custom_field_value_id_put(client):
    """Test case for users_user_id_user_custom_field_value_user_custom_field_value_id_put

    Update a single record of user custom field value
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/users/{user_id}/user_custom_field_value/{user_custom_field_value_id}'.format(user_id='user_id_example', user_custom_field_value_id='user_custom_field_value_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

