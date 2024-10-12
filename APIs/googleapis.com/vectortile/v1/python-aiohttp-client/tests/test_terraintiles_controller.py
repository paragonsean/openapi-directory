# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.terrain_tile import TerrainTile


pytestmark = pytest.mark.asyncio

async def test_vectortile_terraintiles_get(client):
    """Test case for vectortile_terraintiles_get

    
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
                    ('altitudePrecisionCentimeters', 56),
                    ('clientInfo.apiClient', 'client_info_api_client_example'),
                    ('clientInfo.applicationId', 'client_info_application_id_example'),
                    ('clientInfo.applicationVersion', 'client_info_application_version_example'),
                    ('clientInfo.deviceModel', 'client_info_device_model_example'),
                    ('clientInfo.operatingSystem', 'client_info_operating_system_example'),
                    ('clientInfo.platform', 'client_info_platform_example'),
                    ('clientInfo.userId', 'client_info_user_id_example'),
                    ('maxElevationResolutionCells', 56),
                    ('minElevationResolutionCells', 56),
                    ('terrainFormats', ['terrain_formats_example']),
                    ('enableModeledVolumes', True),
                    ('enablePoliticalFeatures', True),
                    ('enablePrivateRoads', True),
                    ('enableUnclippedBuildings', True),
                    ('languageCode', 'language_code_example'),
                    ('regionCode', 'region_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

