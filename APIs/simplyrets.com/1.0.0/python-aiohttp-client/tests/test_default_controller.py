# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing import Listing
from openapi_server.models.open_house import OpenHouse


pytestmark = pytest.mark.asyncio

async def test_openhouses_get(client):
    """Test case for openhouses_get

    The SimplyRETS OpenHouses API
    """
    params = [('type', 'type_example'),
                    ('listingId', 'listing_id_example'),
                    ('cities', ['cities_example']),
                    ('brokers', ['brokers_example']),
                    ('agent', 'agent_example'),
                    ('minprice', 56),
                    ('startdate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('lastId', 56),
                    ('limit', 56),
                    ('sort', 'sort_example'),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/openhouses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_openhouses_open_house_key_get(client):
    """Test case for openhouses_open_house_key_get

    Single OpenHouse Endpoint
    """
    params = [('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/openhouses/{open_house_key}'.format(open_house_key=189018),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_properties_get(client):
    """Test case for properties_get

    The SimplyRETS Listings API
    """
    params = [('q', 'q_example'),
                    ('status', ['status_example']),
                    ('type', ['type_example']),
                    ('subtype', ['subtype_example']),
                    ('agent', 'agent_example'),
                    ('brokers', ['brokers_example']),
                    ('minprice', 56),
                    ('maxprice', 56),
                    ('minarea', 56),
                    ('maxarea', 56),
                    ('minbaths', 56),
                    ('maxbaths', 56),
                    ('minbeds', 56),
                    ('maxbeds', 56),
                    ('maxdom', 56),
                    ('minyear', 56),
                    ('limit', 56),
                    ('offset', 56),
                    ('lastId', 56),
                    ('vendor', 'vendor_example'),
                    ('postalCodes', ['postal_codes_example']),
                    ('features', ['features_example']),
                    ('water', 'water_example'),
                    ('neighborhoods', ['neighborhoods_example']),
                    ('cities', ['cities_example']),
                    ('counties', ['counties_example']),
                    ('points', ['points_example']),
                    ('include', ['include_example']),
                    ('sort', 'sort_example'),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_properties_mls_id_get(client):
    """Test case for properties_mls_id_get

    Single Listing Endpoint
    """
    params = [('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/properties/{mls_id}'.format(mls_id=1005252),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

