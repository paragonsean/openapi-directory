# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_public_v1_policies_types_contacts_get200_response import ApiPublicV1PoliciesTypesContactsGet200Response
from openapi_server.models.api_public_v1_policies_types_notifications_get200_response import ApiPublicV1PoliciesTypesNotificationsGet200Response
from openapi_server.models.api_public_v1_policies_types_timeouts_get200_response import ApiPublicV1PoliciesTypesTimeoutsGet200Response


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_policies_types_contacts_get(client):
    """Test case for api_public_v1_policies_types_contacts_get

    Get the available contact types
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/policies/types/contacts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_policies_types_notifications_get(client):
    """Test case for api_public_v1_policies_types_notifications_get

    Get the available notification types
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/policies/types/notifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_policies_types_timeouts_get(client):
    """Test case for api_public_v1_policies_types_timeouts_get

    Get the available timeout values
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/policies/types/timeouts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

