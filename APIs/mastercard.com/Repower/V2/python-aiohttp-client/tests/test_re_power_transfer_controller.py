# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.repower5_wrapper import Repower5Wrapper
from openapi_server.models.repowerrequest1_wrapper import Repowerrequest1Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_repower_post2(client):
    """Test case for repower_post2

    
    """
    repower_request = openapi_server.Repowerrequest1Wrapper()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/repower/v2/repower',
        headers=headers,
        json=repower_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

