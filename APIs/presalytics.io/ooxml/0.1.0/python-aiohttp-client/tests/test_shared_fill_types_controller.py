# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_fill_types import SharedFillTypes


pytestmark = pytest.mark.asyncio

async def test_shared_filltypes_get(client):
    """Test case for shared_filltypes_get

    FillTypes: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/FillTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_filltypes_get_id(client):
    """Test case for shared_filltypes_get_id

    FillTypes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/FillTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_filltypes_typeid_get_type_id(client):
    """Test case for shared_filltypes_typeid_get_type_id

    FillTypes: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/FillTypes/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

