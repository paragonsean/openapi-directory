# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.s_zentrale_query import SZentraleQuery
from openapi_server.models.station_query import StationQuery


pytestmark = pytest.mark.asyncio

async def test_stations_get(client):
    """Test case for stations_get

    This operation provides the master data for german railway stations.
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('searchstring', 'searchstring_example'),
                    ('category', 'category_example'),
                    ('federalstate', 'federalstate_example'),
                    ('eva', 56),
                    ('ril', 'ril_example'),
                    ('logicaloperator', 'logicaloperator_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/stada/v2/stations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stations_id_get(client):
    """Test case for stations_id_get

    This operation provides the master data for a german railway station selected by its station-id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/stada/v2/stations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_szentralen_get(client):
    """Test case for szentralen_get

    This operation provides the master data for 3-S-Zentralen.
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/stada/v2/szentralen',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_szentralen_id_get(client):
    """Test case for szentralen_id_get

    This operation provides the master data for 3-S-Zentralen select by its id.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/stada/v2/szentralen/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

