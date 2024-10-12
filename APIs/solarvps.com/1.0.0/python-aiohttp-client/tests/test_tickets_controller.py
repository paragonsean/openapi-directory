# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_tickets_department_add_post(client):
    """Test case for tickets_department_add_post

    Open ticket with desired department
    """
    params = [('subject', 'subject_example'),
                    ('contents', 'contents_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tickets/{department}/add'.format(department='department_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tickets_get(client):
    """Test case for tickets_get

    View all your tickets
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tickets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tickets_ticket_id_get(client):
    """Test case for tickets_ticket_id_get

    View details on a specific ticket
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tickets/{ticket_id}'.format(ticket_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tickets_ticketid_update_post(client):
    """Test case for tickets_ticketid_update_post

    Post a reply to a ticket
    """
    params = [('contents', 'contents_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tickets/{ticketid}/update'.format(ticketid=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

