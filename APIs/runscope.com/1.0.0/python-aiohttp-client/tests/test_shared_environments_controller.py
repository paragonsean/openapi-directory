# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.environment import Environment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_environments_environment_id_put(client):
    """Test case for buckets_bucket_key_environments_environment_id_put

    Update the details of a shared environment.
    """
    modified_environment = openapi_server.Environment()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/buckets/{bucket_key}/environments/{environment_id}'.format(bucket_key='bucket_key_example', environment_id='environment_id_example'),
        headers=headers,
        json=modified_environment,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_environments_get(client):
    """Test case for buckets_bucket_key_environments_get

    Returns list of shared environments for a specified bucket.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/environments'.format(bucket_key='bucket_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_environments_post(client):
    """Test case for buckets_bucket_key_environments_post

    Create new shared environment.
    """
    new_environment = openapi_server.Environment()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buckets/{bucket_key}/environments'.format(bucket_key='bucket_key_example'),
        headers=headers,
        json=new_environment,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

