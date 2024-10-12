# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_asset_v1p7beta1_export_assets_request import GoogleCloudAssetV1p7beta1ExportAssetsRequest
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_cloudasset_export_assets(client):
    """Test case for cloudasset_export_assets

    
    """
    body = {"assetTypes":["assetTypes","assetTypes"],"outputConfig":{"gcsDestination":{"uriPrefix":"uriPrefix","uri":"uri"},"bigqueryDestination":{"separateTablesPerAssetType":True,"force":True,"dataset":"dataset","partitionSpec":{"partitionKey":"PARTITION_KEY_UNSPECIFIED"},"table":"table"}},"readTime":"readTime","relationshipTypes":["relationshipTypes","relationshipTypes"],"contentType":"CONTENT_TYPE_UNSPECIFIED"}
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
        path='/v1p7beta1/{parentexport_asset}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

