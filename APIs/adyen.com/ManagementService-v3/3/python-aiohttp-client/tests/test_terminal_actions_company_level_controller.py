# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.external_terminal_action import ExternalTerminalAction
from openapi_server.models.list_external_terminal_actions_response import ListExternalTerminalActionsResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_actions(client):
    """Test case for get_companies_company_id_terminal_actions

    Get a list of terminal actions
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('status', 'status_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalActions'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_actions_action_id(client):
    """Test case for get_companies_company_id_terminal_actions_action_id

    Get terminal action
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalActions/{action_id}'.format(company_id='company_id_example', action_id='action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

