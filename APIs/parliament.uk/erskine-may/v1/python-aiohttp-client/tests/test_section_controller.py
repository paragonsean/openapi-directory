# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erskine_may_section_detail import ErskineMaySectionDetail
from openapi_server.models.erskine_may_section_overview import ErskineMaySectionOverview


pytestmark = pytest.mark.asyncio

async def test_api_section_section_id_get(client):
    """Test case for api_section_section_id_get

    Returns a section by section id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Section/{section_id}'.format(section_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_section_section_idstep_get(client):
    """Test case for api_section_section_idstep_get

    Returns a section overview by section id and step.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Section/{section_idstep}'.format(section_id=56, step=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

