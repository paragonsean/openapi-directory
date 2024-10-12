# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_dialogflow_v2_agent import GoogleCloudDialogflowV2Agent
from openapi_server.models.google_cloud_dialogflow_v2_analyze_content_request import GoogleCloudDialogflowV2AnalyzeContentRequest
from openapi_server.models.google_cloud_dialogflow_v2_analyze_content_response import GoogleCloudDialogflowV2AnalyzeContentResponse
from openapi_server.models.google_cloud_dialogflow_v2_batch_create_entities_request import GoogleCloudDialogflowV2BatchCreateEntitiesRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_delete_entities_request import GoogleCloudDialogflowV2BatchDeleteEntitiesRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_delete_entity_types_request import GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_delete_intents_request import GoogleCloudDialogflowV2BatchDeleteIntentsRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_update_entities_request import GoogleCloudDialogflowV2BatchUpdateEntitiesRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_update_entity_types_request import GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest
from openapi_server.models.google_cloud_dialogflow_v2_batch_update_intents_request import GoogleCloudDialogflowV2BatchUpdateIntentsRequest
from openapi_server.models.google_cloud_dialogflow_v2_clear_suggestion_feature_config_request import GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest
from openapi_server.models.google_cloud_dialogflow_v2_context import GoogleCloudDialogflowV2Context
from openapi_server.models.google_cloud_dialogflow_v2_conversation import GoogleCloudDialogflowV2Conversation
from openapi_server.models.google_cloud_dialogflow_v2_conversation_dataset import GoogleCloudDialogflowV2ConversationDataset
from openapi_server.models.google_cloud_dialogflow_v2_conversation_model import GoogleCloudDialogflowV2ConversationModel
from openapi_server.models.google_cloud_dialogflow_v2_conversation_profile import GoogleCloudDialogflowV2ConversationProfile
from openapi_server.models.google_cloud_dialogflow_v2_create_conversation_model_evaluation_request import GoogleCloudDialogflowV2CreateConversationModelEvaluationRequest
from openapi_server.models.google_cloud_dialogflow_v2_detect_intent_request import GoogleCloudDialogflowV2DetectIntentRequest
from openapi_server.models.google_cloud_dialogflow_v2_detect_intent_response import GoogleCloudDialogflowV2DetectIntentResponse
from openapi_server.models.google_cloud_dialogflow_v2_document import GoogleCloudDialogflowV2Document
from openapi_server.models.google_cloud_dialogflow_v2_environment import GoogleCloudDialogflowV2Environment
from openapi_server.models.google_cloud_dialogflow_v2_environment_history import GoogleCloudDialogflowV2EnvironmentHistory
from openapi_server.models.google_cloud_dialogflow_v2_export_agent_request import GoogleCloudDialogflowV2ExportAgentRequest
from openapi_server.models.google_cloud_dialogflow_v2_export_document_request import GoogleCloudDialogflowV2ExportDocumentRequest
from openapi_server.models.google_cloud_dialogflow_v2_generate_stateless_summary_request import GoogleCloudDialogflowV2GenerateStatelessSummaryRequest
from openapi_server.models.google_cloud_dialogflow_v2_generate_stateless_summary_response import GoogleCloudDialogflowV2GenerateStatelessSummaryResponse
from openapi_server.models.google_cloud_dialogflow_v2_import_agent_request import GoogleCloudDialogflowV2ImportAgentRequest
from openapi_server.models.google_cloud_dialogflow_v2_import_conversation_data_request import GoogleCloudDialogflowV2ImportConversationDataRequest
from openapi_server.models.google_cloud_dialogflow_v2_import_documents_request import GoogleCloudDialogflowV2ImportDocumentsRequest
from openapi_server.models.google_cloud_dialogflow_v2_intent import GoogleCloudDialogflowV2Intent
from openapi_server.models.google_cloud_dialogflow_v2_knowledge_base import GoogleCloudDialogflowV2KnowledgeBase
from openapi_server.models.google_cloud_dialogflow_v2_list_answer_records_response import GoogleCloudDialogflowV2ListAnswerRecordsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_contexts_response import GoogleCloudDialogflowV2ListContextsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_conversation_datasets_response import GoogleCloudDialogflowV2ListConversationDatasetsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_conversation_model_evaluations_response import GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_conversation_models_response import GoogleCloudDialogflowV2ListConversationModelsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_conversation_profiles_response import GoogleCloudDialogflowV2ListConversationProfilesResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_conversations_response import GoogleCloudDialogflowV2ListConversationsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_documents_response import GoogleCloudDialogflowV2ListDocumentsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_environments_response import GoogleCloudDialogflowV2ListEnvironmentsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_intents_response import GoogleCloudDialogflowV2ListIntentsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_knowledge_bases_response import GoogleCloudDialogflowV2ListKnowledgeBasesResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_messages_response import GoogleCloudDialogflowV2ListMessagesResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_participants_response import GoogleCloudDialogflowV2ListParticipantsResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_session_entity_types_response import GoogleCloudDialogflowV2ListSessionEntityTypesResponse
from openapi_server.models.google_cloud_dialogflow_v2_list_versions_response import GoogleCloudDialogflowV2ListVersionsResponse
from openapi_server.models.google_cloud_dialogflow_v2_participant import GoogleCloudDialogflowV2Participant
from openapi_server.models.google_cloud_dialogflow_v2_reload_document_request import GoogleCloudDialogflowV2ReloadDocumentRequest
from openapi_server.models.google_cloud_dialogflow_v2_restore_agent_request import GoogleCloudDialogflowV2RestoreAgentRequest
from openapi_server.models.google_cloud_dialogflow_v2_search_agents_response import GoogleCloudDialogflowV2SearchAgentsResponse
from openapi_server.models.google_cloud_dialogflow_v2_search_knowledge_request import GoogleCloudDialogflowV2SearchKnowledgeRequest
from openapi_server.models.google_cloud_dialogflow_v2_search_knowledge_response import GoogleCloudDialogflowV2SearchKnowledgeResponse
from openapi_server.models.google_cloud_dialogflow_v2_session_entity_type import GoogleCloudDialogflowV2SessionEntityType
from openapi_server.models.google_cloud_dialogflow_v2_set_suggestion_feature_config_request import GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest
from openapi_server.models.google_cloud_dialogflow_v2_suggest_articles_request import GoogleCloudDialogflowV2SuggestArticlesRequest
from openapi_server.models.google_cloud_dialogflow_v2_suggest_articles_response import GoogleCloudDialogflowV2SuggestArticlesResponse
from openapi_server.models.google_cloud_dialogflow_v2_suggest_conversation_summary_request import GoogleCloudDialogflowV2SuggestConversationSummaryRequest
from openapi_server.models.google_cloud_dialogflow_v2_suggest_conversation_summary_response import GoogleCloudDialogflowV2SuggestConversationSummaryResponse
from openapi_server.models.google_cloud_dialogflow_v2_suggest_faq_answers_request import GoogleCloudDialogflowV2SuggestFaqAnswersRequest
from openapi_server.models.google_cloud_dialogflow_v2_suggest_faq_answers_response import GoogleCloudDialogflowV2SuggestFaqAnswersResponse
from openapi_server.models.google_cloud_dialogflow_v2_suggest_smart_replies_request import GoogleCloudDialogflowV2SuggestSmartRepliesRequest
from openapi_server.models.google_cloud_dialogflow_v2_suggest_smart_replies_response import GoogleCloudDialogflowV2SuggestSmartRepliesResponse
from openapi_server.models.google_cloud_dialogflow_v2_validation_result import GoogleCloudDialogflowV2ValidationResult
from openapi_server.models.google_cloud_dialogflow_v2_version import GoogleCloudDialogflowV2Version
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_entity_types_batch_delete(client):
    """Test case for dialogflow_projects_locations_agent_entity_types_batch_delete

    
    """
    body = {"entityTypeNames":["entityTypeNames","entityTypeNames"]}
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
        path='/v2/{parent}/entityTypes:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_entity_types_batch_update(client):
    """Test case for dialogflow_projects_locations_agent_entity_types_batch_update

    
    """
    body = {"entityTypeBatchInline":{"entityTypes":[{"autoExpansionMode":"AUTO_EXPANSION_MODE_UNSPECIFIED","enableFuzzyExtraction":True,"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"displayName":"displayName","kind":"KIND_UNSPECIFIED","name":"name"},{"autoExpansionMode":"AUTO_EXPANSION_MODE_UNSPECIFIED","enableFuzzyExtraction":True,"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"displayName":"displayName","kind":"KIND_UNSPECIFIED","name":"name"}]},"entityTypeBatchUri":"entityTypeBatchUri","languageCode":"languageCode","updateMask":"updateMask"}
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
        path='/v2/{parent}/entityTypes:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_entity_types_entities_batch_create(client):
    """Test case for dialogflow_projects_locations_agent_entity_types_entities_batch_create

    
    """
    body = {"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"languageCode":"languageCode"}
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
        path='/v2/{parent}/entities:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_entity_types_entities_batch_delete(client):
    """Test case for dialogflow_projects_locations_agent_entity_types_entities_batch_delete

    
    """
    body = {"languageCode":"languageCode","entityValues":["entityValues","entityValues"]}
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
        path='/v2/{parent}/entities:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_entity_types_entities_batch_update(client):
    """Test case for dialogflow_projects_locations_agent_entity_types_entities_batch_update

    
    """
    body = {"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"languageCode":"languageCode","updateMask":"updateMask"}
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
        path='/v2/{parent}/entities:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_environments_create(client):
    """Test case for dialogflow_projects_locations_agent_environments_create

    
    """
    body = {"name":"name","textToSpeechSettings":{"sampleRateHertz":0,"synthesizeSpeechConfigs":{"key":{"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name"},"volumeGainDb":1.4658129805029452,"speakingRate":6.027456183070403,"pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]}},"enableTextToSpeech":True,"outputAudioEncoding":"OUTPUT_AUDIO_ENCODING_UNSPECIFIED"},"agentVersion":"agentVersion","description":"description","updateTime":"updateTime","fulfillment":{"genericWebService":{"password":"password","requestHeaders":{"key":"requestHeaders"},"uri":"uri","isCloudFunction":True,"username":"username"},"features":[{"type":"TYPE_UNSPECIFIED"},{"type":"TYPE_UNSPECIFIED"}],"displayName":"displayName","name":"name","enabled":True},"state":"STATE_UNSPECIFIED"}
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
                    ('environmentId', 'environment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_environments_get_history(client):
    """Test case for dialogflow_projects_locations_agent_environments_get_history

    
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
        path='/v2/{parent}/history'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_environments_list(client):
    """Test case for dialogflow_projects_locations_agent_environments_list

    
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
        path='/v2/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_export(client):
    """Test case for dialogflow_projects_locations_agent_export

    
    """
    body = {"agentUri":"agentUri"}
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
        path='/v2/{parent}/agent:export'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_get_validation_result(client):
    """Test case for dialogflow_projects_locations_agent_get_validation_result

    
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
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/agent/validationResult'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_import(client):
    """Test case for dialogflow_projects_locations_agent_import

    
    """
    body = {"agentUri":"agentUri","agentContent":"agentContent"}
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
        path='/v2/{parent}/agent:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_intents_batch_delete(client):
    """Test case for dialogflow_projects_locations_agent_intents_batch_delete

    
    """
    body = {"intents":[{"resetContexts":True,"displayName":"displayName","liveAgentHandoff":True,"priority":1,"endInteraction":True,"followupIntentInfo":[{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"},{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"}],"outputContexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"parentFollowupIntentName":"parentFollowupIntentName","trainingPhrases":[{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"},{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"}],"defaultResponsePlatforms":["PLATFORM_UNSPECIFIED","PLATFORM_UNSPECIFIED"],"webhookState":"WEBHOOK_STATE_UNSPECIFIED","name":"name","action":"action","inputContextNames":["inputContextNames","inputContextNames"],"messages":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}}],"isFallback":True,"rootFollowupIntentName":"rootFollowupIntentName","parameters":[{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]},{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]}],"events":["events","events"],"mlDisabled":True},{"resetContexts":True,"displayName":"displayName","liveAgentHandoff":True,"priority":1,"endInteraction":True,"followupIntentInfo":[{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"},{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"}],"outputContexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"parentFollowupIntentName":"parentFollowupIntentName","trainingPhrases":[{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"},{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"}],"defaultResponsePlatforms":["PLATFORM_UNSPECIFIED","PLATFORM_UNSPECIFIED"],"webhookState":"WEBHOOK_STATE_UNSPECIFIED","name":"name","action":"action","inputContextNames":["inputContextNames","inputContextNames"],"messages":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}}],"isFallback":True,"rootFollowupIntentName":"rootFollowupIntentName","parameters":[{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]},{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]}],"events":["events","events"],"mlDisabled":True}]}
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
        path='/v2/{parent}/intents:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_intents_batch_update(client):
    """Test case for dialogflow_projects_locations_agent_intents_batch_update

    
    """
    body = {"intentBatchUri":"intentBatchUri","intentView":"INTENT_VIEW_UNSPECIFIED","intentBatchInline":{"intents":[{"resetContexts":True,"displayName":"displayName","liveAgentHandoff":True,"priority":1,"endInteraction":True,"followupIntentInfo":[{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"},{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"}],"outputContexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"parentFollowupIntentName":"parentFollowupIntentName","trainingPhrases":[{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"},{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"}],"defaultResponsePlatforms":["PLATFORM_UNSPECIFIED","PLATFORM_UNSPECIFIED"],"webhookState":"WEBHOOK_STATE_UNSPECIFIED","name":"name","action":"action","inputContextNames":["inputContextNames","inputContextNames"],"messages":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}}],"isFallback":True,"rootFollowupIntentName":"rootFollowupIntentName","parameters":[{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]},{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]}],"events":["events","events"],"mlDisabled":True},{"resetContexts":True,"displayName":"displayName","liveAgentHandoff":True,"priority":1,"endInteraction":True,"followupIntentInfo":[{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"},{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"}],"outputContexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"parentFollowupIntentName":"parentFollowupIntentName","trainingPhrases":[{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"},{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"}],"defaultResponsePlatforms":["PLATFORM_UNSPECIFIED","PLATFORM_UNSPECIFIED"],"webhookState":"WEBHOOK_STATE_UNSPECIFIED","name":"name","action":"action","inputContextNames":["inputContextNames","inputContextNames"],"messages":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}}],"isFallback":True,"rootFollowupIntentName":"rootFollowupIntentName","parameters":[{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]},{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]}],"events":["events","events"],"mlDisabled":True}]},"languageCode":"languageCode","updateMask":"updateMask"}
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
        path='/v2/{parent}/intents:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_intents_create(client):
    """Test case for dialogflow_projects_locations_agent_intents_create

    
    """
    body = {"resetContexts":True,"displayName":"displayName","liveAgentHandoff":True,"priority":1,"endInteraction":True,"followupIntentInfo":[{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"},{"followupIntentName":"followupIntentName","parentFollowupIntentName":"parentFollowupIntentName"}],"outputContexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"parentFollowupIntentName":"parentFollowupIntentName","trainingPhrases":[{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"},{"timesAddedCount":5,"name":"name","parts":[{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"},{"entityType":"entityType","userDefined":True,"alias":"alias","text":"text"}],"type":"TYPE_UNSPECIFIED"}],"defaultResponsePlatforms":["PLATFORM_UNSPECIFIED","PLATFORM_UNSPECIFIED"],"webhookState":"WEBHOOK_STATE_UNSPECIFIED","name":"name","action":"action","inputContextNames":["inputContextNames","inputContextNames"],"messages":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"quickReplies":{"quickReplies":["quickReplies","quickReplies"],"title":"title"},"carouselSelect":{"items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"browseCarouselCard":{"imageDisplayOptions":"IMAGE_DISPLAY_OPTIONS_UNSPECIFIED","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"footer":"footer","description":"description","openUriAction":{"urlTypeHint":"URL_TYPE_HINT_UNSPECIFIED","url":"url"},"title":"title"}]},"basicCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","formattedText":"formattedText","title":"title"},"platform":"PLATFORM_UNSPECIFIED","tableCard":{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"buttons":[{"openUriAction":{"uri":"uri"},"title":"title"},{"openUriAction":{"uri":"uri"},"title":"title"}],"subtitle":"subtitle","rows":[{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True},{"cells":[{"text":"text"},{"text":"text"}],"dividerAfter":True}],"title":"title","columnProperties":[{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"},{"horizontalAlignment":"HORIZONTAL_ALIGNMENT_UNSPECIFIED","header":"header"}]},"listSelect":{"subtitle":"subtitle","title":"title","items":[{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}},{"image":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"description":"description","title":"title","info":{"synonyms":["synonyms","synonyms"],"key":"key"}}]},"mediaContent":{"mediaType":"RESPONSE_MEDIA_TYPE_UNSPECIFIED","mediaObjects":[{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"},{"contentUrl":"contentUrl","largeImage":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"icon":{"imageUri":"imageUri","accessibilityText":"accessibilityText"},"name":"name","description":"description"}]},"payload":{"key":""},"linkOutSuggestion":{"destinationName":"destinationName","uri":"uri"},"suggestions":{"suggestions":[{"title":"title"},{"title":"title"}]},"text":{"text":["text","text"]},"simpleResponses":{"simpleResponses":[{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"},{"displayText":"displayText","textToSpeech":"textToSpeech","ssml":"ssml"}]},"card":{"imageUri":"imageUri","buttons":[{"postback":"postback","text":"text"},{"postback":"postback","text":"text"}],"subtitle":"subtitle","title":"title"}}],"isFallback":True,"rootFollowupIntentName":"rootFollowupIntentName","parameters":[{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]},{"defaultValue":"defaultValue","displayName":"displayName","name":"name","entityTypeDisplayName":"entityTypeDisplayName","isList":True,"mandatory":True,"value":"value","prompts":["prompts","prompts"]}],"events":["events","events"],"mlDisabled":True}
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
                    ('intentView', 'intent_view_example'),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/intents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_intents_list(client):
    """Test case for dialogflow_projects_locations_agent_intents_list

    
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
                    ('intentView', 'intent_view_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/intents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_restore(client):
    """Test case for dialogflow_projects_locations_agent_restore

    
    """
    body = {"agentUri":"agentUri","agentContent":"agentContent"}
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
        path='/v2/{parent}/agent:restore'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_search(client):
    """Test case for dialogflow_projects_locations_agent_search

    
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
        path='/v2/{parent}/agent:search'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_contexts_create(client):
    """Test case for dialogflow_projects_locations_agent_sessions_contexts_create

    
    """
    body = {"name":"name","lifespanCount":6,"parameters":{"key":""}}
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
        path='/v2/{parent}/contexts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_contexts_list(client):
    """Test case for dialogflow_projects_locations_agent_sessions_contexts_list

    
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
        path='/v2/{parent}/contexts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_delete_contexts(client):
    """Test case for dialogflow_projects_locations_agent_sessions_delete_contexts

    
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
        path='/v2/{parent}/contexts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_detect_intent(client):
    """Test case for dialogflow_projects_locations_agent_sessions_detect_intent

    
    """
    body = {"outputAudioConfig":{"sampleRateHertz":0,"synthesizeSpeechConfig":{"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name"},"volumeGainDb":1.4658129805029452,"speakingRate":6.027456183070403,"pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]},"audioEncoding":"OUTPUT_AUDIO_ENCODING_UNSPECIFIED"},"outputAudioConfigMask":"outputAudioConfigMask","queryInput":{"text":{"text":"text","languageCode":"languageCode"},"event":{"name":"name","languageCode":"languageCode","parameters":{"key":""}},"audioConfig":{"enableWordInfo":True,"sampleRateHertz":0,"disableNoSpeechRecognizedEvent":True,"optOutConformerModelMigration":True,"speechContexts":[{"boost":6.0274563,"phrases":["phrases","phrases"]},{"boost":6.0274563,"phrases":["phrases","phrases"]}],"audioEncoding":"AUDIO_ENCODING_UNSPECIFIED","enableAutomaticPunctuation":True,"model":"model","languageCode":"languageCode","singleUtterance":True,"modelVariant":"SPEECH_MODEL_VARIANT_UNSPECIFIED","phraseHints":["phraseHints","phraseHints"]}},"queryParams":{"resetContexts":True,"geoLocation":{"latitude":0.8008281904610115,"longitude":6.027456183070403},"payload":{"key":""},"sessionEntityTypes":[{"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"name":"name","entityOverrideMode":"ENTITY_OVERRIDE_MODE_UNSPECIFIED"},{"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"name":"name","entityOverrideMode":"ENTITY_OVERRIDE_MODE_UNSPECIFIED"}],"timeZone":"timeZone","webhookHeaders":{"key":"webhookHeaders"},"contexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"platform":"platform","sentimentAnalysisRequestConfig":{"analyzeQueryTextSentiment":True}},"inputAudio":"inputAudio"}
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
        path='/v2/{sessiondetect_inten}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_entity_types_create(client):
    """Test case for dialogflow_projects_locations_agent_sessions_entity_types_create

    
    """
    body = {"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"name":"name","entityOverrideMode":"ENTITY_OVERRIDE_MODE_UNSPECIFIED"}
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
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/entityTypes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_sessions_entity_types_list(client):
    """Test case for dialogflow_projects_locations_agent_sessions_entity_types_list

    
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
        path='/v2/{parent}/entityTypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_train(client):
    """Test case for dialogflow_projects_locations_agent_train

    
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
        path='/v2/{parent}/agent:train'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_versions_create(client):
    """Test case for dialogflow_projects_locations_agent_versions_create

    
    """
    body = {"createTime":"createTime","name":"name","description":"description","versionNumber":0,"status":"VERSION_STATUS_UNSPECIFIED"}
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
        path='/v2/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_agent_versions_list(client):
    """Test case for dialogflow_projects_locations_agent_versions_list

    
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
        path='/v2/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_answer_records_list(client):
    """Test case for dialogflow_projects_locations_answer_records_list

    
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
        path='/v2/{parent}/answerRecords'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_datasets_create(client):
    """Test case for dialogflow_projects_locations_conversation_datasets_create

    
    """
    body = {"inputConfig":{"gcsSource":{"uris":["uris","uris"]}},"createTime":"createTime","conversationCount":"conversationCount","displayName":"displayName","name":"name","conversationInfo":{"languageCode":"languageCode"},"description":"description"}
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
        path='/v2/{parent}/conversationDatasets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_datasets_import_conversation_data(client):
    """Test case for dialogflow_projects_locations_conversation_datasets_import_conversation_data

    
    """
    body = {"inputConfig":{"gcsSource":{"uris":["uris","uris"]}}}
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
        path='/v2/{nameimport_conversation_dat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_datasets_list(client):
    """Test case for dialogflow_projects_locations_conversation_datasets_list

    
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
        path='/v2/{parent}/conversationDatasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_create(client):
    """Test case for dialogflow_projects_locations_conversation_models_create

    
    """
    body = {"articleSuggestionModelMetadata":{"trainingModelType":"MODEL_TYPE_UNSPECIFIED"},"createTime":"createTime","displayName":"displayName","name":"name","smartReplyModelMetadata":{"trainingModelType":"MODEL_TYPE_UNSPECIFIED"},"datasets":[{"dataset":"dataset"},{"dataset":"dataset"}],"state":"STATE_UNSPECIFIED","languageCode":"languageCode"}
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
        path='/v2/{parent}/conversationModels'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_deploy(client):
    """Test case for dialogflow_projects_locations_conversation_models_deploy

    
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
        path='/v2/{namedeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_evaluations_create(client):
    """Test case for dialogflow_projects_locations_conversation_models_evaluations_create

    
    """
    body = {"conversationModelEvaluation":{"smartReplyMetrics":{"allowlistCoverage":1.4658129,"conversationCount":"conversationCount","topNMetrics":[{"recall":5.637377,"n":5},{"recall":5.637377,"n":5}]},"createTime":"createTime","displayName":"displayName","name":"name","evaluationConfig":{"smartReplyConfig":{"allowlistDocument":"allowlistDocument","maxResultCount":6},"datasets":[{"dataset":"dataset"},{"dataset":"dataset"}],"smartComposeConfig":{"allowlistDocument":"allowlistDocument","maxResultCount":0}},"rawHumanEvalTemplateCsv":"rawHumanEvalTemplateCsv"}}
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
        path='/v2/{parent}/evaluations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_evaluations_list(client):
    """Test case for dialogflow_projects_locations_conversation_models_evaluations_list

    
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
        path='/v2/{parent}/evaluations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_list(client):
    """Test case for dialogflow_projects_locations_conversation_models_list

    
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
        path='/v2/{parent}/conversationModels'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_models_undeploy(client):
    """Test case for dialogflow_projects_locations_conversation_models_undeploy

    
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
        path='/v2/{nameundeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_profiles_clear_suggestion_feature_config(client):
    """Test case for dialogflow_projects_locations_conversation_profiles_clear_suggestion_feature_config

    
    """
    body = {"participantRole":"ROLE_UNSPECIFIED","suggestionFeatureType":"TYPE_UNSPECIFIED"}
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
        path='/v2/{conversation_profileclear_suggestion_feature_confi}'.format(conversation_profile='conversation_profile_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_profiles_create(client):
    """Test case for dialogflow_projects_locations_conversation_profiles_create

    
    """
    body = {"displayName":"displayName","securitySettings":"securitySettings","sttConfig":{"model":"model","useTimeoutBasedEndpointing":True,"speechModelVariant":"SPEECH_MODEL_VARIANT_UNSPECIFIED"},"timeZone":"timeZone","automatedAgentConfig":{"agent":"agent","sessionTtl":"sessionTtl"},"newMessageEventNotificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"},"updateTime":"updateTime","humanAgentHandoffConfig":{"salesforceLiveAgentConfig":{"organizationId":"organizationId","deploymentId":"deploymentId","buttonId":"buttonId","endpointDomain":"endpointDomain"},"livePersonConfig":{"accountNumber":"accountNumber"}},"languageCode":"languageCode","ttsConfig":{"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name"},"volumeGainDb":1.4658129805029452,"speakingRate":6.027456183070403,"pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]},"humanAgentAssistantConfig":{"messageAnalysisConfig":{"enableSentimentAnalysis":True,"enableEntityExtraction":True},"endUserSuggestionConfig":{"groupSuggestionResponses":True,"featureConfigs":[{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True},{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True}]},"notificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"},"humanAgentSuggestionConfig":{"groupSuggestionResponses":True,"featureConfigs":[{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True},{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True}]}},"createTime":"createTime","loggingConfig":{"enableStackdriverLogging":True},"name":"name","notificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"}}
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
        path='/v2/{parent}/conversationProfiles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_profiles_list(client):
    """Test case for dialogflow_projects_locations_conversation_profiles_list

    
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
        path='/v2/{parent}/conversationProfiles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversation_profiles_set_suggestion_feature_config(client):
    """Test case for dialogflow_projects_locations_conversation_profiles_set_suggestion_feature_config

    
    """
    body = {"participantRole":"ROLE_UNSPECIFIED","suggestionFeatureConfig":{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True}}
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
        path='/v2/{conversation_profileset_suggestion_feature_confi}'.format(conversation_profile='conversation_profile_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_complete(client):
    """Test case for dialogflow_projects_locations_conversations_complete

    
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
        path='/v2/{namecomplet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_create(client):
    """Test case for dialogflow_projects_locations_conversations_create

    
    """
    body = {"lifecycleState":"LIFECYCLE_STATE_UNSPECIFIED","phoneNumber":{"phoneNumber":"phoneNumber"},"conversationProfile":"conversationProfile","conversationStage":"CONVERSATION_STAGE_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime"}
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
        path='/v2/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_list(client):
    """Test case for dialogflow_projects_locations_conversations_list

    
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
        path='/v2/{parent}/conversations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_messages_list(client):
    """Test case for dialogflow_projects_locations_conversations_messages_list

    
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
        path='/v2/{parent}/messages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_analyze_content(client):
    """Test case for dialogflow_projects_locations_conversations_participants_analyze_content

    
    """
    body = {"suggestionInput":{"answerRecord":"answerRecord"},"replyAudioConfig":{"sampleRateHertz":0,"synthesizeSpeechConfig":{"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name"},"volumeGainDb":1.4658129805029452,"speakingRate":6.027456183070403,"pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]},"audioEncoding":"OUTPUT_AUDIO_ENCODING_UNSPECIFIED"},"textInput":{"text":"text","languageCode":"languageCode"},"eventInput":{"name":"name","languageCode":"languageCode","parameters":{"key":""}},"queryParams":{"resetContexts":True,"geoLocation":{"latitude":0.8008281904610115,"longitude":6.027456183070403},"payload":{"key":""},"sessionEntityTypes":[{"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"name":"name","entityOverrideMode":"ENTITY_OVERRIDE_MODE_UNSPECIFIED"},{"entities":[{"synonyms":["synonyms","synonyms"],"value":"value"},{"synonyms":["synonyms","synonyms"],"value":"value"}],"name":"name","entityOverrideMode":"ENTITY_OVERRIDE_MODE_UNSPECIFIED"}],"timeZone":"timeZone","webhookHeaders":{"key":"webhookHeaders"},"contexts":[{"name":"name","lifespanCount":6,"parameters":{"key":""}},{"name":"name","lifespanCount":6,"parameters":{"key":""}}],"platform":"platform","sentimentAnalysisRequestConfig":{"analyzeQueryTextSentiment":True}},"requestId":"requestId","assistQueryParams":{"documentsMetadataFilters":{"key":"documentsMetadataFilters"}},"cxParameters":{"key":""}}
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
        path='/v2/{participantanalyze_conten}'.format(participant='participant_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_create(client):
    """Test case for dialogflow_projects_locations_conversations_participants_create

    
    """
    body = {"role":"ROLE_UNSPECIFIED","documentsMetadataFilters":{"key":"documentsMetadataFilters"},"name":"name","obfuscatedExternalUserId":"obfuscatedExternalUserId","sipRecordingMediaLabel":"sipRecordingMediaLabel"}
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
        path='/v2/{parent}/participants'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_list(client):
    """Test case for dialogflow_projects_locations_conversations_participants_list

    
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
        path='/v2/{parent}/participants'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_suggestions_suggest_articles(client):
    """Test case for dialogflow_projects_locations_conversations_participants_suggestions_suggest_articles

    
    """
    body = {"assistQueryParams":{"documentsMetadataFilters":{"key":"documentsMetadataFilters"}},"latestMessage":"latestMessage","contextSize":0}
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
        path='/v2/{parent}/suggestions:suggestArticles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_suggestions_suggest_faq_answers(client):
    """Test case for dialogflow_projects_locations_conversations_participants_suggestions_suggest_faq_answers

    
    """
    body = {"assistQueryParams":{"documentsMetadataFilters":{"key":"documentsMetadataFilters"}},"latestMessage":"latestMessage","contextSize":0}
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
        path='/v2/{parent}/suggestions:suggestFaqAnswers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_participants_suggestions_suggest_smart_replies(client):
    """Test case for dialogflow_projects_locations_conversations_participants_suggestions_suggest_smart_replies

    
    """
    body = {"currentTextInput":{"text":"text","languageCode":"languageCode"},"latestMessage":"latestMessage","contextSize":0}
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
        path='/v2/{parent}/suggestions:suggestSmartReplies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_suggestions_search_knowledge(client):
    """Test case for dialogflow_projects_locations_conversations_suggestions_search_knowledge

    
    """
    body = {"parent":"parent","conversationProfile":"conversationProfile","query":{"text":"text","languageCode":"languageCode"},"latestMessage":"latestMessage","sessionId":"sessionId","conversation":"conversation"}
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
        path='/v2/{conversation}/suggestions:searchKnowledge'.format(conversation='conversation_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_conversations_suggestions_suggest_conversation_summary(client):
    """Test case for dialogflow_projects_locations_conversations_suggestions_suggest_conversation_summary

    
    """
    body = {"assistQueryParams":{"documentsMetadataFilters":{"key":"documentsMetadataFilters"}},"latestMessage":"latestMessage","contextSize":0}
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
        path='/v2/{conversation}/suggestions:suggestConversationSummary'.format(conversation='conversation_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_delete_agent(client):
    """Test case for dialogflow_projects_locations_delete_agent

    
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
        path='/v2/{parent}/agent'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_get_agent(client):
    """Test case for dialogflow_projects_locations_get_agent

    
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
        path='/v2/{parent}/agent'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_create(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_create

    
    """
    body = {"displayName":"displayName","name":"name","languageCode":"languageCode"}
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
        path='/v2/{parent}/knowledgeBases'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_create(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_create

    
    """
    body = {"enableAutoReload":True,"knowledgeTypes":["KNOWLEDGE_TYPE_UNSPECIFIED","KNOWLEDGE_TYPE_UNSPECIFIED"],"metadata":{"key":"metadata"},"displayName":"displayName","contentUri":"contentUri","name":"name","mimeType":"mimeType","state":"STATE_UNSPECIFIED","latestReloadStatus":{"time":"time","status":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},"rawContent":"rawContent"}
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
        path='/v2/{parent}/documents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_delete(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_delete

    
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_export(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_export

    
    """
    body = {"gcsDestination":{"uri":"uri"},"smartMessagingPartialUpdate":True,"exportFullContent":True}
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
        path='/v2/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_import(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_import

    
    """
    body = {"gcsSource":{"uris":["uris","uris"]},"importGcsCustomMetadata":True,"documentTemplate":{"knowledgeTypes":["KNOWLEDGE_TYPE_UNSPECIFIED","KNOWLEDGE_TYPE_UNSPECIFIED"],"metadata":{"key":"metadata"},"mimeType":"mimeType"}}
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
        path='/v2/{parent}/documents:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_list(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_list

    
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
        path='/v2/{parent}/documents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_patch(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_patch

    
    """
    body = {"enableAutoReload":True,"knowledgeTypes":["KNOWLEDGE_TYPE_UNSPECIFIED","KNOWLEDGE_TYPE_UNSPECIFIED"],"metadata":{"key":"metadata"},"displayName":"displayName","contentUri":"contentUri","name":"name","mimeType":"mimeType","state":"STATE_UNSPECIFIED","latestReloadStatus":{"time":"time","status":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},"rawContent":"rawContent"}
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
                    ('updateMask', 'update_mask_example'),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_documents_reload(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_documents_reload

    
    """
    body = {"smartMessagingPartialUpdate":True,"contentUri":"contentUri","importGcsCustomMetadata":True}
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
        path='/v2/{namereloa}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_knowledge_bases_list(client):
    """Test case for dialogflow_projects_locations_knowledge_bases_list

    
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
        path='/v2/{parent}/knowledgeBases'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_list(client):
    """Test case for dialogflow_projects_locations_list

    
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
        path='/v2/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_locations_set_agent(client):
    """Test case for dialogflow_projects_locations_set_agent

    
    """
    body = {"avatarUri":"avatarUri","parent":"parent","apiVersion":"API_VERSION_UNSPECIFIED","supportedLanguageCodes":["supportedLanguageCodes","supportedLanguageCodes"],"tier":"TIER_UNSPECIFIED","displayName":"displayName","description":"description","timeZone":"timeZone","defaultLanguageCode":"defaultLanguageCode","classificationThreshold":0.8008282,"enableLogging":True,"matchMode":"MATCH_MODE_UNSPECIFIED"}
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
        method='POST',
        path='/v2/{parent}/agent'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_operations_cancel(client):
    """Test case for dialogflow_projects_operations_cancel

    
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
        path='/v2/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_operations_get(client):
    """Test case for dialogflow_projects_operations_get

    
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
                    ('intentView', 'intent_view_example'),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_operations_list(client):
    """Test case for dialogflow_projects_operations_list

    
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
        path='/v2/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_suggestions_generate_stateless_summary(client):
    """Test case for dialogflow_projects_suggestions_generate_stateless_summary

    
    """
    body = {"conversationProfile":{"displayName":"displayName","securitySettings":"securitySettings","sttConfig":{"model":"model","useTimeoutBasedEndpointing":True,"speechModelVariant":"SPEECH_MODEL_VARIANT_UNSPECIFIED"},"timeZone":"timeZone","automatedAgentConfig":{"agent":"agent","sessionTtl":"sessionTtl"},"newMessageEventNotificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"},"updateTime":"updateTime","humanAgentHandoffConfig":{"salesforceLiveAgentConfig":{"organizationId":"organizationId","deploymentId":"deploymentId","buttonId":"buttonId","endpointDomain":"endpointDomain"},"livePersonConfig":{"accountNumber":"accountNumber"}},"languageCode":"languageCode","ttsConfig":{"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name"},"volumeGainDb":1.4658129805029452,"speakingRate":6.027456183070403,"pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]},"humanAgentAssistantConfig":{"messageAnalysisConfig":{"enableSentimentAnalysis":True,"enableEntityExtraction":True},"endUserSuggestionConfig":{"groupSuggestionResponses":True,"featureConfigs":[{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True},{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True}]},"notificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"},"humanAgentSuggestionConfig":{"groupSuggestionResponses":True,"featureConfigs":[{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True},{"suggestionTriggerSettings":{"onlyEndUser":True,"noSmalltalk":True},"conversationProcessConfig":{"recentSentencesCount":0},"queryConfig":{"knowledgeBaseQuerySource":{"knowledgeBases":["knowledgeBases","knowledgeBases"]},"contextFilterSettings":{"dropHandoffMessages":True,"dropVirtualAgentMessages":True,"dropIvrMessages":True},"dialogflowQuerySource":{"agent":"agent","humanAgentSideConfig":{"agent":"agent"}},"documentQuerySource":{"documents":["documents","documents"]},"confidenceThreshold":6.0274563,"maxResults":1,"sections":{"sectionTypes":["SECTION_TYPE_UNSPECIFIED","SECTION_TYPE_UNSPECIFIED"]}},"suggestionFeature":{"type":"TYPE_UNSPECIFIED"},"conversationModelConfig":{"model":"model","baselineModelVersion":"baselineModelVersion"},"enableEventBasedSuggestion":True,"disableAgentQueryLogging":True,"enableConversationAugmentedQuery":True}]}},"createTime":"createTime","loggingConfig":{"enableStackdriverLogging":True},"name":"name","notificationConfig":{"messageFormat":"MESSAGE_FORMAT_UNSPECIFIED","topic":"topic"}},"statelessConversation":{"messages":[{"sentimentAnalysis":{"queryTextSentiment":{"score":7.0614014,"magnitude":2.302136}},"createTime":"createTime","name":"name","messageAnnotation":{"containEntities":True,"parts":[{"entityType":"entityType","formattedValue":"","text":"text"},{"entityType":"entityType","formattedValue":"","text":"text"}]},"languageCode":"languageCode","participantRole":"ROLE_UNSPECIFIED","content":"content","participant":"participant","sendTime":"sendTime"},{"sentimentAnalysis":{"queryTextSentiment":{"score":7.0614014,"magnitude":2.302136}},"createTime":"createTime","name":"name","messageAnnotation":{"containEntities":True,"parts":[{"entityType":"entityType","formattedValue":"","text":"text"},{"entityType":"entityType","formattedValue":"","text":"text"}]},"languageCode":"languageCode","participantRole":"ROLE_UNSPECIFIED","content":"content","participant":"participant","sendTime":"sendTime"}]},"latestMessage":"latestMessage","maxContextSize":0}
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
        path='/v2/{parent}/suggestions:generateStatelessSummary'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dialogflow_projects_suggestions_search_knowledge(client):
    """Test case for dialogflow_projects_suggestions_search_knowledge

    
    """
    body = {"parent":"parent","conversationProfile":"conversationProfile","query":{"text":"text","languageCode":"languageCode"},"latestMessage":"latestMessage","sessionId":"sessionId","conversation":"conversation"}
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
        path='/v2/{parent}/suggestions:searchKnowledge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

