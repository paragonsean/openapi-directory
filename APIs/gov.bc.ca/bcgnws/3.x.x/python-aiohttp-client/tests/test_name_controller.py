# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_names_changes_get_0(client):
    """Test case for names_changes_get_0

    Search for names with metadata changes in a given period
    """
    params = [('outputFormat', json),
                    ('fromDate', 2017-01-01),
                    ('toDate', 2017-06-30),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', name),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_decisions_recent_get_0(client):
    """Test case for names_decisions_recent_get_0

    Search for names affected by recent naming decision
    """
    params = [('outputFormat', json),
                    ('days', 30),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', name),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/decisions/recent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_decisions_year_get_0(client):
    """Test case for names_decisions_year_get_0

    Search for names affected by naming decisions in a given year
    """
    params = [('outputFormat', json),
                    ('year', 2007),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', name),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/decisions/year',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_inside_get_0(client):
    """Test case for names_inside_get_0

    Search in a geographic area
    """
    params = [('outputFormat', json),
                    ('bbox', '-119,49,-118,50'),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', name),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/inside',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_name_id_output_format_get(client):
    """Test case for names_name_id_output_format_get

    Get a name by its nameId
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/{name_id_output_format}'.format(name_id=22474, output_format=json),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_near_get_0(client):
    """Test case for names_near_get_0

    Search near to a geographic point
    """
    params = [('outputFormat', json),
                    ('featurePoint', '-120,51'),
                    ('distance', 'distance_example'),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', name),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/near',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_not_official_search_get_0(client):
    """Test case for names_not_official_search_get_0

    Search by name, limit to unofficial names only
    """
    params = [('outputFormat', json),
                    ('name', 'Victoria'),
                    ('exactSpelling', 0),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', relevance),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/notOfficial/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_official_search_get_0(client):
    """Test case for names_official_search_get_0

    Search by name, limit to official names only
    """
    params = [('outputFormat', json),
                    ('name', 'Victoria'),
                    ('exactSpelling', 0),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', relevance),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/official/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_search_get_0(client):
    """Test case for names_search_get_0

    Search by name
    """
    params = [('outputFormat', json),
                    ('name', 'Victoria'),
                    ('exactSpelling', 0),
                    ('featureClass', '*'),
                    ('featureCategory', '*'),
                    ('featureType', '*'),
                    ('sortBy', relevance),
                    ('outputSRS', 4326),
                    ('embed', 56),
                    ('outputStyle', summary),
                    ('itemsPerPage', 20),
                    ('startIndex', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/names/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

