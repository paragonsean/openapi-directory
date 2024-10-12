# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_list import DatasetList
from openapi_server.models.deletion_response import DeletionResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_dataset(client):
    """Test case for create_dataset

    Create a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('labels', 'labels_example')
    data.add_field('name', 'name_example')
    data.add_field('type', 'type_example')
    response = await client.request(
        method='POST',
        path='/v2/vision/datasets',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dataset1(client):
    """Test case for delete_dataset1

    Delete a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/vision/datasets/{dataset_id}'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get1(client):
    """Test case for get1

    Get Deletion Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/deletion/{id}'.format(id='Z2JTFBF3A7XKIJC5QEJXMO4HSY'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset1(client):
    """Test case for get_dataset1

    Get a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/datasets/{dataset_id}'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_datasets1(client):
    """Test case for list_datasets1

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
        path='/v2/vision/datasets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_dataset_async1(client):
    """Test case for upload_dataset_async1

    Create a Dataset From a Zip File Asynchronously
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
        path='/v2/vision/datasets/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_dataset_sync1(client):
    """Test case for upload_dataset_sync1

    Create a Dataset From a Zip File Synchronously
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
        path='/v2/vision/datasets/upload/sync',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

