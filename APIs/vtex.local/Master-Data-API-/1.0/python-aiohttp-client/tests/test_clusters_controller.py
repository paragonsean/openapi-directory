# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_validatedocumentbyclusters(client):
    """Test case for validatedocumentbyclusters

    Validate document by clusters
    """
    body = [
    {
        "name": "male",        
        "rule": "gender=male"
    },
    {
        "name": "complex",
        "rule": "((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"
    },    
    {
        "name": "complex2",
        "rule": "((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"
    },
    {
        "name": "createdIn",
        "rule": "createdIn between 2015-10-28 AND 2015-10-30"
    }
]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dataentities/{data_entity_name}/documents/{id}/clusters'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

