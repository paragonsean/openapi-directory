# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_terminals_request import AssignTerminalsRequest
from openapi_server.models.assign_terminals_response import AssignTerminalsResponse
from openapi_server.models.find_terminal_request import FindTerminalRequest
from openapi_server.models.find_terminal_response import FindTerminalResponse
from openapi_server.models.get_stores_under_account_request import GetStoresUnderAccountRequest
from openapi_server.models.get_stores_under_account_response import GetStoresUnderAccountResponse
from openapi_server.models.get_terminal_details_request import GetTerminalDetailsRequest
from openapi_server.models.get_terminal_details_response import GetTerminalDetailsResponse
from openapi_server.models.get_terminals_under_account_request import GetTerminalsUnderAccountRequest
from openapi_server.models.get_terminals_under_account_response import GetTerminalsUnderAccountResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_assign_terminals(client):
    """Test case for post_assign_terminals

    Assign terminals
    """
    body = {"merchantAccount":"merchantAccount","merchantInventory":True,"store":"store","companyAccount":"companyAccount","terminals":["terminals","terminals"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/postfmapi/terminal/v1/assignTerminals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_find_terminal(client):
    """Test case for post_find_terminal

    Get the account or store of a terminal
    """
    body = {"terminal":"terminal"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/postfmapi/terminal/v1/findTerminal',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_stores_under_account(client):
    """Test case for post_get_stores_under_account

    Get the stores of an account
    """
    body = {"merchantAccount":"merchantAccount","companyAccount":"companyAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/postfmapi/terminal/v1/getStoresUnderAccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_terminal_details(client):
    """Test case for post_get_terminal_details

    Get the details of a terminal
    """
    body = {"terminal":"terminal"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/postfmapi/terminal/v1/getTerminalDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_terminals_under_account(client):
    """Test case for post_get_terminals_under_account

    Get the list of terminals
    """
    body = {"merchantAccount":"merchantAccount","store":"store","companyAccount":"companyAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/postfmapi/terminal/v1/getTerminalsUnderAccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

