# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lifestyle_asset_model import LifestyleAssetModel
from openapi_server.models.lifestyle_asset_with_id_model import LifestyleAssetWithIdModel
from openapi_server.models.lifestyle_assets_model import LifestyleAssetsModel


pytestmark = pytest.mark.asyncio

async def test_lifestyle_assets_delete_by_id(client):
    """Test case for lifestyle_assets_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/LifestyleAssets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifestyle_assets_get_by_id(client):
    """Test case for lifestyle_assets_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifestyleAssets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifestyle_assets_get_lifestyle_assets_by_fact_finder_id_by_factfinderid(client):
    """Test case for lifestyle_assets_get_lifestyle_assets_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifestyleAssets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lifestyle_assets_post_by_model(client):
    """Test case for lifestyle_assets_post_by_model

    
    """
    model = {"owner":"Client","factFinderId":0,"purchaseDate":"2000-01-23T04:56:07.000+00:00","description":"description","marketValue":6.027456183070403,"type":5,"externalDestinationId":"externalDestinationId","purchaseAmount":1.4658129805029452}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/LifestyleAssets',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lifestyle_assets_put_by_id_model(client):
    """Test case for lifestyle_assets_put_by_id_model

    
    """
    model = {"owner":"Client","factFinderId":0,"purchaseDate":"2000-01-23T04:56:07.000+00:00","description":"description","marketValue":6.027456183070403,"type":5,"externalDestinationId":"externalDestinationId","purchaseAmount":1.4658129805029452}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/LifestyleAssets/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

