# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bet_delayed import BetDelayed
from openapi_server.models.bet_history_response import BetHistoryResponse
from openapi_server.models.bet_placed import BetPlaced
from openapi_server.models.bet_slip_request import BetSlipRequest
from openapi_server.models.bet_slip_response import BetSlipResponse
from openapi_server.models.cash_in_response import CashInResponse
from openapi_server.models.complex_bet_request_body import ComplexBetRequestBody
from openapi_server.models.errors import Errors
from openapi_server.models.free_bet_detail import FreeBetDetail
from openapi_server.models.single_bet_request_body import SingleBetRequestBody


pytestmark = pytest.mark.asyncio

async def test_cashin(client):
    """Test case for cashin

    Allows a trusted application to cash in a bet (take a return on a bet) on behalf of the customer
    """
    params = [('cashInValue', 3.4),
                    ('cashinBetDelayId', 'cashin_bet_delay_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='PUT',
        path='/v2/bets/{bet_id}/cashin'.format(bet_id='bet_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bet_history(client):
    """Test case for get_bet_history

    Retrieves the customer’s bet history.
    """
    params = [('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('page', 1),
                    ('pageSize', 100),
                    ('sort', 'transDateTime,asc'),
                    ('settled', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/bets/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_free_bets(client):
    """Test case for get_free_bets

    Returns available free bets
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/bets/freebets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_complex_bet(client):
    """Test case for place_complex_bet

    Places a multiple or a complex bet.
    """
    body = openapi_server.ComplexBetRequestBody()
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/bets/bet/complex',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_single_bet(client):
    """Test case for place_single_bet

    Places a single bet
    """
    body = openapi_server.SingleBetRequestBody()
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/bets/bet/single',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_betslip(client):
    """Test case for validate_betslip

    
    """
    body = openapi_server.BetSlipRequest()
    params = [('expanded', 'expanded_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/bets/betslips',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

