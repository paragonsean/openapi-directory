# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_datalabeling_v1beta1_annotation_spec_set import GoogleCloudDatalabelingV1beta1AnnotationSpecSet
from openapi_server.models.google_cloud_datalabeling_v1beta1_create_annotation_spec_set_request import GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_create_dataset_request import GoogleCloudDatalabelingV1beta1CreateDatasetRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_create_evaluation_job_request import GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_create_instruction_request import GoogleCloudDatalabelingV1beta1CreateInstructionRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_dataset import GoogleCloudDatalabelingV1beta1Dataset
from openapi_server.models.google_cloud_datalabeling_v1beta1_evaluation_job import GoogleCloudDatalabelingV1beta1EvaluationJob
from openapi_server.models.google_cloud_datalabeling_v1beta1_export_data_request import GoogleCloudDatalabelingV1beta1ExportDataRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_feedback_message import GoogleCloudDatalabelingV1beta1FeedbackMessage
from openapi_server.models.google_cloud_datalabeling_v1beta1_import_data_request import GoogleCloudDatalabelingV1beta1ImportDataRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_label_image_request import GoogleCloudDatalabelingV1beta1LabelImageRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_label_text_request import GoogleCloudDatalabelingV1beta1LabelTextRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_label_video_request import GoogleCloudDatalabelingV1beta1LabelVideoRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_annotated_datasets_response import GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_annotation_spec_sets_response import GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_data_items_response import GoogleCloudDatalabelingV1beta1ListDataItemsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_datasets_response import GoogleCloudDatalabelingV1beta1ListDatasetsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_evaluation_jobs_response import GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_examples_response import GoogleCloudDatalabelingV1beta1ListExamplesResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_feedback_messages_response import GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_feedback_threads_response import GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_list_instructions_response import GoogleCloudDatalabelingV1beta1ListInstructionsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_search_evaluations_response import GoogleCloudDatalabelingV1beta1SearchEvaluationsResponse
from openapi_server.models.google_cloud_datalabeling_v1beta1_search_example_comparisons_request import GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequest
from openapi_server.models.google_cloud_datalabeling_v1beta1_search_example_comparisons_response import GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_annotation_spec_sets_create(client):
    """Test case for datalabeling_projects_annotation_spec_sets_create

    
    """
    body = {"annotationSpecSet":{"displayName":"displayName","name":"name","blockingResources":["blockingResources","blockingResources"],"description":"description","annotationSpecs":[{"displayName":"displayName","description":"description","index":0},{"displayName":"displayName","description":"description","index":0}]}}
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
        path='/v1beta1/{parent}/annotationSpecSets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_annotation_spec_sets_list(client):
    """Test case for datalabeling_projects_annotation_spec_sets_list

    
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
        path='/v1beta1/{parent}/annotationSpecSets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_annotated_datasets_examples_list(client):
    """Test case for datalabeling_projects_datasets_annotated_datasets_examples_list

    
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
        path='/v1beta1/{parent}/examples'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_annotated_datasets_feedback_threads_feedback_messages_create(client):
    """Test case for datalabeling_projects_datasets_annotated_datasets_feedback_threads_feedback_messages_create

    
    """
    body = {"image":"image","createTime":"createTime","name":"name","operatorFeedbackMetadata":"{}","requesterFeedbackMetadata":"{}","body":"body"}
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
        path='/v1beta1/{parent}/feedbackMessages'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_annotated_datasets_feedback_threads_feedback_messages_list(client):
    """Test case for datalabeling_projects_datasets_annotated_datasets_feedback_threads_feedback_messages_list

    
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
        path='/v1beta1/{parent}/feedbackMessages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_annotated_datasets_feedback_threads_list(client):
    """Test case for datalabeling_projects_datasets_annotated_datasets_feedback_threads_list

    
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
        path='/v1beta1/{parent}/feedbackThreads'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_annotated_datasets_list(client):
    """Test case for datalabeling_projects_datasets_annotated_datasets_list

    
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
        path='/v1beta1/{parent}/annotatedDatasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_create(client):
    """Test case for datalabeling_projects_datasets_create

    
    """
    body = {"dataset":{"lastMigrateTime":"lastMigrateTime","createTime":"createTime","displayName":"displayName","name":"name","blockingResources":["blockingResources","blockingResources"],"description":"description","dataItemCount":"dataItemCount","inputConfigs":[{"dataType":"DATA_TYPE_UNSPECIFIED","annotationType":"ANNOTATION_TYPE_UNSPECIFIED","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"mimeType":"mimeType","inputUri":"inputUri"},"textMetadata":{"languageCode":"languageCode"},"classificationMetadata":{"isMultiLabel":True}},{"dataType":"DATA_TYPE_UNSPECIFIED","annotationType":"ANNOTATION_TYPE_UNSPECIFIED","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"mimeType":"mimeType","inputUri":"inputUri"},"textMetadata":{"languageCode":"languageCode"},"classificationMetadata":{"isMultiLabel":True}}]}}
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
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_data_items_list(client):
    """Test case for datalabeling_projects_datasets_data_items_list

    
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
        path='/v1beta1/{parent}/dataItems'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_evaluations_example_comparisons_search(client):
    """Test case for datalabeling_projects_datasets_evaluations_example_comparisons_search

    
    """
    body = {"pageSize":0,"pageToken":"pageToken"}
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
        path='/v1beta1/{parent}/exampleComparisons:search'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_export_data(client):
    """Test case for datalabeling_projects_datasets_export_data

    
    """
    body = {"filter":"filter","outputConfig":{"gcsDestination":{"outputUri":"outputUri","mimeType":"mimeType"},"gcsFolderDestination":{"outputFolderUri":"outputFolderUri"}},"userEmailAddress":"userEmailAddress","annotatedDataset":"annotatedDataset"}
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
        path='/v1beta1/{nameexport_dat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_image_label(client):
    """Test case for datalabeling_projects_datasets_image_label

    
    """
    body = {"boundingPolyConfig":{"annotationSpecSet":"annotationSpecSet","instructionMessage":"instructionMessage"},"feature":"FEATURE_UNSPECIFIED","imageClassificationConfig":{"annotationSpecSet":"annotationSpecSet","allowMultiLabel":True,"answerAggregationType":"STRING_AGGREGATION_TYPE_UNSPECIFIED"},"basicConfig":{"labelGroup":"labelGroup","annotatedDatasetDescription":"annotatedDatasetDescription","replicaCount":5,"contributorEmails":["contributorEmails","contributorEmails"],"instruction":"instruction","userEmailAddress":"userEmailAddress","questionDuration":"questionDuration","languageCode":"languageCode","annotatedDatasetDisplayName":"annotatedDatasetDisplayName"},"polylineConfig":{"annotationSpecSet":"annotationSpecSet","instructionMessage":"instructionMessage"},"segmentationConfig":{"annotationSpecSet":"annotationSpecSet","instructionMessage":"instructionMessage"}}
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
        path='/v1beta1/{parent}/image:label'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_import_data(client):
    """Test case for datalabeling_projects_datasets_import_data

    
    """
    body = {"inputConfig":{"dataType":"DATA_TYPE_UNSPECIFIED","annotationType":"ANNOTATION_TYPE_UNSPECIFIED","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"mimeType":"mimeType","inputUri":"inputUri"},"textMetadata":{"languageCode":"languageCode"},"classificationMetadata":{"isMultiLabel":True}},"userEmailAddress":"userEmailAddress"}
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
        path='/v1beta1/{nameimport_dat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_list(client):
    """Test case for datalabeling_projects_datasets_list

    
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
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_text_label(client):
    """Test case for datalabeling_projects_datasets_text_label

    
    """
    body = {"feature":"FEATURE_UNSPECIFIED","textEntityExtractionConfig":{"annotationSpecSet":"annotationSpecSet"},"basicConfig":{"labelGroup":"labelGroup","annotatedDatasetDescription":"annotatedDatasetDescription","replicaCount":5,"contributorEmails":["contributorEmails","contributorEmails"],"instruction":"instruction","userEmailAddress":"userEmailAddress","questionDuration":"questionDuration","languageCode":"languageCode","annotatedDatasetDisplayName":"annotatedDatasetDisplayName"},"textClassificationConfig":{"annotationSpecSet":"annotationSpecSet","sentimentConfig":{"enableLabelSentimentSelection":True},"allowMultiLabel":True}}
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
        path='/v1beta1/{parent}/text:label'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_datasets_video_label(client):
    """Test case for datalabeling_projects_datasets_video_label

    
    """
    body = {"eventConfig":{"overlapLength":6,"clipLength":0,"annotationSpecSets":["annotationSpecSets","annotationSpecSets"]},"feature":"FEATURE_UNSPECIFIED","videoClassificationConfig":{"applyShotDetection":True,"annotationSpecSetConfigs":[{"annotationSpecSet":"annotationSpecSet","allowMultiLabel":True},{"annotationSpecSet":"annotationSpecSet","allowMultiLabel":True}]},"basicConfig":{"labelGroup":"labelGroup","annotatedDatasetDescription":"annotatedDatasetDescription","replicaCount":5,"contributorEmails":["contributorEmails","contributorEmails"],"instruction":"instruction","userEmailAddress":"userEmailAddress","questionDuration":"questionDuration","languageCode":"languageCode","annotatedDatasetDisplayName":"annotatedDatasetDisplayName"},"objectTrackingConfig":{"annotationSpecSet":"annotationSpecSet","overlapLength":5,"clipLength":5},"objectDetectionConfig":{"annotationSpecSet":"annotationSpecSet","extractionFrameRate":1.4658129805029452}}
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
        path='/v1beta1/{parent}/video:label'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluation_jobs_create(client):
    """Test case for datalabeling_projects_evaluation_jobs_create

    
    """
    body = {"job":{"labelMissingGroundTruth":True,"schedule":"schedule","annotationSpecSet":"annotationSpecSet","createTime":"createTime","modelVersion":"modelVersion","evaluationJobConfig":{"inputConfig":{"dataType":"DATA_TYPE_UNSPECIFIED","annotationType":"ANNOTATION_TYPE_UNSPECIFIED","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"mimeType":"mimeType","inputUri":"inputUri"},"textMetadata":{"languageCode":"languageCode"},"classificationMetadata":{"isMultiLabel":True}},"boundingPolyConfig":{"annotationSpecSet":"annotationSpecSet","instructionMessage":"instructionMessage"},"evaluationJobAlertConfig":{"minAcceptableMeanAveragePrecision":6.027456183070403,"email":"email"},"humanAnnotationConfig":{"labelGroup":"labelGroup","annotatedDatasetDescription":"annotatedDatasetDescription","replicaCount":5,"contributorEmails":["contributorEmails","contributorEmails"],"instruction":"instruction","userEmailAddress":"userEmailAddress","questionDuration":"questionDuration","languageCode":"languageCode","annotatedDatasetDisplayName":"annotatedDatasetDisplayName"},"imageClassificationConfig":{"annotationSpecSet":"annotationSpecSet","allowMultiLabel":True,"answerAggregationType":"STRING_AGGREGATION_TYPE_UNSPECIFIED"},"exampleCount":1,"exampleSamplePercentage":5.962133916683182,"textClassificationConfig":{"annotationSpecSet":"annotationSpecSet","sentimentConfig":{"enableLabelSentimentSelection":True},"allowMultiLabel":True},"evaluationConfig":{"boundingBoxEvaluationOptions":{"iouThreshold":0.8008282}},"bigqueryImportKeys":{"key":"bigqueryImportKeys"}},"name":"name","description":"description","state":"STATE_UNSPECIFIED","attempts":[{"attemptTime":"attemptTime","partialFailures":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}]},{"attemptTime":"attemptTime","partialFailures":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}]}]}}
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
        path='/v1beta1/{parent}/evaluationJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluation_jobs_list(client):
    """Test case for datalabeling_projects_evaluation_jobs_list

    
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
        path='/v1beta1/{parent}/evaluationJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluation_jobs_patch(client):
    """Test case for datalabeling_projects_evaluation_jobs_patch

    
    """
    body = {"labelMissingGroundTruth":True,"schedule":"schedule","annotationSpecSet":"annotationSpecSet","createTime":"createTime","modelVersion":"modelVersion","evaluationJobConfig":{"inputConfig":{"dataType":"DATA_TYPE_UNSPECIFIED","annotationType":"ANNOTATION_TYPE_UNSPECIFIED","bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"mimeType":"mimeType","inputUri":"inputUri"},"textMetadata":{"languageCode":"languageCode"},"classificationMetadata":{"isMultiLabel":True}},"boundingPolyConfig":{"annotationSpecSet":"annotationSpecSet","instructionMessage":"instructionMessage"},"evaluationJobAlertConfig":{"minAcceptableMeanAveragePrecision":6.027456183070403,"email":"email"},"humanAnnotationConfig":{"labelGroup":"labelGroup","annotatedDatasetDescription":"annotatedDatasetDescription","replicaCount":5,"contributorEmails":["contributorEmails","contributorEmails"],"instruction":"instruction","userEmailAddress":"userEmailAddress","questionDuration":"questionDuration","languageCode":"languageCode","annotatedDatasetDisplayName":"annotatedDatasetDisplayName"},"imageClassificationConfig":{"annotationSpecSet":"annotationSpecSet","allowMultiLabel":True,"answerAggregationType":"STRING_AGGREGATION_TYPE_UNSPECIFIED"},"exampleCount":1,"exampleSamplePercentage":5.962133916683182,"textClassificationConfig":{"annotationSpecSet":"annotationSpecSet","sentimentConfig":{"enableLabelSentimentSelection":True},"allowMultiLabel":True},"evaluationConfig":{"boundingBoxEvaluationOptions":{"iouThreshold":0.8008282}},"bigqueryImportKeys":{"key":"bigqueryImportKeys"}},"name":"name","description":"description","state":"STATE_UNSPECIFIED","attempts":[{"attemptTime":"attemptTime","partialFailures":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}]},{"attemptTime":"attemptTime","partialFailures":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}]}]}
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluation_jobs_pause(client):
    """Test case for datalabeling_projects_evaluation_jobs_pause

    
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
        path='/v1beta1/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluation_jobs_resume(client):
    """Test case for datalabeling_projects_evaluation_jobs_resume

    
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
        path='/v1beta1/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_evaluations_search(client):
    """Test case for datalabeling_projects_evaluations_search

    
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
        path='/v1beta1/{parent}/evaluations:search'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_instructions_create(client):
    """Test case for datalabeling_projects_instructions_create

    
    """
    body = {"instruction":{"createTime":"createTime","displayName":"displayName","dataType":"DATA_TYPE_UNSPECIFIED","name":"name","blockingResources":["blockingResources","blockingResources"],"description":"description","updateTime":"updateTime","csvInstruction":{"gcsFileUri":"gcsFileUri"},"pdfInstruction":{"gcsFileUri":"gcsFileUri"}}}
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
        path='/v1beta1/{parent}/instructions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_instructions_list(client):
    """Test case for datalabeling_projects_instructions_list

    
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
        path='/v1beta1/{parent}/instructions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_operations_cancel(client):
    """Test case for datalabeling_projects_operations_cancel

    
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
        path='/v1beta1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_operations_delete(client):
    """Test case for datalabeling_projects_operations_delete

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_operations_get(client):
    """Test case for datalabeling_projects_operations_get

    
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
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datalabeling_projects_operations_list(client):
    """Test case for datalabeling_projects_operations_list

    
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
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

