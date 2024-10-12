# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.app_category_response import AppCategoryResponse
from openapi_server.models.app_info_localizations_response import AppInfoLocalizationsResponse
from openapi_server.models.app_info_response import AppInfoResponse
from openapi_server.models.app_info_update_request import AppInfoUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_infos_age_rating_declaration_get_to_one_related(client):
    """Test case for app_infos_age_rating_declaration_get_to_one_related

    
    """
    params = [('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/ageRatingDeclaration'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_app_info_localizations_get_to_many_related(client):
    """Test case for app_infos_app_info_localizations_get_to_many_related

    
    """
    params = [('filter[locale]', ['filter_locale_example']),
                    ('fields[appInfos]', ['fields_app_infos_example']),
                    ('fields[appInfoLocalizations]', ['fields_app_info_localizations_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/appInfoLocalizations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_get_instance(client):
    """Test case for app_infos_get_instance

    
    """
    params = [('fields[appInfos]', ['fields_app_infos_example']),
                    ('include', ['include_example']),
                    ('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example']),
                    ('fields[appCategories]', ['fields_app_categories_example']),
                    ('fields[appInfoLocalizations]', ['fields_app_info_localizations_example']),
                    ('limit[appInfoLocalizations]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_primary_category_get_to_one_related(client):
    """Test case for app_infos_primary_category_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/primaryCategory'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_primary_subcategory_one_get_to_one_related(client):
    """Test case for app_infos_primary_subcategory_one_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/primarySubcategoryOne'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_primary_subcategory_two_get_to_one_related(client):
    """Test case for app_infos_primary_subcategory_two_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/primarySubcategoryTwo'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_secondary_category_get_to_one_related(client):
    """Test case for app_infos_secondary_category_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/secondaryCategory'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_secondary_subcategory_one_get_to_one_related(client):
    """Test case for app_infos_secondary_subcategory_one_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/secondarySubcategoryOne'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_secondary_subcategory_two_get_to_one_related(client):
    """Test case for app_infos_secondary_subcategory_two_get_to_one_related

    
    """
    params = [('fields[appCategories]', ['fields_app_categories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appInfos/{id}/secondarySubcategoryTwo'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_infos_update_instance(client):
    """Test case for app_infos_update_instance

    
    """
    body = {"data":{"relationships":{"secondaryCategory":{"data":{"id":"id","type":"appCategories"}},"primaryCategory":{"data":{"id":"id","type":"appCategories"}},"secondarySubcategoryOne":{"data":{"id":"id","type":"appCategories"}},"primarySubcategoryTwo":{"data":{"id":"id","type":"appCategories"}},"secondarySubcategoryTwo":{"data":{"id":"id","type":"appCategories"}},"primarySubcategoryOne":{"data":{"id":"id","type":"appCategories"}}},"id":"id","type":"appInfos"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appInfos/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

