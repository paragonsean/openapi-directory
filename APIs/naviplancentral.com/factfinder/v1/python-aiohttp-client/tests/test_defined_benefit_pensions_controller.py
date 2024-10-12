# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.defined_benefit_pension_model import DefinedBenefitPensionModel
from openapi_server.models.defined_benefit_pension_with_id_model import DefinedBenefitPensionWithIdModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel


pytestmark = pytest.mark.asyncio

async def test_defined_benefit_pensions_delete_defined_benefit_pension_by_id(client):
    """Test case for defined_benefit_pensions_delete_defined_benefit_pension_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/DefinedBenefitPensions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defined_benefit_pensions_get_by_id(client):
    """Test case for defined_benefit_pensions_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DefinedBenefitPensions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defined_benefit_pensions_get_defined_benefit_pensions_by_fact_finder_id_by_factfinderid(client):
    """Test case for defined_benefit_pensions_get_defined_benefit_pensions_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DefinedBenefitPensions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_defined_benefit_pensions_post_by_model(client):
    """Test case for defined_benefit_pensions_post_by_model

    
    """
    model = {"factFinderId":6,"member":"Client","description":"description","estimatedAmount":0.8008281904610115,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/DefinedBenefitPensions',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_defined_benefit_pensions_put_defined_benefit_pension_by_id_model(client):
    """Test case for defined_benefit_pensions_put_defined_benefit_pension_by_id_model

    
    """
    model = {"factFinderId":6,"member":"Client","description":"description","estimatedAmount":0.8008281904610115,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/DefinedBenefitPensions/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

