# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report import Report
from openapi_server.models.report_request import ReportRequest


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_reports_generate(client):
    """Test case for doubleclicksearch_reports_generate

    
    """
    body = {"maxRowsPerFile":0,"startRow":1,"columns":[{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}],"downloadFormat":"downloadFormat","orderBy":[{"sortOrder":"sortOrder","column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}},{"sortOrder":"sortOrder","column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}}],"statisticsCurrency":"statisticsCurrency","filters":[{"values":["",""],"column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},"operator":"operator"},{"values":["",""],"column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},"operator":"operator"}],"reportType":"reportType","verifySingleTimeZone":True,"includeDeletedEntities":True,"rowCount":6,"includeRemovedEntities":True,"reportScope":{"keywordId":"keywordId","adId":"adId","campaignId":"campaignId","agencyId":"agencyId","engineAccountId":"engineAccountId","adGroupId":"adGroupId","advertiserId":"advertiserId"},"timeRange":{"changedMetricsSinceTimestamp":"changedMetricsSinceTimestamp","endDate":"endDate","changedAttributesSinceTimestamp":"changedAttributesSinceTimestamp","startDate":"startDate"}}
    params = [('$.xgafv', 'xgafv_example'),
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
        path='/doubleclicksearch/v2/reports/generate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_reports_get(client):
    """Test case for doubleclicksearch_reports_get

    
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
        path='/doubleclicksearch/v2/reports/{report_id}'.format(report_id='report_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_reports_get_file(client):
    """Test case for doubleclicksearch_reports_get_file

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclicksearch/v2/reports/{report_id}/files/{report_fragment}'.format(report_id='report_id_example', report_fragment=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_reports_get_id_mapping_file(client):
    """Test case for doubleclicksearch_reports_get_id_mapping_file

    
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
        path='/doubleclicksearch/v2/agency/{agency_id}/advertiser/{advertiser_id}/idmapping'.format(agency_id='agency_id_example', advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_reports_request(client):
    """Test case for doubleclicksearch_reports_request

    
    """
    body = {"maxRowsPerFile":0,"startRow":1,"columns":[{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}],"downloadFormat":"downloadFormat","orderBy":[{"sortOrder":"sortOrder","column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}},{"sortOrder":"sortOrder","column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"}}],"statisticsCurrency":"statisticsCurrency","filters":[{"values":["",""],"column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},"operator":"operator"},{"values":["",""],"column":{"productReportPerspective":"productReportPerspective","savedColumnName":"savedColumnName","headerText":"headerText","endDate":"endDate","customDimensionName":"customDimensionName","groupByColumn":True,"customMetricName":"customMetricName","startDate":"startDate","columnName":"columnName","platformSource":"platformSource"},"operator":"operator"}],"reportType":"reportType","verifySingleTimeZone":True,"includeDeletedEntities":True,"rowCount":6,"includeRemovedEntities":True,"reportScope":{"keywordId":"keywordId","adId":"adId","campaignId":"campaignId","agencyId":"agencyId","engineAccountId":"engineAccountId","adGroupId":"adGroupId","advertiserId":"advertiserId"},"timeRange":{"changedMetricsSinceTimestamp":"changedMetricsSinceTimestamp","endDate":"endDate","changedAttributesSinceTimestamp":"changedAttributesSinceTimestamp","startDate":"startDate"}}
    params = [('$.xgafv', 'xgafv_example'),
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
        path='/doubleclicksearch/v2/reports',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

