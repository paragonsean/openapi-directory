# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration_address_enum_auto_creation_type import ConfigurationAddressEnumAutoCreationType
from openapi_server.models.configuration_address_enum_method import ConfigurationAddressEnumMethod
from openapi_server.models.configuration_address_enum_type import ConfigurationAddressEnumType
from openapi_server.models.conversations_v1_configuration_address import ConversationsV1ConfigurationAddress
from openapi_server.models.list_configuration_address_response import ListConfigurationAddressResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_configuration_address(client):
    """Test case for create_configuration_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address': 'address_example',
        'address_country': 'address_country_example',
        'auto_creation_conversation_service_sid': 'auto_creation_conversation_service_sid_example',
        'auto_creation_enabled': True,
        'auto_creation_studio_flow_sid': 'auto_creation_studio_flow_sid_example',
        'auto_creation_studio_retry_count': 56,
        'auto_creation_type': openapi_server.ConfigurationAddressEnumAutoCreationType(),
        'auto_creation_webhook_filters': ['auto_creation_webhook_filters_example'],
        'auto_creation_webhook_method': openapi_server.ConfigurationAddressEnumMethod(),
        'auto_creation_webhook_url': 'auto_creation_webhook_url_example',
        'friendly_name': 'friendly_name_example',
        'type': openapi_server.ConfigurationAddressEnumType()
        }
    response = await client.request(
        method='POST',
        path='/v1/Configuration/Addresses',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_configuration_address(client):
    """Test case for delete_configuration_address

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Configuration/Addresses/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_configuration_address(client):
    """Test case for fetch_configuration_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Configuration/Addresses/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_configuration_address(client):
    """Test case for list_configuration_address

    
    """
    params = [('Type', 'type_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Configuration/Addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_configuration_address(client):
    """Test case for update_configuration_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auto_creation_conversation_service_sid': 'auto_creation_conversation_service_sid_example',
        'auto_creation_enabled': True,
        'auto_creation_studio_flow_sid': 'auto_creation_studio_flow_sid_example',
        'auto_creation_studio_retry_count': 56,
        'auto_creation_type': openapi_server.ConfigurationAddressEnumAutoCreationType(),
        'auto_creation_webhook_filters': ['auto_creation_webhook_filters_example'],
        'auto_creation_webhook_method': openapi_server.ConfigurationAddressEnumMethod(),
        'auto_creation_webhook_url': 'auto_creation_webhook_url_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Configuration/Addresses/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

