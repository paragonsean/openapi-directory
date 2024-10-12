# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.join_storage_session_request import JoinStorageSessionRequest


pytestmark = pytest.mark.asyncio

async def test_join_storage_session(client):
    """Test case for join_storage_session

    
    """
    body = openapi_server.JoinStorageSessionRequest()
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
        path='/joinStorageSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

