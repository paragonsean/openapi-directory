# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_dataset(client):
    """Test case for get_dataset

    Get metadata about a dataset.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/{dataset}'.format(dataset='dataset_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datasets(client):
    """Test case for get_datasets

    Get a list of all datasets.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

