# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenancy_model import TenancyModel
from openapi_server.models.tenancy_model_results import TenancyModelResults


pytestmark = pytest.mark.asyncio

async def test_lettings_controller_get_advertised(client):
    """Test case for lettings_controller_get_advertised

    Search all properties available for rent given a range of search criteria.
    """
    params = [('branchID', 'branch_id_example'),
                    ('offset', 56),
                    ('count', 56),
                    ('areaID', 'area_id_example'),
                    ('rentMinimum', 3.4),
                    ('rentMaximum', 3.4),
                    ('maximumTenants', 56),
                    ('wantSharedProperties', True),
                    ('wantStudentProperties', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/lettings/advertised'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lettings_controller_get_advertised_between_dates(client):
    """Test case for lettings_controller_get_advertised_between_dates

    Search all properties available for rent given a range of search criteria and dates.
    """
    params = [('branchID', 'branch_id_example'),
                    ('offset', 56),
                    ('count', 56),
                    ('rangeStartDate', '2013-10-20T19:20:30+01:00'),
                    ('rangeEndDate', '2013-10-20T19:20:30+01:00'),
                    ('areaID', 'area_id_example'),
                    ('rentMinimum', 3.4),
                    ('rentMaximum', 3.4),
                    ('maximumTenants', 56),
                    ('wantSharedProperties', True),
                    ('wantStudentProperties', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/lettings/advertisedbetweendates'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lettings_controller_get_tenancy_brochure(client):
    """Test case for lettings_controller_get_tenancy_brochure

    Downloads the brochure relating to the latest advertised rental of a property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/lettings/tenancies/{tenancy_id}/brochure'.format(short_name='short_name_example', tenancy_id='tenancy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_lettings_tenancies_get(client):
    """Test case for v2_tier2_short_name_lettings_tenancies_get

    A collection of all the company's tenancies
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/lettings/tenancies'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_lettings_tenancies_tenancy_idget(client):
    """Test case for v2_tier2_short_name_lettings_tenancies_tenancy_idget

    Get a specific tenancy given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/lettings/tenancies/{tenancy_id}'.format(short_name='short_name_example', tenancy_id='tenancy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

