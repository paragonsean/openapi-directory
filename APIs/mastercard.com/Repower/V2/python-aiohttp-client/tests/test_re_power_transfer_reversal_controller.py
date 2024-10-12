# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.repowerreversal11_wrapper import Repowerreversal11Wrapper
from openapi_server.models.repowerreversalrequest10_wrapper import Repowerreversalrequest10Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_repower_reversal_post2(client):
    """Test case for repower_reversal_post2

    
    """
    repower_reversal_request = openapi_server.Repowerreversalrequest10Wrapper()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/repower/v2/repowerreversal',
        headers=headers,
        json=repower_reversal_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

