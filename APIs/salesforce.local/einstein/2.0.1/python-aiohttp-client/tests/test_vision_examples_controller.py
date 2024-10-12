# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.dataset import Dataset
from openapi_server.models.example import Example
from openapi_server.models.example_list import ExampleList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_example(client):
    """Test case for add_example

    Create an Example
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('label_id', 56)
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v2/vision/datasets/{dataset_id}/examples'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_examples1(client):
    """Test case for get_examples1

    Get All Examples
    """
    params = [('offset', '0'),
                    ('count', '100'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/datasets/{dataset_id}/examples'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_examples_by_label1(client):
    """Test case for get_examples_by_label1

    Get All Examples for Label
    """
    params = [('labelId', 'SomeLabelId'),
                    ('offset', '0'),
                    ('count', '100')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/examples',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_provide_feedback1(client):
    """Test case for provide_feedback1

    Create a Feedback Example
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('expected_label', 'expected_label_example')
    data.add_field('model_id', 'model_id_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v2/vision/feedback',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_dataset_async1(client):
    """Test case for update_dataset_async1

    Create Feedback Examples From a Zip File
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('model_id', 'model_id_example')
    response = await client.request(
        method='PUT',
        path='/v2/vision/bulkfeedback',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_dataset_async2(client):
    """Test case for update_dataset_async2

    Create Examples From a Zip File
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('path', 'path_example')
    response = await client.request(
        method='PUT',
        path='/v2/vision/datasets/{dataset_id}/upload'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

