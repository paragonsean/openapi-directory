# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataset_type_collection_output import DatasetTypeCollectionOutput
from openapi_server.models.dataset_type_output import DatasetTypeOutput
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_query_datataset_information_of_all_the_resource_types_v1_dataset_ip_get(client):
    """Test case for query_datataset_information_of_all_the_resource_types_v1_dataset_ip_get

    Get the list of all the datasets available in the platform.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/dataset/ip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_datataset_information_of_the_resource_type_v1_dataset_ip_name_get(client):
    """Test case for query_datataset_information_of_the_resource_type_v1_dataset_ip_name_get

    Get the detailed information of the dataset queried.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/dataset/ip/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

