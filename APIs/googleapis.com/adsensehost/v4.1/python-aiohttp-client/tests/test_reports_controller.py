# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report import Report


pytestmark = pytest.mark.asyncio

async def test_adsensehost_reports_generate(client):
    """Test case for adsensehost_reports_generate

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('dimension', ['dimension_example']),
                    ('filter', ['filter_example']),
                    ('locale', 'locale_example'),
                    ('maxResults', 56),
                    ('metric', ['metric_example']),
                    ('sort', ['sort_example']),
                    ('startIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

