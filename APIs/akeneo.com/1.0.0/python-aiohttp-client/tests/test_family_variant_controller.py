# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.family_variants import FamilyVariants
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_families_family_code_variants_request import PatchFamiliesFamilyCodeVariantsRequest
from openapi_server.models.post_families_family_code_variants_request import PostFamiliesFamilyCodeVariantsRequest
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_families_family_code_variants(client):
    """Test case for get_families_family_code_variants

    Get list of family variants
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/families/{family_code}/variants'.format(family_code='family_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_families_family_code_variants_code(client):
    """Test case for get_families_family_code_variants_code

    Get a family variant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/families/{family_code}/variants/{code}'.format(family_code='family_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_families_family_code_variants(client):
    """Test case for patch_families_family_code_variants

    Update/create several family variants
    """
    body = openapi_server.PatchFamiliesFamilyCodeVariantsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/families/{family_code}/variants'.format(family_code='family_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_families_family_code_variants_code(client):
    """Test case for patch_families_family_code_variants_code

    Update/create a family variant
    """
    body = openapi_server.PostFamiliesFamilyCodeVariantsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/families/{family_code}/variants/{code}'.format(family_code='family_code_example', code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

