# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_v3_sidekiq_compound_metrics(client):
    """Test case for get_v3_sidekiq_compound_metrics

    Get the Sidekiq Compound metrics. Includes queue, process, and job statistics
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sidekiq/compound_metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_sidekiq_job_stats(client):
    """Test case for get_v3_sidekiq_job_stats

    Get the Sidekiq job statistics
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sidekiq/job_stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_sidekiq_process_metrics(client):
    """Test case for get_v3_sidekiq_process_metrics

    Get the Sidekiq process metrics
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sidekiq/process_metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_sidekiq_queue_metrics(client):
    """Test case for get_v3_sidekiq_queue_metrics

    Get the Sidekiq queue metrics
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sidekiq/queue_metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

