# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_create_custom_vocabulary_item_request import BatchCreateCustomVocabularyItemRequest
from openapi_server.models.batch_create_custom_vocabulary_item_response import BatchCreateCustomVocabularyItemResponse
from openapi_server.models.batch_delete_custom_vocabulary_item_request import BatchDeleteCustomVocabularyItemRequest
from openapi_server.models.batch_delete_custom_vocabulary_item_response import BatchDeleteCustomVocabularyItemResponse
from openapi_server.models.batch_update_custom_vocabulary_item_request import BatchUpdateCustomVocabularyItemRequest
from openapi_server.models.batch_update_custom_vocabulary_item_response import BatchUpdateCustomVocabularyItemResponse
from openapi_server.models.build_bot_locale_response import BuildBotLocaleResponse
from openapi_server.models.create_bot_alias_request import CreateBotAliasRequest
from openapi_server.models.create_bot_alias_response import CreateBotAliasResponse
from openapi_server.models.create_bot_locale_request import CreateBotLocaleRequest
from openapi_server.models.create_bot_locale_response import CreateBotLocaleResponse
from openapi_server.models.create_bot_request import CreateBotRequest
from openapi_server.models.create_bot_response import CreateBotResponse
from openapi_server.models.create_bot_version_request import CreateBotVersionRequest
from openapi_server.models.create_bot_version_response import CreateBotVersionResponse
from openapi_server.models.create_export_request import CreateExportRequest
from openapi_server.models.create_export_response import CreateExportResponse
from openapi_server.models.create_intent_request import CreateIntentRequest
from openapi_server.models.create_intent_response import CreateIntentResponse
from openapi_server.models.create_resource_policy_response import CreateResourcePolicyResponse
from openapi_server.models.create_resource_policy_statement_request import CreateResourcePolicyStatementRequest
from openapi_server.models.create_resource_policy_statement_response import CreateResourcePolicyStatementResponse
from openapi_server.models.create_slot_request import CreateSlotRequest
from openapi_server.models.create_slot_response import CreateSlotResponse
from openapi_server.models.create_slot_type_request import CreateSlotTypeRequest
from openapi_server.models.create_slot_type_response import CreateSlotTypeResponse
from openapi_server.models.create_test_set_discrepancy_report_request import CreateTestSetDiscrepancyReportRequest
from openapi_server.models.create_test_set_discrepancy_report_response import CreateTestSetDiscrepancyReportResponse
from openapi_server.models.create_upload_url_response import CreateUploadUrlResponse
from openapi_server.models.delete_bot_alias_response import DeleteBotAliasResponse
from openapi_server.models.delete_bot_locale_response import DeleteBotLocaleResponse
from openapi_server.models.delete_bot_response import DeleteBotResponse
from openapi_server.models.delete_bot_version_response import DeleteBotVersionResponse
from openapi_server.models.delete_custom_vocabulary_response import DeleteCustomVocabularyResponse
from openapi_server.models.delete_export_response import DeleteExportResponse
from openapi_server.models.delete_import_response import DeleteImportResponse
from openapi_server.models.delete_resource_policy_response import DeleteResourcePolicyResponse
from openapi_server.models.delete_resource_policy_statement_response import DeleteResourcePolicyStatementResponse
from openapi_server.models.describe_bot_alias_response import DescribeBotAliasResponse
from openapi_server.models.describe_bot_locale_response import DescribeBotLocaleResponse
from openapi_server.models.describe_bot_recommendation_response import DescribeBotRecommendationResponse
from openapi_server.models.describe_bot_response import DescribeBotResponse
from openapi_server.models.describe_bot_version_response import DescribeBotVersionResponse
from openapi_server.models.describe_custom_vocabulary_metadata_response import DescribeCustomVocabularyMetadataResponse
from openapi_server.models.describe_export_response import DescribeExportResponse
from openapi_server.models.describe_import_response import DescribeImportResponse
from openapi_server.models.describe_intent_response import DescribeIntentResponse
from openapi_server.models.describe_resource_policy_response import DescribeResourcePolicyResponse
from openapi_server.models.describe_slot_response import DescribeSlotResponse
from openapi_server.models.describe_slot_type_response import DescribeSlotTypeResponse
from openapi_server.models.describe_test_execution_response import DescribeTestExecutionResponse
from openapi_server.models.describe_test_set_discrepancy_report_response import DescribeTestSetDiscrepancyReportResponse
from openapi_server.models.describe_test_set_generation_response import DescribeTestSetGenerationResponse
from openapi_server.models.describe_test_set_response import DescribeTestSetResponse
from openapi_server.models.get_test_execution_artifacts_url_response import GetTestExecutionArtifactsUrlResponse
from openapi_server.models.list_aggregated_utterances_request import ListAggregatedUtterancesRequest
from openapi_server.models.list_aggregated_utterances_response import ListAggregatedUtterancesResponse
from openapi_server.models.list_bot_aliases_request import ListBotAliasesRequest
from openapi_server.models.list_bot_aliases_response import ListBotAliasesResponse
from openapi_server.models.list_bot_locales_request import ListBotLocalesRequest
from openapi_server.models.list_bot_locales_response import ListBotLocalesResponse
from openapi_server.models.list_bot_recommendations_request import ListBotRecommendationsRequest
from openapi_server.models.list_bot_recommendations_response import ListBotRecommendationsResponse
from openapi_server.models.list_bot_versions_request import ListBotVersionsRequest
from openapi_server.models.list_bot_versions_response import ListBotVersionsResponse
from openapi_server.models.list_bots_request import ListBotsRequest
from openapi_server.models.list_bots_response import ListBotsResponse
from openapi_server.models.list_built_in_intents_request import ListBuiltInIntentsRequest
from openapi_server.models.list_built_in_intents_response import ListBuiltInIntentsResponse
from openapi_server.models.list_built_in_slot_types_request import ListBuiltInSlotTypesRequest
from openapi_server.models.list_built_in_slot_types_response import ListBuiltInSlotTypesResponse
from openapi_server.models.list_custom_vocabulary_items_request import ListCustomVocabularyItemsRequest
from openapi_server.models.list_custom_vocabulary_items_response import ListCustomVocabularyItemsResponse
from openapi_server.models.list_exports_request import ListExportsRequest
from openapi_server.models.list_exports_response import ListExportsResponse
from openapi_server.models.list_imports_request import ListImportsRequest
from openapi_server.models.list_imports_response import ListImportsResponse
from openapi_server.models.list_intent_metrics_request import ListIntentMetricsRequest
from openapi_server.models.list_intent_metrics_response import ListIntentMetricsResponse
from openapi_server.models.list_intent_paths_request import ListIntentPathsRequest
from openapi_server.models.list_intent_paths_response import ListIntentPathsResponse
from openapi_server.models.list_intent_stage_metrics_request import ListIntentStageMetricsRequest
from openapi_server.models.list_intent_stage_metrics_response import ListIntentStageMetricsResponse
from openapi_server.models.list_intents_request import ListIntentsRequest
from openapi_server.models.list_intents_response import ListIntentsResponse
from openapi_server.models.list_recommended_intents_request import ListRecommendedIntentsRequest
from openapi_server.models.list_recommended_intents_response import ListRecommendedIntentsResponse
from openapi_server.models.list_session_analytics_data_request import ListSessionAnalyticsDataRequest
from openapi_server.models.list_session_analytics_data_response import ListSessionAnalyticsDataResponse
from openapi_server.models.list_session_metrics_request import ListSessionMetricsRequest
from openapi_server.models.list_session_metrics_response import ListSessionMetricsResponse
from openapi_server.models.list_slot_types_request import ListSlotTypesRequest
from openapi_server.models.list_slot_types_response import ListSlotTypesResponse
from openapi_server.models.list_slots_request import ListSlotsRequest
from openapi_server.models.list_slots_response import ListSlotsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_test_execution_result_items_request import ListTestExecutionResultItemsRequest
from openapi_server.models.list_test_execution_result_items_response import ListTestExecutionResultItemsResponse
from openapi_server.models.list_test_executions_request import ListTestExecutionsRequest
from openapi_server.models.list_test_executions_response import ListTestExecutionsResponse
from openapi_server.models.list_test_set_records_request import ListTestSetRecordsRequest
from openapi_server.models.list_test_set_records_response import ListTestSetRecordsResponse
from openapi_server.models.list_test_sets_request import ListTestSetsRequest
from openapi_server.models.list_test_sets_response import ListTestSetsResponse
from openapi_server.models.list_utterance_analytics_data_request import ListUtteranceAnalyticsDataRequest
from openapi_server.models.list_utterance_analytics_data_response import ListUtteranceAnalyticsDataResponse
from openapi_server.models.list_utterance_metrics_request import ListUtteranceMetricsRequest
from openapi_server.models.list_utterance_metrics_response import ListUtteranceMetricsResponse
from openapi_server.models.search_associated_transcripts_request import SearchAssociatedTranscriptsRequest
from openapi_server.models.search_associated_transcripts_response import SearchAssociatedTranscriptsResponse
from openapi_server.models.start_bot_recommendation_request import StartBotRecommendationRequest
from openapi_server.models.start_bot_recommendation_response import StartBotRecommendationResponse
from openapi_server.models.start_import_request import StartImportRequest
from openapi_server.models.start_import_response import StartImportResponse
from openapi_server.models.start_test_execution_request import StartTestExecutionRequest
from openapi_server.models.start_test_execution_response import StartTestExecutionResponse
from openapi_server.models.start_test_set_generation_request import StartTestSetGenerationRequest
from openapi_server.models.start_test_set_generation_response import StartTestSetGenerationResponse
from openapi_server.models.stop_bot_recommendation_response import StopBotRecommendationResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_bot_alias_request import UpdateBotAliasRequest
from openapi_server.models.update_bot_alias_response import UpdateBotAliasResponse
from openapi_server.models.update_bot_locale_request import UpdateBotLocaleRequest
from openapi_server.models.update_bot_locale_response import UpdateBotLocaleResponse
from openapi_server.models.update_bot_recommendation_request import UpdateBotRecommendationRequest
from openapi_server.models.update_bot_recommendation_response import UpdateBotRecommendationResponse
from openapi_server.models.update_bot_request import UpdateBotRequest
from openapi_server.models.update_bot_response import UpdateBotResponse
from openapi_server.models.update_export_request import UpdateExportRequest
from openapi_server.models.update_export_response import UpdateExportResponse
from openapi_server.models.update_intent_request import UpdateIntentRequest
from openapi_server.models.update_intent_response import UpdateIntentResponse
from openapi_server.models.update_resource_policy_request import UpdateResourcePolicyRequest
from openapi_server.models.update_resource_policy_response import UpdateResourcePolicyResponse
from openapi_server.models.update_slot_request import UpdateSlotRequest
from openapi_server.models.update_slot_response import UpdateSlotResponse
from openapi_server.models.update_slot_type_request import UpdateSlotTypeRequest
from openapi_server.models.update_slot_type_response import UpdateSlotTypeResponse
from openapi_server.models.update_test_set_request import UpdateTestSetRequest
from openapi_server.models.update_test_set_response import UpdateTestSetResponse


