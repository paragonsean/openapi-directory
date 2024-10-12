# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.program import Program
from openapi_server.models.programs import Programs


pytestmark = pytest.mark.asyncio

async def test_get_opted_in_programs(client):
    """Test case for get_opted_in_programs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/program/get_opted_in_programs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opt_in_to_program(client):
    """Test case for opt_in_to_program

    
    """
    body = {"programType":"programType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/program/opt_in',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opt_out_of_program(client):
    """Test case for opt_out_of_program

    
    """
    body = {"programType":"programType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/program/opt_out',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

