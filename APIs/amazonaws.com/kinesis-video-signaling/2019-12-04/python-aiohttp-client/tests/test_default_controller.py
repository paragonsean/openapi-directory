# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_ice_server_config_request import GetIceServerConfigRequest
from openapi_server.models.get_ice_server_config_response import GetIceServerConfigResponse
from openapi_server.models.send_alexa_offer_to_master_request import SendAlexaOfferToMasterRequest
from openapi_server.models.send_alexa_offer_to_master_response import SendAlexaOfferToMasterResponse


pytestmark = pytest.mark.asyncio

async def test_get_ice_server_config(client):
    """Test case for get_ice_server_config

    
    """
    body = {"ChannelARN":"","Username":"","ClientId":"","Service":""}
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
        path='/v1/get-ice-server-config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_alexa_offer_to_master(client):
    """Test case for send_alexa_offer_to_master

    
    """
    body = {"ChannelARN":"","SenderClientId":"","MessagePayload":""}
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
        path='/v1/send-alexa-offer-to-master',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

