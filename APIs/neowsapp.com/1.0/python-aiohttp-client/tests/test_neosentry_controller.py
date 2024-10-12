# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sentry_impact_risk_object import SentryImpactRiskObject
from openapi_server.models.sentry_object_paging_dto import SentryObjectPagingDto


pytestmark = pytest.mark.asyncio

async def test_retrieve_sentry_risk_data(client):
    """Test case for retrieve_sentry_risk_data

    Retrieve Sentry (Impact Risk ) Near Earth Objects
    """
    params = [('is_active', True),
                    ('page', 0),
                    ('size', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/neo/sentry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_sentry_risk_data_by_id(client):
    """Test case for retrieve_sentry_risk_data_by_id

    Retrieve Sentry (Impact Risk ) Near Earth Objectby ID 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/neo/sentry/{asteroid_id}'.format(asteroid_id='asteroid_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

