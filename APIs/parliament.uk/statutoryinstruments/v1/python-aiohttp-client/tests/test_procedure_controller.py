# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.procedure_details_resource import ProcedureDetailsResource
from openapi_server.models.procedure_resource_collection import ProcedureResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_procedures_by_id_v1(client):
    """Test case for get_procedures_by_id_v1

    Returns procedure by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Procedure/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_procedures_v1(client):
    """Test case for get_procedures_v1

    Returns all procedures.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Procedure',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

