# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets_get200_response import BucketsGet200Response
from openapi_server.models.error import Error
from openapi_server.models.new_bucket import NewBucket


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_delete(client):
    """Test case for buckets_bucket_key_delete

    Delete a single bucket resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/buckets/{bucket_key}'.format(bucket_key='bucket_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_get(client):
    """Test case for buckets_bucket_key_get

    Returns a single bucket resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}'.format(bucket_key='bucket_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_get(client):
    """Test case for buckets_get

    Returns a list of buckets.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_post(client):
    """Test case for buckets_post

    Create a new bucket
    """
    new_bucket = openapi_server.NewBucket()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buckets',
        headers=headers,
        json=new_bucket,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

