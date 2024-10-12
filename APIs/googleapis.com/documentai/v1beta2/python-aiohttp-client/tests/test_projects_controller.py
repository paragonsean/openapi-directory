# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_documentai_v1beta2_batch_process_documents_request import GoogleCloudDocumentaiV1beta2BatchProcessDocumentsRequest
from openapi_server.models.google_cloud_documentai_v1beta2_document import GoogleCloudDocumentaiV1beta2Document
from openapi_server.models.google_cloud_documentai_v1beta2_process_document_request import GoogleCloudDocumentaiV1beta2ProcessDocumentRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_documents_batch_process(client):
    """Test case for documentai_projects_locations_documents_batch_process

    
    """
    body = {"requests":[{"inputConfig":{"contents":"contents","mimeType":"mimeType","gcsSource":{"uri":"uri"}},"parent":"parent","ocrParams":{"languageHints":["languageHints","languageHints"]},"entityExtractionParams":{"modelVersion":"modelVersion","enabled":True},"formExtractionParams":{"modelVersion":"modelVersion","keyValuePairHints":[{"valueTypes":["valueTypes","valueTypes"],"key":"key"},{"valueTypes":["valueTypes","valueTypes"],"key":"key"}],"enabled":True},"documentType":"documentType","outputConfig":{"gcsDestination":{"uri":"uri"},"pagesPerShard":0},"tableExtractionParams":{"headerHints":["headerHints","headerHints"],"tableBoundHints":[{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2},{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2}],"modelVersion":"modelVersion","enabled":True},"automlParams":{"model":"model"}},{"inputConfig":{"contents":"contents","mimeType":"mimeType","gcsSource":{"uri":"uri"}},"parent":"parent","ocrParams":{"languageHints":["languageHints","languageHints"]},"entityExtractionParams":{"modelVersion":"modelVersion","enabled":True},"formExtractionParams":{"modelVersion":"modelVersion","keyValuePairHints":[{"valueTypes":["valueTypes","valueTypes"],"key":"key"},{"valueTypes":["valueTypes","valueTypes"],"key":"key"}],"enabled":True},"documentType":"documentType","outputConfig":{"gcsDestination":{"uri":"uri"},"pagesPerShard":0},"tableExtractionParams":{"headerHints":["headerHints","headerHints"],"tableBoundHints":[{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2},{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2}],"modelVersion":"modelVersion","enabled":True},"automlParams":{"model":"model"}}]}
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
        path='/v1beta2/{parent}/documents:batchProcess'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_documents_process(client):
    """Test case for documentai_projects_locations_documents_process

    
    """
    body = {"inputConfig":{"contents":"contents","mimeType":"mimeType","gcsSource":{"uri":"uri"}},"parent":"parent","ocrParams":{"languageHints":["languageHints","languageHints"]},"entityExtractionParams":{"modelVersion":"modelVersion","enabled":True},"formExtractionParams":{"modelVersion":"modelVersion","keyValuePairHints":[{"valueTypes":["valueTypes","valueTypes"],"key":"key"},{"valueTypes":["valueTypes","valueTypes"],"key":"key"}],"enabled":True},"documentType":"documentType","outputConfig":{"gcsDestination":{"uri":"uri"},"pagesPerShard":0},"tableExtractionParams":{"headerHints":["headerHints","headerHints"],"tableBoundHints":[{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2},{"boundingBox":{"vertices":[{"x":5,"y":5},{"x":5,"y":5}],"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]},"pageNumber":2}],"modelVersion":"modelVersion","enabled":True},"automlParams":{"model":"model"}}
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
        path='/v1beta2/{parent}/documents:process'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_operations_get(client):
    """Test case for documentai_projects_operations_get

    
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
        method='GET',
        path='/v1beta2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

