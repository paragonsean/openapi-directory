# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validate_probe_input import ValidateProbeInput
from openapi_server.models.validate_probe_output import ValidateProbeOutput


pytestmark = pytest.mark.asyncio

async def test_validate_probe(client):
    """Test case for validate_probe

    
    """
    validate_probe_input = {"probeURL":"probeURL"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Cdn/validateProbe'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=validate_probe_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

