# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.proposed_negative_statutory_instrument_resource import ProposedNegativeStatutoryInstrumentResource
from openapi_server.models.proposed_negative_statutory_instrument_resource_collection import ProposedNegativeStatutoryInstrumentResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_business_items_by_proposed_negative_statutory_instrument_id(client):
    """Test case for get_business_items_by_proposed_negative_statutory_instrument_id

    Returns business items belonging to a proposed negative statutory instrument.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ProposedNegativeStatutoryInstrument/{id}/BusinessItems'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_proposed_negative_statutory_instrument_by_id(client):
    """Test case for get_proposed_negative_statutory_instrument_by_id

    Returns proposed negative statutory instrument by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ProposedNegativeStatutoryInstrument/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_proposed_negative_statutory_instruments(client):
    """Test case for get_proposed_negative_statutory_instruments

    Returns a list of proposed negative statutory instruments.
    """
    params = [('Name', 'name_example'),
                    ('RecommendedForProcedureChange', True),
                    ('DepartmentId', 56),
                    ('LayingBodyId', 'laying_body_id_example'),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ProposedNegativeStatutoryInstrument',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

