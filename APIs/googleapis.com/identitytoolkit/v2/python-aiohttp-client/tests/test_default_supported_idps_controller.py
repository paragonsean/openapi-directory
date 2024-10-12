# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_identitytoolkit_admin_v2_list_default_supported_idps_response import GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponse


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_default_supported_idps_list(client):
    """Test case for identitytoolkit_default_supported_idps_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/defaultSupportedIdps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

