# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_documentai_v1_batch_process_request import GoogleCloudDocumentaiV1BatchProcessRequest
from openapi_server.models.google_cloud_documentai_v1_evaluate_processor_version_request import GoogleCloudDocumentaiV1EvaluateProcessorVersionRequest
from openapi_server.models.google_cloud_documentai_v1_fetch_processor_types_response import GoogleCloudDocumentaiV1FetchProcessorTypesResponse
from openapi_server.models.google_cloud_documentai_v1_list_evaluations_response import GoogleCloudDocumentaiV1ListEvaluationsResponse
from openapi_server.models.google_cloud_documentai_v1_list_processor_types_response import GoogleCloudDocumentaiV1ListProcessorTypesResponse
from openapi_server.models.google_cloud_documentai_v1_list_processor_versions_response import GoogleCloudDocumentaiV1ListProcessorVersionsResponse
from openapi_server.models.google_cloud_documentai_v1_list_processors_response import GoogleCloudDocumentaiV1ListProcessorsResponse
from openapi_server.models.google_cloud_documentai_v1_process_request import GoogleCloudDocumentaiV1ProcessRequest
from openapi_server.models.google_cloud_documentai_v1_process_response import GoogleCloudDocumentaiV1ProcessResponse
from openapi_server.models.google_cloud_documentai_v1_processor import GoogleCloudDocumentaiV1Processor
from openapi_server.models.google_cloud_documentai_v1_review_document_request import GoogleCloudDocumentaiV1ReviewDocumentRequest
from openapi_server.models.google_cloud_documentai_v1_set_default_processor_version_request import GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequest
from openapi_server.models.google_cloud_documentai_v1_train_processor_version_request import GoogleCloudDocumentaiV1TrainProcessorVersionRequest
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_fetch_processor_types(client):
    """Test case for documentai_projects_locations_fetch_processor_types

    
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
        path='/v1/{parentfetch_processor_type}'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_list(client):
    """Test case for documentai_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_operations_cancel(client):
    """Test case for documentai_projects_locations_operations_cancel

    
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
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processor_types_list(client):
    """Test case for documentai_projects_locations_processor_types_list

    
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
        path='/v1/{parent}/processorTypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_create(client):
    """Test case for documentai_projects_locations_processors_create

    
    """
    body = {"processorVersionAliases":[{"alias":"alias","processorVersion":"processorVersion"},{"alias":"alias","processorVersion":"processorVersion"}],"createTime":"createTime","displayName":"displayName","name":"name","processEndpoint":"processEndpoint","state":"STATE_UNSPECIFIED","type":"type","defaultProcessorVersion":"defaultProcessorVersion","kmsKeyName":"kmsKeyName"}
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
        path='/v1/{parent}/processors'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_disable(client):
    """Test case for documentai_projects_locations_processors_disable

    
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
        path='/v1/{namedisabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_enable(client):
    """Test case for documentai_projects_locations_processors_enable

    
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
        path='/v1/{nameenabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_human_review_config_review_document(client):
    """Test case for documentai_projects_locations_processors_human_review_config_review_document

    
    """
    body = {"enableSchemaValidation":True,"documentSchema":{"metadata":{"skipNamingValidation":True,"documentSplitter":True,"prefixedNamingOnProperties":True,"documentAllowMultipleLabels":True},"displayName":"displayName","description":"description","entityTypes":[{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}},{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}}]},"priority":"DEFAULT","inlineDocument":{"pages":[{"image":{"width":6,"mimeType":"mimeType","content":"content","height":2},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"pageNumber":6,"blocks":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"transforms":[{"data":"data","rows":3,"type":7,"cols":3},{"data":"data","rows":3,"type":7,"cols":3}],"detectedBarcodes":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}}],"paragraphs":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"symbols":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]}],"visualElements":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"}],"imageQualityScores":{"detectedDefects":[{"confidence":6.878052,"type":"type"},{"confidence":6.878052,"type":"type"}],"qualityScore":5.9448957},"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"tables":[{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]},{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"tokens":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}}],"formFields":[{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}},{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}}],"lines":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"dimension":{"unit":"unit","width":1.284659,"height":6.965118}},{"image":{"width":6,"mimeType":"mimeType","content":"content","height":2},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"pageNumber":6,"blocks":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"transforms":[{"data":"data","rows":3,"type":7,"cols":3},{"data":"data","rows":3,"type":7,"cols":3}],"detectedBarcodes":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}}],"paragraphs":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"symbols":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]}],"visualElements":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"}],"imageQualityScores":{"detectedDefects":[{"confidence":6.878052,"type":"type"},{"confidence":6.878052,"type":"type"}],"qualityScore":5.9448957},"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"tables":[{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]},{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"tokens":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}}],"formFields":[{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}},{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}}],"lines":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"dimension":{"unit":"unit","width":1.284659,"height":6.965118}}],"entities":[{"mentionId":"mentionId","mentionText":"mentionText","pageAnchor":{"pageRefs":[{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"},{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"}]},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"redacted":True,"confidence":0.8008282,"id":"id","normalizedValue":{"dateValue":{"month":5,"year":5,"day":1},"addressValue":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":6},"datetimeValue":{"hours":7,"seconds":4,"utcOffset":"utcOffset","month":3,"nanos":2,"year":7,"minutes":9,"timeZone":{"id":"id","version":"version"},"day":2},"floatValue":1.2315135,"booleanValue":True,"integerValue":1,"moneyValue":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"text":"text"},"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"type":"type","properties":[null,null]},{"mentionId":"mentionId","mentionText":"mentionText","pageAnchor":{"pageRefs":[{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"},{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"}]},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"redacted":True,"confidence":0.8008282,"id":"id","normalizedValue":{"dateValue":{"month":5,"year":5,"day":1},"addressValue":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":6},"datetimeValue":{"hours":7,"seconds":4,"utcOffset":"utcOffset","month":3,"nanos":2,"year":7,"minutes":9,"timeZone":{"id":"id","version":"version"},"day":2},"floatValue":1.2315135,"booleanValue":True,"integerValue":1,"moneyValue":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"text":"text"},"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"type":"type","properties":[null,null]}],"entityRelations":[{"objectId":"objectId","subjectId":"subjectId","relation":"relation"},{"objectId":"objectId","subjectId":"subjectId","relation":"relation"}],"revisions":[{"parent":[5,5],"agent":"agent","createTime":"createTime","parentIds":["parentIds","parentIds"],"humanReview":{"stateMessage":"stateMessage","state":"state"},"id":"id","processor":"processor"},{"parent":[5,5],"agent":"agent","createTime":"createTime","parentIds":["parentIds","parentIds"],"humanReview":{"stateMessage":"stateMessage","state":"state"},"id":"id","processor":"processor"}],"mimeType":"mimeType","text":"text","textStyles":[{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontFamily":"fontFamily","color":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontSize":{"unit":"unit","size":3.2588565},"textDecoration":"textDecoration","textStyle":"textStyle","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"fontWeight":"fontWeight"},{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontFamily":"fontFamily","color":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontSize":{"unit":"unit","size":3.2588565},"textDecoration":"textDecoration","textStyle":"textStyle","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"fontWeight":"fontWeight"}],"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"textChanges":[{"provenance":[{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}],"changedText":"changedText","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]}},{"provenance":[{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}],"changedText":"changedText","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]}}],"shardInfo":{"textOffset":"textOffset","shardIndex":"shardIndex","shardCount":"shardCount"},"uri":"uri","content":"content"}}
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
        path='/v1/{human_review_configreview_documen}'.format(human_review_config='human_review_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_list(client):
    """Test case for documentai_projects_locations_processors_list

    
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
        path='/v1/{parent}/processors'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_batch_process(client):
    """Test case for documentai_projects_locations_processors_processor_versions_batch_process

    
    """
    body = {"documentOutputConfig":{"gcsOutputConfig":{"fieldMask":"fieldMask","shardingConfig":{"pagesOverlap":0,"pagesPerShard":6},"gcsUri":"gcsUri"}},"skipHumanReview":True,"inputDocuments":{"gcsDocuments":{"documents":[{"mimeType":"mimeType","gcsUri":"gcsUri"},{"mimeType":"mimeType","gcsUri":"gcsUri"}]},"gcsPrefix":{"gcsUriPrefix":"gcsUriPrefix"}},"processOptions":{"fromEnd":1,"individualPageSelector":{"pages":[5,5]},"schemaOverride":{"metadata":{"skipNamingValidation":True,"documentSplitter":True,"prefixedNamingOnProperties":True,"documentAllowMultipleLabels":True},"displayName":"displayName","description":"description","entityTypes":[{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}},{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}}]},"ocrConfig":{"enableImageQualityScores":True,"hints":{"languageHints":["languageHints","languageHints"]},"computeStyleInfo":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"],"disableCharacterBoxesDetection":True,"enableNativePdfParsing":True,"premiumFeatures":{"computeStyleInfo":True,"enableMathOcr":True,"enableSelectionMarkDetection":True},"enableSymbol":True},"fromStart":5},"labels":{"key":"labels"}}
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
        path='/v1/{namebatch_proces}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_delete(client):
    """Test case for documentai_projects_locations_processors_processor_versions_delete

    
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

async def test_documentai_projects_locations_processors_processor_versions_deploy(client):
    """Test case for documentai_projects_locations_processors_processor_versions_deploy

    
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
        path='/v1/{namedeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_evaluate_processor_version(client):
    """Test case for documentai_projects_locations_processors_processor_versions_evaluate_processor_version

    
    """
    body = {"evaluationDocuments":{"gcsDocuments":{"documents":[{"mimeType":"mimeType","gcsUri":"gcsUri"},{"mimeType":"mimeType","gcsUri":"gcsUri"}]},"gcsPrefix":{"gcsUriPrefix":"gcsUriPrefix"}}}
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
        path='/v1/{processor_versionevaluate_processor_versio}'.format(processor_version='processor_version_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_evaluations_list(client):
    """Test case for documentai_projects_locations_processors_processor_versions_evaluations_list

    
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
        path='/v1/{parent}/evaluations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_list(client):
    """Test case for documentai_projects_locations_processors_processor_versions_list

    
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
        path='/v1/{parent}/processorVersions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_process(client):
    """Test case for documentai_projects_locations_processors_processor_versions_process

    
    """
    body = {"fieldMask":"fieldMask","rawDocument":{"displayName":"displayName","mimeType":"mimeType","content":"content"},"skipHumanReview":True,"processOptions":{"fromEnd":1,"individualPageSelector":{"pages":[5,5]},"schemaOverride":{"metadata":{"skipNamingValidation":True,"documentSplitter":True,"prefixedNamingOnProperties":True,"documentAllowMultipleLabels":True},"displayName":"displayName","description":"description","entityTypes":[{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}},{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}}]},"ocrConfig":{"enableImageQualityScores":True,"hints":{"languageHints":["languageHints","languageHints"]},"computeStyleInfo":True,"advancedOcrOptions":["advancedOcrOptions","advancedOcrOptions"],"disableCharacterBoxesDetection":True,"enableNativePdfParsing":True,"premiumFeatures":{"computeStyleInfo":True,"enableMathOcr":True,"enableSelectionMarkDetection":True},"enableSymbol":True},"fromStart":5},"gcsDocument":{"mimeType":"mimeType","gcsUri":"gcsUri"},"inlineDocument":{"pages":[{"image":{"width":6,"mimeType":"mimeType","content":"content","height":2},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"pageNumber":6,"blocks":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"transforms":[{"data":"data","rows":3,"type":7,"cols":3},{"data":"data","rows":3,"type":7,"cols":3}],"detectedBarcodes":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}}],"paragraphs":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"symbols":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]}],"visualElements":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"}],"imageQualityScores":{"detectedDefects":[{"confidence":6.878052,"type":"type"},{"confidence":6.878052,"type":"type"}],"qualityScore":5.9448957},"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"tables":[{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]},{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"tokens":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}}],"formFields":[{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}},{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}}],"lines":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"dimension":{"unit":"unit","width":1.284659,"height":6.965118}},{"image":{"width":6,"mimeType":"mimeType","content":"content","height":2},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"pageNumber":6,"blocks":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"transforms":[{"data":"data","rows":3,"type":7,"cols":3},{"data":"data","rows":3,"type":7,"cols":3}],"detectedBarcodes":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"barcode":{"rawValue":"rawValue","format":"format","valueFormat":"valueFormat"}}],"paragraphs":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"symbols":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}]}],"visualElements":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"type":"type"}],"imageQualityScores":{"detectedDefects":[{"confidence":6.878052,"type":"type"},{"confidence":6.878052,"type":"type"}],"qualityScore":5.9448957},"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"tables":[{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]},{"bodyRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}],"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"headerRows":[{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]},{"cells":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"rowSpan":3,"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"colSpan":3}]}]}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"tokens":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"styleInfo":{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontType":"fontType","subscript":True,"superscript":True,"letterSpacing":8.969578798196912,"bold":True,"handwritten":True,"italic":True,"textColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"smallcaps":True,"strikeout":True,"pixelFontSize":7.740351818741173,"underlined":True,"fontSize":0,"fontWeight":4},"detectedBreak":{"type":"TYPE_UNSPECIFIED"}}],"formFields":[{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}},{"fieldName":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"valueDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"valueType":"valueType","correctedKeyText":"correctedKeyText","correctedValueText":"correctedValueText","nameDetectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"fieldValue":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}}}],"lines":[{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}},{"layout":{"orientation":"ORIENTATION_UNSPECIFIED","confidence":3.5571952,"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]}},"detectedLanguages":[{"confidence":6.4384236,"languageCode":"languageCode"},{"confidence":6.4384236,"languageCode":"languageCode"}],"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}}],"dimension":{"unit":"unit","width":1.284659,"height":6.965118}}],"entities":[{"mentionId":"mentionId","mentionText":"mentionText","pageAnchor":{"pageRefs":[{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"},{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"}]},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"redacted":True,"confidence":0.8008282,"id":"id","normalizedValue":{"dateValue":{"month":5,"year":5,"day":1},"addressValue":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":6},"datetimeValue":{"hours":7,"seconds":4,"utcOffset":"utcOffset","month":3,"nanos":2,"year":7,"minutes":9,"timeZone":{"id":"id","version":"version"},"day":2},"floatValue":1.2315135,"booleanValue":True,"integerValue":1,"moneyValue":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"text":"text"},"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"type":"type","properties":[null,null]},{"mentionId":"mentionId","mentionText":"mentionText","pageAnchor":{"pageRefs":[{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"},{"confidence":5.025005,"layoutType":"LAYOUT_TYPE_UNSPECIFIED","page":"page","boundingPoly":{"vertices":[{"x":1,"y":4},{"x":1,"y":4}],"normalizedVertices":[{"x":6.846853,"y":7.4577446},{"x":6.846853,"y":7.4577446}]},"layoutId":"layoutId"}]},"provenance":{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},"redacted":True,"confidence":0.8008282,"id":"id","normalizedValue":{"dateValue":{"month":5,"year":5,"day":1},"addressValue":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":6},"datetimeValue":{"hours":7,"seconds":4,"utcOffset":"utcOffset","month":3,"nanos":2,"year":7,"minutes":9,"timeZone":{"id":"id","version":"version"},"day":2},"floatValue":1.2315135,"booleanValue":True,"integerValue":1,"moneyValue":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"text":"text"},"textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"type":"type","properties":[null,null]}],"entityRelations":[{"objectId":"objectId","subjectId":"subjectId","relation":"relation"},{"objectId":"objectId","subjectId":"subjectId","relation":"relation"}],"revisions":[{"parent":[5,5],"agent":"agent","createTime":"createTime","parentIds":["parentIds","parentIds"],"humanReview":{"stateMessage":"stateMessage","state":"state"},"id":"id","processor":"processor"},{"parent":[5,5],"agent":"agent","createTime":"createTime","parentIds":["parentIds","parentIds"],"humanReview":{"stateMessage":"stateMessage","state":"state"},"id":"id","processor":"processor"}],"mimeType":"mimeType","text":"text","textStyles":[{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontFamily":"fontFamily","color":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontSize":{"unit":"unit","size":3.2588565},"textDecoration":"textDecoration","textStyle":"textStyle","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"fontWeight":"fontWeight"},{"backgroundColor":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontFamily":"fontFamily","color":{"red":6.519181,"green":7.05877,"blue":0.8851375,"alpha":7.143538},"fontSize":{"unit":"unit","size":3.2588565},"textDecoration":"textDecoration","textStyle":"textStyle","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]},"fontWeight":"fontWeight"}],"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"textChanges":[{"provenance":[{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}],"changedText":"changedText","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]}},{"provenance":[{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9},{"id":9,"type":"OPERATION_TYPE_UNSPECIFIED","parents":[{"index":6,"id":9,"revision":8},{"index":6,"id":9,"revision":8}],"revision":9}],"changedText":"changedText","textAnchor":{"content":"content","textSegments":[{"startIndex":"startIndex","endIndex":"endIndex"},{"startIndex":"startIndex","endIndex":"endIndex"}]}}],"shardInfo":{"textOffset":"textOffset","shardIndex":"shardIndex","shardCount":"shardCount"},"uri":"uri","content":"content"},"labels":{"key":"labels"}}
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
        path='/v1/{nameproces}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_train(client):
    """Test case for documentai_projects_locations_processors_processor_versions_train

    
    """
    body = {"inputData":{"trainingDocuments":{"gcsDocuments":{"documents":[{"mimeType":"mimeType","gcsUri":"gcsUri"},{"mimeType":"mimeType","gcsUri":"gcsUri"}]},"gcsPrefix":{"gcsUriPrefix":"gcsUriPrefix"}},"testDocuments":{"gcsDocuments":{"documents":[{"mimeType":"mimeType","gcsUri":"gcsUri"},{"mimeType":"mimeType","gcsUri":"gcsUri"}]},"gcsPrefix":{"gcsUriPrefix":"gcsUriPrefix"}}},"baseProcessorVersion":"baseProcessorVersion","documentSchema":{"metadata":{"skipNamingValidation":True,"documentSplitter":True,"prefixedNamingOnProperties":True,"documentAllowMultipleLabels":True},"displayName":"displayName","description":"description","entityTypes":[{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}},{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}}]},"processorVersion":{"createTime":"createTime","displayName":"displayName","documentSchema":{"metadata":{"skipNamingValidation":True,"documentSplitter":True,"prefixedNamingOnProperties":True,"documentAllowMultipleLabels":True},"displayName":"displayName","description":"description","entityTypes":[{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}},{"displayName":"displayName","name":"name","baseTypes":["baseTypes","baseTypes"],"properties":[{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"},{"displayName":"displayName","valueType":"valueType","name":"name","occurrenceType":"OCCURRENCE_TYPE_UNSPECIFIED"}],"enumValues":{"values":["values","values"]}}]},"deprecationInfo":{"deprecationTime":"deprecationTime","replacementProcessorVersion":"replacementProcessorVersion"},"name":"name","latestEvaluation":{"evaluation":"evaluation","aggregateMetricsExact":{"predictedOccurrencesCount":4,"predictedDocumentCount":2,"falsePositivesCount":2,"precision":3.6160767,"recall":7.386282,"groundTruthDocumentCount":7,"groundTruthOccurrencesCount":9,"totalDocumentsCount":1,"truePositivesCount":1,"f1Score":5.962134,"falseNegativesCount":5},"operation":"operation","aggregateMetrics":{"predictedOccurrencesCount":4,"predictedDocumentCount":2,"falsePositivesCount":2,"precision":3.6160767,"recall":7.386282,"groundTruthDocumentCount":7,"groundTruthOccurrencesCount":9,"totalDocumentsCount":1,"truePositivesCount":1,"f1Score":5.962134,"falseNegativesCount":5}},"modelType":"MODEL_TYPE_UNSPECIFIED","state":"STATE_UNSPECIFIED","googleManaged":True,"kmsKeyVersionName":"kmsKeyVersionName","kmsKeyName":"kmsKeyName"},"customDocumentExtractionOptions":{"trainingMethod":"TRAINING_METHOD_UNSPECIFIED"}}
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
        path='/v1/{parent}/processorVersions:train'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_processor_versions_undeploy(client):
    """Test case for documentai_projects_locations_processors_processor_versions_undeploy

    
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
        path='/v1/{nameundeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documentai_projects_locations_processors_set_default_processor_version(client):
    """Test case for documentai_projects_locations_processors_set_default_processor_version

    
    """
    body = {"defaultProcessorVersion":"defaultProcessorVersion"}
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
        path='/v1/{processorset_default_processor_versio}'.format(processor='processor_example'),
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

