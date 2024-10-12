# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_credits_consumption_get_collection200_response import ApiCreditsConsumptionGetCollection200Response
from openapi_server.models.credits_consumption_get import CreditsConsumptionGet
from openapi_server.models.credits_consumption_jsonld_get import CreditsConsumptionJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_credits_consumption_get_collection(client):
    """Test case for api_credits_consumption_get_collection

    Retrieves the collection of CreditsConsumption resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/credits-consumption',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_credits_consumption_id_get(client):
    """Test case for api_credits_consumption_id_get

    Retrieves a CreditsConsumption resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/credits-consumption/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

