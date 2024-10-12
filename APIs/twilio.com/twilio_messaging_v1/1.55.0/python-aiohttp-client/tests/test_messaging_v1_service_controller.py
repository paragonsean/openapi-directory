# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.messaging_v1_service import MessagingV1Service
from openapi_server.models.service_enum_scan_message_content import ServiceEnumScanMessageContent


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
        'area_code_geomatch': True,
        'fallback_method': 'fallback_method_example',
        'fallback_to_long_code': True,
        'fallback_url': 'fallback_url_example',
        'friendly_name': 'friendly_name_example',
        'inbound_method': 'inbound_method_example',
        'inbound_request_url': 'inbound_request_url_example',
        'mms_converter': True,
        'scan_message_content': openapi_server.ServiceEnumScanMessageContent(),
        'smart_encoding': True,
        'status_callback': 'status_callback_example',
        'sticky_sender': True,
        'synchronous_validation': True,
        'use_inbound_webhook_on_number': True,
        'usecase': 'usecase_example',
        'validity_period': 56
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
        'area_code_geomatch': True,
        'fallback_method': 'fallback_method_example',
        'fallback_to_long_code': True,
        'fallback_url': 'fallback_url_example',
        'friendly_name': 'friendly_name_example',
        'inbound_method': 'inbound_method_example',
        'inbound_request_url': 'inbound_request_url_example',
        'mms_converter': True,
        'scan_message_content': openapi_server.ServiceEnumScanMessageContent(),
        'smart_encoding': True,
        'status_callback': 'status_callback_example',
        'sticky_sender': True,
        'synchronous_validation': True,
        'use_inbound_webhook_on_number': True,
        'usecase': 'usecase_example',
        'validity_period': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

