# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_section import NewSection
from openapi_server.models.section_details import SectionDetails
from openapi_server.models.section_list import SectionList


pytestmark = pytest.mark.asyncio

async def test_section_delete(client):
    """Test case for section_delete

    Delete a Section
    """
    params = [('SectionID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Section',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_section_get(client):
    """Test case for section_get

    Gets list of Sections
    """
    params = [('ProjectID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Section',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_section_post(client):
    """Test case for section_post

    Create a Section
    """
    model = {"EndDateUTC":"2000-01-23T04:56:07.000+00:00","ProjectIDFK":0,"Title":"Title","StartDateUTC":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Section',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

