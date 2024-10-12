# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_v1_statistics_consolidated_0(client):
    """Test case for v1_statistics_consolidated_0

    /v1/Statistics/consolidated
    """
    params = [('DeviceToken', ''),
                    ('StartDate', '2021-01-18'),
                    ('EndDate', '2021-03-18'),
                    ('Tag', ''),
                    ('InstanceId', ''),
                    ('AppId', ''),
                    ('CompanyId', '')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Statistics/consolidated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_statistics_consolidated_daily_0(client):
    """Test case for v1_statistics_consolidated_daily_0

    /v1/Statistics/consolidated/daily
    """
    params = [('DeviceToken', ''),
                    ('StartDate', '2021-01-17'),
                    ('EndDate', '2021-01-18'),
                    ('Tag', ''),
                    ('InstanceId', ''),
                    ('AppId', ''),
                    ('CompanyId', '')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Statistics/consolidated/daily',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

