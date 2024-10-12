# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_definition import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_definition_attribute import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
from openapi_server.models.content_submission_shared_business_entities_content_definition import ContentSubmissionSharedBusinessEntitiesContentDefinition
from openapi_server.models.content_submission_shared_business_entities_content_definition_attribute import ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute


pytestmark = pytest.mark.asyncio

async def test_content_definitions_delete_content_definition(client):
    """Test case for content_definitions_delete_content_definition

    Delete a ContentDefinition
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentDefinitions/{content_definition_id}'.format(content_definition_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_definitions_delete_content_definition_attribute(client):
    """Test case for content_definitions_delete_content_definition_attribute

    Remove an Attribute from a ContentDefinition
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentDefinitionAttributes/{content_definition_attribute_id}'.format(content_definition_attribute_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_definitions_get_content_definition(client):
    """Test case for content_definitions_get_content_definition

    Get a ContentDefinition by ID
    """
    params = [('includeAttributes', 'include_attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentDefinitions/{content_definition_id}'.format(content_definition_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_definitions_get_content_definition_attributes(client):
    """Test case for content_definitions_get_content_definition_attributes

    Get Attributes for a ContentDefinition
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentDefinitions/{content_definition_id}/Attributes'.format(content_definition_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_definitions_get_content_definitions(client):
    """Test case for content_definitions_get_content_definitions

    Get ContentDefinitions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56),
                    ('includeAttributes', 'include_attributes_example'),
                    ('name', 'name_example'),
                    ('typeID', 56),
                    ('packageTypeID', 'package_type_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_post_content_definition(client):
    """Test case for content_definitions_post_content_definition

    Create a ContentDefinition
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinition()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentDefinitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_post_content_definition_attribute(client):
    """Test case for content_definitions_post_content_definition_attribute

    Add an Attribute to a ContentDefinition
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentDefinitions/{content_definition_id}/Attributes'.format(content_definition_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_post_content_definition_attributes(client):
    """Test case for content_definitions_post_content_definition_attributes

    No Documentation Found.
    """
    body = [openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentDefinitions/{content_definition_id}/Attributes/Batch'.format(content_definition_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_put_content_definition(client):
    """Test case for content_definitions_put_content_definition

    Update a ContentDefinition
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinition()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentDefinitions/{content_definition_id}'.format(content_definition_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_put_content_definition_attribute_async(client):
    """Test case for content_definitions_put_content_definition_attribute_async

    Update an Attribute for a ContentDefinition
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentDefinitionAttributes/{content_definition_attribute_id}'.format(content_definition_attribute_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_definitions_put_content_definition_attributes(client):
    """Test case for content_definitions_put_content_definition_attributes

    No Documentation Found.
    """
    body = [openapi_server.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentDefinitionAttributes/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

