# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_data_get(client):
    """Test case for api_data_get

    Download Daymet Data
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('vars', ['vars_example']),
                    ('years', ['years_example']),
                    ('start', '2013-10-20'),
                    ('end', '2013-10-20'),
                    ('format', 'format_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/single-pixel/api/data',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preview_get(client):
    """Test case for preview_get

    Preview Daymet Data in a web browser
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('vars', ['vars_example']),
                    ('years', ['years_example']),
                    ('start', '2013-10-20'),
                    ('end', '2013-10-20'),
                    ('format', 'format_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/single-pixel/preview',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_save_data_get(client):
    """Test case for send_save_data_get

    Download Daymet Data
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('vars', ['vars_example']),
                    ('years', ['years_example']),
                    ('start', '2013-10-20'),
                    ('end', '2013-10-20'),
                    ('format', 'format_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/single-pixel/send/saveData',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_get(client):
    """Test case for visualize_get

    Visualize Daymet Data in a web browser
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('vars', ['vars_example']),
                    ('years', ['years_example']),
                    ('start', '2013-10-20'),
                    ('end', '2013-10-20'),
                    ('format', 'format_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/single-pixel/visualize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

