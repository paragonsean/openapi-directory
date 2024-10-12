# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.dataset import Dataset
from openapi_server.models.example import Example
from openapi_server.models.example_list import ExampleList


pytestmark = pytest.mark.asyncio

async def test_get_examples(client):
    """Test case for get_examples

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
        path='/v2/language/datasets/{dataset_id}/examples'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_examples_by_label(client):
    """Test case for get_examples_by_label

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
        path='/v2/language/examples',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_provide_feedback(client):
    """Test case for provide_feedback

    Create a Feedback Example
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('document', 'document_example')
    data.add_field('expected_label', 'expected_label_example')
    data.add_field('model_id', 'model_id_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v2/language/feedback',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_dataset_async(client):
    """Test case for update_dataset_async

    Create Examples From a File
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('type', 'type_example')
    response = await client.request(
        method='PUT',
        path='/v2/language/datasets/{dataset_id}/upload'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

