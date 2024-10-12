# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_identitytoolkit_v2_password_policy import GoogleCloudIdentitytoolkitV2PasswordPolicy
from openapi_server.models.google_cloud_identitytoolkit_v2_recaptcha_config import GoogleCloudIdentitytoolkitV2RecaptchaConfig


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_get_password_policy(client):
    """Test case for identitytoolkit_get_password_policy

    
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
                    ('tenantId', 'tenant_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/passwordPolicy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_get_recaptcha_config(client):
    """Test case for identitytoolkit_get_recaptcha_config

    
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
                    ('clientType', 'client_type_example'),
                    ('tenantId', 'tenant_id_example'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/recaptchaConfig',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

