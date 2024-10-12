# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_batch_annotate_images_request import AsyncBatchAnnotateImagesRequest
from openapi_server.models.batch_annotate_images_request import BatchAnnotateImagesRequest
from openapi_server.models.batch_annotate_images_response import BatchAnnotateImagesResponse
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_vision_images_annotate(client):
    """Test case for vision_images_annotate

    
    """
    body = {"parent":"parent","requests":[{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"image":{"source":{"imageUri":"imageUri","gcsImageUri":"gcsImageUri"},"content":"content"},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}},{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"image":{"source":{"imageUri":"imageUri","gcsImageUri":"gcsImageUri"},"content":"content"},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}}],"labels":{"key":"labels"}}
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
        path='/v1/images:annotate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_images_async_batch_annotate(client):
    """Test case for vision_images_async_batch_annotate

    
    """
    body = {"parent":"parent","outputConfig":{"gcsDestination":{"uri":"uri"},"batchSize":0},"requests":[{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"image":{"source":{"imageUri":"imageUri","gcsImageUri":"gcsImageUri"},"content":"content"},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}},{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"image":{"source":{"imageUri":"imageUri","gcsImageUri":"gcsImageUri"},"content":"content"},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}}],"labels":{"key":"labels"}}
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
        path='/v1/images:asyncBatchAnnotate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

