# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project_status_types_get200_response import ProjectStatusTypesGet200Response


pytestmark = pytest.mark.asyncio

async def test_project_status_types_get(client):
    """Test case for project_status_types_get

    Get a list of project status types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project_status_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

