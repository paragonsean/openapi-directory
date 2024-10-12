# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.challenge_enum_challenge_statuses import ChallengeEnumChallengeStatuses
from openapi_server.models.challenge_enum_list_orders import ChallengeEnumListOrders
from openapi_server.models.list_challenge_response import ListChallengeResponse
from openapi_server.models.verify_v2_service_entity_challenge import VerifyV2ServiceEntityChallenge


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_challenge(client):
    """Test case for create_challenge

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auth_payload': 'auth_payload_example',
        'details_fields': None,
        'details_message': 'details_message_example',
        'expiration_date': '2013-10-20T19:20:30+01:00',
        'factor_sid': 'factor_sid_example',
        'hidden_details': None
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Entities/{identity}/Challenges'.format(service_sid='service_sid_example', identity='identity_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_challenge(client):
    """Test case for fetch_challenge

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}'.format(service_sid='service_sid_example', identity='identity_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_challenge(client):
    """Test case for list_challenge

    
    """
    params = [('FactorSid', 'factor_sid_example'),
                    ('Status', openapi_server.ChallengeEnumChallengeStatuses()),
                    ('Order', openapi_server.ChallengeEnumListOrders()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Entities/{identity}/Challenges'.format(service_sid='service_sid_example', identity='identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_challenge(client):
    """Test case for update_challenge

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auth_payload': 'auth_payload_example',
        'metadata': None
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}'.format(service_sid='service_sid_example', identity='identity_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

