# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_dash_types import SharedDashTypes


pytestmark = pytest.mark.asyncio

async def test_shared_dashtypes_get(client):
    """Test case for shared_dashtypes_get

    DashTypes: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/DashTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_dashtypes_get_id(client):
    """Test case for shared_dashtypes_get_id

    DashTypes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/DashTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_dashtypes_typeid_get_type_id(client):
    """Test case for shared_dashtypes_typeid_get_type_id

    DashTypes: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/DashTypes/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

