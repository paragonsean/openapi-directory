# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_types import AssociationTypes
from openapi_server.models.association_types_post_request import AssociationTypesPostRequest
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.several_association_types_patch_request import SeveralAssociationTypesPatchRequest


pytestmark = pytest.mark.asyncio

async def test_association_types_get(client):
    """Test case for association_types_get

    Get an association type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/association-types/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_association_types_get_list(client):
    """Test case for association_types_get_list

    Get a list of association types
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/association-types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_association_types_patch(client):
    """Test case for association_types_patch

    Update/create an association type
    """
    body = openapi_server.AssociationTypesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/association-types/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_association_types_post(client):
    """Test case for association_types_post

    Create a new association type
    """
    body = openapi_server.AssociationTypesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/association-types',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_several_association_types_patch(client):
    """Test case for several_association_types_patch

    Update/create several association types
    """
    body = openapi_server.SeveralAssociationTypesPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/association-types',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

