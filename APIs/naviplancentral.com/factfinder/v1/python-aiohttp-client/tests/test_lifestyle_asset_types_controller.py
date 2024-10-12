# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lifestyle_asset_type_model import LifestyleAssetTypeModel
from openapi_server.models.lifestyle_asset_types_model import LifestyleAssetTypesModel


pytestmark = pytest.mark.asyncio

async def test_lifestyle_asset_types_get_by_country(client):
    """Test case for lifestyle_asset_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifestyleAssetTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifestyle_asset_types_get_by_id(client):
    """Test case for lifestyle_asset_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifestyleAssetTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

