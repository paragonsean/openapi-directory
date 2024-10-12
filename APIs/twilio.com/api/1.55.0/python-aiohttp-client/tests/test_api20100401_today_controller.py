# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_usage_record_today_response import ListUsageRecordTodayResponse
from openapi_server.models.usage_record_today_enum_category import UsageRecordTodayEnumCategory


pytestmark = pytest.mark.asyncio

async def test_list_usage_record_today(client):
    """Test case for list_usage_record_today

    
    """
    params = [('Category', openapi_server.UsageRecordTodayEnumCategory()),
                    ('StartDate', '2013-10-20'),
                    ('EndDate', '2013-10-20'),
                    ('IncludeSubaccounts', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Records/Today.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

