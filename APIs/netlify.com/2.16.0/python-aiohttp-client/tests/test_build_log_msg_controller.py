# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_log_msg import BuildLogMsg
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_update_site_build_log(client):
    """Test case for update_site_build_log

    
    """
    msg = openapi_server.BuildLogMsg()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/builds/{build_id}/log'.format(build_id='build_id_example'),
        headers=headers,
        json=msg,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

