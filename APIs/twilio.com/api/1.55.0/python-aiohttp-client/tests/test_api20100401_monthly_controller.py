# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_usage_record_monthly_response import ListUsageRecordMonthlyResponse
from openapi_server.models.usage_record_monthly_enum_category import UsageRecordMonthlyEnumCategory


pytestmark = pytest.mark.asyncio

async def test_list_usage_record_monthly(client):
    """Test case for list_usage_record_monthly

    
    """
    params = [('Category', openapi_server.UsageRecordMonthlyEnumCategory()),
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
        path='/2010-04-01/Accounts/{account_sid}/Usage/Records/Monthly.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

