# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_filter import AccountFilter
from openapi_server.models.account_filter_collection import AccountFilterCollection
from openapi_server.models.api_error import ApiError


pytestmark = pytest.mark.asyncio

async def test_account_filters_create_or_update(client):
    """Test case for account_filters_create_or_update

    Create or update an Account Filter
    """
    parameters = {"properties":{"firstQuality":{"bitrate":0},"presentationTimeRange":{"liveBackoffDuration":1,"presentationWindowDuration":5,"timescale":2,"endTimestamp":6,"forceEndTimestamp":True,"startTimestamp":5},"tracks":[{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/accountFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', filter_name='filter_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_filters_delete(client):
    """Test case for account_filters_delete

    Delete an Account Filter.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/accountFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', filter_name='filter_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_filters_get(client):
    """Test case for account_filters_get

    Get an Account Filter.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/accountFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', filter_name='filter_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_filters_list(client):
    """Test case for account_filters_list

    List Account Filters
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/accountFilters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_filters_update(client):
    """Test case for account_filters_update

    Update an Account Filter
    """
    parameters = {"properties":{"firstQuality":{"bitrate":0},"presentationTimeRange":{"liveBackoffDuration":1,"presentationWindowDuration":5,"timescale":2,"endTimestamp":6,"forceEndTimestamp":True,"startTimestamp":5},"tracks":[{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Equal","value":"value"},{"property":"Unknown","operation":"Equal","value":"value"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/accountFilters/{filter_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', filter_name='filter_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

