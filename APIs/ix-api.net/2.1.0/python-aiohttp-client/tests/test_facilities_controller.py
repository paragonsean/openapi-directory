# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.facility import Facility


pytestmark = pytest.mark.asyncio

async def test_facilities_list(client):
    """Test case for facilities_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('capability_media_type', 'capability_media_type_example'),
                    ('capability_speed', 56),
                    ('capability_speed__lt', 56),
                    ('capability_speed__lte', 56),
                    ('capability_speed__gt', 56),
                    ('capability_speed__gte', 56),
                    ('organisation_name', 'organisation_name_example'),
                    ('metro_area', 'metro_area_example'),
                    ('metro_area_network', 'metro_area_network_example'),
                    ('address_country', 'address_country_example'),
                    ('address_locality', 'address_locality_example'),
                    ('postal_code', 'postal_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/facilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_facilities_read(client):
    """Test case for facilities_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/facilities/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

