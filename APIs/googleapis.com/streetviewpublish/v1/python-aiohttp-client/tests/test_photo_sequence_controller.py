# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.photo_sequence import PhotoSequence
from openapi_server.models.upload_ref import UploadRef


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_sequence_create(client):
    """Test case for streetviewpublish_photo_sequence_create

    
    """
    body = {"captureTimeOverride":"captureTimeOverride","distanceMeters":0.8008281904610115,"uploadReference":{"uploadUrl":"uploadUrl"},"gpsSource":"PHOTO_SEQUENCE","uploadTime":"uploadTime","photos":[{"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"},{"transferStatus":"TRANSFER_STATUS_UNKNOWN","captureTime":"captureTime","pose":{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},"downloadUrl":"downloadUrl","uploadReference":{"uploadUrl":"uploadUrl"},"photoId":{"id":"id"},"shareLink":"shareLink","uploadTime":"uploadTime","places":[{"name":"name","placeId":"placeId","languageCode":"languageCode"},{"name":"name","placeId":"placeId","languageCode":"languageCode"}],"viewCount":"viewCount","mapsPublishStatus":"UNSPECIFIED_MAPS_PUBLISH_STATUS","connections":[{"target":{"id":"id"}},{"target":{"id":"id"}}],"thumbnailUrl":"thumbnailUrl"}],"imu":{"gyroRps":[{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377},{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377}],"accelMpsps":[{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377},{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377}],"magUt":[{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377},{"captureTime":"captureTime","x":1.4658129,"y":5.962134,"z":5.637377}]},"processingState":"PROCESSING_STATE_UNSPECIFIED","filename":"filename","failureDetails":{"gpsDataGapDetails":{"gapStartTime":"gapStartTime","gapDuration":"gapDuration"},"imuDataGapDetails":{"gapStartTime":"gapStartTime","gapDuration":"gapDuration"},"noOverlapGpsDetails":{"videoEndTime":"videoEndTime","videoStartTime":"videoStartTime","gpsStartTime":"gpsStartTime","gpsEndTime":"gpsEndTime"},"notOutdoorsDetails":{"startTime":"startTime"},"insufficientGpsDetails":{"gpsPointsFound":6}},"sequenceBounds":{"southwest":{"latitude":5.962133916683182,"longitude":5.637376656633329},"northeast":{"latitude":5.962133916683182,"longitude":5.637376656633329}},"failureReason":"PROCESSING_FAILURE_REASON_UNSPECIFIED","id":"id","viewCount":"viewCount","rawGpsTimeline":[{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109},{"gpsRecordTimestampUnixEpoch":"gpsRecordTimestampUnixEpoch","altitude":6.027456183070403,"accuracyMeters":0.8008282,"latLngPair":{"latitude":5.962133916683182,"longitude":5.637376656633329},"heading":1.4658129805029452,"level":{"number":2.3021358869347655,"name":"name"},"roll":9.301444243932576,"pitch":7.061401241503109}]}
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
                    ('inputType', 'input_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/photoSequence',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_sequence_delete(client):
    """Test case for streetviewpublish_photo_sequence_delete

    
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
        path='/v1/photoSequence/{sequence_id}'.format(sequence_id='sequence_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_sequence_get(client):
    """Test case for streetviewpublish_photo_sequence_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/photoSequence/{sequence_id}'.format(sequence_id='sequence_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streetviewpublish_photo_sequence_start_upload(client):
    """Test case for streetviewpublish_photo_sequence_start_upload

    
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
        path='/v1/photoSequence:startUpload',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

