# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.demographics_dependent_model import DemographicsDependentModel
from openapi_server.models.demographics_dependent_with_id_model import DemographicsDependentWithIdModel
from openapi_server.models.demographics_dependents_model import DemographicsDependentsModel
from openapi_server.models.demographics_model import DemographicsModel
from openapi_server.models.demographics_with_id_model import DemographicsWithIdModel


pytestmark = pytest.mark.asyncio

async def test_demographics_delete_dependent_by_demographicid_id(client):
    """Test case for demographics_delete_dependent_by_demographicid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Demographics/{demographic_id}/Dependents/{id}'.format(demographic_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demographics_get_by_id(client):
    """Test case for demographics_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Demographics/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demographics_get_demographics_by_fact_finder_id_by_factfinderid(client):
    """Test case for demographics_get_demographics_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Demographics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demographics_get_dependent_by_demographicid_id(client):
    """Test case for demographics_get_dependent_by_demographicid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Demographics/{demographic_id}/Dependents/{id}'.format(demographic_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demographics_get_dependents_by_demographicid(client):
    """Test case for demographics_get_dependents_by_demographicid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Demographics/{demographic_id}/Dependents'.format(demographic_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_demographics_post_by_demographicid_model(client):
    """Test case for demographics_post_by_demographicid_model

    
    """
    model = {"firstName":"firstName","lastName":"lastName","relationship":"Son","birthDate":"2000-01-23T04:56:07.000+00:00","dependentOf":"Client","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Demographics/{demographic_id}/Dependents'.format(demographic_id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_demographics_post_by_model(client):
    """Test case for demographics_post_by_model

    
    """
    model = {"factFinderId":0,"city":"city","jointAnalysis":True,"head1":{"alreadyRetired":True,"firstName":"firstName","lastName":"lastName","taxFilingStatus":1,"gender":"Male","birthDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"},"externalSourceId":"externalSourceId","head2":{"alreadyRetired":True,"firstName":"firstName","lastName":"lastName","taxFilingStatus":1,"gender":"Male","birthDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"},"state":6,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Demographics',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_demographics_put_by_demographicid_id_model(client):
    """Test case for demographics_put_by_demographicid_id_model

    
    """
    model = {"firstName":"firstName","lastName":"lastName","relationship":"Son","birthDate":"2000-01-23T04:56:07.000+00:00","dependentOf":"Client","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Demographics/{demographic_id}/Dependents/{id}'.format(demographic_id=56, id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_demographics_put_by_id_model(client):
    """Test case for demographics_put_by_id_model

    
    """
    model = {"factFinderId":0,"city":"city","jointAnalysis":True,"head1":{"alreadyRetired":True,"firstName":"firstName","lastName":"lastName","taxFilingStatus":1,"gender":"Male","birthDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"},"externalSourceId":"externalSourceId","head2":{"alreadyRetired":True,"firstName":"firstName","lastName":"lastName","taxFilingStatus":1,"gender":"Male","birthDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"},"state":6,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Demographics/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

