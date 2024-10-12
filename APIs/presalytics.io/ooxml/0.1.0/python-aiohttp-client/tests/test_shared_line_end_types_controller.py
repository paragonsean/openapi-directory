# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_line_end_types import SharedLineEndTypes


pytestmark = pytest.mark.asyncio

async def test_shared_lineendtypes_get(client):
    """Test case for shared_lineendtypes_get

    LineEndTypes: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/LineEndTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_lineendtypes_get_id(client):
    """Test case for shared_lineendtypes_get_id

    LineEndTypes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/LineEndTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_lineendtypes_typeid_get_type_id(client):
    """Test case for shared_lineendtypes_typeid_get_type_id

    LineEndTypes: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/LineEndTypes/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

