# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_sas_definition_bundle import DeletedSasDefinitionBundle
from openapi_server.models.deleted_sas_definition_list_result import DeletedSasDefinitionListResult
from openapi_server.models.deleted_storage_bundle import DeletedStorageBundle
from openapi_server.models.deleted_storage_list_result import DeletedStorageListResult
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.sas_definition_bundle import SasDefinitionBundle
from openapi_server.models.storage_bundle import StorageBundle


pytestmark = pytest.mark.asyncio

async def test_get_deleted_sas_definition(client):
    """Test case for get_deleted_sas_definition

    Gets the specified deleted sas definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedstorage/{storage_account_name}/sas/{sas_definition_name}'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_sas_definitions(client):
    """Test case for get_deleted_sas_definitions

    Lists deleted SAS definitions for the specified vault and storage account.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedstorage/{storage_account_name}/sas'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_storage_account(client):
    """Test case for get_deleted_storage_account

    Gets the specified deleted storage account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedstorage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_storage_accounts(client):
    """Test case for get_deleted_storage_accounts

    Lists deleted storage accounts for the specified vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedstorage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purge_deleted_storage_account(client):
    """Test case for purge_deleted_storage_account

    Permanently deletes the specified storage account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/deletedstorage/{storage_account_name}'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_deleted_sas_definition(client):
    """Test case for recover_deleted_sas_definition

    Recovers the deleted SAS definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/deletedstorage/{storage_account_name}/sas/{sas_definition_name}/recover'.format(storage_account_name='storage_account_name_example', sas_definition_name='sas_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_deleted_storage_account(client):
    """Test case for recover_deleted_storage_account

    Recovers the deleted storage account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/deletedstorage/{storage_account_name}/recover'.format(storage_account_name='storage_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

