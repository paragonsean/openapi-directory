# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.statements_view_model_item import StatementsViewModelItem
from openapi_server.models.statements_view_model_search_result import StatementsViewModelSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_writtenstatements_statements_date_uin_get(client):
    """Test case for api_writtenstatements_statements_date_uin_get

    Returns a written statemnet
    """
    params = [('expandMember', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenstatements/statements/{_date}/{uin}'.format(_date='2013-10-20T19:20:30+01:00', uin='uin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_writtenstatements_statements_get(client):
    """Test case for api_writtenstatements_statements_get

    Returns a list of written statements
    """
    params = [('madeWhenFrom', '2013-10-20T19:20:30+01:00'),
                    ('madeWhenTo', '2013-10-20T19:20:30+01:00'),
                    ('searchTerm', 'search_term_example'),
                    ('uIN', 'u_in_example'),
                    ('answeringBodies', [56]),
                    ('members', [56]),
                    ('house', openapi_server.HouseEnum()),
                    ('skip', 56),
                    ('take', 56),
                    ('expandMember', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenstatements/statements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_writtenstatements_statements_id_get(client):
    """Test case for api_writtenstatements_statements_id_get

    Returns a written statement
    """
    params = [('expandMember', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenstatements/statements/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

