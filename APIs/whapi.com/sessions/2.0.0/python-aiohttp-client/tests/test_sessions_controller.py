# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.login_request import LoginRequest
from openapi_server.models.logoutresponse import Logoutresponse
from openapi_server.models.service_ticket import ServiceTicket
from openapi_server.models.session import Session
from openapi_server.models.sessions_errors import SessionsErrors
from openapi_server.models.ticketvalidityresponse import Ticketvalidityresponse


pytestmark = pytest.mark.asyncio

async def test_get_service_ticket(client):
    """Test case for get_service_ticket

    Obtains a one-time Service Ticket that can be used to access other William Hill services.
    """
    params = [('languageAsPerTerritory', 'true'),
                    ('target', 'target_example'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sessions/tickets/{tgt}/serviceTicket'.format(tgt='tgt_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_in(client):
    """Test case for log_in

    Logs in a customer and obtains an authentication ticket.
    """
    login = openapi_server.LoginRequest()
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/sessions/tickets',
        headers=headers,
        json=login,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_out(client):
    """Test case for log_out

    Log out a customer.
    """
    params = [('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/sessions/tickets/{tgt}'.format(tgt='tgt_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_session(client):
    """Test case for validate_session

    Checks the validity of a session ticket.
    """
    params = [('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sessions/tickets/{tgt}'.format(tgt='tgt_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

