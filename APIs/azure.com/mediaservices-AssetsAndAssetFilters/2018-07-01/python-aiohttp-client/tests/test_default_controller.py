# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.asset import Asset
from openapi_server.models.asset_collection import AssetCollection
from openapi_server.models.asset_container_sas import AssetContainerSas
from openapi_server.models.asset_filter import AssetFilter
from openapi_server.models.asset_filter_collection import AssetFilterCollection
from openapi_server.models.list_container_sas_input import ListContainerSasInput
from openapi_server.models.list_streaming_locators_response import ListStreamingLocatorsResponse
from openapi_server.models.storage_encrypted_asset_decryption_data import StorageEncryptedAssetDecryptionData


pytestmark = pytest.mark.asyncio

async def test_asset_filters_create_or_update(client):
    """Test case for asset_filters_create_or_update

    Create or update an Asset Filter
    """
    parameters = {"properties":{"firstQuality":{"bitrate":0},"presentationTimeRange":{"liveBackoffDuration":1,"presentationWindowDuration":5,"timescale":2,"endTimestamp":6,"forceEndTimestamp":True,"startTimestamp":5},"tracks":[{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/assetFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example', filter_name='filter_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_filters_delete(client):
    """Test case for asset_filters_delete

    Delete an Asset Filter.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/assetFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example', filter_name='filter_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_filters_get(client):
    """Test case for asset_filters_get

    Get an Asset Filter.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/assetFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example', filter_name='filter_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_filters_list(client):
    """Test case for asset_filters_list

    List Asset Filters
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/assetFilters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asset_filters_update(client):
    """Test case for asset_filters_update

    Update an Asset Filter
    """
    parameters = {"properties":{"firstQuality":{"bitrate":0},"presentationTimeRange":{"liveBackoffDuration":1,"presentationWindowDuration":5,"timescale":2,"endTimestamp":6,"forceEndTimestamp":True,"startTimestamp":5},"tracks":[{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/assetFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example', filter_name='filter_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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

async def test_assets_list_streaming_locators(client):
    """Test case for assets_list_streaming_locators

    List Streaming Locators
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/assets/{asset_name}/listStreamingLocators'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', asset_name='asset_name_example'),
        headers=headers,
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

