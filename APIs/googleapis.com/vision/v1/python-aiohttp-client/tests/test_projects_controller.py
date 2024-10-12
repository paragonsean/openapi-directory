# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_product_to_product_set_request import AddProductToProductSetRequest
from openapi_server.models.async_batch_annotate_files_request import AsyncBatchAnnotateFilesRequest
from openapi_server.models.async_batch_annotate_images_request import AsyncBatchAnnotateImagesRequest
from openapi_server.models.batch_annotate_files_request import BatchAnnotateFilesRequest
from openapi_server.models.batch_annotate_files_response import BatchAnnotateFilesResponse
from openapi_server.models.batch_annotate_images_request import BatchAnnotateImagesRequest
from openapi_server.models.batch_annotate_images_response import BatchAnnotateImagesResponse
from openapi_server.models.import_product_sets_request import ImportProductSetsRequest
from openapi_server.models.list_product_sets_response import ListProductSetsResponse
from openapi_server.models.list_products_in_product_set_response import ListProductsInProductSetResponse
from openapi_server.models.list_products_response import ListProductsResponse
from openapi_server.models.list_reference_images_response import ListReferenceImagesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.product import Product
from openapi_server.models.product_set import ProductSet
from openapi_server.models.purge_products_request import PurgeProductsRequest
from openapi_server.models.reference_image import ReferenceImage
from openapi_server.models.remove_product_from_product_set_request import RemoveProductFromProductSetRequest


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
        path='/v1/{parent}/files:annotate'.format(parent='parent_example'),
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
        path='/v1/{parent}/files:asyncBatchAnnotate'.format(parent='parent_example'),
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
        path='/v1/{parent}/images:annotate'.format(parent='parent_example'),
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
        path='/v1/{parent}/images:asyncBatchAnnotate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_add_product(client):
    """Test case for vision_projects_locations_product_sets_add_product

    
    """
    body = {"product":"product"}
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
        path='/v1/{nameadd_produc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_create(client):
    """Test case for vision_projects_locations_product_sets_create

    
    """
    body = {"indexTime":"indexTime","displayName":"displayName","name":"name","indexError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}
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
                    ('productSetId', 'product_set_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/productSets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_delete(client):
    """Test case for vision_projects_locations_product_sets_delete

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_import(client):
    """Test case for vision_projects_locations_product_sets_import

    
    """
    body = {"inputConfig":{"gcsSource":{"csvFileUri":"csvFileUri"}}}
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
        path='/v1/{parent}/productSets:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_list(client):
    """Test case for vision_projects_locations_product_sets_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/productSets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_patch(client):
    """Test case for vision_projects_locations_product_sets_patch

    
    """
    body = {"indexTime":"indexTime","displayName":"displayName","name":"name","indexError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}
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
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_products_list(client):
    """Test case for vision_projects_locations_product_sets_products_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/products'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_product_sets_remove_product(client):
    """Test case for vision_projects_locations_product_sets_remove_product

    
    """
    body = {"product":"product"}
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
        path='/v1/{nameremove_produc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_products_create(client):
    """Test case for vision_projects_locations_products_create

    
    """
    body = {"productLabels":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"displayName":"displayName","name":"name","description":"description","productCategory":"productCategory"}
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
                    ('productId', 'product_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_products_list(client):
    """Test case for vision_projects_locations_products_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_products_purge(client):
    """Test case for vision_projects_locations_products_purge

    
    """
    body = {"deleteOrphanProducts":True,"productSetPurgeConfig":{"productSetId":"productSetId"},"force":True}
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
        path='/v1/{parent}/products:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_products_reference_images_create(client):
    """Test case for vision_projects_locations_products_reference_images_create

    
    """
    body = {"boundingPolys":[{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]},{"vertices":[{"x":5,"y":2},{"x":5,"y":2}],"normalizedVertices":[{"x":1.4658129,"y":5.962134},{"x":1.4658129,"y":5.962134}]}],"name":"name","uri":"uri"}
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
                    ('referenceImageId', 'reference_image_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/referenceImages'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_locations_products_reference_images_list(client):
    """Test case for vision_projects_locations_products_reference_images_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/referenceImages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vision_projects_operations_get(client):
    """Test case for vision_projects_operations_get

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
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