pytestmark = pytest.mark.asyncio

async def test_batch_create_custom_vocabulary_item(client):
    """Test case for batch_create_custom_vocabulary_item

    
    """
    body = {"customVocabularyItemList":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary/DEFAULT/batchcreate'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_delete_custom_vocabulary_item(client):
    """Test case for batch_delete_custom_vocabulary_item

    
    """
    body = {"customVocabularyItemList":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary/DEFAULT/batchdelete'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_update_custom_vocabulary_item(client):
    """Test case for batch_update_custom_vocabulary_item

    
    """
    body = {"customVocabularyItemList":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary/DEFAULT/batchupdate'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_bot_locale(client):
    """Test case for build_bot_locale

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_bot(client):
    """Test case for create_bot

    
    """
    body = {"testBotAliasTags":"","botName":"","roleArn":"","botTags":"","botType":"","description":"","dataPrivacy":{"childDirected":""},"idleSessionTTLInSeconds":"","botMembers":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_bot_alias(client):
    """Test case for create_bot_alias

    
    """
    body = {"botAliasLocaleSettings":"","sentimentAnalysisSettings":{"detectSentiment":""},"description":"","botAliasName":"","botVersion":"","conversationLogSettings":{"textLogSettings":"","audioLogSettings":""},"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botaliases'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_bot_locale(client):
    """Test case for create_bot_locale

    
    """
    body = {"nluIntentConfidenceThreshold":"","description":"","voiceSettings":{"voiceId":"","engine":""},"localeId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales'.format(bot_id='bot_id_example', bot_version='bot_version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_bot_version(client):
    """Test case for create_bot_version

    
    """
    body = {"botVersionLocaleSpecification":"","description":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_export(client):
    """Test case for create_export

    
    """
    body = {"filePassword":"","resourceSpecification":{"testSetExportSpecification":{"testSetId":""},"customVocabularyExportSpecification":{"botId":"","botVersion":"","localeId":""},"botExportSpecification":{"botId":"","botVersion":""},"botLocaleExportSpecification":{"botId":"","botVersion":"","localeId":""}},"fileFormat":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/exports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_intent(client):
    """Test case for create_intent

    
    """
    body = {"sampleUtterances":"","parentIntentSignature":"","inputContexts":"","outputContexts":"","intentConfirmationSetting":{"declinationResponse":{"messageGroups":"","allowInterrupt":""},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"active":"","confirmationNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""},"declinationNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"promptSpecification":{"messageGroups":"","maxRetries":"","allowInterrupt":"","promptAttemptsSpecification":"","messageSelectionStrategy":""},"confirmationConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"confirmationResponse":{"messageGroups":"","allowInterrupt":""},"elicitationCodeHook":{"enableCodeHookInvocation":"","invocationLabel":""},"declinationConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""}},"intentName":"","description":"","kendraConfiguration":{"kendraIndex":"","queryFilterStringEnabled":"","queryFilterString":""},"fulfillmentCodeHook":{"active":"","postFulfillmentStatusSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"fulfillmentUpdatesSpecification":{"active":"","startResponse":{"messageGroups":"","allowInterrupt":"","delayInSeconds":""},"updateResponse":{"messageGroups":"","allowInterrupt":"","frequencyInSeconds":""},"timeoutInSeconds":""},"enabled":""},"intentClosingSetting":{"conditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"closingResponse":{"messageGroups":"","allowInterrupt":""},"active":"","nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"dialogCodeHook":{"enabled":""},"initialResponseSetting":{"conditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"initialResponse":{"messageGroups":"","allowInterrupt":""},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_resource_policy(client):
    """Test case for create_resource_policy

    
    """
    body = {"policy":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/policy/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_resource_policy_statement(client):
    """Test case for create_resource_policy_statement

    
    """
    body = {"principal":"","condition":"","effect":"","statementId":"","action":""}
    params = [('expectedRevisionId', 'expected_revision_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/policy/{resource_arn}/statements'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_slot(client):
    """Test case for create_slot

    
    """
    body = {"slotName":"","subSlotSetting":{"expression":"","slotSpecifications":""},"slotTypeId":"","description":"","valueElicitationSetting":{"sampleUtterances":"","slotConstraint":"","waitAndContinueSpecification":{"continueResponse":{"messageGroups":"","allowInterrupt":""},"waitingResponse":{"messageGroups":"","allowInterrupt":""},"active":"","stillWaitingResponse":{"messageGroups":"","allowInterrupt":"","frequencyInSeconds":"","timeoutInSeconds":""}},"defaultValueSpecification":{"defaultValueList":""},"promptSpecification":{"messageGroups":"","maxRetries":"","allowInterrupt":"","promptAttemptsSpecification":"","messageSelectionStrategy":""},"slotCaptureSetting":{"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"captureResponse":{"messageGroups":"","allowInterrupt":""},"elicitationCodeHook":{"enableCodeHookInvocation":"","invocationLabel":""},"captureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureResponse":{"messageGroups":"","allowInterrupt":""},"captureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""}}},"obfuscationSetting":{"obfuscationSettingType":""},"multipleValuesSetting":{"allowMultipleValues":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}/slots'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', intent_id='intent_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_slot_type(client):
    """Test case for create_slot_type

    
    """
    body = {"externalSourceSetting":{"grammarSlotTypeSetting":{"source":{"s3ObjectKey":"","kmsKeyArn":"","s3BucketName":""}}},"parentSlotTypeSignature":"","slotTypeName":"","description":"","valueSelectionSetting":{"resolutionStrategy":"","regexFilter":{"pattern":""},"advancedRecognitionSetting":{"audioRecognitionStrategy":""}},"compositeSlotTypeSetting":{"subSlots":""},"slotTypeValues":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/slottypes'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_test_set_discrepancy_report(client):
    """Test case for create_test_set_discrepancy_report

    
    """
    body = {"target":{"botAliasTarget":{"botAliasId":"","botId":"","localeId":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testsets/{test_set_id}/testsetdiscrepancy'.format(test_set_id='test_set_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_upload_url(client):
    """Test case for create_upload_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createuploadurl/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot(client):
    """Test case for delete_bot

    
    """
    params = [('skipResourceInUseCheck', True)]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}'.format(bot_id='bot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot_alias(client):
    """Test case for delete_bot_alias

    
    """
    params = [('skipResourceInUseCheck', True)]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botaliases/{bot_alias_id}'.format(bot_alias_id='bot_alias_id_example', bot_id='bot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot_locale(client):
    """Test case for delete_bot_locale

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot_version(client):
    """Test case for delete_bot_version

    
    """
    params = [('skipResourceInUseCheck', True)]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}'.format(bot_id='bot_id_example', bot_version='bot_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_vocabulary(client):
    """Test case for delete_custom_vocabulary

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_export(client):
    """Test case for delete_export

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/exports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_import(client):
    """Test case for delete_import

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/imports/{import_id}'.format(import_id='import_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_intent(client):
    """Test case for delete_intent

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}'.format(intent_id='intent_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_resource_policy(client):
    """Test case for delete_resource_policy

    
    """
    params = [('expectedRevisionId', 'expected_revision_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/policy/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_resource_policy_statement(client):
    """Test case for delete_resource_policy_statement

    
    """
    params = [('expectedRevisionId', 'expected_revision_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/policy/{resource_arn}/statements/{statement_id}'.format(resource_arn='resource_arn_example', statement_id='statement_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_slot(client):
    """Test case for delete_slot

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}/slots/{slot_id}'.format(slot_id='slot_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', intent_id='intent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_slot_type(client):
    """Test case for delete_slot_type

    
    """
    params = [('skipResourceInUseCheck', True)]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/slottypes/{slot_type_id}'.format(slot_type_id='slot_type_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_test_set(client):
    """Test case for delete_test_set

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/testsets/{test_set_id}'.format(test_set_id='test_set_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_utterances(client):
    """Test case for delete_utterances

    
    """
    params = [('localeId', 'locale_id_example'),
                    ('sessionId', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bots/{bot_id}/utterances'.format(bot_id='bot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_bot(client):
    """Test case for describe_bot

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}'.format(bot_id='bot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_bot_alias(client):
    """Test case for describe_bot_alias

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botaliases/{bot_alias_id}'.format(bot_alias_id='bot_alias_id_example', bot_id='bot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_bot_locale(client):
    """Test case for describe_bot_locale

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_bot_recommendation(client):
    """Test case for describe_bot_recommendation

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations/{bot_recommendation_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', bot_recommendation_id='bot_recommendation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_bot_version(client):
    """Test case for describe_bot_version

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}'.format(bot_id='bot_id_example', bot_version='bot_version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_custom_vocabulary_metadata(client):
    """Test case for describe_custom_vocabulary_metadata

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary/DEFAULT/metadata'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_export(client):
    """Test case for describe_export

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/exports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_import(client):
    """Test case for describe_import

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/imports/{import_id}'.format(import_id='import_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_intent(client):
    """Test case for describe_intent

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}'.format(intent_id='intent_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_resource_policy(client):
    """Test case for describe_resource_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/policy/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_slot(client):
    """Test case for describe_slot

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}/slots/{slot_id}'.format(slot_id='slot_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', intent_id='intent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_slot_type(client):
    """Test case for describe_slot_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/slottypes/{slot_type_id}'.format(slot_type_id='slot_type_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_test_execution(client):
    """Test case for describe_test_execution

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/testexecutions/{test_execution_id}'.format(test_execution_id='test_execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_test_set(client):
    """Test case for describe_test_set

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/testsets/{test_set_id}'.format(test_set_id='test_set_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_test_set_discrepancy_report(client):
    """Test case for describe_test_set_discrepancy_report

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/testsetdiscrepancy/{test_set_discrepancy_report_id}'.format(test_set_discrepancy_report_id='test_set_discrepancy_report_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_test_set_generation(client):
    """Test case for describe_test_set_generation

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/testsetgenerations/{test_set_generation_id}'.format(test_set_generation_id='test_set_generation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_execution_artifacts_url(client):
    """Test case for get_test_execution_artifacts_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/testexecutions/{test_execution_id}/artifacturl'.format(test_execution_id='test_execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_aggregated_utterances(client):
    """Test case for list_aggregated_utterances

    
    """
    body = {"botAliasId":"","maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":"","aggregationDuration":{"relativeAggregationDuration":{"timeDimension":"","timeValue":""}},"botVersion":"","localeId":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/aggregatedutterances'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bot_aliases(client):
    """Test case for list_bot_aliases

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botaliases'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bot_locales(client):
    """Test case for list_bot_locales

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales'.format(bot_id='bot_id_example', bot_version='bot_version_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bot_recommendations(client):
    """Test case for list_bot_recommendations

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bot_versions(client):
    """Test case for list_bot_versions

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bots(client):
    """Test case for list_bots

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_built_in_intents(client):
    """Test case for list_built_in_intents

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/builtins/locales/{locale_id}/intents'.format(locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_built_in_slot_types(client):
    """Test case for list_built_in_slot_types

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/builtins/locales/{locale_id}/slottypes'.format(locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_custom_vocabulary_items(client):
    """Test case for list_custom_vocabulary_items

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/customvocabulary/DEFAULT/list'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_exports(client):
    """Test case for list_exports

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"botId":"","filters":"","botVersion":"","localeId":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/exports/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_imports(client):
    """Test case for list_imports

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"botId":"","filters":"","botVersion":"","localeId":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/imports/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_intent_metrics(client):
    """Test case for list_intent_metrics

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","binBy":"","metrics":"","groupBy":"","filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/intentmetrics'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_intent_paths(client):
    """Test case for list_intent_paths

    
    """
    body = {"startDateTime":"","intentPath":"","filters":"","endDateTime":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/intentpaths'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_intent_stage_metrics(client):
    """Test case for list_intent_stage_metrics

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","binBy":"","metrics":"","groupBy":"","filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/intentstagemetrics'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_intents(client):
    """Test case for list_intents

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_recommended_intents(client):
    """Test case for list_recommended_intents

    
    """
    body = {"nextToken":"","maxResults":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations/{bot_recommendation_id}/intents'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', bot_recommendation_id='bot_recommendation_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_session_analytics_data(client):
    """Test case for list_session_analytics_data

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","sortBy":{"name":"","order":""},"filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/sessions'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_session_metrics(client):
    """Test case for list_session_metrics

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","binBy":"","metrics":"","groupBy":"","filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/sessionmetrics'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_slot_types(client):
    """Test case for list_slot_types

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/slottypes'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_slots(client):
    """Test case for list_slots

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""},"filters":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}/slots'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', intent_id='intent_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_execution_result_items(client):
    """Test case for list_test_execution_result_items

    
    """
    body = {"maxResults":"","nextToken":"","resultFilterBy":{"resultTypeFilter":"","conversationLevelTestResultsFilterBy":{"endToEndResult":""}}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testexecutions/{test_execution_id}/results'.format(test_execution_id='test_execution_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_executions(client):
    """Test case for list_test_executions

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testexecutions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_set_records(client):
    """Test case for list_test_set_records

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testsets/{test_set_id}/records'.format(test_set_id='test_set_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_sets(client):
    """Test case for list_test_sets

    
    """
    body = {"maxResults":"","nextToken":"","sortBy":{"attribute":"","order":""}}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testsets',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_utterance_analytics_data(client):
    """Test case for list_utterance_analytics_data

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","sortBy":{"name":"","order":""},"filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/utterances'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_utterance_metrics(client):
    """Test case for list_utterance_metrics

    
    """
    body = {"startDateTime":"","maxResults":"","nextToken":"","binBy":"","attributes":"","metrics":"","groupBy":"","filters":"","endDateTime":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/analytics/utterancemetrics'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_associated_transcripts(client):
    """Test case for search_associated_transcripts

    
    """
    body = {"maxResults":"","filters":"","nextIndex":"","searchOrder":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations/{bot_recommendation_id}/associatedtranscripts'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', bot_recommendation_id='bot_recommendation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_bot_recommendation(client):
    """Test case for start_bot_recommendation

    
    """
    body = {"encryptionSetting":{"associatedTranscriptsPassword":"","botLocaleExportPassword":"","kmsKeyArn":""},"transcriptSourceSetting":{"s3BucketTranscriptSource":{"transcriptFilter":{"lexTranscriptFilter":{"dateRangeFilter":{"startDateTime":"","endDateTime":""}}},"kmsKeyArn":"","s3BucketName":"","pathFormat":{"objectPrefixes":""},"transcriptFormat":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_import(client):
    """Test case for start_import

    
    """
    body = {"importId":"","filePassword":"","mergeStrategy":"","resourceSpecification":{"customVocabularyImportSpecification":{"botId":"","botVersion":"","localeId":""},"testSetImportResourceSpecification":{"testSetTags":"","modality":"","roleArn":"","description":"","storageLocation":{"s3Path":"","kmsKeyArn":"","s3BucketName":""},"importInputLocation":{"s3Path":"","s3BucketName":""},"testSetName":""},"botLocaleImportSpecification":{"nluIntentConfidenceThreshold":"","voiceSettings":{"voiceId":"","engine":""},"botId":"","botVersion":"","localeId":""},"botImportSpecification":{"testBotAliasTags":"","botName":"","roleArn":"","botTags":"","dataPrivacy":{"childDirected":""},"idleSessionTTLInSeconds":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/imports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_test_execution(client):
    """Test case for start_test_execution

    
    """
    body = {"testExecutionModality":"","apiMode":"","target":{"botAliasTarget":{"botAliasId":"","botId":"","localeId":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/testsets/{test_set_id}/testexecutions'.format(test_set_id='test_set_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_test_set_generation(client):
    """Test case for start_test_set_generation

    
    """
    body = {"testSetTags":"","roleArn":"","description":"","storageLocation":{"s3Path":"","kmsKeyArn":"","s3BucketName":""},"generationDataSource":{"conversationLogsDataSource":{"filter":{"inputMode":"","startTime":"","endTime":""},"botAliasId":"","botId":"","localeId":""}},"testSetName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/testsetgenerations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_bot_recommendation(client):
    """Test case for stop_bot_recommendation

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations/{bot_recommendation_id}/stopbotrecommendation'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', bot_recommendation_id='bot_recommendation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{resource_ar_ntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bot(client):
    """Test case for update_bot

    
    """
    body = {"botName":"","roleArn":"","botType":"","description":"","dataPrivacy":{"childDirected":""},"idleSessionTTLInSeconds":"","botMembers":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}'.format(bot_id='bot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bot_alias(client):
    """Test case for update_bot_alias

    
    """
    body = {"botAliasLocaleSettings":"","sentimentAnalysisSettings":{"detectSentiment":""},"description":"","botAliasName":"","botVersion":"","conversationLogSettings":{"textLogSettings":"","audioLogSettings":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botaliases/{bot_alias_id}'.format(bot_alias_id='bot_alias_id_example', bot_id='bot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bot_locale(client):
    """Test case for update_bot_locale

    
    """
    body = {"nluIntentConfidenceThreshold":"","description":"","voiceSettings":{"voiceId":"","engine":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bot_recommendation(client):
    """Test case for update_bot_recommendation

    
    """
    body = {"encryptionSetting":{"associatedTranscriptsPassword":"","botLocaleExportPassword":"","kmsKeyArn":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/botrecommendations/{bot_recommendation_id}'.format(bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', bot_recommendation_id='bot_recommendation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_export(client):
    """Test case for update_export

    
    """
    body = {"filePassword":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/exports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_intent(client):
    """Test case for update_intent

    
    """
    body = {"sampleUtterances":"","parentIntentSignature":"","intentConfirmationSetting":{"declinationResponse":{"messageGroups":"","allowInterrupt":""},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"active":"","confirmationNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""},"declinationNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"promptSpecification":{"messageGroups":"","maxRetries":"","allowInterrupt":"","promptAttemptsSpecification":"","messageSelectionStrategy":""},"confirmationConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"confirmationResponse":{"messageGroups":"","allowInterrupt":""},"elicitationCodeHook":{"enableCodeHookInvocation":"","invocationLabel":""},"declinationConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""}},"intentName":"","description":"","intentClosingSetting":{"conditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"closingResponse":{"messageGroups":"","allowInterrupt":""},"active":"","nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"initialResponseSetting":{"conditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"initialResponse":{"messageGroups":"","allowInterrupt":""},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""}},"slotPriorities":"","inputContexts":"","outputContexts":"","kendraConfiguration":{"kendraIndex":"","queryFilterStringEnabled":"","queryFilterString":""},"fulfillmentCodeHook":{"active":"","postFulfillmentStatusSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"fulfillmentUpdatesSpecification":{"active":"","startResponse":{"messageGroups":"","allowInterrupt":"","delayInSeconds":""},"updateResponse":{"messageGroups":"","allowInterrupt":"","frequencyInSeconds":""},"timeoutInSeconds":""},"enabled":""},"dialogCodeHook":{"enabled":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}'.format(intent_id='intent_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_resource_policy(client):
    """Test case for update_resource_policy

    
    """
    body = {"policy":""}
    params = [('expectedRevisionId', 'expected_revision_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/policy/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_slot(client):
    """Test case for update_slot

    
    """
    body = {"slotName":"","subSlotSetting":{"expression":"","slotSpecifications":""},"slotTypeId":"","description":"","valueElicitationSetting":{"sampleUtterances":"","slotConstraint":"","waitAndContinueSpecification":{"continueResponse":{"messageGroups":"","allowInterrupt":""},"waitingResponse":{"messageGroups":"","allowInterrupt":""},"active":"","stillWaitingResponse":{"messageGroups":"","allowInterrupt":"","frequencyInSeconds":"","timeoutInSeconds":""}},"defaultValueSpecification":{"defaultValueList":""},"promptSpecification":{"messageGroups":"","maxRetries":"","allowInterrupt":"","promptAttemptsSpecification":"","messageSelectionStrategy":""},"slotCaptureSetting":{"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"captureResponse":{"messageGroups":"","allowInterrupt":""},"elicitationCodeHook":{"enableCodeHookInvocation":"","invocationLabel":""},"captureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureResponse":{"messageGroups":"","allowInterrupt":""},"captureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"codeHook":{"postCodeHookSpecification":{"successResponse":{"messageGroups":"","allowInterrupt":""},"successConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"successNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"timeoutResponse":{"messageGroups":"","allowInterrupt":""},"failureNextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}},"failureConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""},"failureResponse":{"messageGroups":"","allowInterrupt":""},"timeoutConditional":{"defaultBranch":{"response":{"messageGroups":"","allowInterrupt":""},"nextStep":{"dialogAction":{"suppressNextMessage":"","type":"","slotToElicit":""},"sessionAttributes":"","intent":{"slots":"","name":""}}},"active":"","conditionalBranches":""}},"active":"","enableCodeHookInvocation":"","invocationLabel":""}}},"obfuscationSetting":{"obfuscationSettingType":""},"multipleValuesSetting":{"allowMultipleValues":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/intents/{intent_id}/slots/{slot_id}'.format(slot_id='slot_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example', intent_id='intent_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_slot_type(client):
    """Test case for update_slot_type

    
    """
    body = {"externalSourceSetting":{"grammarSlotTypeSetting":{"source":{"s3ObjectKey":"","kmsKeyArn":"","s3BucketName":""}}},"parentSlotTypeSignature":"","slotTypeName":"","description":"","valueSelectionSetting":{"resolutionStrategy":"","regexFilter":{"pattern":""},"advancedRecognitionSetting":{"audioRecognitionStrategy":""}},"compositeSlotTypeSetting":{"subSlots":""},"slotTypeValues":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bots/{bot_id}/botversions/{bot_version}/botlocales/{locale_id}/slottypes/{slot_type_id}'.format(slot_type_id='slot_type_id_example', bot_id='bot_id_example', bot_version='bot_version_example', locale_id='locale_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_test_set(client):
    """Test case for update_test_set

    
    """
    body = {"description":"","testSetName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/testsets/{test_set_id}'.format(test_set_id='test_set_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

