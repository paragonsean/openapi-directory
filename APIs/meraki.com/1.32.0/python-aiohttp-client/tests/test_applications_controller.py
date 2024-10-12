# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_insight_application_health_by_time200_response_inner import GetNetworkInsightApplicationHealthByTime200ResponseInner
from openapi_server.models.get_organization_insight_applications200_response_inner import GetOrganizationInsightApplications200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_insight_application_health_by_time_1(client):
    """Test case for get_network_insight_application_health_by_time_1

    Get application health by time
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/insight/applications/{application_id}/healthByTime'.format(network_id='network_id_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_insight_applications_1(client):
    """Test case for get_organization_insight_applications_1

    List all Insight tracked applications
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/insight/applications'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

