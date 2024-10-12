# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_et_version_locations_format(client):
    """Test case for g_et_version_locations_format

    Unpaginated geojson response
    """
    params = [('occurred_before', 56),
                    ('occurred_after', 56),
                    ('incident_type', 'incident_type_example'),
                    ('proximity', 'proximity_example'),
                    ('proximity_square', 100),
                    ('query', 'query_example'),
                    ('limit', 56),
                    ('all', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_version_locations_markers_format(client):
    """Test case for g_et_version_locations_markers_format

    Unpaginated geojson response with simplestyled markers
    """
    params = [('occurred_before', 56),
                    ('occurred_after', 56),
                    ('incident_type', 'incident_type_example'),
                    ('proximity', 'proximity_example'),
                    ('proximity_square', 100),
                    ('query', 'query_example'),
                    ('limit', 56),
                    ('all', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2/locations/markers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

