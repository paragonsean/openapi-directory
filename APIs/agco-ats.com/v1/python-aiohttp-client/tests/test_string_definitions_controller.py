# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_string_definition import APIIPagedResponseGlobalResourcesSharedModelsStringDefinition
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_string_definition import GlobalResourcesSharedModelsStringDefinition


pytestmark = pytest.mark.asyncio

async def test_string_definitions_get_definition(client):
    """Test case for string_definitions_get_definition

    Get a paged response of Global String Definitions.
    """
    params = [('includeTranslations', True),
                    ('includeDeletedLanguages', True),
                    ('languageIds', 'language_ids_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/StringDefinitions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_string_definitions_get_definitions(client):
    """Test case for string_definitions_get_definitions

    Get a paged response of Global String Definitions.
    """
    params = [('limit', 56),
                    ('modifiedAfterTimestamp', 'modified_after_timestamp_example'),
                    ('includeTranslations', True),
                    ('stringText', 'string_text_example'),
                    ('descriptionText', 'description_text_example'),
                    ('useFullText', True),
                    ('includeDeletedLanguages', True),
                    ('languageIds', 'language_ids_example'),
                    ('stringIds', 'string_ids_example'),
                    ('matchingTranslationsOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/StringDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_string_definitions_post_definition(client):
    """Test case for string_definitions_post_definition

    Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing.
    """
    body = [openapi_server.GlobalResourcesSharedModelsStringDefinition()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/StringDefinitions/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_string_definitions_update_definitions(client):
    """Test case for string_definitions_update_definitions

    Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation.
    """
    body = [openapi_server.GlobalResourcesSharedModelsStringDefinition()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/StringDefinitions/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

