# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_tags_request import CreateOrUpdateTagsRequest
from openapi_server.models.create_or_update_tags_response import CreateOrUpdateTagsResponse
from openapi_server.models.verify_token_request import VerifyTokenRequest


pytestmark = pytest.mark.asyncio

async def test_playgrouping_apps_tokens_tags_create_or_update(client):
    """Test case for playgrouping_apps_tokens_tags_create_or_update

    
    """
    body = {"tags":[{"int64Value":"int64Value","stringValue":"stringValue","booleanValue":True,"timeValue":"timeValue","key":"key"},{"int64Value":"int64Value","stringValue":"stringValue","booleanValue":True,"timeValue":"timeValue","key":"key"}]}
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
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{app_package}/{token}/tags:createOrUpdate'.format(app_package='app_package_example', token='token_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playgrouping_apps_tokens_verify(client):
    """Test case for playgrouping_apps_tokens_verify

    
    """
    body = {"persona":"persona"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{app_package}/{tokenverif}'.format(app_package='app_package_example', token='token_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

