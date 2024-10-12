# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_information_model import ServiceInformationModel


pytestmark = pytest.mark.asyncio

async def test_fact_finder_service_information_get(client):
    """Test case for fact_finder_service_information_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/ServiceInformation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

