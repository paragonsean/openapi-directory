# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commission_list import CommissionList
from openapi_server.models.error import Error
from openapi_server.models.report_filter import ReportFilter


pytestmark = pytest.mark.asyncio

async def test_get_commissions(client):
    """Test case for get_commissions

    Returns a commission list of current client.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commissions_by_filter(client):
    """Test case for get_commissions_by_filter

    Returns a commission list of current client.
    """
    body = {"target_languages":["target_languages","target_languages"],"budget_code":"budget_code","source_languages":["source_languages","source_languages"],"date_to":"2000-01-23T04:56:07.000+00:00","users":[0,0],"date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/commissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

