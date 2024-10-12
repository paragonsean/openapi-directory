# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_maps_playablelocations_v3_log_impressions_request import GoogleMapsPlayablelocationsV3LogImpressionsRequest
from openapi_server.models.google_maps_playablelocations_v3_log_player_reports_request import GoogleMapsPlayablelocationsV3LogPlayerReportsRequest
from openapi_server.models.google_maps_playablelocations_v3_sample_playable_locations_request import GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest
from openapi_server.models.google_maps_playablelocations_v3_sample_playable_locations_response import GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse


pytestmark = pytest.mark.asyncio

async def test_playablelocations_log_impressions(client):
    """Test case for playablelocations_log_impressions

    
    """
    body = {"requestId":"requestId","clientInfo":{"applicationVersion":"applicationVersion","apiClient":"apiClient","operatingSystemBuild":"operatingSystemBuild","deviceModel":"deviceModel","applicationId":"applicationId","languageCode":"languageCode","operatingSystem":"operatingSystem","platform":"PLATFORM_UNSPECIFIED"},"impressions":[{"gameObjectType":0,"locationName":"locationName","impressionType":"IMPRESSION_TYPE_UNSPECIFIED"},{"gameObjectType":0,"locationName":"locationName","impressionType":"IMPRESSION_TYPE_UNSPECIFIED"}]}
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
        path='/v3:logImpressions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playablelocations_log_player_reports(client):
    """Test case for playablelocations_log_player_reports

    
    """
    body = {"playerReports":[{"locationName":"locationName","reasons":["BAD_LOCATION_REASON_UNSPECIFIED","BAD_LOCATION_REASON_UNSPECIFIED"],"languageCode":"languageCode","reasonDetails":"reasonDetails"},{"locationName":"locationName","reasons":["BAD_LOCATION_REASON_UNSPECIFIED","BAD_LOCATION_REASON_UNSPECIFIED"],"languageCode":"languageCode","reasonDetails":"reasonDetails"}],"requestId":"requestId","clientInfo":{"applicationVersion":"applicationVersion","apiClient":"apiClient","operatingSystemBuild":"operatingSystemBuild","deviceModel":"deviceModel","applicationId":"applicationId","languageCode":"languageCode","operatingSystem":"operatingSystem","platform":"PLATFORM_UNSPECIFIED"}}
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
        path='/v3:logPlayerReports',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playablelocations_sample_playable_locations(client):
    """Test case for playablelocations_sample_playable_locations

    
    """
    body = {"criteria":[{"filter":{"includedTypes":["includedTypes","includedTypes"],"spacing":{"pointType":"POINT_TYPE_UNSPECIFIED","minSpacingMeters":6.027456183070403},"maxLocationCount":0},"fieldsToReturn":"fieldsToReturn","gameObjectType":1},{"filter":{"includedTypes":["includedTypes","includedTypes"],"spacing":{"pointType":"POINT_TYPE_UNSPECIFIED","minSpacingMeters":6.027456183070403},"maxLocationCount":0},"fieldsToReturn":"fieldsToReturn","gameObjectType":1}],"areaFilter":{"s2CellId":"s2CellId"}}
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
        path='/v3:samplePlayableLocations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

