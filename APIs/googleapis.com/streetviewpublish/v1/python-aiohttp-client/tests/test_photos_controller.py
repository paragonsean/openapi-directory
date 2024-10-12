# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_delete_photos_request import BatchDeletePhotosRequest
from openapi_server.models.batch_delete_photos_response import BatchDeletePhotosResponse
from openapi_server.models.batch_get_photos_response import BatchGetPhotosResponse
from openapi_server.models.batch_update_photos_request import BatchUpdatePhotosRequest
from openapi_server.models.batch_update_photos_response import BatchUpdatePhotosResponse
from openapi_server.models.list_photos_response import ListPhotosResponse


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photos_batch_delete(client):
    """Test case for streetviewpublish_photos_batch_delete

    
    """
    body = {"photoIds":["photoIds","photoIds"]}
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
        path='/v1/photos:batchDelete',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photos_batch_get(client):
    """Test case for streetviewpublish_photos_batch_get

    
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
                    ('photoIds', ['photo_ids_example']),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/photos:batchGet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photos_batch_update(client):
    """Test case for streetviewpublish_photos_batch_update

    
    """
    body = {"updatePhotoRequests":[{"photo":{"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"},"updateMask":"updateMask"},{"photo":{"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"},"updateMask":"updateMask"}]}
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
        path='/v1/photos:batchUpdate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photos_list(client):
    """Test case for streetviewpublish_photos_list

    
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
                    ('filter', 'filter_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/photos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

