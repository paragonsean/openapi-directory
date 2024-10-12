# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_us_app_to_person_response import ListUsAppToPersonResponse
from openapi_server.models.messaging_v1_service_us_app_to_person import MessagingV1ServiceUsAppToPerson


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_us_app_to_person(client):
    """Test case for create_us_app_to_person

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'age_gated': True,
        'brand_registration_sid': 'brand_registration_sid_example',
        'description': 'description_example',
        'direct_lending': True,
        'has_embedded_links': True,
        'has_embedded_phone': True,
        'help_keywords': ['help_keywords_example'],
        'help_message': 'help_message_example',
        'message_flow': 'message_flow_example',
        'message_samples': ['message_samples_example'],
        'opt_in_keywords': ['opt_in_keywords_example'],
        'opt_in_message': 'opt_in_message_example',
        'opt_out_keywords': ['opt_out_keywords_example'],
        'opt_out_message': 'opt_out_message_example',
        'subscriber_opt_in': True,
        'us_app_to_person_usecase': 'us_app_to_person_usecase_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p'.format(messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_us_app_to_person(client):
    """Test case for delete_us_app_to_person

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}'.format(messaging_service_sid='messaging_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_us_app_to_person(client):
    """Test case for fetch_us_app_to_person

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}'.format(messaging_service_sid='messaging_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_us_app_to_person(client):
    """Test case for list_us_app_to_person

    
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
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p'.format(messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_us_app_to_person(client):
    """Test case for update_us_app_to_person

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'age_gated': True,
        'description': 'description_example',
        'direct_lending': True,
        'has_embedded_links': True,
        'has_embedded_phone': True,
        'message_flow': 'message_flow_example',
        'message_samples': ['message_samples_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}'.format(messaging_service_sid='messaging_service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

