# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_ticket_messages import GetTicketMessages
from openapi_server.models.get_tickets import GetTickets
from openapi_server.models.new_ticket import NewTicket
from openapi_server.models.new_ticket_message import NewTicketMessage
from openapi_server.models.ticket_status import TicketStatus


pytestmark = pytest.mark.asyncio

async def test_ticket_post(client):
    """Test case for ticket_post

    Creates a new trouble ticket
    """
    new_ticket = {"orderId":"orderId","description":"description","from":"from","body":"body","message":{"visibility":"visibility","body":"body"},"type":"type","customer":{"phoneNumber":"phoneNumber","name":"name"}}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/ticket',
        headers=headers,
        json=new_ticket,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ticket_ticket_id_message_post(client):
    """Test case for ticket_ticket_id_message_post

    Add new message to trouble ticket
    """
    message = {"visibility":"visibility","body":"body"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/ticket/{ticket_id}/message'.format(ticket_id='ticket_id_example'),
        headers=headers,
        json=message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ticket_ticket_id_messages_get(client):
    """Test case for ticket_ticket_id_messages_get

    Get trouble ticket messages
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/ticket/{ticket_id}/messages'.format(ticket_id='ticket_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ticket_ticket_id_status_put(client):
    """Test case for ticket_ticket_id_status_put

    Update trouble ticket status
    """
    body = {"ticketStatus":"ticketStatus"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/ticket/{ticket_id}/status'.format(ticket_id='ticket_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tickets_get(client):
    """Test case for tickets_get

    Get customers trouble tickets
    """
    params = [('status', 'status_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/tickets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

