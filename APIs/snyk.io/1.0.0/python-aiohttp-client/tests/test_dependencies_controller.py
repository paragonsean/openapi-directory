# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_all_dependencies200_response import ListAllDependencies200Response
from openapi_server.models.list_all_dependencies_request import ListAllDependenciesRequest


pytestmark = pytest.mark.asyncio

async def test_list_all_dependencies(client):
    """Test case for list_all_dependencies

    List all dependencies
    """
    body = openapi_server.ListAllDependenciesRequest()
    params = [('sortBy', dependency),
                    ('order', asc),
                    ('page', 1),
                    ('perPage', 20)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/dependencies'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

