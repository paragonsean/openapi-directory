# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_factor_enum_factor_types import NewFactorEnumFactorTypes
from openapi_server.models.new_factor_enum_notification_platforms import NewFactorEnumNotificationPlatforms
from openapi_server.models.new_factor_enum_totp_algorithms import NewFactorEnumTotpAlgorithms
from openapi_server.models.verify_v2_service_entity_new_factor import VerifyV2ServiceEntityNewFactor


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_new_factor(client):
    """Test case for create_new_factor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'binding_alg': 'binding_alg_example',
        'binding_public_key': 'binding_public_key_example',
        'binding_secret': 'binding_secret_example',
        'config_alg': openapi_server.NewFactorEnumTotpAlgorithms(),
        'config_app_id': 'config_app_id_example',
        'config_code_length': 56,
        'config_notification_platform': openapi_server.NewFactorEnumNotificationPlatforms(),
        'config_notification_token': 'config_notification_token_example',
        'config_sdk_version': 'config_sdk_version_example',
        'config_skew': 56,
        'config_time_step': 56,
        'factor_type': openapi_server.NewFactorEnumFactorTypes(),
        'friendly_name': 'friendly_name_example',
        'metadata': None
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Entities/{identity}/Factors'.format(service_sid='service_sid_example', identity='identity_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

