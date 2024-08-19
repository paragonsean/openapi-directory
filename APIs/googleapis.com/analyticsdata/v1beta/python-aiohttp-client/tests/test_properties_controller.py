# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audience_export import AudienceExport
from openapi_server.models.batch_run_pivot_reports_request import BatchRunPivotReportsRequest
from openapi_server.models.batch_run_pivot_reports_response import BatchRunPivotReportsResponse
from openapi_server.models.batch_run_reports_request import BatchRunReportsRequest
from openapi_server.models.batch_run_reports_response import BatchRunReportsResponse
from openapi_server.models.check_compatibility_request import CheckCompatibilityRequest
from openapi_server.models.check_compatibility_response import CheckCompatibilityResponse
from openapi_server.models.list_audience_exports_response import ListAudienceExportsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.query_audience_export_request import QueryAudienceExportRequest
from openapi_server.models.query_audience_export_response import QueryAudienceExportResponse
from openapi_server.models.run_pivot_report_request import RunPivotReportRequest
from openapi_server.models.run_pivot_report_response import RunPivotReportResponse
from openapi_server.models.run_realtime_report_request import RunRealtimeReportRequest
from openapi_server.models.run_realtime_report_response import RunRealtimeReportResponse
from openapi_server.models.run_report_request import RunReportRequest
from openapi_server.models.run_report_response import RunReportResponse


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_audience_exports_create(client):
    """Test case for analyticsdata_properties_audience_exports_create

    
    """
    body = {"audience":"audience","percentageCompleted":6.027456183070403,"beginCreatingTime":"beginCreatingTime","audienceDisplayName":"audienceDisplayName","errorMessage":"errorMessage","name":"name","creationQuotaTokensCharged":0,"rowCount":1,"state":"STATE_UNSPECIFIED","dimensions":[{"dimensionName":"dimensionName"},{"dimensionName":"dimensionName"}]}
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
        path='/v1beta/{parent}/audienceExports'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_audience_exports_get(client):
    """Test case for analyticsdata_properties_audience_exports_get

    
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
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_audience_exports_list(client):
    """Test case for analyticsdata_properties_audience_exports_list

    
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
        path='/v1beta/{parent}/audienceExports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_audience_exports_query(client):
    """Test case for analyticsdata_properties_audience_exports_query

    
    """
    body = {"offset":"offset","limit":"limit"}
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
        path='/v1beta/{namequer}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_batch_run_pivot_reports(client):
    """Test case for analyticsdata_properties_batch_run_pivot_reports

    
    """
    body = {"requests":[{"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"keepEmptyRows":True,"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"pivots":[{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]},{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}]},{"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"keepEmptyRows":True,"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"pivots":[{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]},{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}]}]}
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
        path='/v1beta/{propertybatch_run_pivot_report}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_batch_run_reports(client):
    """Test case for analyticsdata_properties_batch_run_reports

    
    """
    body = {"requests":[{"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"offset":"offset","keepEmptyRows":True,"metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"limit":"limit","metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]},{"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"offset":"offset","keepEmptyRows":True,"metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"limit":"limit","metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}]}
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
        path='/v1beta/{propertybatch_run_report}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_check_compatibility(client):
    """Test case for analyticsdata_properties_check_compatibility

    
    """
    body = {"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"compatibilityFilter":"COMPATIBILITY_UNSPECIFIED","metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}]}
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
        path='/v1beta/{propertycheck_compatibilit}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_run_pivot_report(client):
    """Test case for analyticsdata_properties_run_pivot_report

    
    """
    body = {"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"keepEmptyRows":True,"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"pivots":[{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]},{"offset":"offset","fieldNames":["fieldNames","fieldNames"],"limit":"limit","metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}]}
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
        path='/v1beta/{propertyrun_pivot_repor}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_run_realtime_report(client):
    """Test case for analyticsdata_properties_run_realtime_report

    
    """
    body = {"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"minuteRanges":[{"endMinutesAgo":0,"startMinutesAgo":6,"name":"name"},{"endMinutesAgo":0,"startMinutesAgo":6,"name":"name"}],"limit":"limit","metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"returnPropertyQuota":True,"metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}
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
        path='/v1beta/{propertyrun_realtime_repor}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsdata_properties_run_report(client):
    """Test case for analyticsdata_properties_run_report

    
    """
    body = {"dimensionFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"cohortSpec":{"cohortReportSettings":{"accumulate":True},"cohortsRange":{"endOffset":0,"startOffset":6,"granularity":"GRANULARITY_UNSPECIFIED"},"cohorts":[{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"},{"dateRange":{"endDate":"endDate","name":"name","startDate":"startDate"},"name":"name","dimension":"dimension"}]},"offset":"offset","keepEmptyRows":True,"metricAggregations":["METRIC_AGGREGATION_UNSPECIFIED","METRIC_AGGREGATION_UNSPECIFIED"],"dateRanges":[{"endDate":"endDate","name":"name","startDate":"startDate"},{"endDate":"endDate","name":"name","startDate":"startDate"}],"limit":"limit","metricFilter":{"filter":{"fieldName":"fieldName","inListFilter":{"caseSensitive":True,"values":["values","values"]},"betweenFilter":{"fromValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452},"toValue":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"numericFilter":{"operation":"OPERATION_UNSPECIFIED","value":{"int64Value":"int64Value","doubleValue":1.4658129805029452}},"stringFilter":{"caseSensitive":True,"matchType":"MATCH_TYPE_UNSPECIFIED","value":"value"}},"orGroup":{"expressions":[null,null]},"andGroup":{"expressions":[null,null]}},"property":"property","returnPropertyQuota":True,"metrics":[{"expression":"expression","name":"name","invisible":True},{"expression":"expression","name":"name","invisible":True}],"currencyCode":"currencyCode","dimensions":[{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}},{"name":"name","dimensionExpression":{"concatenate":{"dimensionNames":["dimensionNames","dimensionNames"],"delimiter":"delimiter"},"upperCase":{"dimensionName":"dimensionName"},"lowerCase":{"dimensionName":"dimensionName"}}}],"orderBys":[{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True},{"metric":{"metricName":"metricName"},"pivot":{"metricName":"metricName","pivotSelections":[{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"},{"dimensionValue":"dimensionValue","dimensionName":"dimensionName"}]},"dimension":{"orderType":"ORDER_TYPE_UNSPECIFIED","dimensionName":"dimensionName"},"desc":True}]}
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
        path='/v1beta/{propertyrun_repor}'.format(_property='_property_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

