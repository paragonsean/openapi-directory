# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_profile_response_list import PaginatedProfileResponseList
from openapi_server.models.profile_request_base import ProfileRequestBase
from openapi_server.models.profile_response import ProfileResponse


pytestmark = pytest.mark.asyncio

async def test_profiles_create(client):
    """Test case for profiles_create

    Create a Profile.
    """
    input_request = {"inputData":"inputData","name":"name","description":"description","kvTags":{"key":"kvTags"},"properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{image_id}/profiles'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', image_id='image_id_example'),
        headers=headers,
        json=input_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_list_query(client):
    """Test case for profiles_list_query

    Get a list of Image Profiles.
    """
    params = [('name', 'name_example'),
                    ('description', 'description_example'),
                    ('tags', 'tags_example'),
                    ('properties', 'properties_example'),
                    ('count', 56),
                    ('$skipToken', 'skip_token_example'),
                    ('orderBy', CreatedAtDesc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{image_id}/profiles'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', image_id='image_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_query_by_id(client):
    """Test case for profiles_query_by_id

    Get a Profile.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{image_id}/profiles/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', image_id='image_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

