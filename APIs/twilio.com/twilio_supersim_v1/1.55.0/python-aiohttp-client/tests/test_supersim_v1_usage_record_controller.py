# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_usage_record_response import ListUsageRecordResponse
from openapi_server.models.usage_record_enum_granularity import UsageRecordEnumGranularity
from openapi_server.models.usage_record_enum_group import UsageRecordEnumGroup


pytestmark = pytest.mark.asyncio

async def test_list_usage_record(client):
    """Test case for list_usage_record

    
    """
    params = [('Sim', 'sim_example'),
                    ('Fleet', 'fleet_example'),
                    ('Network', 'network_example'),
                    ('IsoCountry', 'iso_country_example'),
                    ('Group', openapi_server.UsageRecordEnumGroup()),
                    ('Granularity', openapi_server.UsageRecordEnumGranularity()),
                    ('StartTime', '2013-10-20T19:20:30+01:00'),
                    ('EndTime', '2013-10-20T19:20:30+01:00'),
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

