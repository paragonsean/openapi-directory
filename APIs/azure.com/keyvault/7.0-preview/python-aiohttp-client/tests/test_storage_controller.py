# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_storage_result import BackupStorageResult
from openapi_server.models.deleted_sas_definition_bundle import DeletedSasDefinitionBundle
from openapi_server.models.deleted_storage_bundle import DeletedStorageBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.sas_definition_bundle import SasDefinitionBundle
from openapi_server.models.sas_definition_create_parameters import SasDefinitionCreateParameters
from openapi_server.models.sas_definition_list_result import SasDefinitionListResult
from openapi_server.models.sas_definition_update_parameters import SasDefinitionUpdateParameters
from openapi_server.models.storage_account_create_parameters import StorageAccountCreateParameters
from openapi_server.models.storage_account_regenerte_key_parameters import StorageAccountRegenerteKeyParameters
from openapi_server.models.storage_account_update_parameters import StorageAccountUpdateParameters
from openapi_server.models.storage_bundle import StorageBundle
from openapi_server.models.storage_list_result import StorageListResult
from openapi_server.models.storage_restore_parameters import StorageRestoreParameters


pytestmark = pytest.mark.asyncio

async def test_backup_storage_account(client):
    """Test case for backup_storage_account

    Backs up the specified storage account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/storage/{storage_account_name}/backup'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sas_definition(client):
    """Test case for delete_sas_definition

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/{storage_account_name}/sas/{sas_definition_name}'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_storage_account(client):
    """Test case for delete_storage_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/storage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sas_definition(client):
    """Test case for get_sas_definition

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/storage/{storage_account_name}/sas/{sas_definition_name}'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sas_definitions(client):
    """Test case for get_sas_definitions

    
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/storage/{storage_account_name}/sas'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_storage_account(client):
    """Test case for get_storage_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/storage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_storage_accounts(client):
    """Test case for get_storage_accounts

    
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/storage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_storage_account_key(client):
    """Test case for regenerate_storage_account_key

    
    """
    parameters = {"keyName":"keyName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/storage/{storage_account_name}/regeneratekey'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_storage_account(client):
    """Test case for restore_storage_account

    Restores a backed up storage account to a vault.
    """
    parameters = {"value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/storage/restore',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_sas_definition(client):
    """Test case for set_sas_definition

    
    """
    parameters = {"sasType":"account","validityPeriod":"validityPeriod","templateUri":"templateUri","attributes":{"created":0,"recoveryLevel":"Purgeable","updated":6,"enabled":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/storage/{storage_account_name}/sas/{sas_definition_name}'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_storage_account(client):
    """Test case for set_storage_account

    
    """
    parameters = {"activeKeyName":"activeKeyName","resourceId":"resourceId","regenerationPeriod":"regenerationPeriod","attributes":{"created":0,"recoveryLevel":"Purgeable","updated":6,"enabled":True},"autoRegenerateKey":True,"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/storage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_sas_definition(client):
    """Test case for update_sas_definition

    
    """
    parameters = {"sasType":"account","validityPeriod":"validityPeriod","templateUri":"templateUri","attributes":{"created":0,"recoveryLevel":"Purgeable","updated":6,"enabled":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/storage/{storage_account_name}/sas/{sas_definition_name}'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_storage_account(client):
    """Test case for update_storage_account

    
    """
    parameters = {"activeKeyName":"activeKeyName","regenerationPeriod":"regenerationPeriod","attributes":{"created":0,"recoveryLevel":"Purgeable","updated":6,"enabled":True},"autoRegenerateKey":True,"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/storage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

