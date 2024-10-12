# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_servicebroker_get_iam_policy(client):
    """Test case for servicebroker_get_iam_policy

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_set_iam_policy(client):
    """Test case for servicebroker_set_iam_policy

    
    """
    body = openapi_server.GoogleIamV1SetIamPolicyRequest()
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_test_iam_permissions(client):
    """Test case for servicebroker_test_iam_permissions

    
    """
    body = openapi_server.GoogleIamV1TestIamPermissionsRequest()
    params = [('$.xgafv', 'xgafv_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('callback', 'param_callback_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

