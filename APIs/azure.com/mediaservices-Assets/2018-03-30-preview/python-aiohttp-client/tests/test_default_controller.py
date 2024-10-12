# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_collection import AssetCollection
from openapi_server.models.asset_container_sas import AssetContainerSas
from openapi_server.models.asset_storage_encryption_key import AssetStorageEncryptionKey
from openapi_server.models.assets_list_default_response import AssetsListDefaultResponse
from openapi_server.models.list_container_sas_input import ListContainerSasInput


pytestmark = pytest.mark.asyncio

async def test_assets_create_or_update(client):
    """Test case for assets_create_or_update

    Create or update an Asset
    """
    parameters = {"properties":{"alternateId":"alternateId","container":"container","assetId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","created":"2000-01-23T04:56:07.000+00:00","storageEncryptionFormat":"None","description":"description","storageAccountName":"storageAccountName","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_delete(client):
    """Test case for assets_delete

    Delete an Asset.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_get(client):
    """Test case for assets_get

    Get an Asset
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_get_encryption_key(client):
    """Test case for assets_get_encryption_key

    Gets the Asset storage key
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/getEncryptionKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_list(client):
    """Test case for assets_list

    List Assets
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_list_container_sas(client):
    """Test case for assets_list_container_sas

    List the Asset URLs
    """
    parameters = {"permissions":"Read","expiryTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/listContainerSas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_update(client):
    """Test case for assets_update

    Update an Asset
    """
    parameters = {"properties":{"alternateId":"alternateId","container":"container","assetId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","created":"2000-01-23T04:56:07.000+00:00","storageEncryptionFormat":"None","description":"description","storageAccountName":"storageAccountName","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

