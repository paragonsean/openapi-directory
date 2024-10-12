# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.update_system_models_checkin_result import UpdateSystemModelsCheckinResult


pytestmark = pytest.mark.asyncio

async def test_update_system_get_cached_files(client):
    """Test case for update_system_get_cached_files

    Get a list of Cached Files installed on the client Machine.
    """
    params = [('Expired', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients/{client_id}/CachedFiles'.format(client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_system_get_checkin(client):
    """Test case for update_system_get_checkin

    Checks the Client ID into the Update System.
    """
    params = [('ClientID', 'client_id_example'),
                    ('Preview', True),
                    ('RunAllInventories', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateSystem',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

