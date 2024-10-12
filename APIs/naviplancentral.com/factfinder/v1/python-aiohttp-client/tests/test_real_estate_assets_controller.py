# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.real_estate_asset_model import RealEstateAssetModel
from openapi_server.models.real_estate_asset_with_id_model import RealEstateAssetWithIdModel
from openapi_server.models.real_estate_assets_model import RealEstateAssetsModel


pytestmark = pytest.mark.asyncio

async def test_real_estate_assets_delete_by_id(client):
    """Test case for real_estate_assets_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/RealEstateAssets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_real_estate_assets_get_by_id(client):
    """Test case for real_estate_assets_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RealEstateAssets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_real_estate_assets_get_real_estate_assets_by_fact_finder_id_by_factfinderid(client):
    """Test case for real_estate_assets_get_real_estate_assets_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RealEstateAssets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_real_estate_assets_post_by_model(client):
    """Test case for real_estate_assets_post_by_model

    
    """
    model = {"owner":"Client","factFinderId":0,"purchaseDate":"2000-01-23T04:56:07.000+00:00","rentalIncome":5.637376656633329,"description":"description","marketValue":1.4658129805029452,"externalDestinationId":"externalDestinationId","frequency":6,"purchaseAmount":5.962133916683182}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/RealEstateAssets',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_real_estate_assets_put_by_id_model(client):
    """Test case for real_estate_assets_put_by_id_model

    
    """
    model = {"owner":"Client","factFinderId":0,"purchaseDate":"2000-01-23T04:56:07.000+00:00","rentalIncome":5.637376656633329,"description":"description","marketValue":1.4658129805029452,"externalDestinationId":"externalDestinationId","frequency":6,"purchaseAmount":5.962133916683182}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/RealEstateAssets/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

