# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.send_ssh_public_key_request import SendSSHPublicKeyRequest
from openapi_server.models.send_ssh_public_key_response import SendSSHPublicKeyResponse
from openapi_server.models.send_serial_console_ssh_public_key_request import SendSerialConsoleSSHPublicKeyRequest
from openapi_server.models.send_serial_console_ssh_public_key_response import SendSerialConsoleSSHPublicKeyResponse


pytestmark = pytest.mark.asyncio

async def test_send_serial_console_ssh_public_key(client):
    """Test case for send_serial_console_ssh_public_key

    
    """
    body = {"SerialPort":"","InstanceId":"","SSHPublicKey":""}
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
        path='/#X-Amz-Target=AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_ssh_public_key(client):
    """Test case for send_ssh_public_key

    
    """
    body = {"InstanceOSUser":"","InstanceId":"","SSHPublicKey":"","AvailabilityZone":""}
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
        path='/#X-Amz-Target=AWSEC2InstanceConnectService.SendSSHPublicKey',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

