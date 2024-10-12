# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_feature_categories_get(client):
    """Test case for feature_categories_get

    Get all feature categories
    """
    params = [('outputFormat', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/featureCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_feature_classes_get(client):
    """Test case for feature_classes_get

    Get all feature classes
    """
    params = [('outputFormat', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/featureClasses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_feature_types_get(client):
    """Test case for feature_types_get

    Get all feature types
    """
    params = [('outputFormat', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/featureTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

