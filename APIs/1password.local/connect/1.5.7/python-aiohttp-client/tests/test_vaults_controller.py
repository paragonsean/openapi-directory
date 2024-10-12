# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.vault import Vault


pytestmark = pytest.mark.asyncio

async def test_get_vault_by_id(client):
    """Test case for get_vault_by_id

    Get Vault details and metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}'.format(vault_uuid='vault_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vaults(client):
    """Test case for get_vaults

    Get all Vaults
    """
    params = [('filter', 'name eq \"Some Vault Name\"')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

