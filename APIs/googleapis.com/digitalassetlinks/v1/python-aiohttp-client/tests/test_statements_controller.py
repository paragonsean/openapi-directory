# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_response import ListResponse


pytestmark = pytest.mark.asyncio

async def test_digitalassetlinks_statements_list(client):
    """Test case for digitalassetlinks_statements_list

    
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
                    ('relation', 'relation_example'),
                    ('source.androidApp.certificate.sha256Fingerprint', 'source_android_app_certificate_sha256_fingerprint_example'),
                    ('source.androidApp.packageName', 'source_android_app_package_name_example'),
                    ('source.web.site', 'source_web_site_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/statements:list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

