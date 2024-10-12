# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_analytics_reports_query(client):
    """Test case for youtube_analytics_reports_query

    
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
                    ('currency', 'currency_example'),
                    ('dimensions', 'dimensions_example'),
                    ('endDate', 'end_date_example'),
                    ('filters', 'filters_example'),
                    ('ids', 'ids_example'),
                    ('includeHistoricalChannelData', True),
                    ('maxResults', 56),
                    ('metrics', 'metrics_example'),
                    ('sort', 'sort_example'),
                    ('startDate', 'start_date_example'),
                    ('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

