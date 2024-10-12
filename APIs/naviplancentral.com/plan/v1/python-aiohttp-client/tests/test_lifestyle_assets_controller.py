# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lifestyle_asset_model import LifestyleAssetModel
from openapi_server.models.lifestyle_assets_model import LifestyleAssetsModel


pytestmark = pytest.mark.asyncio

async def test_lifestyle_assets_get_by_id_planid(client):
    """Test case for lifestyle_assets_get_by_id_planid

    Retrieve lifestyle assets
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LifestyleAssets/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lifestyle_assets_get_by_planid(client):
    """Test case for lifestyle_assets_get_by_planid

    Retrieve lifestyle assets
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/LifestyleAssets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

