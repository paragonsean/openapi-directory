# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.jql_function_precomputation_update_request_bean import JqlFunctionPrecomputationUpdateRequestBean
from openapi_server.models.page_bean_jql_function_precomputation_bean import PageBeanJqlFunctionPrecomputationBean


pytestmark = pytest.mark.asyncio

async def test_get_precomputations(client):
    """Test case for get_precomputations

    Get precomputations (apps)
    """
    params = [('functionKey', ['function_key_example']),
                    ('startAt', 0),
                    ('maxResults', 100),
                    ('orderBy', 'order_by_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/jql/function/computation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_precomputations(client):
    """Test case for update_precomputations

    Update precomputations (apps)
    """
    body = {"values":[{"id":0,"value":"value"},{"id":0,"value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/function/computation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

