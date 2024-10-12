# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.photo import Photo
from openapi_server.models.upload_ref import UploadRef


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_create(client):
    """Test case for streetviewpublish_photo_create

    
    """
    body = {"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"}
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
        path='/v1/photo',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_delete(client):
    """Test case for streetviewpublish_photo_delete

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/photo/{photo_id}'.format(photo_id='photo_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_get(client):
    """Test case for streetviewpublish_photo_get

    
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
                    ('languageCode', 'language_code_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/photo/{photo_id}'.format(photo_id='photo_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_start_upload(client):
    """Test case for streetviewpublish_photo_start_upload

    
    """
    body = None
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
        path='/v1/photo:startUpload',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_update(client):
    """Test case for streetviewpublish_photo_update

    
    """
    body = {"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/photo/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

