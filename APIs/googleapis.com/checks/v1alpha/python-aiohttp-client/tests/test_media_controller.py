# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_checks_report_v1alpha_analyze_upload_request import GoogleChecksReportV1alphaAnalyzeUploadRequest
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_checks_media_upload(client):
    """Test case for checks_media_upload

    
    """
    body = openapi_server.GoogleChecksReportV1alphaAnalyzeUploadRequest()
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
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/reports:analyzeUpload'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

