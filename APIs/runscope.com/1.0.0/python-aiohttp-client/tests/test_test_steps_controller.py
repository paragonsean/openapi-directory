# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.standard_error import StandardError
from openapi_server.models.test_step import TestStep


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_steps_get(client):
    """Test case for buckets_bucket_key_tests_test_id_steps_get

    List test steps for a test.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/tests/{test_id}/steps'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_tests_test_id_steps_post(client):
    """Test case for buckets_bucket_key_tests_test_id_steps_post

    Add new test step.
    """
    test_step = openapi_server.TestStep()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buckets/{bucket_key}/tests/{test_id}/steps'.format(bucket_key='bucket_key_example', test_id='test_id_example'),
        headers=headers,
        json=test_step,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_tests_test_id_steps_step_id_delete(client):
    """Test case for buckets_bucket_key_tests_test_id_steps_step_id_delete

    Delete a step from a test.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/buckets/{bucket_key}/tests/{test_id}/steps/{step_id}'.format(bucket_key='bucket_key_example', test_id='test_id_example', step_id='step_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_tests_test_id_steps_step_id_put(client):
    """Test case for buckets_bucket_key_tests_test_id_steps_step_id_put

    Update the details of a single test step.
    """
    test_step = openapi_server.TestStep()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/buckets/{bucket_key}/tests/{test_id}/steps/{step_id}'.format(bucket_key='bucket_key_example', test_id='test_id_example', step_id='step_id_example'),
        headers=headers,
        json=test_step,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

