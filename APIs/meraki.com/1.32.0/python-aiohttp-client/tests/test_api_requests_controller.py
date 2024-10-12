# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_api_requests200_response_inner import GetOrganizationApiRequests200ResponseInner
from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_1(client):
    """Test case for get_organization_api_requests_1

    List the API requests made by an organization
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('adminId', 'admin_id_example'),
                    ('path', 'path_example'),
                    ('method', 'method_example'),
                    ('responseCode', 56),
                    ('sourceIp', 'source_ip_example'),
                    ('userAgent', 'user_agent_example'),
                    ('version', 56),
                    ('operationIds', ['operation_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_overview_1(client):
    """Test case for get_organization_api_requests_overview_1

    Return an aggregated overview of API requests data
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_overview_response_codes_by_interval_1(client):
    """Test case for get_organization_api_requests_overview_response_codes_by_interval_1

    Tracks organizations' API requests by response code across a given time period
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('interval', 56),
                    ('version', 56),
                    ('operationIds', ['operation_ids_example']),
                    ('sourceIps', ['source_ips_example']),
                    ('adminIds', ['admin_ids_example']),
                    ('userAgent', 'user_agent_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests/overview/responseCodes/byInterval'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

