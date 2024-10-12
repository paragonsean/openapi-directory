# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creative_asset_metadata import CreativeAssetMetadata


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_dfareporting_creative_assets_insert(client):
    """Test case for dfareporting_creative_assets_insert

    
    """
    body = openapi_server.CreativeAssetMetadata()
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/creativeAssets/{advertiser_id}/creativeAssets'.format(profile_id='profile_id_example', advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

