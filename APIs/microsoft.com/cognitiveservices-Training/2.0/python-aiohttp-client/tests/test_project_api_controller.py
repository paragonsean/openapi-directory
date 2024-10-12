# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export import Export
from openapi_server.models.image_performance import ImagePerformance
from openapi_server.models.iteration import Iteration
from openapi_server.models.iteration_performance import IterationPerformance
from openapi_server.models.project import Project


pytestmark = pytest.mark.asyncio

async def test_create_project(client):
    """Test case for create_project

    Create a project
    """
    params = [('name', 'My New Project'),
                    ('description', 'A test project'),
                    ('domainId', 'ee85a74c-405e-4adc-bb47-ffa8ca0c9f31')]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Training/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_iteration(client):
    """Test case for delete_iteration

    Delete a specific iteration of a project
    """
    headers = { 
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', iteration_id='e31a14ab-5d78-4f7b-a267-3a1e4fd8a758'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Delete a specific project
    """
    headers = { 
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v2.0/Training/projects/{project_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_iteration(client):
    """Test case for export_iteration

    Export a trained iteration
    """
    params = [('platform', 'tensorflow'),
                    ('flavor', 'flavor_example')]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}/export'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', iteration_id='e31a14ab-5d78-4f7b-a267-3a1e4fd8a758'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_exports(client):
    """Test case for get_exports

    Get the list of exports for a specific iteration
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}/export'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', iteration_id='e31a14ab-5d78-4f7b-a267-3a1e4fd8a758'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_performance_count(client):
    """Test case for get_image_performance_count

    Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}
    """
    params = [('tagIds', ['[\"b5f7e6a2-a481-49a6-afec-a7cef1af3544\"]'])]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}/performance/images/count'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', iteration_id='cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_performances(client):
    """Test case for get_image_performances

    Get image with its prediction for a given project iteration
    """
    params = [('tagIds', ['[\"\"]']),
                    ('orderBy', 'Newest'),
                    ('take', 50),
                    ('skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}/performance/images'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', iteration_id='b7b9d99c-a2c6-4658-9900-a98d2ff5bc66'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_iteration(client):
    """Test case for get_iteration

    Get a specific iteration
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', iteration_id='e31a14ab-5d78-4f7b-a267-3a1e4fd8a758'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_iteration_performance(client):
    """Test case for get_iteration_performance

    Get detailed performance information about an iteration
    """
    params = [('threshold', 0.9),
                    ('overlapThreshold', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}/performance'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', iteration_id='fe1e83c4-6f50-4899-9544-6bb08cf0e15a'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_iterations(client):
    """Test case for get_iterations

    Get iterations for the project
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    Get a specific project
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects/{project_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects(client):
    """Test case for get_projects

    Get your projects
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v2.0/Training/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_train_project(client):
    """Test case for train_project

    Queues project for training
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Training/projects/{project_id}/train'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_iteration(client):
    """Test case for update_iteration

    Update a specific iteration
    """
    body = {"isDefault":True,"exportable":True,"trainedAt":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","lastModified":"2000-01-23T04:56:07.000+00:00","projectId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","domainId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='PATCH',
        path='/customvision/v2.0/Training/projects/{project_id}/iterations/{iteration_id}'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', iteration_id='e31a14ab-5d78-4f7b-a267-3a1e4fd8a758'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_project(client):
    """Test case for update_project

    Update a specific project
    """
    body = {"settings":{"domainId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"created":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","lastModified":"2000-01-23T04:56:07.000+00:00","thumbnailUri":"thumbnailUri"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='PATCH',
        path='/customvision/v2.0/Training/projects/{project_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

