# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_multi_daily_metrics_time_series_response import FetchMultiDailyMetricsTimeSeriesResponse
from openapi_server.models.get_daily_metrics_time_series_response import GetDailyMetricsTimeSeriesResponse
from openapi_server.models.list_search_keyword_impressions_monthly_response import ListSearchKeywordImpressionsMonthlyResponse


pytestmark = pytest.mark.asyncio

async def test_businessprofileperformance_locations_fetch_multi_daily_metrics_time_series(client):
    """Test case for businessprofileperformance_locations_fetch_multi_daily_metrics_time_series

    
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
                    ('dailyMetrics', ['daily_metrics_example']),
                    ('dailyRange.endDate.day', 56),
                    ('dailyRange.endDate.month', 56),
                    ('dailyRange.endDate.year', 56),
                    ('dailyRange.startDate.day', 56),
                    ('dailyRange.startDate.month', 56),
                    ('dailyRange.startDate.year', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{locationfetch_multi_daily_metrics_time_serie}'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_businessprofileperformance_locations_get_daily_metrics_time_series(client):
    """Test case for businessprofileperformance_locations_get_daily_metrics_time_series

    
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
                    ('dailyMetric', 'daily_metric_example'),
                    ('dailyRange.endDate.day', 56),
                    ('dailyRange.endDate.month', 56),
                    ('dailyRange.endDate.year', 56),
                    ('dailyRange.startDate.day', 56),
                    ('dailyRange.startDate.month', 56),
                    ('dailyRange.startDate.year', 56),
                    ('dailySubEntityType.dayOfWeek', 'daily_sub_entity_type_day_of_week_example'),
                    ('dailySubEntityType.timeOfDay.hours', 56),
                    ('dailySubEntityType.timeOfDay.minutes', 56),
                    ('dailySubEntityType.timeOfDay.nanos', 56),
                    ('dailySubEntityType.timeOfDay.seconds', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{nameget_daily_metrics_time_serie}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_businessprofileperformance_locations_searchkeywords_impressions_monthly_list(client):
    """Test case for businessprofileperformance_locations_searchkeywords_impressions_monthly_list

    
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
                    ('monthlyRange.endMonth.day', 56),
                    ('monthlyRange.endMonth.month', 56),
                    ('monthlyRange.endMonth.year', 56),
                    ('monthlyRange.startMonth.day', 56),
                    ('monthlyRange.startMonth.month', 56),
                    ('monthlyRange.startMonth.year', 56),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/searchkeywords/impressions/monthly'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

