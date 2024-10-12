# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_messaging_configuration_response import ListMessagingConfigurationResponse
from openapi_server.models.verify_v2_service_messaging_configuration import VerifyV2ServiceMessagingConfiguration


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_messaging_configuration(client):
    """Test case for create_messaging_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'country': 'country_example',
        'messaging_service_sid': 'messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/MessagingConfigurations'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_messaging_configuration(client):
    """Test case for delete_messaging_configuration

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/MessagingConfigurations/{country}'.format(service_sid='service_sid_example', country='country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_messaging_configuration(client):
    """Test case for fetch_messaging_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/MessagingConfigurations/{country}'.format(service_sid='service_sid_example', country='country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_messaging_configuration(client):
    """Test case for list_messaging_configuration

    
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
        path='/v2/Services/{service_sid}/MessagingConfigurations'.format(service_sid='service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_messaging_configuration(client):
    """Test case for update_messaging_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'messaging_service_sid': 'messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/MessagingConfigurations/{country}'.format(service_sid='service_sid_example', country='country_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

