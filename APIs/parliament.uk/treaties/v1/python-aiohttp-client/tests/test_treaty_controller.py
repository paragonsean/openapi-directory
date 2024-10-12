# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.house import House
from openapi_server.models.parliamentary_process import ParliamentaryProcess
from openapi_server.models.series_membership_type import SeriesMembershipType
from openapi_server.models.treaty_resource import TreatyResource
from openapi_server.models.treaty_resource_collection import TreatyResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_business_items_by_treaty_id(client):
    """Test case for get_business_items_by_treaty_id

    Returns business items belonging to the treaty with ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Treaty/{id}/BusinessItems'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_treaties(client):
    """Test case for get_treaties

    Returns a list of treaties.
    """
    params = [('SearchText', 'search_text_example'),
                    ('GovernmentOrganisationId', 56),
                    ('Series', openapi_server.SeriesMembershipType()),
                    ('ParliamentaryProcess', openapi_server.ParliamentaryProcess()),
                    ('DebateScheduled', True),
                    ('MotionToNotRatify', True),
                    ('RecommendedNotRatify', True),
                    ('House', openapi_server.House()),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Treaty',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_treaty_by_id(client):
    """Test case for get_treaty_by_id

    Returns a treaty by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Treaty/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

