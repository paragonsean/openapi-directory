# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.factor_enum_totp_algorithms import FactorEnumTotpAlgorithms
from openapi_server.models.list_factor_response import ListFactorResponse
from openapi_server.models.verify_v2_service_entity_factor import VerifyV2ServiceEntityFactor


pytestmark = pytest.mark.asyncio

async def test_delete_factor(client):
    """Test case for delete_factor

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}'.format(service_sid='service_sid_example', identity='identity_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_factor(client):
    """Test case for fetch_factor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}'.format(service_sid='service_sid_example', identity='identity_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_factor(client):
    """Test case for list_factor

    
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
        path='/v2/Services/{service_sid}/Entities/{identity}/Factors'.format(service_sid='service_sid_example', identity='identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_factor(client):
    """Test case for update_factor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auth_payload': 'auth_payload_example',
        'config_alg': openapi_server.FactorEnumTotpAlgorithms(),
        'config_code_length': 56,
        'config_notification_platform': 'config_notification_platform_example',
        'config_notification_token': 'config_notification_token_example',
        'config_sdk_version': 'config_sdk_version_example',
        'config_skew': 56,
        'config_time_step': 56,
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}'.format(service_sid='service_sid_example', identity='identity_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

