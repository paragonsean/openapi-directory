# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_raw_message_content_response import GetRawMessageContentResponse
from openapi_server.models.put_raw_message_content_request import PutRawMessageContentRequest


pytestmark = pytest.mark.asyncio

async def test_get_raw_message_content(client):
    """Test case for get_raw_message_content

    
    """
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
        path='/messages/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_raw_message_content(client):
    """Test case for put_raw_message_content

    
    """
    body = {"content":{"s3Reference":{"bucket":"","objectVersion":"","key":""}}}
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
        path='/messages/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

