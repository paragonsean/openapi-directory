# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_chartjs280(client):
    """Test case for get_chartjs280

    Chart.js as image API
    """
    params = [('c', 'c_example'),
                    ('chart', 'chart_example'),
                    ('width', 500),
                    ('height', 300),
                    ('backgroundColor', 'background_color_example'),
                    ('bkg', 'bkg_example'),
                    ('encoding', url),
                    ('icac', 'icac_example'),
                    ('ichm', 'ichm_example'),
                    ('icretina', 'icretina_example')]
    headers = { 
        'Accept': 'image/svg+xml',
    }
    response = await client.request(
        method='GET',
        path='/chart.js/2.8.0',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

