# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.substance import Substance
from openapi_server.models.substance_composition import SubstanceComposition
from openapi_server.models.substance_study import SubstanceStudy
from openapi_server.models.substance_study_summary import SubstanceStudySummary


pytestmark = pytest.mark.asyncio

async def test_get_substance_by_uuid(client):
    """Test case for get_substance_by_uuid

    Get a substance
    """
    params = [('property_uris[]', 'property_uris_example'),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/substance/{uuid}'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_composition_0(client):
    """Test case for get_substance_composition_0

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
        path='/nanoreg1/enm/{db}/substance/{uuid}/composition'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_structures_0(client):
    """Test case for get_substance_structures_0

    Get substance composition as a dataset
    """
    params = [('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/substance/{uuid}/structures'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_study_0(client):
    """Test case for get_substance_study_0

    get substance study
    """
    params = [('top', 'top_example'),
                    ('category', 'category_example'),
                    ('property_uri', 'property_uri_example'),
                    ('property', '_property_example'),
                    ('investigation_uuid', 'investigation_uuid_example'),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/substance/{uuid}/study'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_study_summary_0(client):
    """Test case for get_substance_study_summary_0

    Get study summary for the substance
    """
    params = [('top', 'top_example'),
                    ('category', 'category_example'),
                    ('property_uri', 'property_uri_example'),
                    ('property', '_property_example'),
                    ('result', True),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/substance/{uuid}/studySummary'.format(db=nanoreg1, uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substances(client):
    """Test case for get_substances

    List substances
    """
    params = [('search', 'search_example'),
                    ('type', 'type_example'),
                    ('compound_uri', 'compound_uri_example'),
                    ('bundle_uri', 'bundle_uri_example'),
                    ('addDummySubstance', True),
                    ('studysummary', True),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/substance'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

