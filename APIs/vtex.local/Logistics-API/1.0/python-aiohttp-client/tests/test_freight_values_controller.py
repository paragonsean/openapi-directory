# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_freight_values_request import CreateUpdateFreightValuesRequest
from openapi_server.models.freight_values200_response_inner import FreightValues200ResponseInner


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_freight_values(client):
    """Test case for create_update_freight_values

    Create/update freight values
    """
    body = [openapi_server.CreateUpdateFreightValuesRequest()]
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/freights/{carrier_id}/values/update'.format(carrier_id='carrier123'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_freight_values(client):
    """Test case for freight_values

    List freight values
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/freights/{carrier_id}/{cep}/values'.format(carrier_id='carrier-123', cep='12345000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

