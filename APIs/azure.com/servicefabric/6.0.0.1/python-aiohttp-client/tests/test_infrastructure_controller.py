# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError


pytestmark = pytest.mark.asyncio

async def test_invoke_infrastructure_command(client):
    """Test case for invoke_infrastructure_command

    Invokes an administrative command on the given Infrastructure Service instance.
    """
    params = [('api-version', 6.0),
                    ('Command', 'command_example'),
                    ('ServiceId', 'service_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/InvokeInfrastructureCommand',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoke_infrastructure_query(client):
    """Test case for invoke_infrastructure_query

    Invokes a read-only query on the given infrastructure service instance.
    """
    params = [('api-version', 6.0),
                    ('Command', 'command_example'),
                    ('ServiceId', 'service_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/InvokeInfrastructureQuery',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

