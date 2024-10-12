# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_exception import BadRequestException
from openapi_server.models.put_events_request import PutEventsRequest


pytestmark = pytest.mark.asyncio

async def test_put_events(client):
    """Test case for put_events

    
    """
    body = openapi_server.PutEventsRequest()
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
        'x_amz_client_context': 'x_amz_client_context_example',
        'x_amz_client_context_encoding': 'x_amz_client_context_encoding_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2014-06-05/events#x-amz-Client-Context',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

