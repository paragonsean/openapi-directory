# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_terminals_response import ListTerminalsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_reassignment_request import TerminalReassignmentRequest


pytestmark = pytest.mark.asyncio

async def test_get_terminals(client):
    """Test case for get_terminals

    Get a list of terminals
    """
    params = [('searchQuery', 'search_query_example'),
                    ('otpQuery', 'otp_query_example'),
                    ('countries', 'countries_example'),
                    ('merchantIds', 'merchant_ids_example'),
                    ('storeIds', 'store_ids_example'),
                    ('brandModels', 'brand_models_example'),
                    ('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/terminals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_terminals_terminal_id_reassign(client):
    """Test case for post_terminals_terminal_id_reassign

    Reassign a terminal
    """
    body = {"companyId":"companyId","merchantId":"merchantId","inventory":True,"storeId":"storeId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/terminals/{terminal_id}/reassign'.format(terminal_id='terminal_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

