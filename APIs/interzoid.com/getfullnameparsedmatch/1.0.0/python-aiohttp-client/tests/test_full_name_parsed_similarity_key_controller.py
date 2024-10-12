# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getfullnameparsedmatch200_response import Getfullnameparsedmatch200Response


pytestmark = pytest.mark.asyncio

async def test_getfullnameparsedmatch(client):
    """Test case for getfullnameparsedmatch

    Gets a similarity key for matching purposes for parsed full name data
    """
    params = [('license', 'license_example'),
                    ('firstname', 'firstname_example'),
                    ('lastname', 'lastname_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getfullnameparsedmatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

