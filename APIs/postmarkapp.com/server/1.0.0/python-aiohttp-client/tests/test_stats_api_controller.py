# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_bounce_counts200_response import GetBounceCounts200Response
from openapi_server.models.get_outbound_open_counts200_response import GetOutboundOpenCounts200Response
from openapi_server.models.get_outbound_open_counts_by_email_client200_response import GetOutboundOpenCountsByEmailClient200Response
from openapi_server.models.get_outbound_open_counts_by_platform200_response import GetOutboundOpenCountsByPlatform200Response
from openapi_server.models.get_spam_complaints200_response import GetSpamComplaints200Response
from openapi_server.models.get_tracked_email_counts200_response import GetTrackedEmailCounts200Response
from openapi_server.models.outbound_overview_stats_response import OutboundOverviewStatsResponse
from openapi_server.models.sent_counts_response import SentCountsResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_get_bounce_counts(client):
    """Test case for get_bounce_counts

    Get bounce counts
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/bounces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_click_counts(client):
    """Test case for get_outbound_click_counts

    Get click counts
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/clicks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_click_counts_by_browser_family(client):
    """Test case for get_outbound_click_counts_by_browser_family

    Get browser usage by family
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/clicks/browserfamilies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_click_counts_by_location(client):
    """Test case for get_outbound_click_counts_by_location

    Get clicks by body location
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/clicks/location',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_click_counts_by_platform(client):
    """Test case for get_outbound_click_counts_by_platform

    Get browser plaform usage
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/clicks/platforms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_open_counts(client):
    """Test case for get_outbound_open_counts

    Get email open counts
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/opens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_open_counts_by_email_client(client):
    """Test case for get_outbound_open_counts_by_email_client

    Get email client usage
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/opens/emailclients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_open_counts_by_platform(client):
    """Test case for get_outbound_open_counts_by_platform

    Get email platform usage
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/opens/platforms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_overview_statistics(client):
    """Test case for get_outbound_overview_statistics

    Get outbound overview
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sent_counts(client):
    """Test case for get_sent_counts

    Get sent counts
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/sends',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spam_complaints(client):
    """Test case for get_spam_complaints

    Get spam complaints
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/spam',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tracked_email_counts(client):
    """Test case for get_tracked_email_counts

    Get tracked email counts
    """
    params = [('tag', 'tag_example'),
                    ('fromdate', '2013-10-20'),
                    ('todate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/stats/outbound/tracked',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

