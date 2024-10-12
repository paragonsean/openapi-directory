# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vault_extended_info_resource import VaultExtendedInfoResource


pytestmark = pytest.mark.asyncio

async def test_vault_extended_info_create_or_update(client):
    """Test case for vault_extended_info_create_or_update

    
    """
    resource_resource_extended_info_details = {"properties":{"encryptionKeyThumbprint":"encryptionKeyThumbprint","encryptionKey":"encryptionKey","integrityKey":"integrityKey","algorithm":"algorithm"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/extendedInformation/vaultExtendedInfo'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        json=resource_resource_extended_info_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vault_extended_info_get(client):
    """Test case for vault_extended_info_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/extendedInformation/vaultExtendedInfo'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vault_extended_info_update(client):
    """Test case for vault_extended_info_update

    
    """
    resource_resource_extended_info_details = {"properties":{"encryptionKeyThumbprint":"encryptionKeyThumbprint","encryptionKey":"encryptionKey","integrityKey":"integrityKey","algorithm":"algorithm"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/extendedInformation/vaultExtendedInfo'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        json=resource_resource_extended_info_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

