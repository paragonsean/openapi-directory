# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.decode_integrity_token_request import DecodeIntegrityTokenRequest
from openapi_server.models.decode_integrity_token_response import DecodeIntegrityTokenResponse


pytestmark = pytest.mark.asyncio

async def test_playintegrity_decode_integrity_token(client):
    """Test case for playintegrity_decode_integrity_token

    
    """
    body = {"integrityToken":"integrityToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{package_namedecode_integrity_toke}'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

