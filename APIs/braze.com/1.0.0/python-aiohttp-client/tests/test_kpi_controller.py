# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_daily_active_users_by_date_0(client):
    """Test case for daily_active_users_by_date_0

    Daily Active Users by Date
    """
    params = [('length', '10'),
                    ('ending_at', '2018-06-28T23:59:59-5:00'),
                    ('app_id', '{{app_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/kpi/dau/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_daily_new_users_by_date_0(client):
    """Test case for daily_new_users_by_date_0

    Daily New Users by Date
    """
    params = [('length', '14'),
                    ('ending_at', '2018-06-28T23:59:59-5:00'),
                    ('app_id', '{{app_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/kpi/new_users/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kp_is_for_daily_app_uninstalls_by_date_0(client):
    """Test case for kp_is_for_daily_app_uninstalls_by_date_0

    KPIs for Daily App Uninstalls by Date
    """
    params = [('length', '14'),
                    ('ending_at', '2018-06-28T23:59:59-5:00'),
                    ('app_id', '{{app_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/kpi/uninstalls/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monthly_active_users_for_last30_days_0(client):
    """Test case for monthly_active_users_for_last30_days_0

    Monthly Active Users for Last 30 Days
    """
    params = [('length', '7'),
                    ('ending_at', '2018-06-28T23:59:59-05:00'),
                    ('app_id', '{{app_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/kpi/mau/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

