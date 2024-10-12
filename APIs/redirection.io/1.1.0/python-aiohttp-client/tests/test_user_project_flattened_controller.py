# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_project_flattened_read import UserProjectFlattenedRead


pytestmark = pytest.mark.asyncio

async def test_get_user_project_flattened_item(client):
    """Test case for get_user_project_flattened_item

    Retrieves a UserProjectFlattened resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/user-project-flatteneds/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

