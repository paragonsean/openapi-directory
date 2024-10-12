# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_vision_v1p2beta1_async_batch_annotate_files_request import GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesRequest
from openapi_server.models.google_cloud_vision_v1p2beta1_async_batch_annotate_images_request import GoogleCloudVisionV1p2beta1AsyncBatchAnnotateImagesRequest
from openapi_server.models.google_cloud_vision_v1p2beta1_batch_annotate_files_request import GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest
from openapi_server.models.google_cloud_vision_v1p2beta1_batch_annotate_files_response import GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponse
from openapi_server.models.google_cloud_vision_v1p2beta1_batch_annotate_images_request import GoogleCloudVisionV1p2beta1BatchAnnotateImagesRequest
from openapi_server.models.google_cloud_vision_v1p2beta1_batch_annotate_images_response import GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponse
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_files_annotate(client):
    """Test case for vision_projects_locations_files_annotate

    
    """
    body = {"parent":"parent","requests":[{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"inputConfig":{"mimeType":"mimeType","gcsSource":{"uri":"uri"},"content":"content"},"pages":[1,1],"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}},{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"inputConfig":{"mimeType":"mimeType","gcsSource":{"uri":"uri"},"content":"content"},"pages":[1,1],"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}}],"labels":{"key":"labels"}}
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
        path='/v1p2beta1/{parent}/files:annotate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_files_async_batch_annotate(client):
    """Test case for vision_projects_locations_files_async_batch_annotate

    
    """
    body = {"parent":"parent","requests":[{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"inputConfig":{"mimeType":"mimeType","gcsSource":{"uri":"uri"},"content":"content"},"outputConfig":{"gcsDestination":{"uri":"uri"},"batchSize":0},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}},{"features":[{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"},{"maxResults":0,"model":"model","type":"TYPE_UNSPECIFIED"}],"inputConfig":{"mimeType":"mimeType","gcsSource":{"uri":"uri"},"content":"content"},"outputConfig":{"gcsDestination":{"uri":"uri"},"batchSize":0},"imageContext":{"webDetectionParams":{"includeGeoResults":True},"cropHintsParams":{"aspectRatios":[6.0274563,6.0274563]},"productSearchParams":{"filter":"filter","productCategories":["productCategories","productCategories"],"boundingPoly":{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},"productSet":"productSet"},"languageHints":["languageHints","languageHints"],"latLongRect":{"minLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016},"maxLatLng":{"latitude":6.878052220127876,"longitude":5.944895607614016}},"textDetectionParams":{"enableTextDetectionConfidenceScore":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"]}}}],"labels":{"key":"labels"}}
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
        path='/v1p2beta1/{parent}/files:asyncBatchAnnotate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_images_annotate(client):
    """Test case for vision_projects_locations_images_annotate

    
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
        path='/v1p2beta1/{parent}/images:annotate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_images_async_batch_annotate(client):
    """Test case for vision_projects_locations_images_async_batch_annotate

    
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
        path='/v1p2beta1/{parent}/images:asyncBatchAnnotate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

