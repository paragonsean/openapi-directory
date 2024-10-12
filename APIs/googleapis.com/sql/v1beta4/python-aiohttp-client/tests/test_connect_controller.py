# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connect_settings import ConnectSettings
from openapi_server.models.generate_ephemeral_cert_request import GenerateEphemeralCertRequest
from openapi_server.models.generate_ephemeral_cert_response import GenerateEphemeralCertResponse


pytestmark = pytest.mark.asyncio

async def test_sql_connect_generate_ephemeral(client):
    """Test case for sql_connect_generate_ephemeral

    
    """
    body = {"access_token":"access_token","public_key":"public_key","readTime":"readTime","validDuration":"validDuration"}
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
        path='/sql/v1beta4/projects/{project}/instances/{instancegenerate_ephemeral_cer}'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_connect_get(client):
    """Test case for sql_connect_get

    
    """
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
                    ('uploadType', 'upload_type_example'),
                    ('readTime', 'read_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/connectSettings'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

