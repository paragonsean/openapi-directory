# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_api_key_response import GenerateApiKeyResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(client):
    """Test case for post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key

    Generate new API key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}/generateApiKey'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

