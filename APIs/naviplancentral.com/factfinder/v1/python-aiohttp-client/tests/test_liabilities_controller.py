# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.liability_model import LiabilityModel
from openapi_server.models.liability_with_id_model import LiabilityWithIdModel


pytestmark = pytest.mark.asyncio

async def test_liabilities_delete_by_id(client):
    """Test case for liabilities_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Liabilities/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_liabilities_get_by_id(client):
    """Test case for liabilities_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Liabilities/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_liabilities_get_liabilities_by_fact_finder_id_by_factfinderid_externalsourceid(client):
    """Test case for liabilities_get_liabilities_by_fact_finder_id_by_factfinderid_externalsourceid

    
    """
    params = [('factFinderId', 56),
                    ('externalSourceId', 'external_source_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Liabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_liabilities_post_by_model(client):
    """Test case for liabilities_post_by_model

    
    """
    model = {"interestRate":29.810669583415912,"originalPrincipal":2.3021358869347655,"owner":"Client","description":"description","liabilityType":5,"frequency":1,"paymentType":"InterestOnly","lastUpdated":"2000-01-23T04:56:07.000+00:00","externalSourceName":"externalSourceName","factFinderId":6,"balance":0.8008281904610115,"loanDate":"2000-01-23T04:56:07.000+00:00","externalSourceId":"externalSourceId","payment":7.061401241503109,"balanceAsOfDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Liabilities',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_liabilities_put_by_id_model(client):
    """Test case for liabilities_put_by_id_model

    
    """
    model = {"interestRate":29.810669583415912,"originalPrincipal":2.3021358869347655,"owner":"Client","description":"description","liabilityType":5,"frequency":1,"paymentType":"InterestOnly","lastUpdated":"2000-01-23T04:56:07.000+00:00","externalSourceName":"externalSourceName","factFinderId":6,"balance":0.8008281904610115,"loanDate":"2000-01-23T04:56:07.000+00:00","externalSourceId":"externalSourceId","payment":7.061401241503109,"balanceAsOfDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Liabilities/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

