# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_contactcenterinsights_v1_analysis import GoogleCloudContactcenterinsightsV1Analysis
from openapi_server.models.google_cloud_contactcenterinsights_v1_bulk_analyze_conversations_request import GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_bulk_delete_conversations_request import GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_calculate_issue_model_stats_response import GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_calculate_stats_response import GoogleCloudContactcenterinsightsV1CalculateStatsResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_conversation import GoogleCloudContactcenterinsightsV1Conversation
from openapi_server.models.google_cloud_contactcenterinsights_v1_deploy_issue_model_request import GoogleCloudContactcenterinsightsV1DeployIssueModelRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_export_insights_data_request import GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_export_issue_model_request import GoogleCloudContactcenterinsightsV1ExportIssueModelRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_import_issue_model_request import GoogleCloudContactcenterinsightsV1ImportIssueModelRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_ingest_conversations_request import GoogleCloudContactcenterinsightsV1IngestConversationsRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_issue_model import GoogleCloudContactcenterinsightsV1IssueModel
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_analyses_response import GoogleCloudContactcenterinsightsV1ListAnalysesResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_conversations_response import GoogleCloudContactcenterinsightsV1ListConversationsResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_issue_models_response import GoogleCloudContactcenterinsightsV1ListIssueModelsResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_issues_response import GoogleCloudContactcenterinsightsV1ListIssuesResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_phrase_matchers_response import GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_list_views_response import GoogleCloudContactcenterinsightsV1ListViewsResponse
from openapi_server.models.google_cloud_contactcenterinsights_v1_phrase_matcher import GoogleCloudContactcenterinsightsV1PhraseMatcher
from openapi_server.models.google_cloud_contactcenterinsights_v1_undeploy_issue_model_request import GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_upload_conversation_request import GoogleCloudContactcenterinsightsV1UploadConversationRequest
from openapi_server.models.google_cloud_contactcenterinsights_v1_view import GoogleCloudContactcenterinsightsV1View
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_analyses_create(client):
    """Test case for contactcenterinsights_projects_locations_conversations_analyses_create

    
    """
    body = {"requestTime":"requestTime","createTime":"createTime","annotatorSelector":{"runIssueModelAnnotator":True,"runSummarizationAnnotator":True,"summarizationConfig":{"summarizationModel":"SUMMARIZATION_MODEL_UNSPECIFIED","conversationProfile":"conversationProfile"},"runInterruptionAnnotator":True,"runSilenceAnnotator":True,"runSentimentAnnotator":True,"phraseMatchers":["phraseMatchers","phraseMatchers"],"runIntentAnnotator":True,"issueModels":["issueModels","issueModels"],"runPhraseMatcherAnnotator":True,"runEntityAnnotator":True},"name":"name","analysisResult":{"callAnalysisMetadata":{"intents":{"key":{"displayName":"displayName","id":"id"}},"entities":{"key":{"salience":7.0614014,"sentiment":{"score":5.637377,"magnitude":5.962134},"metadata":{"key":"metadata"},"displayName":"displayName","type":"TYPE_UNSPECIFIED"}},"annotations":[{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"},{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"}],"phraseMatchers":{"key":{"displayName":"displayName","phraseMatcher":"phraseMatcher"}},"sentiments":[{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9},{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9}],"issueModelResult":{"issueModel":"issueModel","issues":[{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"},{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}]}},"endTime":"endTime"}}
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
        path='/v1/{parent}/analyses'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_analyses_list(client):
    """Test case for contactcenterinsights_projects_locations_conversations_analyses_list

    
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
        path='/v1/{parent}/analyses'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_bulk_analyze(client):
    """Test case for contactcenterinsights_projects_locations_conversations_bulk_analyze

    
    """
    body = {"filter":"filter","parent":"parent","analysisPercentage":0.8008282,"annotatorSelector":{"runIssueModelAnnotator":True,"runSummarizationAnnotator":True,"summarizationConfig":{"summarizationModel":"SUMMARIZATION_MODEL_UNSPECIFIED","conversationProfile":"conversationProfile"},"runInterruptionAnnotator":True,"runSilenceAnnotator":True,"runSentimentAnnotator":True,"phraseMatchers":["phraseMatchers","phraseMatchers"],"runIntentAnnotator":True,"issueModels":["issueModels","issueModels"],"runPhraseMatcherAnnotator":True,"runEntityAnnotator":True}}
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
        path='/v1/{parent}/conversations:bulkAnalyze'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_bulk_delete(client):
    """Test case for contactcenterinsights_projects_locations_conversations_bulk_delete

    
    """
    body = {"filter":"filter","parent":"parent","maxDeleteCount":0,"force":True}
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
        path='/v1/{parent}/conversations:bulkDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_calculate_stats(client):
    """Test case for contactcenterinsights_projects_locations_conversations_calculate_stats

    
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
        path='/v1/{location}/conversations:calculateStats'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_create(client):
    """Test case for contactcenterinsights_projects_locations_conversations_create

    
    """
    body = {"agentId":"agentId","obfuscatedUserId":"obfuscatedUserId","latestSummary":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"updateTime":"updateTime","medium":"MEDIUM_UNSPECIFIED","dialogflowIntents":{"key":{"displayName":"displayName"}},"languageCode":"languageCode","qualityMetadata":{"waitDuration":"waitDuration","agentInfo":[{"agentId":"agentId","displayName":"displayName","team":"team","dispositionCode":"dispositionCode"},{"agentId":"agentId","displayName":"displayName","team":"team","dispositionCode":"dispositionCode"}],"menuPath":"menuPath","customerSatisfactionRating":5},"runtimeAnnotations":[{"faqAnswer":{"confidenceScore":7.0614014,"metadata":{"key":"metadata"},"answer":"answer","question":"question","source":"source","queryRecord":"queryRecord"},"startBoundary":{"transcriptIndex":0,"wordIndex":6},"dialogflowInteraction":{"confidence":2.302136,"dialogflowIntentId":"dialogflowIntentId"},"createTime":"createTime","answerFeedback":{"displayed":True,"clicked":True,"correctnessLevel":"CORRECTNESS_LEVEL_UNSPECIFIED"},"smartComposeSuggestion":{"confidenceScore":9.301444243932576,"metadata":{"key":"metadata"},"suggestion":"suggestion","queryRecord":"queryRecord"},"articleSuggestion":{"confidenceScore":5.637377,"metadata":{"key":"metadata"},"source":"source","title":"title","uri":"uri","queryRecord":"queryRecord"},"annotationId":"annotationId","conversationSummarizationSuggestion":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"endBoundary":{"transcriptIndex":0,"wordIndex":6},"smartReply":{"confidenceScore":3.616076749251911,"metadata":{"key":"metadata"},"reply":"reply","queryRecord":"queryRecord"}},{"faqAnswer":{"confidenceScore":7.0614014,"metadata":{"key":"metadata"},"answer":"answer","question":"question","source":"source","queryRecord":"queryRecord"},"startBoundary":{"transcriptIndex":0,"wordIndex":6},"dialogflowInteraction":{"confidence":2.302136,"dialogflowIntentId":"dialogflowIntentId"},"createTime":"createTime","answerFeedback":{"displayed":True,"clicked":True,"correctnessLevel":"CORRECTNESS_LEVEL_UNSPECIFIED"},"smartComposeSuggestion":{"confidenceScore":9.301444243932576,"metadata":{"key":"metadata"},"suggestion":"suggestion","queryRecord":"queryRecord"},"articleSuggestion":{"confidenceScore":5.637377,"metadata":{"key":"metadata"},"source":"source","title":"title","uri":"uri","queryRecord":"queryRecord"},"annotationId":"annotationId","conversationSummarizationSuggestion":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"endBoundary":{"transcriptIndex":0,"wordIndex":6},"smartReply":{"confidenceScore":3.616076749251911,"metadata":{"key":"metadata"},"reply":"reply","queryRecord":"queryRecord"}}],"ttl":"ttl","labels":{"key":"labels"},"callMetadata":{"agentChannel":0,"customerChannel":6},"duration":"duration","expireTime":"expireTime","transcript":{"transcriptSegments":[{"dialogflowSegmentMetadata":{"smartReplyAllowlistCovered":True},"messageTime":"messageTime","sentiment":{"score":5.637377,"magnitude":5.962134},"confidence":4.145608,"words":[{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"},{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"}],"text":"text","languageCode":"languageCode","channelTag":2,"segmentParticipant":{"role":"ROLE_UNSPECIFIED","dialogflowParticipant":"dialogflowParticipant","dialogflowParticipantName":"dialogflowParticipantName","obfuscatedExternalUserId":"obfuscatedExternalUserId","userId":"userId"}},{"dialogflowSegmentMetadata":{"smartReplyAllowlistCovered":True},"messageTime":"messageTime","sentiment":{"score":5.637377,"magnitude":5.962134},"confidence":4.145608,"words":[{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"},{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"}],"text":"text","languageCode":"languageCode","channelTag":2,"segmentParticipant":{"role":"ROLE_UNSPECIFIED","dialogflowParticipant":"dialogflowParticipant","dialogflowParticipantName":"dialogflowParticipantName","obfuscatedExternalUserId":"obfuscatedExternalUserId","userId":"userId"}}]},"createTime":"createTime","name":"name","latestAnalysis":{"requestTime":"requestTime","createTime":"createTime","annotatorSelector":{"runIssueModelAnnotator":True,"runSummarizationAnnotator":True,"summarizationConfig":{"summarizationModel":"SUMMARIZATION_MODEL_UNSPECIFIED","conversationProfile":"conversationProfile"},"runInterruptionAnnotator":True,"runSilenceAnnotator":True,"runSentimentAnnotator":True,"phraseMatchers":["phraseMatchers","phraseMatchers"],"runIntentAnnotator":True,"issueModels":["issueModels","issueModels"],"runPhraseMatcherAnnotator":True,"runEntityAnnotator":True},"name":"name","analysisResult":{"callAnalysisMetadata":{"intents":{"key":{"displayName":"displayName","id":"id"}},"entities":{"key":{"salience":7.0614014,"sentiment":{"score":5.637377,"magnitude":5.962134},"metadata":{"key":"metadata"},"displayName":"displayName","type":"TYPE_UNSPECIFIED"}},"annotations":[{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"},{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"}],"phraseMatchers":{"key":{"displayName":"displayName","phraseMatcher":"phraseMatcher"}},"sentiments":[{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9},{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9}],"issueModelResult":{"issueModel":"issueModel","issues":[{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"},{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}]}},"endTime":"endTime"}},"turnCount":1,"startTime":"startTime","dataSource":{"dialogflowSource":{"dialogflowConversation":"dialogflowConversation","audioUri":"audioUri"},"gcsSource":{"transcriptUri":"transcriptUri","audioUri":"audioUri"}}}
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
                    ('conversationId', 'conversation_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_ingest(client):
    """Test case for contactcenterinsights_projects_locations_conversations_ingest

    
    """
    body = {"parent":"parent","speechConfig":{"speechRecognizer":"speechRecognizer"},"transcriptObjectConfig":{"medium":"MEDIUM_UNSPECIFIED"},"conversationConfig":{"agentId":"agentId","agentChannel":0,"customerChannel":6},"redactionConfig":{"deidentifyTemplate":"deidentifyTemplate","inspectTemplate":"inspectTemplate"},"gcsSource":{"bucketUri":"bucketUri","bucketObjectType":"BUCKET_OBJECT_TYPE_UNSPECIFIED","customMetadataKeys":["customMetadataKeys","customMetadataKeys"],"metadataBucketUri":"metadataBucketUri"}}
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
        path='/v1/{parent}/conversations:ingest'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_list(client):
    """Test case for contactcenterinsights_projects_locations_conversations_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_conversations_upload(client):
    """Test case for contactcenterinsights_projects_locations_conversations_upload

    
    """
    body = {"parent":"parent","speechConfig":{"speechRecognizer":"speechRecognizer"},"conversationId":"conversationId","redactionConfig":{"deidentifyTemplate":"deidentifyTemplate","inspectTemplate":"inspectTemplate"},"conversation":{"agentId":"agentId","obfuscatedUserId":"obfuscatedUserId","latestSummary":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"updateTime":"updateTime","medium":"MEDIUM_UNSPECIFIED","dialogflowIntents":{"key":{"displayName":"displayName"}},"languageCode":"languageCode","qualityMetadata":{"waitDuration":"waitDuration","agentInfo":[{"agentId":"agentId","displayName":"displayName","team":"team","dispositionCode":"dispositionCode"},{"agentId":"agentId","displayName":"displayName","team":"team","dispositionCode":"dispositionCode"}],"menuPath":"menuPath","customerSatisfactionRating":5},"runtimeAnnotations":[{"faqAnswer":{"confidenceScore":7.0614014,"metadata":{"key":"metadata"},"answer":"answer","question":"question","source":"source","queryRecord":"queryRecord"},"startBoundary":{"transcriptIndex":0,"wordIndex":6},"dialogflowInteraction":{"confidence":2.302136,"dialogflowIntentId":"dialogflowIntentId"},"createTime":"createTime","answerFeedback":{"displayed":True,"clicked":True,"correctnessLevel":"CORRECTNESS_LEVEL_UNSPECIFIED"},"smartComposeSuggestion":{"confidenceScore":9.301444243932576,"metadata":{"key":"metadata"},"suggestion":"suggestion","queryRecord":"queryRecord"},"articleSuggestion":{"confidenceScore":5.637377,"metadata":{"key":"metadata"},"source":"source","title":"title","uri":"uri","queryRecord":"queryRecord"},"annotationId":"annotationId","conversationSummarizationSuggestion":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"endBoundary":{"transcriptIndex":0,"wordIndex":6},"smartReply":{"confidenceScore":3.616076749251911,"metadata":{"key":"metadata"},"reply":"reply","queryRecord":"queryRecord"}},{"faqAnswer":{"confidenceScore":7.0614014,"metadata":{"key":"metadata"},"answer":"answer","question":"question","source":"source","queryRecord":"queryRecord"},"startBoundary":{"transcriptIndex":0,"wordIndex":6},"dialogflowInteraction":{"confidence":2.302136,"dialogflowIntentId":"dialogflowIntentId"},"createTime":"createTime","answerFeedback":{"displayed":True,"clicked":True,"correctnessLevel":"CORRECTNESS_LEVEL_UNSPECIFIED"},"smartComposeSuggestion":{"confidenceScore":9.301444243932576,"metadata":{"key":"metadata"},"suggestion":"suggestion","queryRecord":"queryRecord"},"articleSuggestion":{"confidenceScore":5.637377,"metadata":{"key":"metadata"},"source":"source","title":"title","uri":"uri","queryRecord":"queryRecord"},"annotationId":"annotationId","conversationSummarizationSuggestion":{"conversationModel":"conversationModel","metadata":{"key":"metadata"},"answerRecord":"answerRecord","confidence":1.4658129,"textSections":{"key":"textSections"},"text":"text"},"endBoundary":{"transcriptIndex":0,"wordIndex":6},"smartReply":{"confidenceScore":3.616076749251911,"metadata":{"key":"metadata"},"reply":"reply","queryRecord":"queryRecord"}}],"ttl":"ttl","labels":{"key":"labels"},"callMetadata":{"agentChannel":0,"customerChannel":6},"duration":"duration","expireTime":"expireTime","transcript":{"transcriptSegments":[{"dialogflowSegmentMetadata":{"smartReplyAllowlistCovered":True},"messageTime":"messageTime","sentiment":{"score":5.637377,"magnitude":5.962134},"confidence":4.145608,"words":[{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"},{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"}],"text":"text","languageCode":"languageCode","channelTag":2,"segmentParticipant":{"role":"ROLE_UNSPECIFIED","dialogflowParticipant":"dialogflowParticipant","dialogflowParticipantName":"dialogflowParticipantName","obfuscatedExternalUserId":"obfuscatedExternalUserId","userId":"userId"}},{"dialogflowSegmentMetadata":{"smartReplyAllowlistCovered":True},"messageTime":"messageTime","sentiment":{"score":5.637377,"magnitude":5.962134},"confidence":4.145608,"words":[{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"},{"endOffset":"endOffset","startOffset":"startOffset","confidence":7.386282,"word":"word"}],"text":"text","languageCode":"languageCode","channelTag":2,"segmentParticipant":{"role":"ROLE_UNSPECIFIED","dialogflowParticipant":"dialogflowParticipant","dialogflowParticipantName":"dialogflowParticipantName","obfuscatedExternalUserId":"obfuscatedExternalUserId","userId":"userId"}}]},"createTime":"createTime","name":"name","latestAnalysis":{"requestTime":"requestTime","createTime":"createTime","annotatorSelector":{"runIssueModelAnnotator":True,"runSummarizationAnnotator":True,"summarizationConfig":{"summarizationModel":"SUMMARIZATION_MODEL_UNSPECIFIED","conversationProfile":"conversationProfile"},"runInterruptionAnnotator":True,"runSilenceAnnotator":True,"runSentimentAnnotator":True,"phraseMatchers":["phraseMatchers","phraseMatchers"],"runIntentAnnotator":True,"issueModels":["issueModels","issueModels"],"runPhraseMatcherAnnotator":True,"runEntityAnnotator":True},"name":"name","analysisResult":{"callAnalysisMetadata":{"intents":{"key":{"displayName":"displayName","id":"id"}},"entities":{"key":{"salience":7.0614014,"sentiment":{"score":5.637377,"magnitude":5.962134},"metadata":{"key":"metadata"},"displayName":"displayName","type":"TYPE_UNSPECIFIED"}},"annotations":[{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"},{"issueMatchData":{"issueAssignment":{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}},"holdData":"{}","intentMatchData":{"intentUniqueId":"intentUniqueId"},"sentimentData":{"score":5.637377,"magnitude":5.962134},"silenceData":"{}","annotationEndBoundary":{"transcriptIndex":0,"wordIndex":6},"annotationStartBoundary":{"transcriptIndex":0,"wordIndex":6},"entityMentionData":{"sentiment":{"score":5.637377,"magnitude":5.962134},"entityUniqueId":"entityUniqueId","type":"MENTION_TYPE_UNSPECIFIED"},"phraseMatchData":{"displayName":"displayName","phraseMatcher":"phraseMatcher"},"channelTag":1,"interruptionData":"{}"}],"phraseMatchers":{"key":{"displayName":"displayName","phraseMatcher":"phraseMatcher"}},"sentiments":[{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9},{"sentimentData":{"score":5.637377,"magnitude":5.962134},"channelTag":9}],"issueModelResult":{"issueModel":"issueModel","issues":[{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"},{"score":2.3021358869347655,"issue":"issue","displayName":"displayName"}]}},"endTime":"endTime"}},"turnCount":1,"startTime":"startTime","dataSource":{"dialogflowSource":{"dialogflowConversation":"dialogflowConversation","audioUri":"audioUri"},"gcsSource":{"transcriptUri":"transcriptUri","audioUri":"audioUri"}}}}
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
        path='/v1/{parent}/conversations:upload'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_insightsdata_export(client):
    """Test case for contactcenterinsights_projects_locations_insightsdata_export

    
    """
    body = {"bigQueryDestination":{"dataset":"dataset","projectId":"projectId","table":"table"},"filter":"filter","parent":"parent","kmsKey":"kmsKey","writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED"}
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
        path='/v1/{parent}/insightsdata:export'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_calculate_issue_model_stats(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_calculate_issue_model_stats

    
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
        path='/v1/{issue_modelcalculate_issue_model_stat}'.format(issue_model='issue_model_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_create(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","trainingStats":{"unclassifiedConversationsCount":"unclassifiedConversationsCount","issueStats":{"key":{"issue":"issue","displayName":"displayName","labeledConversationsCount":"labeledConversationsCount"}},"analyzedConversationsCount":"analyzedConversationsCount"},"updateTime":"updateTime","modelType":"MODEL_TYPE_UNSPECIFIED","state":"STATE_UNSPECIFIED","languageCode":"languageCode","issueCount":"issueCount","inputDataConfig":{"filter":"filter","trainingConversationsCount":"trainingConversationsCount","medium":"MEDIUM_UNSPECIFIED"}}
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
        path='/v1/{parent}/issueModels'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_deploy(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_deploy

    
    """
    body = {"name":"name"}
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

async def test_contactcenterinsights_projects_locations_issue_models_export(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_export

    
    """
    body = {"gcsDestination":{"objectUri":"objectUri"},"name":"name"}
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
        path='/v1/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_import(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_import

    
    """
    body = {"createNewModel":True,"parent":"parent","gcsSource":{"objectUri":"objectUri"}}
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
        path='/v1/{parent}/issueModels:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_issues_list(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_issues_list

    
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
        path='/v1/{parent}/issues'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_list(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_list

    
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
        path='/v1/{parent}/issueModels'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_issue_models_undeploy(client):
    """Test case for contactcenterinsights_projects_locations_issue_models_undeploy

    
    """
    body = {"name":"name"}
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

async def test_contactcenterinsights_projects_locations_operations_cancel(client):
    """Test case for contactcenterinsights_projects_locations_operations_cancel

    
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

async def test_contactcenterinsights_projects_locations_operations_list(client):
    """Test case for contactcenterinsights_projects_locations_operations_list

    
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_phrase_matchers_create(client):
    """Test case for contactcenterinsights_projects_locations_phrase_matchers_create

    
    """
    body = {"revisionId":"revisionId","displayName":"displayName","name":"name","active":True,"updateTime":"updateTime","versionTag":"versionTag","revisionCreateTime":"revisionCreateTime","type":"PHRASE_MATCHER_TYPE_UNSPECIFIED","activationUpdateTime":"activationUpdateTime","phraseMatchRuleGroups":[{"phraseMatchRules":[{"negated":True,"query":"query","config":{"exactMatchConfig":{"caseSensitive":True}}},{"negated":True,"query":"query","config":{"exactMatchConfig":{"caseSensitive":True}}}],"type":"PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED"},{"phraseMatchRules":[{"negated":True,"query":"query","config":{"exactMatchConfig":{"caseSensitive":True}}},{"negated":True,"query":"query","config":{"exactMatchConfig":{"caseSensitive":True}}}],"type":"PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED"}],"roleMatch":"ROLE_UNSPECIFIED"}
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
        path='/v1/{parent}/phraseMatchers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_phrase_matchers_list(client):
    """Test case for contactcenterinsights_projects_locations_phrase_matchers_list

    
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
        path='/v1/{parent}/phraseMatchers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_views_create(client):
    """Test case for contactcenterinsights_projects_locations_views_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","updateTime":"updateTime","value":"value"}
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
        path='/v1/{parent}/views'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_views_delete(client):
    """Test case for contactcenterinsights_projects_locations_views_delete

    
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
                    ('force', True)]
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

async def test_contactcenterinsights_projects_locations_views_get(client):
    """Test case for contactcenterinsights_projects_locations_views_get

    
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
                    ('view', 'view_example')]
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


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_views_list(client):
    """Test case for contactcenterinsights_projects_locations_views_list

    
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
        path='/v1/{parent}/views'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contactcenterinsights_projects_locations_views_patch(client):
    """Test case for contactcenterinsights_projects_locations_views_patch

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","updateTime":"updateTime","value":"value"}
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

