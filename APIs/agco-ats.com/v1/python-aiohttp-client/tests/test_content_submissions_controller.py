# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_submission import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_submission_attribute import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
from openapi_server.models.build_system_shared_interfaces_i_job_run import BuildSystemSharedInterfacesIJobRun
from openapi_server.models.content_submission_shared_business_entities_content_submission import ContentSubmissionSharedBusinessEntitiesContentSubmission
from openapi_server.models.content_submission_shared_business_entities_content_submission_attribute import ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute


pytestmark = pytest.mark.asyncio

async def test_content_submissions_delete_content_submission(client):
    """Test case for content_submissions_delete_content_submission

    Delete a ContentSubmission
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentSubmissions/{content_submission_id}'.format(content_submission_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submissions_delete_content_submission_attribute(client):
    """Test case for content_submissions_delete_content_submission_attribute

    Remove an Attribute from a ContentSubmission
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentSubmissionAttributes/{content_submission_attribute_id}'.format(content_submission_attribute_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submissions_get_content_submission(client):
    """Test case for content_submissions_get_content_submission

    Get a ContentSubmission by ID
    """
    params = [('includeAttributes', 'include_attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissions/{content_submission_id}'.format(content_submission_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submissions_get_content_submission_attributes(client):
    """Test case for content_submissions_get_content_submission_attributes

    Get Attributes for a ContentSubmission
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissions/{content_submission_id}/Attributes'.format(content_submission_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submissions_get_content_submission_status(client):
    """Test case for content_submissions_get_content_submission_status

    Get the status of a ContentSubmission
    """
    params = [('includeActivityRunDetails', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissions/{content_submission_id}/Status'.format(content_submission_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submissions_get_content_submissions(client):
    """Test case for content_submissions_get_content_submissions

    Get ContentSubmissions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56),
                    ('contentDefinitionID', 56),
                    ('includeAttributes', 'include_attributes_example'),
                    ('releaseID', 56),
                    ('typeID', 56),
                    ('version', 56),
                    ('includeDefinition', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_post_content_submission(client):
    """Test case for content_submissions_post_content_submission

    Create a ContentSubmission
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmission()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentSubmissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_post_content_submission_attribute(client):
    """Test case for content_submissions_post_content_submission_attribute

    Add an Attribute to a ContentSubmission
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentSubmissions/{content_submission_id}/Attributes'.format(content_submission_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_post_content_submission_attributes(client):
    """Test case for content_submissions_post_content_submission_attributes

    No Documentation Found.
    """
    body = [openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentSubmissions/{content_submission_id}/Attributes/Batch'.format(content_submission_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_put_content_submission(client):
    """Test case for content_submissions_put_content_submission

    Update a ContentSubmission
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmission()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentSubmissions/{content_submission_id}'.format(content_submission_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_put_content_submission_attribute_async(client):
    """Test case for content_submissions_put_content_submission_attribute_async

    Update an Attribute for a ContentSubmission
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentSubmissionAttributes/{content_submission_attribute_id}'.format(content_submission_attribute_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submissions_put_content_submission_attributes(client):
    """Test case for content_submissions_put_content_submission_attributes

    No Documentation Found.
    """
    body = [openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentSubmissionAttributes/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

