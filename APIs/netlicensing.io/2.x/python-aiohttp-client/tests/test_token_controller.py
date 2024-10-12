# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_token(client):
    """Test case for create_token

    Create token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'action': 'action_example',
        'api_key_role': 'api_key_role_example',
        'cancel_url': 'cancel_url_example',
        'cancel_url_title': 'cancel_url_title_example',
        'license_template_number': 'license_template_number_example',
        'licensee_number': 'licensee_number_example',
        'predefined_shopping_item': 'predefined_shopping_item_example',
        'private_key': 'private_key_example',
        'product_number': 'product_number_example',
        'success_url': 'success_url_example',
        'success_url_title': 'success_url_title_example',
        'token_type': 'token_type_example',
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_token(client):
    """Test case for delete_token

    Delete token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/token/{token_number}'.format(token_number='token_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token(client):
    """Test case for get_token

    Get token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/token/{token_number}'.format(token_number='token_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tokens(client):
    """Test case for list_tokens

    List Tokens
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

