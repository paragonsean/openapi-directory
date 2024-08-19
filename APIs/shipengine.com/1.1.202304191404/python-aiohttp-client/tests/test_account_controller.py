# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_account_settings_image_request_body import CreateAccountSettingsImageRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_account_settings_images_response_body import GetAccountSettingsImagesResponseBody
from openapi_server.models.get_account_settings_response_body import GetAccountSettingsResponseBody
from openapi_server.models.list_account_settings_images_response_body import ListAccountSettingsImagesResponseBody
from openapi_server.models.update_account_settings_image_request_body import UpdateAccountSettingsImageRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_account_image(client):
    """Test case for create_account_image

    Create an Account Image
    """
    body = openapi_server.CreateAccountSettingsImageRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/settings/images',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account_image_by_id(client):
    """Test case for delete_account_image_by_id

    Delete Account Image By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/account/settings/images/{label_image_id}'.format(label_image_id='label_image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_settings_images_by_id(client):
    """Test case for get_account_settings_images_by_id

    Get Account Image By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/settings/images/{label_image_id}'.format(label_image_id='label_image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_images(client):
    """Test case for list_account_images

    List Account Images
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/settings/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_settings(client):
    """Test case for list_account_settings

    List Account Settings
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_settings_images_by_id(client):
    """Test case for update_account_settings_images_by_id

    Update Account Image By ID
    """
    body = openapi_server.UpdateAccountSettingsImageRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/account/settings/images/{label_image_id}'.format(label_image_id='label_image_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

