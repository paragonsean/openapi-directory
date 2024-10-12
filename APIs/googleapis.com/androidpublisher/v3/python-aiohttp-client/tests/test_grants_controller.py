# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.grant import Grant


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_grants_create(client):
    """Test case for androidpublisher_grants_create

    
    """
    body = {"name":"name","packageName":"packageName","appLevelPermissions":["APP_LEVEL_PERMISSION_UNSPECIFIED","APP_LEVEL_PERMISSION_UNSPECIFIED"]}
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
        path='/androidpublisher/v3/{parent}/grants'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

