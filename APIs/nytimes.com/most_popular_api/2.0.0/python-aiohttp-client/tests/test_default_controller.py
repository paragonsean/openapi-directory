# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_mostemailed_section_time_period_json200_response import GETMostemailedSectionTimePeriodJson200Response
from openapi_server.models.get_mostemailed_section_time_period_json400_response import GETMostemailedSectionTimePeriodJson400Response
from openapi_server.models.get_mostshared_section_time_period_json200_response import GETMostsharedSectionTimePeriodJson200Response


pytestmark = pytest.mark.asyncio

async def test_g_et_mostemailed_section_time_period_json(client):
    """Test case for g_et_mostemailed_section_time_period_json

    Most Emailed by Section & Time Period
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/mostpopular/v2/mostemailed/{section}/{time_period_jso}'.format(section='section_example', time_period='time_period_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_mostshared_section_time_period_json(client):
    """Test case for g_et_mostshared_section_time_period_json

    Most Shared by Section & Time Period
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/mostpopular/v2/mostshared/{section}/{time_period_jso}'.format(section='section_example', time_period='time_period_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_mostviewed_section_time_period_json(client):
    """Test case for g_et_mostviewed_section_time_period_json

    Most Viewed by Section & Time Period
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/mostpopular/v2/mostviewed/{section}/{time_period_jso}'.format(section='section_example', time_period='time_period_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

