# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.user_custom_field_attributes_get200_response import UserCustomFieldAttributesGet200Response
from openapi_server.models.user_custom_field_attributes_user_custom_field_attribute_id_get200_response import UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_user_custom_field_attributes_get(client):
    """Test case for user_custom_field_attributes_get

    Get a list of user custom field attributes
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user_custom_field_attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_field_attributes_user_custom_field_attribute_id_get(client):
    """Test case for user_custom_field_attributes_user_custom_field_attribute_id_get

    Details of 1 user custom field attribute
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user_custom_field_attributes/{user_custom_field_attribute_id}'.format(user_custom_field_attribute_id='user_custom_field_attribute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

