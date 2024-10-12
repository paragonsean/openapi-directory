# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_policytroubleshooter_v1_troubleshoot_iam_policy_request import GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequest
from openapi_server.models.google_cloud_policytroubleshooter_v1_troubleshoot_iam_policy_response import GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_policytroubleshooter_iam_troubleshoot(client):
    """Test case for policytroubleshooter_iam_troubleshoot

    
    """
    body = {"accessTuple":{"principal":"principal","fullResourceName":"fullResourceName","permission":"permission"}}
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
        path='/v1/iam:troubleshoot',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

