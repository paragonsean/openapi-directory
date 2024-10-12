# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_usage_record_enum_granularity import AccountUsageRecordEnumGranularity
from openapi_server.models.list_account_usage_record_response import ListAccountUsageRecordResponse
from openapi_server.models.list_usage_record_response import ListUsageRecordResponse
from openapi_server.models.usage_record_enum_granularity import UsageRecordEnumGranularity


pytestmark = pytest.mark.asyncio

async def test_list_account_usage_record(client):
    """Test case for list_account_usage_record

    
    """
    params = [('End', '2013-10-20T19:20:30+01:00'),
                    ('Start', '2013-10-20T19:20:30+01:00'),
                    ('Granularity', openapi_server.AccountUsageRecordEnumGranularity()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/UsageRecords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_usage_record(client):
    """Test case for list_usage_record

    
    """
    params = [('End', '2013-10-20T19:20:30+01:00'),
                    ('Start', '2013-10-20T19:20:30+01:00'),
                    ('Granularity', openapi_server.UsageRecordEnumGranularity()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims/{sim_sid}/UsageRecords'.format(sim_sid='sim_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

