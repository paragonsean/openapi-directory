# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_getreportstatusby_id(client):
    """Test case for getreportstatusby_id

    Get report status by ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/reportStatus/{report_id}'.format(report_id='report_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requestreportby_status(client):
    """Test case for requestreportby_status

    Retrieve Subscription report by Status
    """
    params = [('requesterEmail', 'user@vtex.com.br'),
                    ('status', 1)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/subscriptionsByStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requestreportbydate(client):
    """Test case for requestreportbydate

    Retrieve Subscription report by date
    """
    params = [('requesterEmail', 'user@vtex.com.br'),
                    ('beginDate', 20190101),
                    ('endDate', 20190701)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/subscriptionsByDate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requestreportbyorderdate(client):
    """Test case for requestreportbyorderdate

    Retrieve Subscription report by order date
    """
    params = [('requesterEmail', 'user@vtex.com.br'),
                    ('beginDate', 20190101),
                    ('endDate', 20190701)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/subscriptionsOrderByDate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requestreportbyschedule(client):
    """Test case for requestreportbyschedule

    Retrieve Subscription report by schedule
    """
    params = [('requesterEmail', 'user@vtex.com.br'),
                    ('beginDate', 20190101),
                    ('endDate', 20190701)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/subscriptionsScheduled',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requestreportbyupdate(client):
    """Test case for requestreportbyupdate

    Request report by update
    """
    params = [('requesterEmail', 'user@vtex.com.br'),
                    ('beginDate', 20190101),
                    ('endDate', 20190701)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/report/subscriptionsUpdated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

