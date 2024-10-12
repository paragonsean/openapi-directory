# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.send_command_request import SendCommandRequest
from openapi_server.models.send_command_result import SendCommandResult


pytestmark = pytest.mark.asyncio

async def test_send_command(client):
    """Test case for send_command

    
    """
    body = {"CommitTransaction":{"CommitDigest":"","TransactionId":""},"ExecuteStatement":{"Parameters":"","Statement":"","TransactionId":""},"SessionToken":"","FetchPage":{"NextPageToken":"","TransactionId":""},"EndSession":"","AbortTransaction":"","StartSession":{"LedgerName":""},"StartTransaction":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=QLDBSession.SendCommand',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

