# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.billing_position import BillingPosition
from openapi_server.models.service_costs import ServiceCosts


pytestmark = pytest.mark.asyncio

async def test_get_positions_for_organization(client):
    """Test case for get_positions_for_organization

    Get billing positions for a given organization
    """
    params = [('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/billing/{organization_id}/positions'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sum_for_organization(client):
    """Test case for get_sum_for_organization

    Get billing amount of services for a given organization
    """
    params = [('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/billing/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

