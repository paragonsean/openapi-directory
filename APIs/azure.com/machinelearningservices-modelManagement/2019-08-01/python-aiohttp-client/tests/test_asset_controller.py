# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_asset_list import PaginatedAssetList


pytestmark = pytest.mark.asyncio

async def test_assets_create(client):
    """Test case for assets_create

    Create an Asset.
    """
    asset = {"meta":{"key":"meta"},"name":"name","createdTime":"2000-01-23T04:56:07.000+00:00","description":"description","kvTags":{"key":"kvTags"},"id":"id","runid":"runid","properties":{"key":"properties"},"artifacts":[{"prefix":"prefix","id":"id"},{"prefix":"prefix","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        json=asset,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_delete(client):
    """Test case for assets_delete

    Delete an Asset.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_list_query(client):
    """Test case for assets_list_query

    Query the list of Assets in a workspace.
    """
    params = [('runId', 'run_id_example'),
                    ('name', 'name_example'),
                    ('count', 56),
                    ('$skipToken', 'skip_token_example'),
                    ('tags', 'tags_example'),
                    ('properties', 'properties_example'),
                    ('orderby', CreatedAtDesc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_patch(client):
    """Test case for assets_patch

    Update an Asset.
    """
    patch = [openapi_server.JsonPatchOperation()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        json=patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assets_query_by_id(client):
    """Test case for assets_query_by_id

    Get an Asset.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

