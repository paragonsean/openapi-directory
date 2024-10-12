# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_app_sessions_by_time(client):
    """Test case for app_sessions_by_time

    App Sessions by Time
    """
    params = [('length', '14'),
                    ('unit', 'day'),
                    ('ending_at', '2018-06-28T23:59:59-5:00'),
                    ('app_id', '{{app_identifier}}'),
                    ('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/sessions/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaign_analytics(client):
    """Test case for campaign_analytics

    Campaign Analytics
    """
    params = [('campaign_id', '{{campaign_identifier}}'),
                    ('length', '7'),
                    ('ending_at', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaign_details(client):
    """Test case for campaign_details

    Campaign Details
    """
    params = [('campaign_id', '{{campaign_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaign_list(client):
    """Test case for campaign_list

    Campaign List
    """
    params = [('page', '0'),
                    ('include_archived', 'false'),
                    ('sort_direction', 'desc'),
                    ('last_edit.time[gt]', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_data_analytics_summary(client):
    """Test case for canvas_data_analytics_summary

    Canvas Data Analytics Summary
    """
    params = [('canvas_id', '{{canvas_id}}'),
                    ('ending_at', '2018-05-30T23:59:59-5:00'),
                    ('starting_at', '2018-05-28T23:59:59-5:00'),
                    ('length', '5'),
                    ('include_variant_breakdown', 'true'),
                    ('include_step_breakdown', 'true'),
                    ('include_deleted_step_data', 'true')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/data_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_data_series_analytics(client):
    """Test case for canvas_data_series_analytics

    Canvas Data Series Analytics
    """
    params = [('canvas_id', '{{canvas_id}}'),
                    ('ending_at', '2018-05-30T23:59:59-5:00'),
                    ('starting_at', '2018-05-28T23:59:59-5:00'),
                    ('length', '10'),
                    ('include_variant_breakdown', 'true'),
                    ('include_step_breakdown', 'true'),
                    ('include_deleted_step_data', 'true')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_details(client):
    """Test case for canvas_details

    Canvas Details
    """
    params = [('canvas_id', '{{canvas_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_list(client):
    """Test case for canvas_list

    Canvas List
    """
    params = [('page', '1'),
                    ('include_archived', 'false'),
                    ('sort_direction', 'desc'),
                    ('last_edit.time[gt]', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_events_analytics(client):
    """Test case for custom_events_analytics

    Custom Events Analytics
    """
    params = [('event', 'event_name'),
                    ('length', '24'),
                    ('unit', 'hour'),
                    ('ending_at', '2014-12-10T23:59:59-05:00'),
                    ('app_id', '{{app_identifier}}'),
                    ('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/events/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_events_list(client):
    """Test case for custom_events_list

    Custom Events List
    """
    params = [('page', '3')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/events/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_daily_active_users_by_date(client):
    """Test case for daily_active_users_by_date

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

async def test_daily_new_users_by_date(client):
    """Test case for daily_new_users_by_date

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

async def test_kp_is_for_daily_app_uninstalls_by_date(client):
    """Test case for kp_is_for_daily_app_uninstalls_by_date

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

async def test_monthly_active_users_for_last30_days(client):
    """Test case for monthly_active_users_for_last30_days

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


pytestmark = pytest.mark.asyncio

async def test_news_feed_card_analytics(client):
    """Test case for news_feed_card_analytics

    News Feed Card Analytics
    """
    params = [('card_id', '{{card_identifier}}'),
                    ('length', '14'),
                    ('unit', 'day'),
                    ('ending_at', '2018-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_feed_cards_details(client):
    """Test case for news_feed_cards_details

    News Feed Cards Details
    """
    params = [('card_id', '{{card_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_feed_cards_list(client):
    """Test case for news_feed_cards_list

    News Feed Cards List
    """
    params = [('page', '1'),
                    ('include_archived', 'true'),
                    ('sort_direction', 'desc')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_segment_analytics(client):
    """Test case for segment_analytics

    Segment Analytics
    """
    params = [('segment_id', '{{segment_identifier}}'),
                    ('length', '14'),
                    ('ending_at', '2018-06-27T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_segment_details(client):
    """Test case for segment_details

    Segment Details
    """
    params = [('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_segment_list(client):
    """Test case for segment_list

    Segment List
    """
    params = [('page', '1'),
                    ('sort_direction', 'desc')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_analytics(client):
    """Test case for send_analytics

    Send Analytics
    """
    params = [('campaign_id', '{{campaign_identifier}}'),
                    ('send_id', '{{send_identifier}}'),
                    ('length', '30'),
                    ('ending_at', '2014-12-10T23:59:59-05:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/sends/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

