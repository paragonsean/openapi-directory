# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.performance_report_list import PerformanceReportList


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_performance_report_list(client):
    """Test case for adexchangebuyer_performance_report_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('accountId', 'account_id_example'),
                    ('endDateTime', 'end_date_time_example'),
                    ('startDateTime', 'start_date_time_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/performancereport',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

