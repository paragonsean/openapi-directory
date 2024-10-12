# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_check_request import BulkCheckRequest
from openapi_server.models.bulk_check_response import BulkCheckResponse
from openapi_server.models.check_response import CheckResponse


pytestmark = pytest.mark.asyncio

async def test_digitalassetlinks_assetlinks_bulk_check(client):
    """Test case for digitalassetlinks_assetlinks_bulk_check

    
    """
    body = {"allowGoogleInternalDataSources":True,"defaultRelation":"defaultRelation","defaultTarget":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}},"skipCacheLookup":True,"defaultSource":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}},"statements":[{"source":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}},"relation":"relation","target":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}}},{"source":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}},"relation":"relation","target":{"androidApp":{"certificate":{"sha256Fingerprint":"sha256Fingerprint"},"packageName":"packageName"},"web":{"site":"site"}}}]}
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
        path='/v1/assetlinks:bulkCheck',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digitalassetlinks_assetlinks_check(client):
    """Test case for digitalassetlinks_assetlinks_check

    
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
                    ('source.web.site', 'source_web_site_example'),
                    ('target.androidApp.certificate.sha256Fingerprint', 'target_android_app_certificate_sha256_fingerprint_example'),
                    ('target.androidApp.packageName', 'target_android_app_package_name_example'),
                    ('target.web.site', 'target_web_site_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/assetlinks:check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

