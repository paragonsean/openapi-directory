# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.facet import Facet
from openapi_server.models.investigation import Investigation
from openapi_server.models.substance_study import SubstanceStudy
from openapi_server.models.substance_study_summary import SubstanceStudySummary


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_summary(client):
    """Test case for get_endpoint_summary

    Search endpoint summary
    """
    params = [('top', 'top_example'),
                    ('category', 'category_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/query/study'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_investigation_results(client):
    """Test case for get_investigation_results

    Details of multiple studies
    """
    params = [('type', 'bystudytype'),
                    ('search', 'PC_GRANULOMETRY_SECTION'),
                    ('inchikey', 'YUYCVXFAYWRXLS-UHFFFAOYSA-N'),
                    ('id', 'id_example'),
                    ('page', 0),
                    ('pagesize', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/investigation'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_substance_study(client):
    """Test case for get_substance_study

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

async def test_get_substance_study_summary(client):
    """Test case for get_substance_study_summary

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

