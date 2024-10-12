# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.file_reference import FileReference
from openapi_server.models.get_apk_details_response import GetApkDetailsResponse


pytestmark = pytest.mark.asyncio

async def test_testing_application_detail_service_get_apk_details(client):
    """Test case for testing_application_detail_service_get_apk_details

    
    """
    body = {"gcsPath":"gcsPath"}
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
                    ('bundleLocation.gcsPath', 'bundle_location_gcs_path_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/applicationDetailService/getApkDetails',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

