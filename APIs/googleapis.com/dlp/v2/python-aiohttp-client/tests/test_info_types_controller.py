# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_privacy_dlp_v2_list_info_types_response import GooglePrivacyDlpV2ListInfoTypesResponse


pytestmark = pytest.mark.asyncio

async def test_dlp_info_types_list(client):
    """Test case for dlp_info_types_list

    
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
                    ('filter', 'filter_example'),
                    ('languageCode', 'language_code_example'),
                    ('locationId', 'location_id_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/infoTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

