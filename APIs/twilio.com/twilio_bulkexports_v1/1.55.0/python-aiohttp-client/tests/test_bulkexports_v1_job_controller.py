# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_job import BulkexportsV1ExportJob


pytestmark = pytest.mark.asyncio

async def test_delete_job(client):
    """Test case for delete_job

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Exports/Jobs/{job_sid}'.format(job_sid='job_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_job(client):
    """Test case for fetch_job

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/Jobs/{job_sid}'.format(job_sid='job_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

