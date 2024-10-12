# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_groups import AttributeGroups
from openapi_server.models.attribute_groups_post_request import AttributeGroupsPostRequest
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.several_attribute_groups_patch_request import SeveralAttributeGroupsPatchRequest


pytestmark = pytest.mark.asyncio

async def test_attribute_groups_get(client):
    """Test case for attribute_groups_get

    Get an attribute group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/attribute-groups/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_groups_get_list(client):
    """Test case for attribute_groups_get_list

    Get list of attribute groups
    """
    params = [('search', 'search_example'),
                    ('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/attribute-groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_groups_patch(client):
    """Test case for attribute_groups_patch

    Update/create an attribute group
    """
    body = openapi_server.AttributeGroupsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/attribute-groups/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_attribute_groups_post(client):
    """Test case for attribute_groups_post

    Create a new attribute group
    """
    body = openapi_server.AttributeGroupsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/attribute-groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_several_attribute_groups_patch(client):
    """Test case for several_attribute_groups_patch

    Update/create several attribute groups
    """
    body = openapi_server.SeveralAttributeGroupsPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/attribute-groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

