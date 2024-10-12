# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.ticket_counts_detailed_entity import TicketCountsDetailedEntity
from openapi_server.models.ticket_counts_entity import TicketCountsEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_detailed_ticket_counts(client):
    """Test case for fetch_all_detailed_ticket_counts

    Find all detailed ticket counts for one event
    """
    params = [('from_date', '2013-10-20'),
                    ('to_date', '2013-10-20'),
                    ('show_ignored', False),
                    ('show_not_approved', False),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/ticket-counts/detailed'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_ticket_counts(client):
    """Test case for fetch_all_ticket_counts

    Find all ticket counts for one event
    """
    params = [('from_date', '2013-10-20'),
                    ('to_date', '2013-10-20'),
                    ('show_ignored', False),
                    ('show_not_approved', False),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/ticket-counts'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_detailed_ticket_count(client):
    """Test case for fetch_one_detailed_ticket_count

    Get one detailed ticket count by ID
    """
    params = [('show_ignored', False)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/ticket-counts/detailed/{ticket_count_id}'.format(event_id=56, ticket_count_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_ticket_count(client):
    """Test case for fetch_one_ticket_count

    Get one ticket count by ID
    """
    params = [('show_ignored', False)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/ticket-counts/{ticket_count_id}'.format(event_id=56, ticket_count_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

