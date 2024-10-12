# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.buckets_bucket_key_tests_get200_response import BucketsBucketKeyTestsGet200Response
from openapi_server.models.error import Error
from openapi_server.models.metrics import Metrics
from openapi_server.models.test import Test
from openapi_server.models.test_detail import TestDetail


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_get(client):
    """Test case for buckets_bucket_key_tests_get

    Returns a list of tests.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/tests'.format(bucket_key='bucket_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_tests_post(client):
    """Test case for buckets_bucket_key_tests_post

    Create a test.
    """
    new_test = openapi_server.Test()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buckets/{bucket_key}/tests'.format(bucket_key='bucket_key_example'),
        headers=headers,
        json=new_test,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_delete(client):
    """Test case for buckets_bucket_key_tests_test_id_delete

    Delete a test, including all steps, schedules, test-specific environments and results.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/buckets/{bucket_key}/tests/{test_id}'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_get(client):
    """Test case for buckets_bucket_key_tests_test_id_get

    Retrieve the details of a given test by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/tests/{test_id}'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_metrics_get(client):
    """Test case for buckets_bucket_key_tests_test_id_metrics_get

    Return details of the test metrics for the specified timeframe.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/tests/{test_id}/metrics'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_put(client):
    """Test case for buckets_bucket_key_tests_test_id_put

    Modify a test's name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/buckets/{bucket_key}/tests/{test_id}'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

