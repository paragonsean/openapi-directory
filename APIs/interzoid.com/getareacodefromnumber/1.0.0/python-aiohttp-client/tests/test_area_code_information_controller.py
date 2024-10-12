# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getareacodefromnumber200_response import Getareacodefromnumber200Response


pytestmark = pytest.mark.asyncio

async def test_getareacodefromnumber(client):
    """Test case for getareacodefromnumber

    Gets area code information from a telephone number
    """
    params = [('license', 'license_example'),
                    ('number', 'number_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getareacodefromnumber',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

