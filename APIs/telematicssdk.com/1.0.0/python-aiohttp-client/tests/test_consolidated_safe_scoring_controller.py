# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v1_scorings_consolidated_daily200_response import V1ScoringsConsolidatedDaily200Response


pytestmark = pytest.mark.asyncio

async def test_v1_scorings_consolidated_0(client):
    """Test case for v1_scorings_consolidated_0

    /v1/Scorings/consolidated
    """
    params = [('DeviceToken', ''),
                    ('StartDate', '2021-01-17T01:04:22.840Z'),
                    ('EndDate', '2021-01-18T01:04:22.840Z'),
                    ('Tag', ''),
                    ('InstanceId', ''),
                    ('AppId', ''),
                    ('CompanyId', '')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Scorings/consolidated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_scorings_consolidated_daily_0(client):
    """Test case for v1_scorings_consolidated_daily_0

    /v1/Scorings/consolidated/daily
    """
    params = [('DeviceToken', ''),
                    ('StartDate', '2021-01-17T01:04:22.840Z'),
                    ('EndDate', '2021-01-18T01:04:22.840Z'),
                    ('Tag', ''),
                    ('InstanceId', ''),
                    ('AppId', ''),
                    ('CompanyId', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Scorings/consolidated/daily',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

