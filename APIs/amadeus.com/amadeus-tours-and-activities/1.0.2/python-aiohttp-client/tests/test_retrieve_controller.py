# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.successful_search1 import SuccessfulSearch1


pytestmark = pytest.mark.asyncio

async def test_g_et_activity(client):
    """Test case for g_et_activity

    Retrieve one activity by its id
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shopping/activities/{activity_id}'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

