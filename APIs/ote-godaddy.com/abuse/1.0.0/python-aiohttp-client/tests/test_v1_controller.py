# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.abuse_ticket import AbuseTicket
from openapi_server.models.abuse_ticket_create import AbuseTicketCreate
from openapi_server.models.abuse_ticket_id import AbuseTicketId
from openapi_server.models.abuse_ticket_list import AbuseTicketList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_create_ticket(client):
    """Test case for create_ticket

    Create a new abuse ticket
    """
    body = {"proxy":"proxy","infoUrl":"http://example.com/aeiou","intentional":False,"source":"source","type":"A_RECORD","info":"info","target":"target"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/abuse/tickets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ticket_info(client):
    """Test case for get_ticket_info

    Return the abuse ticket data for a given ticket id
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/abuse/tickets/{ticket_id}'.format(ticket_id='ticket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tickets(client):
    """Test case for get_tickets

    List all abuse tickets ids that match user provided filters
    """
    params = [('type', 'type_example'),
                    ('closed', False),
                    ('sourceDomainOrIp', 'source_domain_or_ip_example'),
                    ('target', 'target_example'),
                    ('createdStart', 'created_start_example'),
                    ('createdEnd', 'created_end_example'),
                    ('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/abuse/tickets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

