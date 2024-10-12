# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_response import AccessResponse
from openapi_server.models.getaccesstoken_id_request import GetaccesstokenIdRequest
from openapi_server.models.sample import Sample


pytestmark = pytest.mark.asyncio

async def test_get_authorization_code_id(client):
    """Test case for get_authorization_code_id

    Get Authorization Code
    """
    params = [('client_id', 'client_id_example'),
                    ('response_type', 'response_type_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('state', 'state_example'),
                    ('Code_challenge', 'base64_url_encode_without_padding(sha256(code_verifier))'),
                    ('Code_challenge_method', 'code_challenge_method_example'),
                    ('dl_flow', 'dl_flow_example'),
                    ('Verified_mobile', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getaccesstoken_id(client):
    """Test case for getaccesstoken_id

    Get Access Token
    """
    body = openapi_server.GetaccesstokenIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

