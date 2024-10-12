from typing import List, Dict
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
from openapi_server import util


async def batch_create_custom_vocabulary_item(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_custom_vocabulary_item

    Create a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

    :param bot_id: The identifier of the bot associated with this custom vocabulary.
    :type bot_id: str
    :param bot_version: The identifier of the version of the bot associated with this custom vocabulary.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchCreateCustomVocabularyItemRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_custom_vocabulary_item(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_custom_vocabulary_item

    Delete a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

    :param bot_id: The identifier of the bot associated with this custom vocabulary.
    :type bot_id: str
    :param bot_version: The identifier of the version of the bot associated with this custom vocabulary.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeleteCustomVocabularyItemRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_custom_vocabulary_item(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_custom_vocabulary_item

    Update a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

    :param bot_id: The identifier of the bot associated with this custom vocabulary
    :type bot_id: str
    :param bot_version: The identifier of the version of the bot associated with this custom vocabulary.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUpdateCustomVocabularyItemRequest.from_dict(body)
    return web.Response(status=200)


async def build_bot_locale(request: web.Request, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """build_bot_locale

    Builds a bot, its intents, and its slot types into a specific locale. A bot can be built into multiple locales. At runtime the locale is used to choose a specific build of the bot.

    :param bot_id: The identifier of the bot to build. The identifier is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation.
    :type bot_id: str
    :param bot_version: The version of the bot to build. This can only be the draft version of the bot.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def create_bot(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bot

    Creates an Amazon Lex conversational bot. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBotRequest.from_dict(body)
    return web.Response(status=200)


async def create_bot_alias(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bot_alias

    &lt;p&gt;Creates an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.&lt;/p&gt; &lt;p&gt;For example, you can create an alias called \&quot;PROD\&quot; that your applications use to call the Amazon Lex bot. &lt;/p&gt;

    :param bot_id: The unique identifier of the bot that the alias applies to.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBotAliasRequest.from_dict(body)
    return web.Response(status=200)


async def create_bot_locale(request: web.Request, bot_id, bot_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bot_locale

    Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.

    :param bot_id: The identifier of the bot to create the locale for.
    :type bot_id: str
    :param bot_version: The version of the bot to create the locale for. This can only be the draft version of the bot.
    :type bot_version: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBotLocaleRequest.from_dict(body)
    return web.Response(status=200)


async def create_bot_version(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bot_version

    &lt;p&gt;Creates a new version of the bot based on the &lt;code&gt;DRAFT&lt;/code&gt; version. If the &lt;code&gt;DRAFT&lt;/code&gt; version of this resource hasn&#39;t changed since you created the last version, Amazon Lex doesn&#39;t create a new version, it returns the last created version.&lt;/p&gt; &lt;p&gt;When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1.&lt;/p&gt;

    :param bot_id: The identifier of the bot to create the version for.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBotVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_export(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_export

    &lt;p&gt;Creates a zip archive containing the contents of a bot or a bot locale. The archive contains a directory structure that contains JSON files that define the bot.&lt;/p&gt; &lt;p&gt;You can create an archive that contains the complete definition of a bot, or you can specify that the archive contain only the definition of a single bot locale.&lt;/p&gt; &lt;p&gt;For more information about exporting bots, and about the structure of the export archive, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html\&quot;&gt; Importing and exporting bots &lt;/a&gt; &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateExportRequest.from_dict(body)
    return web.Response(status=200)


async def create_intent(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_intent

    &lt;p&gt;Creates an intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you define one or more intents. For example, for a pizza ordering bot you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent.&lt;/p&gt; &lt;p&gt;When you create an intent, you must provide a name. You can optionally provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;I want to order a pizza\&quot; and \&quot;Can I order a pizza.\&quot; You can&#39;t provide utterances for built-in intents.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slots for the information that you bot requests from the user. You can specify standard slot types, such as date and time, or custom slot types for your application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent is fulfilled. You can provide a Lambda function or configure the intent to return the intent information to your client application. If you use a Lambda function, Amazon Lex invokes the function when all of the intent information is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to send to the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent is fulfilled. For example, \&quot;I ordered your pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, \&quot;Do you want a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param bot_id: The identifier of the bot associated with this intent.
    :type bot_id: str
    :param bot_version: The version of the bot associated with this intent.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateIntentRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource_policy(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resource_policy

    Creates a new resource policy with the specified policy statements.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource_policy_statement(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, expected_revision_id=None) -> web.Response:
    """create_resource_policy_statement

    &lt;p&gt;Adds a new resource policy statement to a bot or bot alias. If a resource policy exists, the statement is added to the current resource policy. If a policy doesn&#39;t exist, a new policy is created.&lt;/p&gt; &lt;p&gt;You can&#39;t create a resource policy statement that allows cross-account access.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param expected_revision_id: &lt;p&gt;The identifier of the revision of the policy to edit. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt;
    :type expected_revision_id: str

    """
    body = CreateResourcePolicyStatementRequest.from_dict(body)
    return web.Response(status=200)


async def create_slot(request: web.Request, bot_id, bot_version, locale_id, intent_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_slot

    Creates a slot in an intent. A slot is a variable needed to fulfill an intent. For example, an &lt;code&gt;OrderPizza&lt;/code&gt; intent might need slots for size, crust, and number of pizzas. For each slot, you define one or more utterances that Amazon Lex uses to elicit a response from the user. 

    :param bot_id: The identifier of the bot associated with the slot.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the slot.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param intent_id: The identifier of the intent that contains the slot.
    :type intent_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSlotRequest.from_dict(body)
    return web.Response(status=200)


async def create_slot_type(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_slot_type

    &lt;p&gt;Creates a custom slot type&lt;/p&gt; &lt;p&gt; To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume. &lt;/p&gt;

    :param bot_id: The identifier of the bot associated with this slot type.
    :type bot_id: str
    :param bot_version: The identifier of the bot version associated with this slot type.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSlotTypeRequest.from_dict(body)
    return web.Response(status=200)


async def create_test_set_discrepancy_report(request: web.Request, test_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_test_set_discrepancy_report

    Create a report that describes the differences between the bot and the test set.

    :param test_set_id: The test set Id for the test set discrepancy report.
    :type test_set_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTestSetDiscrepancyReportRequest.from_dict(body)
    return web.Response(status=200)


async def create_upload_url(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_upload_url

    Gets a pre-signed S3 write URL that you use to upload the zip archive when importing a bot or a bot locale. 

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_bot(request: web.Request, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_resource_in_use_check=None) -> web.Response:
    """delete_bot

    &lt;p&gt;Deletes all versions of a bot, including the &lt;code&gt;Draft&lt;/code&gt; version. To delete a specific version, use the &lt;code&gt;DeleteBotVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;When you delete a bot, all of the resources contained in the bot are also deleted. Deleting a bot removes all locales, intents, slot, and slot types defined for the bot.&lt;/p&gt; &lt;p&gt;If a bot has an alias, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. If you want to delete the bot and the alias, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

    :param bot_id: The identifier of the bot to delete. 
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param skip_resource_in_use_check: By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the bot is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the bot even if it is being used by another resource.
    :type skip_resource_in_use_check: bool

    """
    return web.Response(status=200)


async def delete_bot_alias(request: web.Request, bot_alias_id, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_resource_in_use_check=None) -> web.Response:
    """delete_bot_alias

    Deletes the specified bot alias.

    :param bot_alias_id: The unique identifier of the bot alias to delete.
    :type bot_alias_id: str
    :param bot_id: The unique identifier of the bot associated with the alias to delete.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param skip_resource_in_use_check: By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the alias is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the alias even if it is being used by another resource.
    :type skip_resource_in_use_check: bool

    """
    return web.Response(status=200)


async def delete_bot_locale(request: web.Request, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bot_locale

    &lt;p&gt;Removes a locale from a bot.&lt;/p&gt; &lt;p&gt;When you delete a locale, all intents, slots, and slot types defined for the locale are also deleted.&lt;/p&gt;

    :param bot_id: The unique identifier of the bot that contains the locale.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the locale. 
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_bot_version(request: web.Request, bot_id, bot_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_resource_in_use_check=None) -> web.Response:
    """delete_bot_version

    Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html\&quot;&gt;DeleteBot&lt;/a&gt; operation.

    :param bot_id: The identifier of the bot that contains the version.
    :type bot_id: str
    :param bot_version: The version of the bot to delete.
    :type bot_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param skip_resource_in_use_check: By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the version is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the version even if it is being used by another resource.
    :type skip_resource_in_use_check: bool

    """
    return web.Response(status=200)


async def delete_custom_vocabulary(request: web.Request, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_custom_vocabulary

    Removes a custom vocabulary from the specified locale in the specified bot.

    :param bot_id: The unique identifier of the bot to remove the custom vocabulary from.
    :type bot_id: str
    :param bot_version: The version of the bot to remove the custom vocabulary from.
    :type bot_version: str
    :param locale_id: The locale identifier for the locale that contains the custom vocabulary to remove.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_export(request: web.Request, export_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_export

    Removes a previous export and the associated files stored in an S3 bucket.

    :param export_id: The unique identifier of the export to delete.
    :type export_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_import(request: web.Request, import_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_import

    Removes a previous import and the associated file stored in an S3 bucket.

    :param import_id: The unique identifier of the import to delete.
    :type import_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_intent(request: web.Request, intent_id, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_intent

    &lt;p&gt;Removes the specified intent.&lt;/p&gt; &lt;p&gt;Deleting an intent also deletes the slots associated with the intent.&lt;/p&gt;

    :param intent_id: The unique identifier of the intent to delete.
    :type intent_id: str
    :param bot_id: The identifier of the bot associated with the intent.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the intent.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, expected_revision_id=None) -> web.Response:
    """delete_resource_policy

    Removes an existing policy from a bot or bot alias. If the resource doesn&#39;t have a policy attached, Amazon Lex returns an exception.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param expected_revision_id: &lt;p&gt;The identifier of the revision to edit. If this ID doesn&#39;t match the current revision number, Amazon Lex returns an exception&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision ID, Amazon Lex will delete the current policy.&lt;/p&gt;
    :type expected_revision_id: str

    """
    return web.Response(status=200)


async def delete_resource_policy_statement(request: web.Request, resource_arn, statement_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, expected_revision_id=None) -> web.Response:
    """delete_resource_policy_statement

    Deletes a policy statement from a resource policy. If you delete the last statement from a policy, the policy is deleted. If you specify a statement ID that doesn&#39;t exist in the policy, or if the bot or bot alias doesn&#39;t have a policy attached, Amazon Lex returns an exception.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    :type resource_arn: str
    :param statement_id: The name of the statement (SID) to delete from the policy.
    :type statement_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param expected_revision_id: &lt;p&gt;The identifier of the revision of the policy to delete the statement from. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex removes the current contents of the statement. &lt;/p&gt;
    :type expected_revision_id: str

    """
    return web.Response(status=200)


async def delete_slot(request: web.Request, slot_id, bot_id, bot_version, locale_id, intent_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_slot

    Deletes the specified slot from an intent.

    :param slot_id: The identifier of the slot to delete. 
    :type slot_id: str
    :param bot_id: The identifier of the bot associated with the slot to delete.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the slot to delete.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param intent_id: The identifier of the intent associated with the slot.
    :type intent_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_slot_type(request: web.Request, slot_type_id, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_resource_in_use_check=None) -> web.Response:
    """delete_slot_type

    &lt;p&gt;Deletes a slot type from a bot locale.&lt;/p&gt; &lt;p&gt;If a slot is using the slot type, Amazon Lex throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. To avoid the exception, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

    :param slot_type_id: The identifier of the slot type to delete.
    :type slot_type_id: str
    :param bot_id: The identifier of the bot associated with the slot type.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the slot type.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param skip_resource_in_use_check: By default, the &lt;code&gt;DeleteSlotType&lt;/code&gt; operations throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if you try to delete a slot type used by a slot. Set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the slot type even if a slot uses it.
    :type skip_resource_in_use_check: bool

    """
    return web.Response(status=200)


async def delete_test_set(request: web.Request, test_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_test_set

    The action to delete the selected test set.

    :param test_set_id: The test set Id of the test set to be deleted.
    :type test_set_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_utterances(request: web.Request, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, locale_id=None, session_id=None) -> web.Response:
    """delete_utterances

    &lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input..&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete utterances for a specific session. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;ListAggregatedUtterances&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt;

    :param bot_id: The unique identifier of the bot that contains the utterances.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param locale_id: The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param session_id: The unique identifier of the session with the user. The ID is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html\&quot;&gt;RecognizeText&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html\&quot;&gt;RecognizeUtterance&lt;/a&gt; operations.
    :type session_id: str

    """
    return web.Response(status=200)


async def describe_bot(request: web.Request, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bot

    Provides metadata information about a bot. 

    :param bot_id: The unique identifier of the bot to describe.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_bot_alias(request: web.Request, bot_alias_id, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bot_alias

    Get information about a specific bot alias.

    :param bot_alias_id: The identifier of the bot alias to describe.
    :type bot_alias_id: str
    :param bot_id: The identifier of the bot associated with the bot alias to describe.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_bot_locale(request: web.Request, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bot_locale

    Describes the settings that a bot has for a specific locale. 

    :param bot_id: The identifier of the bot associated with the locale.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the locale.
    :type bot_version: str
    :param locale_id: The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. 
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_bot_recommendation(request: web.Request, bot_id, bot_version, locale_id, bot_recommendation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bot_recommendation

    Provides metadata information about a bot recommendation. This information will enable you to get a description on the request inputs, to download associated transcripts after processing is complete, and to download intents and slot-types generated by the bot recommendation.

    :param bot_id: The unique identifier of the bot associated with the bot recommendation.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the bot recommendation.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param bot_recommendation_id: The identifier of the bot recommendation to describe.
    :type bot_recommendation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_bot_version(request: web.Request, bot_id, bot_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bot_version

    Provides metadata about a version of a bot.

    :param bot_id: The identifier of the bot containing the version to return metadata for.
    :type bot_id: str
    :param bot_version: The version of the bot to return metadata for.
    :type bot_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_custom_vocabulary_metadata(request: web.Request, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_custom_vocabulary_metadata

    Provides metadata information about a custom vocabulary.

    :param bot_id: The unique identifier of the bot that contains the custom vocabulary.
    :type bot_id: str
    :param bot_version: The bot version of the bot to return metadata for.
    :type bot_version: str
    :param locale_id: The locale to return the custom vocabulary information for. The locale must be &lt;code&gt;en_GB&lt;/code&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_export(request: web.Request, export_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_export

    Gets information about a specific export.

    :param export_id: The unique identifier of the export to describe.
    :type export_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_import(request: web.Request, import_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_import

    Gets information about a specific import.

    :param import_id: The unique identifier of the import to describe.
    :type import_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_intent(request: web.Request, intent_id, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_intent

    Returns metadata about an intent.

    :param intent_id: The identifier of the intent to describe.
    :type intent_id: str
    :param bot_id: The identifier of the bot associated with the intent.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the intent.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource_policy

    Gets the resource policy and policy revision for a bot or bot alias.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_slot(request: web.Request, slot_id, bot_id, bot_version, locale_id, intent_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_slot

    Gets metadata information about a slot.

    :param slot_id: The unique identifier for the slot.
    :type slot_id: str
    :param bot_id: The identifier of the bot associated with the slot.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the slot.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param intent_id: The identifier of the intent that contains the slot.
    :type intent_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_slot_type(request: web.Request, slot_type_id, bot_id, bot_version, locale_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_slot_type

    Gets metadata information about a slot type.

    :param slot_type_id: The identifier of the slot type.
    :type slot_type_id: str
    :param bot_id: The identifier of the bot associated with the slot type.
    :type bot_id: str
    :param bot_version: The version of the bot associated with the slot type.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_test_execution(request: web.Request, test_execution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_test_execution

    Gets metadata information about the test execution.

    :param test_execution_id: The execution Id of the test set execution.
    :type test_execution_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_test_set(request: web.Request, test_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_test_set

    Gets metadata information about the test set.

    :param test_set_id: The test set Id for the test set request.
    :type test_set_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_test_set_discrepancy_report(request: web.Request, test_set_discrepancy_report_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_test_set_discrepancy_report

    Gets metadata information about the test set discrepancy report.

    :param test_set_discrepancy_report_id: The unique identifier of the test set discrepancy report.
    :type test_set_discrepancy_report_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_test_set_generation(request: web.Request, test_set_generation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_test_set_generation

    Gets metadata information about the test set generation.

    :param test_set_generation_id: The unique identifier of the test set generation.
    :type test_set_generation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_test_execution_artifacts_url(request: web.Request, test_execution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_test_execution_artifacts_url

    The pre-signed Amazon S3 URL to download the test execution result artifacts.

    :param test_execution_id: The unique identifier of the completed test execution.
    :type test_execution_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_aggregated_utterances(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_aggregated_utterances

    &lt;p&gt;Provides a list of utterances that users have sent to the bot.&lt;/p&gt; &lt;p&gt;Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase \&quot;I want to order pizza\&quot; are aggregated into the same line in the response.&lt;/p&gt; &lt;p&gt;You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didn&#39;t activate an intent.&lt;/p&gt; &lt;p&gt;Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.&lt;/p&gt; &lt;p&gt;Utterances statistics are not generated under the following conditions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;childDirected&lt;/code&gt; field was set to true when the bot was created.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You are using slot obfuscation with one or more slots.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You opted out of participating in improving Amazon Lex.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param bot_id: The unique identifier of the bot associated with this request.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAggregatedUtterancesRequest.from_dict(body)
    return web.Response(status=200)


async def list_bot_aliases(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bot_aliases

    Gets a list of aliases for the specified bot.

    :param bot_id: The identifier of the bot to list aliases for.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBotAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def list_bot_locales(request: web.Request, bot_id, bot_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bot_locales

    Gets a list of locales for the specified bot.

    :param bot_id: The identifier of the bot to list locales for.
    :type bot_id: str
    :param bot_version: The version of the bot to list locales for.
    :type bot_version: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBotLocalesRequest.from_dict(body)
    return web.Response(status=200)


async def list_bot_recommendations(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bot_recommendations

    Get a list of bot recommendations that meet the specified criteria.

    :param bot_id: The unique identifier of the bot that contains the bot recommendation list.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the bot recommendation list.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the bot recommendation list.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBotRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_bot_versions(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bot_versions

    &lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns a summary of each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns for summaries, one for each numbered version and one for the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt;

    :param bot_id: The identifier of the bot to list versions for.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBotVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_bots(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bots

    Gets a list of available bots.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBotsRequest.from_dict(body)
    return web.Response(status=200)


async def list_built_in_intents(request: web.Request, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_built_in_intents

    &lt;p&gt;Gets a list of built-in intents provided by Amazon Lex that you can use in your bot. &lt;/p&gt; &lt;p&gt;To use a built-in intent as a the base for your own intent, include the built-in intent signature in the &lt;code&gt;parentIntentSignature&lt;/code&gt; parameter when you call the &lt;code&gt;CreateIntent&lt;/code&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html\&quot;&gt;CreateIntent&lt;/a&gt;.&lt;/p&gt;

    :param locale_id: The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBuiltInIntentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_built_in_slot_types(request: web.Request, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_built_in_slot_types

    Gets a list of built-in slot types that meet the specified criteria.

    :param locale_id: The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListBuiltInSlotTypesRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_vocabulary_items(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_vocabulary_items

    Paginated list of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

    :param bot_id: The identifier of the version of the bot associated with this custom vocabulary.
    :type bot_id: str
    :param bot_version: The bot version of the bot to the list custom vocabulary request.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListCustomVocabularyItemsRequest.from_dict(body)
    return web.Response(status=200)


async def list_exports(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_exports

    Lists the exports for a bot, bot locale, or custom vocabulary. Exports are kept in the list for 7 days.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListExportsRequest.from_dict(body)
    return web.Response(status=200)


async def list_imports(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_imports

    Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListImportsRequest.from_dict(body)
    return web.Response(status=200)


async def list_intent_metrics(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_intent_metrics

    &lt;p&gt;Retrieves summary metrics for the intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetric.html\&quot;&gt;AnalyticsIntentMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can specify only one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve intent metrics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIntentMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def list_intent_paths(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_intent_paths

    &lt;p&gt;Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentPath&lt;/code&gt; – Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the &lt;code&gt;intentPath&lt;/code&gt; field with &lt;code&gt;/BookCar/BookHotel&lt;/code&gt; to see details about how many times users invoked the &lt;code&gt;BookCar&lt;/code&gt; and &lt;code&gt;BookHotel&lt;/code&gt; intents in that order.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the optional &lt;code&gt;filters&lt;/code&gt; field to filter the results.&lt;/p&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve intent path metrics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListIntentPathsRequest.from_dict(body)
    return web.Response(status=200)


async def list_intent_stage_metrics(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_intent_stage_metrics

    &lt;p&gt;Retrieves summary metrics for the stages within intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetric.html\&quot;&gt;AnalyticsIntentStageMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can only specify one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve intent stage metrics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIntentStageMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def list_intents(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_intents

    Get a list of intents that meet the specified criteria.

    :param bot_id: The unique identifier of the bot that contains the intent.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the intent.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIntentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_recommended_intents(request: web.Request, bot_id, bot_version, locale_id, bot_recommendation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_recommended_intents

    Gets a list of recommended intents provided by the bot recommendation that you can use in your bot. Intents in the response are ordered by relevance.

    :param bot_id: The unique identifier of the bot associated with the recommended intents.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the recommended intents.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the recommended intents.
    :type locale_id: str
    :param bot_recommendation_id: The identifier of the bot recommendation that contains the recommended intents.
    :type bot_recommendation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRecommendedIntentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_session_analytics_data(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_session_analytics_data

    &lt;p&gt;Retrieves a list of metadata for individual user sessions with your bot. The &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve session analytics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSessionAnalyticsDataRequest.from_dict(body)
    return web.Response(status=200)


async def list_session_metrics(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_session_metrics

    &lt;p&gt;Retrieves summary metrics for the user sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetric.html\&quot;&gt;AnalyticsSessionMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve session metrics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSessionMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def list_slot_types(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_slot_types

    Gets a list of slot types that match the specified criteria.

    :param bot_id: The unique identifier of the bot that contains the slot types.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the slot type.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSlotTypesRequest.from_dict(body)
    return web.Response(status=200)


async def list_slots(request: web.Request, bot_id, bot_version, locale_id, intent_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_slots

    Gets a list of slots that match the specified criteria.

    :param bot_id: The identifier of the bot that contains the slot.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the slot.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param intent_id: The unique identifier of the intent that contains the slot.
    :type intent_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSlotsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Gets a list of tags associated with a resource. Only bots, bot aliases, and bot channels can have tags associated with them.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to get a list of tags for.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_test_execution_result_items(request: web.Request, test_execution_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_test_execution_result_items

    Gets a list of test execution result items.

    :param test_execution_id: The unique identifier of the test execution to list the result items.
    :type test_execution_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTestExecutionResultItemsRequest.from_dict(body)
    return web.Response(status=200)


async def list_test_executions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_test_executions

    The list of test set executions.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTestExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_test_set_records(request: web.Request, test_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_test_set_records

    The list of test set records.

    :param test_set_id: The identifier of the test set to list its test set records.
    :type test_set_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTestSetRecordsRequest.from_dict(body)
    return web.Response(status=200)


async def list_test_sets(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_test_sets

    The list of the test sets

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTestSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_utterance_analytics_data(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_utterance_analytics_data

    &lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves a list of metadata for individual user utterances to your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve utterance analytics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListUtteranceAnalyticsDataRequest.from_dict(body)
    return web.Response(status=200)


async def list_utterance_metrics(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_utterance_metrics

    &lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves summary metrics for the utterances in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetric.html\&quot;&gt;AnalyticsUtteranceMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

    :param bot_id: The identifier for the bot for which you want to retrieve utterance metrics.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListUtteranceMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def search_associated_transcripts(request: web.Request, bot_id, bot_version, locale_id, bot_recommendation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """search_associated_transcripts

    Search for associated transcripts that meet the specified criteria.

    :param bot_id: The unique identifier of the bot associated with the transcripts that you are searching.
    :type bot_id: str
    :param bot_version: The version of the bot containing the transcripts that you are searching.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt; 
    :type locale_id: str
    :param bot_recommendation_id: The unique identifier of the bot recommendation associated with the transcripts to search.
    :type bot_recommendation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SearchAssociatedTranscriptsRequest.from_dict(body)
    return web.Response(status=200)


async def start_bot_recommendation(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_bot_recommendation

    Use this to provide your transcript data, and to start the bot recommendation process.

    :param bot_id: The unique identifier of the bot containing the bot recommendation.
    :type bot_id: str
    :param bot_version: The version of the bot containing the bot recommendation.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt; 
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartBotRecommendationRequest.from_dict(body)
    return web.Response(status=200)


async def start_import(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_import

    Starts importing a bot, bot locale, or custom vocabulary from a zip archive that you uploaded to an S3 bucket.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartImportRequest.from_dict(body)
    return web.Response(status=200)


async def start_test_execution(request: web.Request, test_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_test_execution

    The action to start test set execution.

    :param test_set_id: The test set Id for the test set execution.
    :type test_set_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartTestExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def start_test_set_generation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_test_set_generation

    The action to start the generation of test set.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartTestSetGenerationRequest.from_dict(body)
    return web.Response(status=200)


async def stop_bot_recommendation(request: web.Request, bot_id, bot_version, locale_id, bot_recommendation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_bot_recommendation

    Stop an already running Bot Recommendation request.

    :param bot_id: The unique identifier of the bot containing the bot recommendation to be stopped.
    :type bot_id: str
    :param bot_version: The version of the bot containing the bot recommendation.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt; 
    :type locale_id: str
    :param bot_recommendation_id: The unique identifier of the bot recommendation to be stopped.
    :type bot_recommendation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes tags from a bot, bot alias, or bot channel.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to remove the tags from.
    :type resource_arn: str
    :param tag_keys: A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_bot(request: web.Request, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bot

    Updates the configuration of an existing bot. 

    :param bot_id: The unique identifier of the bot to update. This identifier is returned by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBotRequest.from_dict(body)
    return web.Response(status=200)


async def update_bot_alias(request: web.Request, bot_alias_id, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bot_alias

    Updates the configuration of an existing bot alias.

    :param bot_alias_id: The unique identifier of the bot alias.
    :type bot_alias_id: str
    :param bot_id: The identifier of the bot with the updated alias.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBotAliasRequest.from_dict(body)
    return web.Response(status=200)


async def update_bot_locale(request: web.Request, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bot_locale

    Updates the settings that a bot has for a specific locale.

    :param bot_id: The unique identifier of the bot that contains the locale.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the locale to be updated. The version can only be the &lt;code&gt;DRAFT&lt;/code&gt; version.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBotLocaleRequest.from_dict(body)
    return web.Response(status=200)


async def update_bot_recommendation(request: web.Request, bot_id, bot_version, locale_id, bot_recommendation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bot_recommendation

    Updates an existing bot recommendation request.

    :param bot_id: The unique identifier of the bot containing the bot recommendation to be updated.
    :type bot_id: str
    :param bot_version: The version of the bot containing the bot recommendation to be updated.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt; 
    :type locale_id: str
    :param bot_recommendation_id: The unique identifier of the bot recommendation to be updated.
    :type bot_recommendation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBotRecommendationRequest.from_dict(body)
    return web.Response(status=200)


async def update_export(request: web.Request, export_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_export

    &lt;p&gt;Updates the password used to protect an export zip archive.&lt;/p&gt; &lt;p&gt;The password is not required. If you don&#39;t supply a password, Amazon Lex generates a zip file that is not protected by a password. This is the archive that is available at the pre-signed S3 URL provided by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html\&quot;&gt;DescribeExport&lt;/a&gt; operation.&lt;/p&gt;

    :param export_id: The unique identifier Amazon Lex assigned to the export.
    :type export_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateExportRequest.from_dict(body)
    return web.Response(status=200)


async def update_intent(request: web.Request, intent_id, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_intent

    Updates the settings for an intent.

    :param intent_id: The unique identifier of the intent to update.
    :type intent_id: str
    :param bot_id: The identifier of the bot that contains the intent.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the intent. Must be &lt;code&gt;DRAFT&lt;/code&gt;.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateIntentRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource_policy(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, expected_revision_id=None) -> web.Response:
    """update_resource_policy

    Replaces the existing resource policy for a bot or bot alias with a new one. If the policy doesn&#39;t exist, Amazon Lex returns an exception.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param expected_revision_id: &lt;p&gt;The identifier of the revision of the policy to update. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt;
    :type expected_revision_id: str

    """
    body = UpdateResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_slot(request: web.Request, slot_id, bot_id, bot_version, locale_id, intent_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_slot

    Updates the settings for a slot.

    :param slot_id: The unique identifier for the slot to update.
    :type slot_id: str
    :param bot_id: The unique identifier of the bot that contains the slot.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the slot. Must always be &lt;code&gt;DRAFT&lt;/code&gt;.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param intent_id: The identifier of the intent that contains the slot.
    :type intent_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSlotRequest.from_dict(body)
    return web.Response(status=200)


async def update_slot_type(request: web.Request, slot_type_id, bot_id, bot_version, locale_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_slot_type

    Updates the configuration of an existing slot type.

    :param slot_type_id: The unique identifier of the slot type to update.
    :type slot_type_id: str
    :param bot_id: The identifier of the bot that contains the slot type.
    :type bot_id: str
    :param bot_version: The version of the bot that contains the slot type. Must be &lt;code&gt;DRAFT&lt;/code&gt;.
    :type bot_version: str
    :param locale_id: The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.
    :type locale_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSlotTypeRequest.from_dict(body)
    return web.Response(status=200)


async def update_test_set(request: web.Request, test_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_test_set

    The action to update the test set.

    :param test_set_id: The test set Id for which update test operation to be performed.
    :type test_set_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTestSetRequest.from_dict(body)
    return web.Response(status=200)
