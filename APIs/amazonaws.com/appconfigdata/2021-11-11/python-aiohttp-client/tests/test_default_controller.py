# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_latest_configuration_response import GetLatestConfigurationResponse
from openapi_server.models.start_configuration_session_request import StartConfigurationSessionRequest
from openapi_server.models.start_configuration_session_response import StartConfigurationSessionResponse


pytestmark = pytest.mark.asyncio

async def test_get_latest_configuration(client):
    """Test case for get_latest_configuration

    
    """
    params = [('configuration_token', 'configuration_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/configuration#configuration_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_configuration_session(client):
    """Test case for start_configuration_session

    
    """
    body = {"ConfigurationProfileIdentifier":"","EnvironmentIdentifier":"","ApplicationIdentifier":"","RequiredMinimumPollIntervalInSeconds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/configurationsessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

