# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_entities_model import BusinessEntitiesModel
from openapi_server.models.business_entity_model import BusinessEntityModel


pytestmark = pytest.mark.asyncio

async def test_business_entities_get_by_id_planid(client):
    """Test case for business_entities_get_by_id_planid

    Retrieve a business entity
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/BusinessEntities/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_business_entities_get_by_planid(client):
    """Test case for business_entities_get_by_planid

    Retrieve business entities
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/BusinessEntities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

