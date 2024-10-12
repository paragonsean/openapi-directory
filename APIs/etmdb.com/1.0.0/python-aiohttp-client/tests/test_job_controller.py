# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_job_search_read(client):
    """Test case for job_search_read

    Return job details search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job/search/{job_title}'.format(job_title='job_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_searchall_read(client):
    """Test case for job_searchall_read

    Return job details search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job/searchall/{company_name}'.format(company_name='company_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

