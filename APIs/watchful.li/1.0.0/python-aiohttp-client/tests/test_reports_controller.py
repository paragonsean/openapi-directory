# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_reports_sites_id_get(client):
    """Test case for reports_sites_id_get

    Returns a PDF report for a specific site
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('reports', 'reports_example'),
                    ('log_type', 'log_type_example'),
                    ('compare', 56)]
    headers = { 
        'Accept': 'application/pdf',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/reports/sites/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_tags_id_get(client):
    """Test case for reports_tags_id_get

    Find sites by ID
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('reports', 'reports_example'),
                    ('log_type', 'log_type_example'),
                    ('compare', 56)]
    headers = { 
        'Accept': 'application/pdf',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/reports/tags/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

