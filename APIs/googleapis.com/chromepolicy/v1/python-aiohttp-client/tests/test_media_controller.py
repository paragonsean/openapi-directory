# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_chrome_policy_versions_v1_upload_policy_file_request import GoogleChromePolicyVersionsV1UploadPolicyFileRequest
from openapi_server.models.google_chrome_policy_versions_v1_upload_policy_file_response import GoogleChromePolicyVersionsV1UploadPolicyFileResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_chromepolicy_media_upload(client):
    """Test case for chromepolicy_media_upload

    
    """
    body = openapi_server.GoogleChromePolicyVersionsV1UploadPolicyFileRequest()
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
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{customer}/policies/files:uploadPolicyFile'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

