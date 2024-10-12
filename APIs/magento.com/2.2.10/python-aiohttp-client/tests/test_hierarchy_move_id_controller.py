# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_company_hierarchy_v1_move_node_put_request import CompanyCompanyHierarchyV1MoveNodePutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_company_hierarchy_v1_move_node_put(client):
    """Test case for company_company_hierarchy_v1_move_node_put

    hierarchy/move/{id}
    """
    body = openapi_server.CompanyCompanyHierarchyV1MoveNodePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/hierarchy/move/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

