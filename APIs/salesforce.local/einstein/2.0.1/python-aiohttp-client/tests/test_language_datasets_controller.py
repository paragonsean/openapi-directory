# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_list import DatasetList
from openapi_server.models.deletion_response import DeletionResponse


pytestmark = pytest.mark.asyncio

async def test_delete_dataset(client):
    """Test case for delete_dataset

    Delete a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/language/datasets/{dataset_id}'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Get Deletion Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/language/deletion/{id}'.format(id='Z2JTFBF3A7XKIJC5QEJXMO4HSY'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset(client):
    """Test case for get_dataset

    Get a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/language/datasets/{dataset_id}'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_datasets(client):
    """Test case for list_datasets

    Get All Datasets
    """
    params = [('offset', '0'),
                    ('count', '25'),
                    ('global', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/language/datasets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_dataset_async(client):
    """Test case for upload_dataset_async

    Create a Dataset From a File Asynchronously
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('type', 'type_example')
    response = await client.request(
        method='POST',
        path='/v2/language/datasets/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_dataset_sync(client):
    """Test case for upload_dataset_sync

    Create a Dataset From a File Synchronously
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('type', 'type_example')
    response = await client.request(
        method='POST',
        path='/v2/language/datasets/upload/sync',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

