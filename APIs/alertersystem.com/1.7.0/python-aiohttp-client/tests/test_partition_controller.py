# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_partition_get_collection200_response import ApiPartitionGetCollection200Response
from openapi_server.models.partition_get import PartitionGet
from openapi_server.models.partition_jsonld_get import PartitionJsonldGet
from openapi_server.models.partition_jsonld_post import PartitionJsonldPost
from openapi_server.models.partition_jsonld_put import PartitionJsonldPut
from openapi_server.models.partition_patch import PartitionPatch
from openapi_server.models.partition_post import PartitionPost
from openapi_server.models.partition_put import PartitionPut


pytestmark = pytest.mark.asyncio

async def test_api_partition_get_collection(client):
    """Test case for api_partition_get_collection

    Retrieves the collection of Partition resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/partition',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_partition_id_delete(client):
    """Test case for api_partition_id_delete

    Removes the Partition resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/partition/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_partition_id_get(client):
    """Test case for api_partition_id_get

    Retrieves a Partition resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/partition/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_partition_id_patch(client):
    """Test case for api_partition_id_patch

    Updates the Partition resource.
    """
    body = openapi_server.PartitionPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/partition/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_partition_id_put(client):
    """Test case for api_partition_id_put

    Replaces the Partition resource.
    """
    body = openapi_server.PartitionPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/partition/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_partition_post(client):
    """Test case for api_partition_post

    Creates a Partition resource.
    """
    body = openapi_server.PartitionPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

