# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_enum_factor_types import AccessTokenEnumFactorTypes
from openapi_server.models.verify_v2_service_access_token import VerifyV2ServiceAccessToken


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_access_token(client):
    """Test case for create_access_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'factor_friendly_name': 'factor_friendly_name_example',
        'factor_type': openapi_server.AccessTokenEnumFactorTypes(),
        'identity': 'identity_example',
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/AccessTokens'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_access_token(client):
    """Test case for fetch_access_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/AccessTokens/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

