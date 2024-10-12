# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fact_finder_entity_model import FactFinderEntityModel
from openapi_server.models.fact_finder_model import FactFinderModel
from openapi_server.models.fact_finder_populatable_entity_model import FactFinderPopulatableEntityModel
from openapi_server.models.fact_finder_population_model import FactFinderPopulationModel
from openapi_server.models.fact_finder_snapshot_with_id_model import FactFinderSnapshotWithIdModel
from openapi_server.models.fact_finder_snapshots_model import FactFinderSnapshotsModel
from openapi_server.models.fact_finder_with_id_model import FactFinderWithIdModel


pytestmark = pytest.mark.asyncio

async def test_fact_finders_delete_by_id(client):
    """Test case for fact_finders_delete_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/FactFinders/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_finders_get_by_household_id_by_householdid(client):
    """Test case for fact_finders_get_by_household_id_by_householdid

    
    """
    params = [('householdId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FactFinders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_finders_get_by_id(client):
    """Test case for fact_finders_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FactFinders/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_finders_get_snapshots_by_factfinderid(client):
    """Test case for fact_finders_get_snapshots_by_factfinderid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FactFinders/{fact_finder_id}/Snapshots'.format(fact_finder_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_fact_finders_post_by_model(client):
    """Test case for fact_finders_post_by_model

    
    """
    model = {"householdId":171976544,"planLevel":"Level2","modules":["Demographics","Demographics"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/FactFinders',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_fact_finders_post_populate_by_model(client):
    """Test case for fact_finders_post_populate_by_model

    
    """
    model = {"householdId":171976544,"planLevel":"Level2","planId":1294386358,"modules":["Demographics","Demographics"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/FactFinders/Populate',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_finders_post_snapshots_by_factfinderid(client):
    """Test case for fact_finders_post_snapshots_by_factfinderid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/FactFinders/{fact_finder_id}/Snapshots'.format(fact_finder_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_fact_finders_put_by_id_model(client):
    """Test case for fact_finders_put_by_id_model

    
    """
    model = {"status":"New"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/FactFinders/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_fact_finders_put_populate_fact_finder_by_id_model(client):
    """Test case for fact_finders_put_populate_fact_finder_by_id_model

    
    """
    model = {"planId":171976544}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/FactFinders/{id}/Populate'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

