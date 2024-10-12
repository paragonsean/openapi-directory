# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_discoveryengine_v1alpha_lookup_widget_config_request import GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_lookup_widget_config_response import GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_complete_query_request import GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_complete_query_response import GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_converse_conversation_request import GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_converse_conversation_response import GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_search_request import GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_search_response import GoogleCloudDiscoveryengineV1alphaWidgetSearchResponse


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_locations_lookup_widget_config(client):
    """Test case for discoveryengine_locations_lookup_widget_config

    
    """
    body = {"widgetConfigId":"widgetConfigId"}
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
        path='/v1alpha/{location}/lookupWidgetConfig'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_locations_widget_complete_query(client):
    """Test case for discoveryengine_locations_widget_complete_query

    
    """
    body = {"completeQueryRequest":{"includeTailSuggestions":True,"query":"query","userPseudoId":"userPseudoId","dataStore":"dataStore","queryModel":"queryModel"},"additionalParams":{"token":"token"},"configId":"configId"}
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
        path='/v1alpha/{location}/widgetCompleteQuery'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_locations_widget_converse_conversation(client):
    """Test case for discoveryengine_locations_widget_converse_conversation

    
    """
    body = {"additionalParams":{"token":"token"},"configId":"configId","conversationId":"conversationId","converseConversationRequest":{"filter":"filter","servingConfig":"servingConfig","summarySpec":{"ignoreAdversarialQuery":True,"ignoreNonSummarySeekingQuery":True,"modelSpec":{"version":"version"},"summaryResultCount":2,"includeCitations":True,"languageCode":"languageCode","modelPromptSpec":{"preamble":"preamble"}},"query":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"name":"name","userLabels":{"key":"userLabels"},"safeSearch":True,"boostSpec":{"conditionBoostSpecs":[{"condition":"condition","boost":0.8008282},{"condition":"condition","boost":0.8008282}]},"conversation":{"userPseudoId":"userPseudoId","name":"name","messages":[{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}},{"createTime":"createTime","userInput":{"input":"input","context":{"contextDocuments":["contextDocuments","contextDocuments"],"activeDocument":"activeDocument"}},"reply":{"summary":{"summarySkippedReasons":["SUMMARY_SKIPPED_REASON_UNSPECIFIED","SUMMARY_SKIPPED_REASON_UNSPECIFIED"],"summaryText":"summaryText","summaryWithMetadata":{"summary":"summary","references":[{"document":"document","title":"title","uri":"uri"},{"document":"document","title":"title","uri":"uri"}],"citationMetadata":{"citations":[{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"},{"startIndex":"startIndex","sources":[{"referenceIndex":"referenceIndex"},{"referenceIndex":"referenceIndex"}],"endIndex":"endIndex"}]}},"safetyAttributes":{"scores":[1.4658129,1.4658129],"categories":["categories","categories"]}},"references":[{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"},{"anchorText":"anchorText","start":6,"end":0,"uri":"uri"}],"reply":"reply"}}],"startTime":"startTime","endTime":"endTime","state":"STATE_UNSPECIFIED"}}}
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
        path='/v1alpha/{location}/widgetConverseConversation'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discoveryengine_locations_widget_search(client):
    """Test case for discoveryengine_locations_widget_search

    
    """
    body = {"searchRequest":{"queryExpansionSpec":{"condition":"CONDITION_UNSPECIFIED","pinUnexpandedResults":True},"userInfo":{"userAgent":"userAgent","userId":"userId"},"offset":1,"rankingExpression":"rankingExpression","query":"query","userPseudoId":"userPseudoId","orderBy":"orderBy","pageSize":5,"userLabels":{"key":"userLabels"},"contentSearchSpec":{"extractiveContentSpec":{"maxExtractiveAnswerCount":0,"maxExtractiveSegmentCount":6,"numPreviousSegments":5,"numNextSegments":1},"summarySpec":{"ignoreAdversarialQuery":True,"ignoreNonSummarySeekingQuery":True,"modelSpec":{"version":"version"},"summaryResultCount":2,"includeCitations":True,"languageCode":"languageCode","modelPromptSpec":{"preamble":"preamble"}},"snippetSpec":{"maxSnippetCount":5,"referenceOnly":True,"returnSnippet":True}},"params":{"key":""},"branch":"branch","safeSearch":True,"boostSpec":{"conditionBoostSpecs":[{"condition":"condition","boost":0.8008282},{"condition":"condition","boost":0.8008282}]},"embeddingSpec":{"embeddingVectors":[{"fieldPath":"fieldPath","vector":[0.8008282,0.8008282]},{"fieldPath":"fieldPath","vector":[0.8008282,0.8008282]}]},"filter":"filter","spellCorrectionSpec":{"mode":"MODE_UNSPECIFIED"},"customFineTuningSpec":{"enableSearchAdaptor":True},"imageQuery":{"imageBytes":"imageBytes"},"facetSpecs":[{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":6,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]},{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":6,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]}],"servingConfig":"servingConfig","pageToken":"pageToken","canonicalFilter":"canonicalFilter"},"additionalParams":{"token":"token"},"configId":"configId"}
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
        path='/v1alpha/{location}/widgetSearch'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

