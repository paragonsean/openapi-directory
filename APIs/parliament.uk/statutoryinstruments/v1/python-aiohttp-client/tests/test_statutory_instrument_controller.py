# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.house import House
from openapi_server.models.parliamentary_process import ParliamentaryProcess
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.statutory_instrument_resource import StatutoryInstrumentResource
from openapi_server.models.statutory_instrument_resource_collection import StatutoryInstrumentResourceCollection
from openapi_server.models.statutory_instrument_type import StatutoryInstrumentType


pytestmark = pytest.mark.asyncio

async def test_get_business_items_by_statutory_instrument_id(client):
    """Test case for get_business_items_by_statutory_instrument_id

    Returns business items belonging to statutory instrument with ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/StatutoryInstrument/{id}/BusinessItems'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statutory_instrument_by_id(client):
    """Test case for get_statutory_instrument_by_id

    Returns a statutory instrument by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/StatutoryInstrument/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statutory_instruments(client):
    """Test case for get_statutory_instruments

    Returns a list of statutory instruments.
    """
    params = [('Name', 'name_example'),
                    ('StatutoryInstrumentType', openapi_server.StatutoryInstrumentType()),
                    ('ScheduledDebate', True),
                    ('MotionToStop', True),
                    ('ConcernsRaisedByCommittee', True),
                    ('ParliamentaryProcessConcluded', openapi_server.ParliamentaryProcess()),
                    ('DepartmentId', 56),
                    ('LayingBodyId', 'laying_body_id_example'),
                    ('House', openapi_server.House()),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/StatutoryInstrument',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

