# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.frequency_type_model import FrequencyTypeModel
from openapi_server.models.frequency_types_model import FrequencyTypesModel


pytestmark = pytest.mark.asyncio

async def test_frequency_types_get_by_entity_country(client):
    """Test case for frequency_types_get_by_entity_country

    
    """
    params = [('entity', 'entity_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FrequencyTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_frequency_types_get_by_id(client):
    """Test case for frequency_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FrequencyTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

