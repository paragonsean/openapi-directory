# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_credential import ChatV2Credential
from openapi_server.models.credential_enum_push_service import CredentialEnumPushService
from openapi_server.models.list_credential_response import ListCredentialResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_credential(client):
    """Test case for create_credential

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'api_key': 'api_key_example',
        'certificate': 'certificate_example',
        'friendly_name': 'friendly_name_example',
        'private_key': 'private_key_example',
        'sandbox': True,
        'secret': 'secret_example',
        'type': openapi_server.CredentialEnumPushService()
        }
    response = await client.request(
        method='POST',
        path='/v2/Credentials',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_credential(client):
    """Test case for delete_credential

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Credentials/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_credential(client):
    """Test case for fetch_credential

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Credentials/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_credential(client):
    """Test case for list_credential

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Credentials',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_credential(client):
    """Test case for update_credential

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'api_key': 'api_key_example',
        'certificate': 'certificate_example',
        'friendly_name': 'friendly_name_example',
        'private_key': 'private_key_example',
        'sandbox': True,
        'secret': 'secret_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Credentials/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

