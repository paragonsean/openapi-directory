# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.income_model import IncomeModel
from openapi_server.models.income_with_id_model import IncomeWithIdModel
from openapi_server.models.incomes_model import IncomesModel


pytestmark = pytest.mark.asyncio

async def test_incomes_delete_by_id(client):
    """Test case for incomes_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Incomes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_incomes_get_by_id(client):
    """Test case for incomes_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Incomes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_incomes_get_incomes_by_fact_finder_id_by_factfinderid(client):
    """Test case for incomes_get_incomes_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Incomes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_incomes_post_by_model(client):
    """Test case for incomes_post_by_model

    
    """
    model = {"incomeTypeId":1,"owner":"Client","factFinderId":6,"endDate":"2000-01-23T04:56:07.000+00:00","description":"description","annualAmount":0.8008281904610115,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Incomes',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_incomes_put_by_id_model(client):
    """Test case for incomes_put_by_id_model

    
    """
    model = {"incomeTypeId":1,"owner":"Client","factFinderId":6,"endDate":"2000-01-23T04:56:07.000+00:00","description":"description","annualAmount":0.8008281904610115,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Incomes/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

