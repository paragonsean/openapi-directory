# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_definition_meta import BranchDefinitionMeta
from openapi_server.models.error_definition400 import ErrorDefinition400
from openapi_server.models.error_definition408 import ErrorDefinition408
from openapi_server.models.error_definition429 import ErrorDefinition429
from openapi_server.models.error_definition500 import ErrorDefinition500
from openapi_server.models.error_definition503 import ErrorDefinition503


pytestmark = pytest.mark.asyncio

async def test_open_banking_v22_branches_get(client):
    """Test case for open_banking_v22_branches_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/open-banking/v2.2/branches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_branches_country_country_get(client):
    """Test case for x_open_banking_v22_branches_country_country_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/branches/country/{country}'.format(country='country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_branches_country_country_town_town_get(client):
    """Test case for x_open_banking_v22_branches_country_country_town_town_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/branches/country/{country}/town/{town}'.format(country='country_example', town='town_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_branches_geo_location_lat_latitude_long_longitude_get(client):
    """Test case for x_open_banking_v22_branches_geo_location_lat_latitude_long_longitude_get

    
    """
    params = [('radius', 3.4)]
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/branches/geo-location/lat/{latitude}/long/{longitude}'.format(latitude='latitude_example', longitude='longitude_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_branches_postcode_postcode_get(client):
    """Test case for x_open_banking_v22_branches_postcode_postcode_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/branches/postcode/{postcode}'.format(postcode='postcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_branches_sortcode_sortcode_get(client):
    """Test case for x_open_banking_v22_branches_sortcode_sortcode_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/branches/sortcode/{sortcode}'.format(sortcode='sortcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

