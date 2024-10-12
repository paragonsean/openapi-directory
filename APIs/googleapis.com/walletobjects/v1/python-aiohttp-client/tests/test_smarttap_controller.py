# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.smart_tap import SmartTap


pytestmark = pytest.mark.asyncio

async def test_walletobjects_smarttap_insert(client):
    """Test case for walletobjects_smarttap_insert

    
    """
    body = {"merchantId":"merchantId","kind":"kind","id":"id","infos":[{"signUpInfo":{"classId":"classId"},"action":"ACTION_UNSPECIFIED","value":"value","url":"url"},{"signUpInfo":{"classId":"classId"},"action":"ACTION_UNSPECIFIED","value":"value","url":"url"}]}
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
        path='/walletobjects/v1/smartTap',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

