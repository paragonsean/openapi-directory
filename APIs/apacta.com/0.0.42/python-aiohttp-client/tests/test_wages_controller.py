# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_wages_download_salary_file_get(client):
    """Test case for wages_download_salary_file_get

    Download salary file
    """
    params = [('date_from', '2013-10-20'),
                    ('date_to', '2013-10-20'),
                    ('company_id', 'company_id_example')]
    headers = { 
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/wages/downloadSalaryFile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

