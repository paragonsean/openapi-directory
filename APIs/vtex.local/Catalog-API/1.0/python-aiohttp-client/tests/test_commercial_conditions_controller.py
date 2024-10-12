# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.array_with_information_of_all_the_commercial_conditions_inner import ArrayWithInformationOfAllTheCommercialConditionsInner
from openapi_server.models.get_commercial_conditions200_response import GetCommercialConditions200Response


pytestmark = pytest.mark.asyncio

async def test_get_all_commercial_conditions(client):
    """Test case for get_all_commercial_conditions

    Get all commercial conditions
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/commercialcondition/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commercial_conditions(client):
    """Test case for get_commercial_conditions

    Get commercial condition
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/commercialcondition/{commercial_condition_id}'.format(commercial_condition_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

