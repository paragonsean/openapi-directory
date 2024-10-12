# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_analytics_admin_v1alpha_access_binding import GoogleAnalyticsAdminV1alphaAccessBinding
from openapi_server.models.google_analytics_admin_v1alpha_acknowledge_user_data_collection_request import GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest
from openapi_server.models.google_analytics_admin_v1alpha_ad_sense_link import GoogleAnalyticsAdminV1alphaAdSenseLink
from openapi_server.models.google_analytics_admin_v1alpha_approve_display_video360_advertiser_link_proposal_response import GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse
from openapi_server.models.google_analytics_admin_v1alpha_audience import GoogleAnalyticsAdminV1alphaAudience
from openapi_server.models.google_analytics_admin_v1alpha_batch_create_access_bindings_request import GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest
from openapi_server.models.google_analytics_admin_v1alpha_batch_create_access_bindings_response import GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse
from openapi_server.models.google_analytics_admin_v1alpha_batch_delete_access_bindings_request import GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest
from openapi_server.models.google_analytics_admin_v1alpha_batch_get_access_bindings_response import GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse
from openapi_server.models.google_analytics_admin_v1alpha_batch_update_access_bindings_request import GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest
from openapi_server.models.google_analytics_admin_v1alpha_batch_update_access_bindings_response import GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse
from openapi_server.models.google_analytics_admin_v1alpha_calculated_metric import GoogleAnalyticsAdminV1alphaCalculatedMetric
from openapi_server.models.google_analytics_admin_v1alpha_channel_group import GoogleAnalyticsAdminV1alphaChannelGroup
from openapi_server.models.google_analytics_admin_v1alpha_conversion_event import GoogleAnalyticsAdminV1alphaConversionEvent
from openapi_server.models.google_analytics_admin_v1alpha_create_connected_site_tag_request import GoogleAnalyticsAdminV1alphaCreateConnectedSiteTagRequest
from openapi_server.models.google_analytics_admin_v1alpha_create_rollup_property_request import GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest
from openapi_server.models.google_analytics_admin_v1alpha_create_rollup_property_response import GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse
from openapi_server.models.google_analytics_admin_v1alpha_create_subproperty_request import GoogleAnalyticsAdminV1alphaCreateSubpropertyRequest
from openapi_server.models.google_analytics_admin_v1alpha_create_subproperty_response import GoogleAnalyticsAdminV1alphaCreateSubpropertyResponse
from openapi_server.models.google_analytics_admin_v1alpha_custom_dimension import GoogleAnalyticsAdminV1alphaCustomDimension
from openapi_server.models.google_analytics_admin_v1alpha_custom_metric import GoogleAnalyticsAdminV1alphaCustomMetric
from openapi_server.models.google_analytics_admin_v1alpha_data_stream import GoogleAnalyticsAdminV1alphaDataStream
from openapi_server.models.google_analytics_admin_v1alpha_delete_connected_site_tag_request import GoogleAnalyticsAdminV1alphaDeleteConnectedSiteTagRequest
from openapi_server.models.google_analytics_admin_v1alpha_display_video360_advertiser_link import GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
from openapi_server.models.google_analytics_admin_v1alpha_display_video360_advertiser_link_proposal import GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
from openapi_server.models.google_analytics_admin_v1alpha_event_create_rule import GoogleAnalyticsAdminV1alphaEventCreateRule
from openapi_server.models.google_analytics_admin_v1alpha_expanded_data_set import GoogleAnalyticsAdminV1alphaExpandedDataSet
from openapi_server.models.google_analytics_admin_v1alpha_fetch_automated_ga4_configuration_opt_out_request import GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutRequest
from openapi_server.models.google_analytics_admin_v1alpha_fetch_automated_ga4_configuration_opt_out_response import GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutResponse
from openapi_server.models.google_analytics_admin_v1alpha_fetch_connected_ga4_property_response import GoogleAnalyticsAdminV1alphaFetchConnectedGa4PropertyResponse
from openapi_server.models.google_analytics_admin_v1alpha_firebase_link import GoogleAnalyticsAdminV1alphaFirebaseLink
from openapi_server.models.google_analytics_admin_v1alpha_google_ads_link import GoogleAnalyticsAdminV1alphaGoogleAdsLink
from openapi_server.models.google_analytics_admin_v1alpha_list_access_bindings_response import GoogleAnalyticsAdminV1alphaListAccessBindingsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_ad_sense_links_response import GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_audiences_response import GoogleAnalyticsAdminV1alphaListAudiencesResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_big_query_links_response import GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_calculated_metrics_response import GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_channel_groups_response import GoogleAnalyticsAdminV1alphaListChannelGroupsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_connected_site_tags_request import GoogleAnalyticsAdminV1alphaListConnectedSiteTagsRequest
from openapi_server.models.google_analytics_admin_v1alpha_list_connected_site_tags_response import GoogleAnalyticsAdminV1alphaListConnectedSiteTagsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_conversion_events_response import GoogleAnalyticsAdminV1alphaListConversionEventsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_custom_dimensions_response import GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_custom_metrics_response import GoogleAnalyticsAdminV1alphaListCustomMetricsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_data_streams_response import GoogleAnalyticsAdminV1alphaListDataStreamsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_display_video360_advertiser_link_proposals_response import GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_display_video360_advertiser_links_response import GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_event_create_rules_response import GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_expanded_data_sets_response import GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_firebase_links_response import GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_google_ads_links_response import GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_measurement_protocol_secrets_response import GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_properties_response import GoogleAnalyticsAdminV1alphaListPropertiesResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_rollup_property_source_links_response import GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_skad_network_conversion_value_schemas_response import GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_search_ads360_links_response import GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse
from openapi_server.models.google_analytics_admin_v1alpha_list_subproperty_event_filters_response import GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse
from openapi_server.models.google_analytics_admin_v1alpha_measurement_protocol_secret import GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
from openapi_server.models.google_analytics_admin_v1alpha_property import GoogleAnalyticsAdminV1alphaProperty
from openapi_server.models.google_analytics_admin_v1alpha_rollup_property_source_link import GoogleAnalyticsAdminV1alphaRollupPropertySourceLink
from openapi_server.models.google_analytics_admin_v1alpha_run_access_report_request import GoogleAnalyticsAdminV1alphaRunAccessReportRequest
from openapi_server.models.google_analytics_admin_v1alpha_run_access_report_response import GoogleAnalyticsAdminV1alphaRunAccessReportResponse
from openapi_server.models.google_analytics_admin_v1alpha_skad_network_conversion_value_schema import GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema
from openapi_server.models.google_analytics_admin_v1alpha_search_ads360_link import GoogleAnalyticsAdminV1alphaSearchAds360Link
from openapi_server.models.google_analytics_admin_v1alpha_set_automated_ga4_configuration_opt_out_request import GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutRequest
from openapi_server.models.google_analytics_admin_v1alpha_subproperty_event_filter import GoogleAnalyticsAdminV1alphaSubpropertyEventFilter


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_batch_create(client):
    """Test case for analyticsadmin_properties_access_bindings_batch_create

    
    """
    body = {"requests":[{"parent":"parent","accessBinding":{"roles":["roles","roles"],"name":"name","user":"user"}},{"parent":"parent","accessBinding":{"roles":["roles","roles"],"name":"name","user":"user"}}]}
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
        path='/v1alpha/{parent}/accessBindings:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_batch_delete(client):
    """Test case for analyticsadmin_properties_access_bindings_batch_delete

    
    """
    body = {"requests":[{"name":"name"},{"name":"name"}]}
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
        path='/v1alpha/{parent}/accessBindings:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_batch_get(client):
    """Test case for analyticsadmin_properties_access_bindings_batch_get

    
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
                    ('names', ['names_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/accessBindings:batchGet'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_batch_update(client):
    """Test case for analyticsadmin_properties_access_bindings_batch_update

    
    """
    body = {"requests":[{"accessBinding":{"roles":["roles","roles"],"name":"name","user":"user"}},{"accessBinding":{"roles":["roles","roles"],"name":"name","user":"user"}}]}
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
        path='/v1alpha/{parent}/accessBindings:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_create(client):
    """Test case for analyticsadmin_properties_access_bindings_create

    
    """
    body = {"roles":["roles","roles"],"name":"name","user":"user"}
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
        path='/v1alpha/{parent}/accessBindings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_access_bindings_list(client):
    """Test case for analyticsadmin_properties_access_bindings_list

    
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
        path='/v1alpha/{parent}/accessBindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_acknowledge_user_data_collection(client):
    """Test case for analyticsadmin_properties_acknowledge_user_data_collection

    
    """
    body = {"acknowledgement":"acknowledgement"}
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
        path='/v1alpha/{propertyacknowledge_user_data_collectio}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_ad_sense_links_create(client):
    """Test case for analyticsadmin_properties_ad_sense_links_create

    
    """
    body = {"name":"name","adClientCode":"adClientCode"}
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
        path='/v1alpha/{parent}/adSenseLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_ad_sense_links_list(client):
    """Test case for analyticsadmin_properties_ad_sense_links_list

    
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
        path='/v1alpha/{parent}/adSenseLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_audiences_create(client):
    """Test case for analyticsadmin_properties_audiences_create

    
    """
    body = {"displayName":"displayName","eventTrigger":{"logCondition":"LOG_CONDITION_UNSPECIFIED","eventName":"eventName"},"filterClauses":[{"sequenceFilter":{"scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","sequenceSteps":[{"immediatelyFollows":True,"constraintDuration":"constraintDuration","scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}},{"immediatelyFollows":True,"constraintDuration":"constraintDuration","scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}}],"sequenceMaximumDuration":"sequenceMaximumDuration"},"simpleFilter":{"scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}},"clauseType":"AUDIENCE_CLAUSE_TYPE_UNSPECIFIED"},{"sequenceFilter":{"scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","sequenceSteps":[{"immediatelyFollows":True,"constraintDuration":"constraintDuration","scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}},{"immediatelyFollows":True,"constraintDuration":"constraintDuration","scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}}],"sequenceMaximumDuration":"sequenceMaximumDuration"},"simpleFilter":{"scope":"AUDIENCE_FILTER_SCOPE_UNSPECIFIED","filterExpression":{"eventFilter":{"eventName":"eventName"},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]},"dimensionOrMetricFilter":{"inAnyNDayPeriod":6,"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"atAnyPointInTime":True,"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}}}},"clauseType":"AUDIENCE_CLAUSE_TYPE_UNSPECIFIED"}],"membershipDurationDays":1,"name":"name","description":"description","exclusionDurationMode":"AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED","adsPersonalizationEnabled":True}
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
        path='/v1alpha/{parent}/audiences'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_audiences_list(client):
    """Test case for analyticsadmin_properties_audiences_list

    
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
        path='/v1alpha/{parent}/audiences'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_big_query_links_list(client):
    """Test case for analyticsadmin_properties_big_query_links_list

    
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
        path='/v1alpha/{parent}/bigQueryLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_calculated_metrics_create(client):
    """Test case for analyticsadmin_properties_calculated_metrics_create

    
    """
    body = {"displayName":"displayName","calculatedMetricId":"calculatedMetricId","name":"name","description":"description","formula":"formula","restrictedMetricType":["RESTRICTED_METRIC_TYPE_UNSPECIFIED","RESTRICTED_METRIC_TYPE_UNSPECIFIED"],"invalidMetricReference":True,"metricUnit":"METRIC_UNIT_UNSPECIFIED"}
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
                    ('calculatedMetricId', 'calculated_metric_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/calculatedMetrics'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_calculated_metrics_list(client):
    """Test case for analyticsadmin_properties_calculated_metrics_list

    
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
        path='/v1alpha/{parent}/calculatedMetrics'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_channel_groups_create(client):
    """Test case for analyticsadmin_properties_channel_groups_create

    
    """
    body = {"displayName":"displayName","groupingRule":[{"expression":{"filter":{"fieldName":"fieldName","inListFilter":{"values":["values","values"]},"stringFilter":{"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]}},"displayName":"displayName"},{"expression":{"filter":{"fieldName":"fieldName","inListFilter":{"values":["values","values"]},"stringFilter":{"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"filterExpressions":[null,null]},"andGroup":{"filterExpressions":[null,null]}},"displayName":"displayName"}],"name":"name","description":"description","systemDefined":True}
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
        path='/v1alpha/{parent}/channelGroups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_channel_groups_list(client):
    """Test case for analyticsadmin_properties_channel_groups_list

    
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
        path='/v1alpha/{parent}/channelGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_conversion_events_create(client):
    """Test case for analyticsadmin_properties_conversion_events_create

    
    """
    body = {"countingMethod":"CONVERSION_COUNTING_METHOD_UNSPECIFIED","createTime":"createTime","defaultConversionValue":{"currencyCode":"currencyCode","value":5.962133916683182},"custom":True,"deletable":True,"name":"name","eventName":"eventName"}
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
        path='/v1alpha/{parent}/conversionEvents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_conversion_events_list(client):
    """Test case for analyticsadmin_properties_conversion_events_list

    
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
        path='/v1alpha/{parent}/conversionEvents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_create(client):
    """Test case for analyticsadmin_properties_create

    
    """
    body = {"parent":"parent","industryCategory":"INDUSTRY_CATEGORY_UNSPECIFIED","displayName":"displayName","timeZone":"timeZone","updateTime":"updateTime","serviceLevel":"SERVICE_LEVEL_UNSPECIFIED","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","propertyType":"PROPERTY_TYPE_UNSPECIFIED","name":"name","currencyCode":"currencyCode","account":"account"}
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
        path='/v1alpha/properties',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_create_connected_site_tag(client):
    """Test case for analyticsadmin_properties_create_connected_site_tag

    
    """
    body = {"connectedSiteTag":{"tagId":"tagId","displayName":"displayName"},"property":"property"}
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
        path='/v1alpha/properties:createConnectedSiteTag',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_create_rollup_property(client):
    """Test case for analyticsadmin_properties_create_rollup_property

    
    """
    body = {"sourceProperties":["sourceProperties","sourceProperties"],"rollupProperty":{"parent":"parent","industryCategory":"INDUSTRY_CATEGORY_UNSPECIFIED","displayName":"displayName","timeZone":"timeZone","updateTime":"updateTime","serviceLevel":"SERVICE_LEVEL_UNSPECIFIED","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","propertyType":"PROPERTY_TYPE_UNSPECIFIED","name":"name","currencyCode":"currencyCode","account":"account"}}
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
        path='/v1alpha/properties:createRollupProperty',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_create_subproperty(client):
    """Test case for analyticsadmin_properties_create_subproperty

    
    """
    body = {"parent":"parent","subproperty":{"parent":"parent","industryCategory":"INDUSTRY_CATEGORY_UNSPECIFIED","displayName":"displayName","timeZone":"timeZone","updateTime":"updateTime","serviceLevel":"SERVICE_LEVEL_UNSPECIFIED","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","propertyType":"PROPERTY_TYPE_UNSPECIFIED","name":"name","currencyCode":"currencyCode","account":"account"},"subpropertyEventFilter":{"applyToProperty":"applyToProperty","filterClauses":[{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}},{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}}],"name":"name"}}
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
        path='/v1alpha/properties:createSubproperty',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_custom_dimensions_create(client):
    """Test case for analyticsadmin_properties_custom_dimensions_create

    
    """
    body = {"displayName":"displayName","scope":"DIMENSION_SCOPE_UNSPECIFIED","disallowAdsPersonalization":True,"name":"name","description":"description","parameterName":"parameterName"}
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
        path='/v1alpha/{parent}/customDimensions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_custom_dimensions_list(client):
    """Test case for analyticsadmin_properties_custom_dimensions_list

    
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
        path='/v1alpha/{parent}/customDimensions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_custom_metrics_archive(client):
    """Test case for analyticsadmin_properties_custom_metrics_archive

    
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
        path='/v1alpha/{namearchiv}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_custom_metrics_create(client):
    """Test case for analyticsadmin_properties_custom_metrics_create

    
    """
    body = {"displayName":"displayName","scope":"METRIC_SCOPE_UNSPECIFIED","name":"name","description":"description","restrictedMetricType":["RESTRICTED_METRIC_TYPE_UNSPECIFIED","RESTRICTED_METRIC_TYPE_UNSPECIFIED"],"parameterName":"parameterName","measurementUnit":"MEASUREMENT_UNIT_UNSPECIFIED"}
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
        path='/v1alpha/{parent}/customMetrics'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_custom_metrics_list(client):
    """Test case for analyticsadmin_properties_custom_metrics_list

    
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
        path='/v1alpha/{parent}/customMetrics'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_create(client):
    """Test case for analyticsadmin_properties_data_streams_create

    
    """
    body = {"webStreamData":{"firebaseAppId":"firebaseAppId","defaultUri":"defaultUri","measurementId":"measurementId"},"androidAppStreamData":{"firebaseAppId":"firebaseAppId","packageName":"packageName"},"createTime":"createTime","displayName":"displayName","name":"name","iosAppStreamData":{"firebaseAppId":"firebaseAppId","bundleId":"bundleId"},"updateTime":"updateTime","type":"DATA_STREAM_TYPE_UNSPECIFIED"}
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
        path='/v1alpha/{parent}/dataStreams'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_event_create_rules_create(client):
    """Test case for analyticsadmin_properties_data_streams_event_create_rules_create

    
    """
    body = {"parameterMutations":[{"parameter":"parameter","parameterValue":"parameterValue"},{"parameter":"parameter","parameterValue":"parameterValue"}],"destinationEvent":"destinationEvent","name":"name","eventConditions":[{"negated":True,"field":"field","comparisonType":"COMPARISON_TYPE_UNSPECIFIED","value":"value"},{"negated":True,"field":"field","comparisonType":"COMPARISON_TYPE_UNSPECIFIED","value":"value"}],"sourceCopyParameters":True}
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
        path='/v1alpha/{parent}/eventCreateRules'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_event_create_rules_list(client):
    """Test case for analyticsadmin_properties_data_streams_event_create_rules_list

    
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
        path='/v1alpha/{parent}/eventCreateRules'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_list(client):
    """Test case for analyticsadmin_properties_data_streams_list

    
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
        path='/v1alpha/{parent}/dataStreams'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_measurement_protocol_secrets_create(client):
    """Test case for analyticsadmin_properties_data_streams_measurement_protocol_secrets_create

    
    """
    body = {"secretValue":"secretValue","displayName":"displayName","name":"name"}
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
        path='/v1alpha/{parent}/measurementProtocolSecrets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_measurement_protocol_secrets_list(client):
    """Test case for analyticsadmin_properties_data_streams_measurement_protocol_secrets_list

    
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
        path='/v1alpha/{parent}/measurementProtocolSecrets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_s_kad_network_conversion_value_schema_create(client):
    """Test case for analyticsadmin_properties_data_streams_s_kad_network_conversion_value_schema_create

    
    """
    body = {"postbackWindowOne":{"postbackWindowSettingsEnabled":True,"conversionValues":[{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]},{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]}]},"postbackWindowThree":{"postbackWindowSettingsEnabled":True,"conversionValues":[{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]},{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]}]},"name":"name","applyConversionValues":True,"postbackWindowTwo":{"postbackWindowSettingsEnabled":True,"conversionValues":[{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]},{"displayName":"displayName","lockEnabled":True,"fineValue":7,"coarseValue":"COARSE_VALUE_UNSPECIFIED","eventMappings":[{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655},{"maxEventCount":"maxEventCount","maxEventValue":5.637376656633329,"eventName":"eventName","minEventCount":"minEventCount","minEventValue":2.3021358869347655}]}]}}
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
        path='/v1alpha/{parent}/sKAdNetworkConversionValueSchema'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_data_streams_s_kad_network_conversion_value_schema_list(client):
    """Test case for analyticsadmin_properties_data_streams_s_kad_network_conversion_value_schema_list

    
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
        path='/v1alpha/{parent}/sKAdNetworkConversionValueSchema'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_delete_connected_site_tag(client):
    """Test case for analyticsadmin_properties_delete_connected_site_tag

    
    """
    body = {"tagId":"tagId","property":"property"}
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
        path='/v1alpha/properties:deleteConnectedSiteTag',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_link_proposals_approve(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_link_proposals_approve

    
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
        path='/v1alpha/{nameapprov}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_link_proposals_cancel(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_link_proposals_cancel

    
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
        path='/v1alpha/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_link_proposals_create(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_link_proposals_create

    
    """
    body = {"costDataSharingEnabled":True,"linkProposalStatusDetails":{"linkProposalState":"LINK_PROPOSAL_STATE_UNSPECIFIED","linkProposalInitiatingProduct":"LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED","requestorEmail":"requestorEmail"},"campaignDataSharingEnabled":True,"advertiserDisplayName":"advertiserDisplayName","name":"name","validationEmail":"validationEmail","adsPersonalizationEnabled":True,"advertiserId":"advertiserId"}
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
        path='/v1alpha/{parent}/displayVideo360AdvertiserLinkProposals'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_link_proposals_list(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_link_proposals_list

    
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
        path='/v1alpha/{parent}/displayVideo360AdvertiserLinkProposals'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_links_create(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_links_create

    
    """
    body = {"costDataSharingEnabled":True,"campaignDataSharingEnabled":True,"advertiserDisplayName":"advertiserDisplayName","name":"name","adsPersonalizationEnabled":True,"advertiserId":"advertiserId"}
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
        path='/v1alpha/{parent}/displayVideo360AdvertiserLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_display_video360_advertiser_links_list(client):
    """Test case for analyticsadmin_properties_display_video360_advertiser_links_list

    
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
        path='/v1alpha/{parent}/displayVideo360AdvertiserLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_expanded_data_sets_create(client):
    """Test case for analyticsadmin_properties_expanded_data_sets_create

    
    """
    body = {"metricNames":["metricNames","metricNames"],"dimensionNames":["dimensionNames","dimensionNames"],"displayName":"displayName","name":"name","description":"description","dimensionFilterExpression":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"andGroup":{"filterExpressions":[null,null]}},"dataCollectionStartTime":"dataCollectionStartTime"}
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
        path='/v1alpha/{parent}/expandedDataSets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_expanded_data_sets_list(client):
    """Test case for analyticsadmin_properties_expanded_data_sets_list

    
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
        path='/v1alpha/{parent}/expandedDataSets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_fetch_automated_ga4_configuration_opt_out(client):
    """Test case for analyticsadmin_properties_fetch_automated_ga4_configuration_opt_out

    
    """
    body = {"property":"property"}
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
        path='/v1alpha/properties:fetchAutomatedGa4ConfigurationOptOut',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_fetch_connected_ga4_property(client):
    """Test case for analyticsadmin_properties_fetch_connected_ga4_property

    
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
                    ('property', '_property_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/properties:fetchConnectedGa4Property',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_firebase_links_create(client):
    """Test case for analyticsadmin_properties_firebase_links_create

    
    """
    body = {"createTime":"createTime","name":"name","project":"project"}
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
        path='/v1alpha/{parent}/firebaseLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_firebase_links_list(client):
    """Test case for analyticsadmin_properties_firebase_links_list

    
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
        path='/v1alpha/{parent}/firebaseLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_google_ads_links_create(client):
    """Test case for analyticsadmin_properties_google_ads_links_create

    
    """
    body = {"createTime":"createTime","customerId":"customerId","name":"name","updateTime":"updateTime","creatorEmailAddress":"creatorEmailAddress","canManageClients":True,"adsPersonalizationEnabled":True}
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
        path='/v1alpha/{parent}/googleAdsLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_google_ads_links_list(client):
    """Test case for analyticsadmin_properties_google_ads_links_list

    
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
        path='/v1alpha/{parent}/googleAdsLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_list(client):
    """Test case for analyticsadmin_properties_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_list_connected_site_tags(client):
    """Test case for analyticsadmin_properties_list_connected_site_tags

    
    """
    body = {"property":"property"}
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
        path='/v1alpha/properties:listConnectedSiteTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_rollup_property_source_links_create(client):
    """Test case for analyticsadmin_properties_rollup_property_source_links_create

    
    """
    body = {"name":"name","sourceProperty":"sourceProperty"}
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
        path='/v1alpha/{parent}/rollupPropertySourceLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_rollup_property_source_links_list(client):
    """Test case for analyticsadmin_properties_rollup_property_source_links_list

    
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
        path='/v1alpha/{parent}/rollupPropertySourceLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_run_access_report(client):
    """Test case for analyticsadmin_properties_run_access_report

    
    """
    body = {"dimensionFilter":{"accessFilter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"expandGroups":True,"offset":"offset","includeAllUsers":True,"dateRanges":[{"endDate":"endDate","startDate":"startDate"},{"endDate":"endDate","startDate":"startDate"}],"returnEntityQuota":True,"limit":"limit","metricFilter":{"accessFilter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115},"toValue":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":0.8008281904610115}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"timeZone":"timeZone","metrics":[{"metricName":"metricName"},{"metricName":"metricName"}],"dimensions":[{"dimensionName":"dimensionName"},{"dimensionName":"dimensionName"}],"orderBys":[{"metric":{"metricName":"metricName"},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}
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
        path='/v1alpha/{entityrun_access_repor}'.format(entity='entity_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_search_ads360_links_create(client):
    """Test case for analyticsadmin_properties_search_ads360_links_create

    
    """
    body = {"costDataSharingEnabled":True,"campaignDataSharingEnabled":True,"advertiserDisplayName":"advertiserDisplayName","siteStatsSharingEnabled":True,"name":"name","adsPersonalizationEnabled":True,"advertiserId":"advertiserId"}
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
        path='/v1alpha/{parent}/searchAds360Links'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_search_ads360_links_list(client):
    """Test case for analyticsadmin_properties_search_ads360_links_list

    
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
        path='/v1alpha/{parent}/searchAds360Links'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_set_automated_ga4_configuration_opt_out(client):
    """Test case for analyticsadmin_properties_set_automated_ga4_configuration_opt_out

    
    """
    body = {"optOut":True,"property":"property"}
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
        path='/v1alpha/properties:setAutomatedGa4ConfigurationOptOut',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_subproperty_event_filters_create(client):
    """Test case for analyticsadmin_properties_subproperty_event_filters_create

    
    """
    body = {"applyToProperty":"applyToProperty","filterClauses":[{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}},{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}}],"name":"name"}
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
        path='/v1alpha/{parent}/subpropertyEventFilters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_subproperty_event_filters_delete(client):
    """Test case for analyticsadmin_properties_subproperty_event_filters_delete

    
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

async def test_analyticsadmin_properties_subproperty_event_filters_get(client):
    """Test case for analyticsadmin_properties_subproperty_event_filters_get

    
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

async def test_analyticsadmin_properties_subproperty_event_filters_list(client):
    """Test case for analyticsadmin_properties_subproperty_event_filters_list

    
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
        path='/v1alpha/{parent}/subpropertyEventFilters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_properties_subproperty_event_filters_patch(client):
    """Test case for analyticsadmin_properties_subproperty_event_filters_patch

    
    """
    body = {"applyToProperty":"applyToProperty","filterClauses":[{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}},{"filterClauseType":"FILTER_CLAUSE_TYPE_UNSPECIFIED","filterExpression":{"orGroup":{"filterExpressions":[null,null]},"filterCondition":{"fieldName":"fieldName","stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"},"nullFilter":True}}}],"name":"name"}
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

