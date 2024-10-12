# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intelligence_v2_service import IntelligenceV2Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.service_enum_http_method import ServiceEnumHttpMethod


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service(client):
    """Test case for create_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auto_redaction': True,
        'auto_transcribe': True,
        'data_logging': True,
        'friendly_name': 'friendly_name_example',
        'language_code': 'language_code_example',
        'media_redaction': True,
        'unique_name': 'unique_name_example',
        'webhook_http_method': openapi_server.ServiceEnumHttpMethod(),
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service(client):
    """Test case for fetch_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service(client):
    """Test case for list_service

    
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
        path='/v2/Services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service(client):
    """Test case for update_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auto_redaction': True,
        'auto_transcribe': True,
        'data_logging': True,
        'friendly_name': 'friendly_name_example',
        'language_code': 'language_code_example',
        'media_redaction': True,
        'unique_name': 'unique_name_example',
        'webhook_http_method': openapi_server.ServiceEnumHttpMethod(),
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

