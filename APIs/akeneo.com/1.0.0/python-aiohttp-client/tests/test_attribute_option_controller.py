# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_options import AttributeOptions
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_attributes_attribute_code_options_request import PatchAttributesAttributeCodeOptionsRequest
from openapi_server.models.post_attributes_attribute_code_options_request import PostAttributesAttributeCodeOptionsRequest
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_attributes_attribute_code_options(client):
    """Test case for get_attributes_attribute_code_options

    Get list of attribute options
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attributes_attribute_code_options_code(client):
    """Test case for get_attributes_attribute_code_options_code

    Get an attribute option
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/attributes/{attribute_code}/options/{code}'.format(attribute_code='attribute_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_attributes_attribute_code_options(client):
    """Test case for patch_attributes_attribute_code_options

    Update/create several attribute options
    """
    body = openapi_server.PatchAttributesAttributeCodeOptionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_attributes_attribute_code_options_code(client):
    """Test case for patch_attributes_attribute_code_options_code

    Update/create an attribute option
    """
    body = openapi_server.PostAttributesAttributeCodeOptionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/attributes/{attribute_code}/options/{code}'.format(attribute_code='attribute_code_example', code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_attributes_attribute_code_options(client):
    """Test case for post_attributes_attribute_code_options

    Create a new attribute option
    """
    body = openapi_server.PostAttributesAttributeCodeOptionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

