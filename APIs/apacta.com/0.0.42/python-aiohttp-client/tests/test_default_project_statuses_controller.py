# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_default_project_statuses_error import AddDefaultProjectStatusesError
from openapi_server.models.add_default_project_statuses_success import AddDefaultProjectStatusesSuccess


pytestmark = pytest.mark.asyncio

async def test_project_statuses_add_default_post(client):
    """Test case for project_statuses_add_default_post

    Add default project statuses to company
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project_statuses/add_default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

