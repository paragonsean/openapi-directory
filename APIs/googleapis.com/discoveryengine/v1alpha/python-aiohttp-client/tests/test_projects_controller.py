# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_discoveryengine_v1alpha_batch_create_target_sites_request import GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_complete_query_response import GoogleCloudDiscoveryengineV1alphaCompleteQueryResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_conversation import GoogleCloudDiscoveryengineV1alphaConversation
from openapi_server.models.google_cloud_discoveryengine_v1alpha_converse_conversation_request import GoogleCloudDiscoveryengineV1alphaConverseConversationRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_converse_conversation_response import GoogleCloudDiscoveryengineV1alphaConverseConversationResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_data_store import GoogleCloudDiscoveryengineV1alphaDataStore
from openapi_server.models.google_cloud_discoveryengine_v1alpha_document import GoogleCloudDiscoveryengineV1alphaDocument
from openapi_server.models.google_cloud_discoveryengine_v1alpha_engine import GoogleCloudDiscoveryengineV1alphaEngine
from openapi_server.models.google_cloud_discoveryengine_v1alpha_estimate_data_size_request import GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_fetch_domain_verification_status_response import GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_import_documents_request import GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_import_suggestion_deny_list_entries_request import GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_import_user_events_request import GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_conversations_response import GoogleCloudDiscoveryengineV1alphaListConversationsResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_data_stores_response import GoogleCloudDiscoveryengineV1alphaListDataStoresResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_documents_response import GoogleCloudDiscoveryengineV1alphaListDocumentsResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_engines_response import GoogleCloudDiscoveryengineV1alphaListEnginesResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_schemas_response import GoogleCloudDiscoveryengineV1alphaListSchemasResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_serving_configs_response import GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_list_target_sites_response import GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_purge_documents_request import GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_purge_user_events_request import GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_recommend_request import GoogleCloudDiscoveryengineV1alphaRecommendRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_recommend_response import GoogleCloudDiscoveryengineV1alphaRecommendResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_recrawl_uris_request import GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_schema import GoogleCloudDiscoveryengineV1alphaSchema
from openapi_server.models.google_cloud_discoveryengine_v1alpha_search_request import GoogleCloudDiscoveryengineV1alphaSearchRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_search_response import GoogleCloudDiscoveryengineV1alphaSearchResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_target_site import GoogleCloudDiscoveryengineV1alphaTargetSite
from openapi_server.models.google_cloud_discoveryengine_v1alpha_train_custom_model_request import GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_user_event import GoogleCloudDiscoveryengineV1alphaUserEvent
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_data_stores_site_search_engine_batch_verify_target_sites(client):
    """Test case for discoveryengine_projects_locations_collections_data_stores_site_search_engine_batch_verify_target_sites

    
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
        path='/v1alpha/{parentbatch_verify_target_site}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_data_stores_site_search_engine_fetch_domain_verification_status(client):
    """Test case for discoveryengine_projects_locations_collections_data_stores_site_search_engine_fetch_domain_verification_status

    
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
        path='/v1alpha/{site_search_enginefetch_domain_verification_statu}'.format(site_search_engine='site_search_engine_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_data_stores_train_custom_model(client):
    """Test case for discoveryengine_projects_locations_collections_data_stores_train_custom_model

    
    """
    body = {"gcsTrainingInput":{"trainDataPath":"trainDataPath","testDataPath":"testDataPath","queryDataPath":"queryDataPath","corpusDataPath":"corpusDataPath"},"modelType":"modelType","errorConfig":{"gcsPrefix":"gcsPrefix"}}
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
        path='/v1alpha/{data_storetrain_custom_mode}'.format(data_store='data_store_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_engines_create(client):
    """Test case for discoveryengine_projects_locations_collections_engines_create

    
    """
    body = {"chatEngineMetadata":{"dialogflowAgent":"dialogflowAgent"},"displayName":"displayName","industryVertical":"INDUSTRY_VERTICAL_UNSPECIFIED","allowMultipleDataStoresSearchEngine":True,"searchEngineConfig":{"searchAddOns":["SEARCH_ADD_ON_UNSPECIFIED","SEARCH_ADD_ON_UNSPECIFIED"],"searchTier":"SEARCH_TIER_UNSPECIFIED"},"updateTime":"updateTime","chatEngineConfig":{"agentCreationConfig":{"business":"business","timeZone":"timeZone","defaultLanguageCode":"defaultLanguageCode","location":"location"},"dialogflowAgentToLink":"dialogflowAgentToLink"},"similarDocumentsConfig":"{}","commonConfig":{"companyName":"companyName"},"dataStoreIds":["dataStoreIds","dataStoreIds"],"createTime":"createTime","mediaRecommendationEngineConfig":{"optimizationObjective":"optimizationObjective","trainingState":"TRAINING_STATE_UNSPECIFIED","type":"type","optimizationObjectiveConfig":{"targetField":"targetField","targetFieldValueFloat":0.8008282}},"recommendationMetadata":{"tuningOperation":"tuningOperation","dataState":"DATA_STATE_UNSPECIFIED","lastTuneTime":"lastTuneTime","servingState":"SERVING_STATE_UNSPECIFIED"},"name":"name","solutionType":"SOLUTION_TYPE_UNSPECIFIED"}
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
                    ('engineId', 'engine_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/engines'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_engines_list(client):
    """Test case for discoveryengine_projects_locations_collections_engines_list

    
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
        path='/v1alpha/{parent}/engines'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_engines_pause(client):
    """Test case for discoveryengine_projects_locations_collections_engines_pause

    
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
        path='/v1alpha/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_engines_resume(client):
    """Test case for discoveryengine_projects_locations_collections_engines_resume

    
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
        path='/v1alpha/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_collections_engines_tune(client):
    """Test case for discoveryengine_projects_locations_collections_engines_tune

    
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
        path='/v1alpha/{nametun}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_branches_documents_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_branches_documents_create

    
    """
    body = {"indexTime":"indexTime","jsonData":"jsonData","derivedStructData":{"key":""},"schemaId":"schemaId","aclInfo":{"readers":[{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]},{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]}]},"name":"name","id":"id","content":{"mimeType":"mimeType","uri":"uri","rawBytes":"rawBytes"},"parentDocumentId":"parentDocumentId","structData":{"key":""}}
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
                    ('documentId', 'document_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/documents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_branches_documents_import(client):
    """Test case for discoveryengine_projects_locations_data_stores_branches_documents_import

    
    """
    body = {"idField":"idField","bigquerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]},"autoGenerateIds":True,"inlineSource":{"documents":[{"indexTime":"indexTime","jsonData":"jsonData","derivedStructData":{"key":""},"schemaId":"schemaId","aclInfo":{"readers":[{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]},{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]}]},"name":"name","id":"id","content":{"mimeType":"mimeType","uri":"uri","rawBytes":"rawBytes"},"parentDocumentId":"parentDocumentId","structData":{"key":""}},{"indexTime":"indexTime","jsonData":"jsonData","derivedStructData":{"key":""},"schemaId":"schemaId","aclInfo":{"readers":[{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]},{"principals":[{"groupId":"groupId","userId":"userId"},{"groupId":"groupId","userId":"userId"}]}]},"name":"name","id":"id","content":{"mimeType":"mimeType","uri":"uri","rawBytes":"rawBytes"},"parentDocumentId":"parentDocumentId","structData":{"key":""}}]},"reconciliationMode":"RECONCILIATION_MODE_UNSPECIFIED","errorConfig":{"gcsPrefix":"gcsPrefix"}}
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
        path='/v1alpha/{parent}/documents:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_branches_documents_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_branches_documents_list

    
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
        path='/v1alpha/{parent}/documents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_branches_documents_purge(client):
    """Test case for discoveryengine_projects_locations_data_stores_branches_documents_purge

    
    """
    body = {"filter":"filter","force":True,"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]},"errorConfig":{"gcsPrefix":"gcsPrefix"}}
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
        path='/v1alpha/{parent}/documents:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_complete_query(client):
    """Test case for discoveryengine_projects_locations_data_stores_complete_query

    
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
                    ('includeTailSuggestions', True),
                    ('query', 'query_example'),
                    ('queryModel', 'query_model_example'),
                    ('userPseudoId', 'user_pseudo_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{data_storecomplete_quer}'.format(data_store='data_store_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_conversations_converse(client):
    """Test case for discoveryengine_projects_locations_data_stores_conversations_converse

    
    """
    body = {"filter":"filter","servingConfig":"servingConfig","summarySpec":{"ignoreAdversarialQuery":True,"ignoreNonSummarySeekingQuery":True,"modelSpec":{"version":"version"},"summaryResultCount":2,"includeCitations":True,"languageCode":"languageCode","modelPromptSpec":{"preamble":"preamble"}},"query":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"name":"name","userLabels":{"key":"userLabels"},"safeSearch":True,"boostSpec":{"conditionBoostSpecs":[{"condition":"condition","boost":0.8008282},{"condition":"condition","boost":0.8008282}]},"conversation":{"userPseudoId":"userPseudoId","name":"name","messages":[{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}},{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}}],"startTime":"startTime","endTime":"endTime","state":"STATE_UNSPECIFIED"}}
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
        path='/v1alpha/{nameconvers}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_conversations_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_conversations_create

    
    """
    body = {"userPseudoId":"userPseudoId","name":"name","messages":[{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}},{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}}],"startTime":"startTime","endTime":"endTime","state":"STATE_UNSPECIFIED"}
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
        path='/v1alpha/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_conversations_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_conversations_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_create

    
    """
    body = {"idpConfig":{"externalIdpConfig":{"workforcePoolName":"workforcePoolName"},"idpType":"IDP_TYPE_UNSPECIFIED"},"createTime":"createTime","aclEnabled":True,"displayName":"displayName","industryVertical":"INDUSTRY_VERTICAL_UNSPECIFIED","name":"name","startingSchema":{"structSchema":{"key":""},"jsonSchema":"jsonSchema","name":"name","fieldConfigs":[{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","keyPropertyType":"keyPropertyType","recsFilterableOption":"FILTERABLE_OPTION_UNSPECIFIED","completableOption":"COMPLETABLE_OPTION_UNSPECIFIED","fieldPath":"fieldPath","searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","fieldType":"FIELD_TYPE_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED"},{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","keyPropertyType":"keyPropertyType","recsFilterableOption":"FILTERABLE_OPTION_UNSPECIFIED","completableOption":"COMPLETABLE_OPTION_UNSPECIFIED","fieldPath":"fieldPath","searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","fieldType":"FIELD_TYPE_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED"}]},"contentConfig":"CONTENT_CONFIG_UNSPECIFIED","solutionTypes":["SOLUTION_TYPE_UNSPECIFIED","SOLUTION_TYPE_UNSPECIFIED"],"defaultSchemaId":"defaultSchemaId","documentProcessingConfig":{"name":"name","defaultParsingConfig":{"layoutParsingConfig":"{}","ocrParsingConfig":{"enhancedDocumentElements":["enhancedDocumentElements","enhancedDocumentElements"],"useNativeText":True},"digitalParsingConfig":"{}"},"ocrConfig":{"enhancedDocumentElements":["enhancedDocumentElements","enhancedDocumentElements"],"useNativeText":True,"enabled":True},"parsingConfigOverrides":{"key":{"layoutParsingConfig":"{}","ocrParsingConfig":{"enhancedDocumentElements":["enhancedDocumentElements","enhancedDocumentElements"],"useNativeText":True},"digitalParsingConfig":"{}"}}}}
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
                    ('createAdvancedSiteSearch', True),
                    ('dataStoreId', 'data_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/dataStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_list

    
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
        path='/v1alpha/{parent}/dataStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_schemas_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_schemas_create

    
    """
    body = {"structSchema":{"key":""},"jsonSchema":"jsonSchema","name":"name","fieldConfigs":[{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","keyPropertyType":"keyPropertyType","recsFilterableOption":"FILTERABLE_OPTION_UNSPECIFIED","completableOption":"COMPLETABLE_OPTION_UNSPECIFIED","fieldPath":"fieldPath","searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","fieldType":"FIELD_TYPE_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED"},{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","keyPropertyType":"keyPropertyType","recsFilterableOption":"FILTERABLE_OPTION_UNSPECIFIED","completableOption":"COMPLETABLE_OPTION_UNSPECIFIED","fieldPath":"fieldPath","searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","fieldType":"FIELD_TYPE_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED"}]}
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
                    ('schemaId', 'schema_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/schemas'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_schemas_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_schemas_list

    
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
        path='/v1alpha/{parent}/schemas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_serving_configs_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_serving_configs_list

    
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
        path='/v1alpha/{parent}/servingConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_serving_configs_recommend(client):
    """Test case for discoveryengine_projects_locations_data_stores_serving_configs_recommend

    
    """
    body = {"filter":"filter","userEvent":{"userInfo":{"userAgent":"userAgent","userId":"userId"},"documents":[{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"},{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"}],"attributionToken":"attributionToken","tagIds":["tagIds","tagIds"],"userPseudoId":"userPseudoId","pageInfo":{"referrerUri":"referrerUri","pageCategory":"pageCategory","uri":"uri","pageviewId":"pageviewId"},"promotionIds":["promotionIds","promotionIds"],"eventType":"eventType","sessionId":"sessionId","transactionInfo":{"cost":9.301444,"currency":"currency","tax":2.027123,"discountValue":3.6160767,"value":4.145608,"transactionId":"transactionId"},"filter":"filter","directUserRequest":True,"searchInfo":{"offset":7,"searchQuery":"searchQuery","orderBy":"orderBy"},"eventTime":"eventTime","completionInfo":{"selectedSuggestion":"selectedSuggestion","selectedPosition":6},"attributes":{"key":{"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"]}},"panel":{"panelPosition":5,"panelId":"panelId","displayName":"displayName","totalPanels":2},"mediaInfo":{"mediaProgressPercentage":5.962134,"mediaProgressDuration":"mediaProgressDuration"}},"validateOnly":True,"pageSize":0,"userLabels":{"key":"userLabels"},"params":{"key":""}}
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
        path='/v1alpha/{serving_configrecommen}'.format(serving_config='serving_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_serving_configs_search(client):
    """Test case for discoveryengine_projects_locations_data_stores_serving_configs_search

    
    """
    body = {"queryExpansionSpec":{"condition":"CONDITION_UNSPECIFIED","pinUnexpandedResults":True},"userInfo":{"userAgent":"userAgent","userId":"userId"},"offset":1,"rankingExpression":"rankingExpression","query":"query","userPseudoId":"userPseudoId","orderBy":"orderBy","pageSize":5,"userLabels":{"key":"userLabels"},"contentSearchSpec":{"extractiveContentSpec":{"maxExtractiveAnswerCount":0,"maxExtractiveSegmentCount":6,"numPreviousSegments":5,"numNextSegments":1},"summarySpec":{"ignoreAdversarialQuery":True,"ignoreNonSummarySeekingQuery":True,"modelSpec":{"version":"version"},"summaryResultCount":2,"includeCitations":True,"languageCode":"languageCode","modelPromptSpec":{"preamble":"preamble"}},"snippetSpec":{"maxSnippetCount":5,"referenceOnly":True,"returnSnippet":True}},"params":{"key":""},"branch":"branch","safeSearch":True,"boostSpec":{"conditionBoostSpecs":[{"condition":"condition","boost":0.8008282},{"condition":"condition","boost":0.8008282}]},"embeddingSpec":{"embeddingVectors":[{"fieldPath":"fieldPath","vector":[0.8008282,0.8008282]},{"fieldPath":"fieldPath","vector":[0.8008282,0.8008282]}]},"filter":"filter","spellCorrectionSpec":{"mode":"MODE_UNSPECIFIED"},"customFineTuningSpec":{"enableSearchAdaptor":True},"imageQuery":{"imageBytes":"imageBytes"},"facetSpecs":[{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":6,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]},{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":6,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]}],"servingConfig":"servingConfig","pageToken":"pageToken","canonicalFilter":"canonicalFilter"}
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
        path='/v1alpha/{serving_configsearc}'.format(serving_config='serving_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_disable_advanced_site_search(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_disable_advanced_site_search

    
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
        path='/v1alpha/{site_search_enginedisable_advanced_site_searc}'.format(site_search_engine='site_search_engine_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_enable_advanced_site_search(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_enable_advanced_site_search

    
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
        path='/v1alpha/{site_search_engineenable_advanced_site_searc}'.format(site_search_engine='site_search_engine_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_recrawl_uris(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_recrawl_uris

    
    """
    body = {"uris":["uris","uris"]}
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
        path='/v1alpha/{site_search_enginerecrawl_uri}'.format(site_search_engine='site_search_engine_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_batch_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_batch_create

    
    """
    body = {"requests":[{"parent":"parent","targetSite":{"providedUriPattern":"providedUriPattern","siteVerificationInfo":{"siteVerificationState":"SITE_VERIFICATION_STATE_UNSPECIFIED","verifyTime":"verifyTime"},"exactMatch":True,"failureReason":{"quotaFailure":{"totalRequiredQuota":"totalRequiredQuota"}},"name":"name","indexingStatus":"INDEXING_STATUS_UNSPECIFIED","updateTime":"updateTime","generatedUriPattern":"generatedUriPattern","type":"TYPE_UNSPECIFIED"}},{"parent":"parent","targetSite":{"providedUriPattern":"providedUriPattern","siteVerificationInfo":{"siteVerificationState":"SITE_VERIFICATION_STATE_UNSPECIFIED","verifyTime":"verifyTime"},"exactMatch":True,"failureReason":{"quotaFailure":{"totalRequiredQuota":"totalRequiredQuota"}},"name":"name","indexingStatus":"INDEXING_STATUS_UNSPECIFIED","updateTime":"updateTime","generatedUriPattern":"generatedUriPattern","type":"TYPE_UNSPECIFIED"}}]}
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
        path='/v1alpha/{parent}/targetSites:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_create(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_create

    
    """
    body = {"providedUriPattern":"providedUriPattern","siteVerificationInfo":{"siteVerificationState":"SITE_VERIFICATION_STATE_UNSPECIFIED","verifyTime":"verifyTime"},"exactMatch":True,"failureReason":{"quotaFailure":{"totalRequiredQuota":"totalRequiredQuota"}},"name":"name","indexingStatus":"INDEXING_STATUS_UNSPECIFIED","updateTime":"updateTime","generatedUriPattern":"generatedUriPattern","type":"TYPE_UNSPECIFIED"}
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
        path='/v1alpha/{parent}/targetSites'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_delete(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_delete

    
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_list(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_list

    
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
        path='/v1alpha/{parent}/targetSites'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_patch(client):
    """Test case for discoveryengine_projects_locations_data_stores_site_search_engine_target_sites_patch

    
    """
    body = {"providedUriPattern":"providedUriPattern","siteVerificationInfo":{"siteVerificationState":"SITE_VERIFICATION_STATE_UNSPECIFIED","verifyTime":"verifyTime"},"exactMatch":True,"failureReason":{"quotaFailure":{"totalRequiredQuota":"totalRequiredQuota"}},"name":"name","indexingStatus":"INDEXING_STATUS_UNSPECIFIED","updateTime":"updateTime","generatedUriPattern":"generatedUriPattern","type":"TYPE_UNSPECIFIED"}
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_suggestion_deny_list_entries_import(client):
    """Test case for discoveryengine_projects_locations_data_stores_suggestion_deny_list_entries_import

    
    """
    body = {"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]},"inlineSource":{"entries":[{"blockPhrase":"blockPhrase","matchOperator":"MATCH_OPERATOR_UNSPECIFIED"},{"blockPhrase":"blockPhrase","matchOperator":"MATCH_OPERATOR_UNSPECIFIED"}]}}
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
        path='/v1alpha/{parent}/suggestionDenyListEntries:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_suggestion_deny_list_entries_purge(client):
    """Test case for discoveryengine_projects_locations_data_stores_suggestion_deny_list_entries_purge

    
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
        path='/v1alpha/{parent}/suggestionDenyListEntries:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_user_events_collect(client):
    """Test case for discoveryengine_projects_locations_data_stores_user_events_collect

    
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
                    ('ets', 'ets_example'),
                    ('uri', 'uri_example'),
                    ('userEvent', 'user_event_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/userEvents:collect'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_user_events_import(client):
    """Test case for discoveryengine_projects_locations_data_stores_user_events_import

    
    """
    body = {"bigquerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]},"inlineSource":{"userEvents":[{"userInfo":{"userAgent":"userAgent","userId":"userId"},"documents":[{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"},{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"}],"attributionToken":"attributionToken","tagIds":["tagIds","tagIds"],"userPseudoId":"userPseudoId","pageInfo":{"referrerUri":"referrerUri","pageCategory":"pageCategory","uri":"uri","pageviewId":"pageviewId"},"promotionIds":["promotionIds","promotionIds"],"eventType":"eventType","sessionId":"sessionId","transactionInfo":{"cost":9.301444,"currency":"currency","tax":2.027123,"discountValue":3.6160767,"value":4.145608,"transactionId":"transactionId"},"filter":"filter","directUserRequest":True,"searchInfo":{"offset":7,"searchQuery":"searchQuery","orderBy":"orderBy"},"eventTime":"eventTime","completionInfo":{"selectedSuggestion":"selectedSuggestion","selectedPosition":6},"attributes":{"key":{"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"]}},"panel":{"panelPosition":5,"panelId":"panelId","displayName":"displayName","totalPanels":2},"mediaInfo":{"mediaProgressPercentage":5.962134,"mediaProgressDuration":"mediaProgressDuration"}},{"userInfo":{"userAgent":"userAgent","userId":"userId"},"documents":[{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"},{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"}],"attributionToken":"attributionToken","tagIds":["tagIds","tagIds"],"userPseudoId":"userPseudoId","pageInfo":{"referrerUri":"referrerUri","pageCategory":"pageCategory","uri":"uri","pageviewId":"pageviewId"},"promotionIds":["promotionIds","promotionIds"],"eventType":"eventType","sessionId":"sessionId","transactionInfo":{"cost":9.301444,"currency":"currency","tax":2.027123,"discountValue":3.6160767,"value":4.145608,"transactionId":"transactionId"},"filter":"filter","directUserRequest":True,"searchInfo":{"offset":7,"searchQuery":"searchQuery","orderBy":"orderBy"},"eventTime":"eventTime","completionInfo":{"selectedSuggestion":"selectedSuggestion","selectedPosition":6},"attributes":{"key":{"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"]}},"panel":{"panelPosition":5,"panelId":"panelId","displayName":"displayName","totalPanels":2},"mediaInfo":{"mediaProgressPercentage":5.962134,"mediaProgressDuration":"mediaProgressDuration"}}]},"errorConfig":{"gcsPrefix":"gcsPrefix"}}
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
        path='/v1alpha/{parent}/userEvents:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_user_events_purge(client):
    """Test case for discoveryengine_projects_locations_data_stores_user_events_purge

    
    """
    body = {"filter":"filter","force":True}
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
        path='/v1alpha/{parent}/userEvents:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_data_stores_user_events_write(client):
    """Test case for discoveryengine_projects_locations_data_stores_user_events_write

    
    """
    body = {"userInfo":{"userAgent":"userAgent","userId":"userId"},"documents":[{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"},{"quantity":1,"name":"name","promotionIds":["promotionIds","promotionIds"],"id":"id","uri":"uri"}],"attributionToken":"attributionToken","tagIds":["tagIds","tagIds"],"userPseudoId":"userPseudoId","pageInfo":{"referrerUri":"referrerUri","pageCategory":"pageCategory","uri":"uri","pageviewId":"pageviewId"},"promotionIds":["promotionIds","promotionIds"],"eventType":"eventType","sessionId":"sessionId","transactionInfo":{"cost":9.301444,"currency":"currency","tax":2.027123,"discountValue":3.6160767,"value":4.145608,"transactionId":"transactionId"},"filter":"filter","directUserRequest":True,"searchInfo":{"offset":7,"searchQuery":"searchQuery","orderBy":"orderBy"},"eventTime":"eventTime","completionInfo":{"selectedSuggestion":"selectedSuggestion","selectedPosition":6},"attributes":{"key":{"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"]}},"panel":{"panelPosition":5,"panelId":"panelId","displayName":"displayName","totalPanels":2},"mediaInfo":{"mediaProgressPercentage":5.962134,"mediaProgressDuration":"mediaProgressDuration"}}
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
        path='/v1alpha/{parent}/userEvents:write'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_locations_estimate_data_size(client):
    """Test case for discoveryengine_projects_locations_estimate_data_size

    
    """
    body = {"fileDataSource":{"bigquerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]}},"websiteDataSource":{"estimatorUriPatterns":[{"providedUriPattern":"providedUriPattern","exactMatch":True,"exclusive":True},{"providedUriPattern":"providedUriPattern","exactMatch":True,"exclusive":True}]}}
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
        path='/v1alpha/{locationestimate_data_siz}'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_operations_get(client):
    """Test case for discoveryengine_projects_operations_get

    
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_projects_operations_list(client):
    """Test case for discoveryengine_projects_operations_list

    
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
        path='/v1alpha/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

