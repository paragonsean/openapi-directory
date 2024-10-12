# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_maps_places_v1_autocomplete_places_request import GoogleMapsPlacesV1AutocompletePlacesRequest
from openapi_server.models.google_maps_places_v1_autocomplete_places_response import GoogleMapsPlacesV1AutocompletePlacesResponse
from openapi_server.models.google_maps_places_v1_photo_media import GoogleMapsPlacesV1PhotoMedia
from openapi_server.models.google_maps_places_v1_search_nearby_request import GoogleMapsPlacesV1SearchNearbyRequest
from openapi_server.models.google_maps_places_v1_search_nearby_response import GoogleMapsPlacesV1SearchNearbyResponse
from openapi_server.models.google_maps_places_v1_search_text_request import GoogleMapsPlacesV1SearchTextRequest
from openapi_server.models.google_maps_places_v1_search_text_response import GoogleMapsPlacesV1SearchTextResponse


pytestmark = pytest.mark.asyncio

async def test_places_places_autocomplete(client):
    """Test case for places_places_autocomplete

    
    """
    body = {"includedPrimaryTypes":["includedPrimaryTypes","includedPrimaryTypes"],"locationBias":{"rectangle":{"high":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"low":{"latitude":6.027456183070403,"longitude":1.4658129805029452}},"circle":{"center":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"radius":5.962133916683182}},"input":"input","regionCode":"regionCode","origin":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"inputOffset":0,"sessionToken":"sessionToken","locationRestriction":{"rectangle":{"high":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"low":{"latitude":6.027456183070403,"longitude":1.4658129805029452}},"circle":{"center":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"radius":5.962133916683182}},"includeQueryPredictions":True,"languageCode":"languageCode","includedRegionCodes":["includedRegionCodes","includedRegionCodes"]}
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
        path='/v1/places:autocomplete',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_places_places_photos_get_media(client):
    """Test case for places_places_photos_get_media

    
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
                    ('maxHeightPx', 56),
                    ('maxWidthPx', 56),
                    ('skipHttpRedirect', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_places_places_search_nearby(client):
    """Test case for places_places_search_nearby

    
    """
    body = {"includedPrimaryTypes":["includedPrimaryTypes","includedPrimaryTypes"],"excludedPrimaryTypes":["excludedPrimaryTypes","excludedPrimaryTypes"],"regionCode":"regionCode","includedTypes":["includedTypes","includedTypes"],"rankPreference":"RANK_PREFERENCE_UNSPECIFIED","locationRestriction":{"circle":{"center":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"radius":5.962133916683182}},"languageCode":"languageCode","excludedTypes":["excludedTypes","excludedTypes"],"maxResultCount":0}
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
        path='/v1/places:searchNearby',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_places_places_search_text(client):
    """Test case for places_places_search_text

    
    """
    body = {"locationBias":{"rectangle":{"high":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"low":{"latitude":6.027456183070403,"longitude":1.4658129805029452}},"circle":{"center":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"radius":5.962133916683182}},"regionCode":"regionCode","includedType":"includedType","rankPreference":"RANK_PREFERENCE_UNSPECIFIED","openNow":True,"textQuery":"textQuery","locationRestriction":{"rectangle":{"high":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"low":{"latitude":6.027456183070403,"longitude":1.4658129805029452}}},"minRating":6.027456183070403,"strictTypeFiltering":True,"languageCode":"languageCode","priceLevels":["PRICE_LEVEL_UNSPECIFIED","PRICE_LEVEL_UNSPECIFIED"],"maxResultCount":0}
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
        path='/v1/places:searchText',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

