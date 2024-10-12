# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.substance_composition import SubstanceComposition


pytestmark = pytest.mark.asyncio

async def test_get_substance_composition(client):
    """Test case for get_substance_composition

    Substance composition
    """
    params = [('all', True),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/enm/{db}/substance/{uuid}/composition'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_structures(client):
    """Test case for get_substance_structures

    Get substance composition as a dataset
    """
    params = [('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/enm/{db}/substance/{uuid}/structures'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_by_identifier(client):
    """Test case for search_by_identifier

    Exact chemical structure search
    """
    params = [('search', 'search_example'),
                    ('b64search', 'b64search_example'),
                    ('casesens', True),
                    ('bundle_uri', 'bundle_uri_example'),
                    ('sameas', 'sameas_example'),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/enm/{db}/query/compound/{term}/{representation}'.format(db=nanoreg1, term='term_example', representation='representation_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_by_similarity(client):
    """Test case for search_by_similarity

    Exact similarity search
    """
    params = [('search', 'search_example'),
                    ('b64search', 'b64search_example'),
                    ('type', 'type_example'),
                    ('threshold', 3.4),
                    ('dataset_uri', 'dataset_uri_example'),
                    ('filterBySubstance', True),
                    ('bundle_uri', 'bundle_uri_example'),
                    ('sameas', 'sameas_example'),
                    ('mol', True),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/enm/{db}/query/similarity'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_by_smarts(client):
    """Test case for search_by_smarts

    Substructure search
    """
    params = [('search', 'search_example'),
                    ('b64search', 'b64search_example'),
                    ('type', 'type_example'),
                    ('dataset_uri', 'dataset_uri_example'),
                    ('filterBySubstance', True),
                    ('bundle_uri', 'bundle_uri_example'),
                    ('sameas', 'sameas_example'),
                    ('mol', True),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/enanomapper/enm/{db}/query/smarts'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

