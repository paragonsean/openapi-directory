# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_et_version_incidents_format(client):
    """Test case for g_et_version_incidents_format

    Paginated incidents matching parameters
    """
    params = [('page', 1),
                    ('per_page', 56),
                    ('occurred_before', 56),
                    ('occurred_after', 56),
                    ('incident_type', 'incident_type_example'),
                    ('proximity', 'proximity_example'),
                    ('proximity_square', 100),
                    ('query', 'query_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_version_incidents_id_format(client):
    """Test case for g_et_version_incidents_id_format

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2/incidents/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

