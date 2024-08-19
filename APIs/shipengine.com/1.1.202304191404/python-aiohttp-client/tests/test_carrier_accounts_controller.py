# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.carrier_name import CarrierName
from openapi_server.models.carrier_name_with_settings import CarrierNameWithSettings
from openapi_server.models.connect_carrier_request_body import ConnectCarrierRequestBody
from openapi_server.models.connect_carrier_response_body import ConnectCarrierResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_carrier_settings_response_body import GetCarrierSettingsResponseBody
from openapi_server.models.update_carrier_settings_request_body import UpdateCarrierSettingsRequestBody


pytestmark = pytest.mark.asyncio

async def test_connect_carrier(client):
    """Test case for connect_carrier

    Connect a carrier account
    """
    body = openapi_server.ConnectCarrierRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/carriers/{carrier_name}'.format(carrier_name=openapi_server.CarrierName()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disconnect_carrier(client):
    """Test case for disconnect_carrier

    Disconnect a carrier
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/connections/carriers/{carrier_name}/{carrier_id}'.format(carrier_name=openapi_server.CarrierName(), carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_carrier_settings(client):
    """Test case for get_carrier_settings

    Get carrier settings
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/connections/carriers/{carrier_name}/{carrier_id}/settings'.format(carrier_name=openapi_server.CarrierNameWithSettings(), carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_carrier_settings(client):
    """Test case for update_carrier_settings

    Update carrier settings
    """
    body = openapi_server.UpdateCarrierSettingsRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/connections/carriers/{carrier_name}/{carrier_id}/settings'.format(carrier_name=openapi_server.CarrierNameWithSettings(), carrier_id='se-28529731'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

