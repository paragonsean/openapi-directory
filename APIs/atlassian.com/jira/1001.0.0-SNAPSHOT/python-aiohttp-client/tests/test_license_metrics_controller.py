# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.license_metric import LicenseMetric


pytestmark = pytest.mark.asyncio

async def test_get_approximate_application_license_count(client):
    """Test case for get_approximate_application_license_count

    Get approximate application license count
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/license/approximateLicenseCount/product/{application_key}'.format(application_key='application_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_approximate_license_count(client):
    """Test case for get_approximate_license_count

    Get approximate license count
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/license/approximateLicenseCount',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

