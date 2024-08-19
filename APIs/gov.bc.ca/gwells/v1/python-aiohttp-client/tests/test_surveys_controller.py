# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.survey import Survey


pytestmark = pytest.mark.asyncio

async def test_surveys_list(client):
    """Test case for surveys_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/surveys/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

