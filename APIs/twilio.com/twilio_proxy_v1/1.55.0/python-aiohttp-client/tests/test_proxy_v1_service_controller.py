# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.proxy_v1_service import ProxyV1Service
from openapi_server.models.service_enum_geo_match_level import ServiceEnumGeoMatchLevel
from openapi_server.models.service_enum_number_selection_behavior import ServiceEnumNumberSelectionBehavior


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
        'callback_url': 'callback_url_example',
        'chat_instance_sid': 'chat_instance_sid_example',
        'default_ttl': 56,
        'geo_match_level': openapi_server.ServiceEnumGeoMatchLevel(),
        'intercept_callback_url': 'intercept_callback_url_example',
        'number_selection_behavior': openapi_server.ServiceEnumNumberSelectionBehavior(),
        'out_of_session_callback_url': 'out_of_session_callback_url_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services',
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
        path='/v1/Services/{sid}'.format(sid='sid_example'),
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
        path='/v1/Services/{sid}'.format(sid='sid_example'),
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
        path='/v1/Services',
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
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_url': 'callback_url_example',
        'chat_instance_sid': 'chat_instance_sid_example',
        'default_ttl': 56,
        'geo_match_level': openapi_server.ServiceEnumGeoMatchLevel(),
        'intercept_callback_url': 'intercept_callback_url_example',
        'number_selection_behavior': openapi_server.ServiceEnumNumberSelectionBehavior(),
        'out_of_session_callback_url': 'out_of_session_callback_url_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

