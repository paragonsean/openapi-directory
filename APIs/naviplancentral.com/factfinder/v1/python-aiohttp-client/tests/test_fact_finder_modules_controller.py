# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fact_finder_module_model import FactFinderModuleModel
from openapi_server.models.fact_finder_module_with_id_model import FactFinderModuleWithIdModel
from openapi_server.models.fact_finder_modules_model import FactFinderModulesModel


pytestmark = pytest.mark.asyncio

async def test_fact_finder_modules_get_by_factfinderid(client):
    """Test case for fact_finder_modules_get_by_factfinderid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FactFinders/{fact_finder_id}/Modules'.format(fact_finder_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_finder_modules_get_by_factfinderid_id(client):
    """Test case for fact_finder_modules_get_by_factfinderid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FactFinders/{fact_finder_id}/Modules/{id}'.format(fact_finder_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_fact_finder_modules_put_by_model_factfinderid_id(client):
    """Test case for fact_finder_modules_put_by_model_factfinderid_id

    
    """
    model = {"available":True,"moduleName":"Demographics","visited":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/FactFinders/{fact_finder_id}/Modules/{id}'.format(fact_finder_id=56, id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

