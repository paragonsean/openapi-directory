# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_job_result import BulkJobResult


pytestmark = pytest.mark.asyncio

async def test_v2_bulk_jobs_bulk_jobs_id_results_get(client):
    """Test case for v2_bulk_jobs_bulk_jobs_id_results_get

    List job data for a completed bulk job.
    """
    params = [('status', ['status_example']),
                    ('id', None),
                    ('per_page', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/bulk_jobs/{bulk_jobs_id}/results'.format(bulk_jobs_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

