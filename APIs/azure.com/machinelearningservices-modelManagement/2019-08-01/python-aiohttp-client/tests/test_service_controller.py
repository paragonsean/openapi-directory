# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_keys import AuthKeys
from openapi_server.models.auth_token import AuthToken
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_service_list import PaginatedServiceList
from openapi_server.models.regenerate_service_keys_request import RegenerateServiceKeysRequest
from openapi_server.models.service_response_base import ServiceResponseBase


pytestmark = pytest.mark.asyncio

async def test_services_create(client):
    """Test case for services_create

    Create a Service.
    """
    request = {"deploymentType":"HttpRealtimeEndpoint","computeType":"AKS","imageId":"imageId","environmentImageRequest":{"environment":{"python":{"baseCondaEnvironment":"baseCondaEnvironment","userManagedDependencies":True,"condaDependencies":"{}","interpreterPath":"interpreterPath"},"spark":{"repositories":["repositories","repositories"],"precachePackages":True,"packages":[{"artifact":"artifact","version":"version","group":"group"},{"artifact":"artifact","version":"version","group":"group"}]},"environmentVariables":{"key":"environmentVariables"},"inferencingStackVersion":"latest","name":"mydevenvironment","version":"1","docker":{"gpuSupport":False,"shmSize":"1g","sharedVolumes":True,"baseImage":"ubuntu:latest","arguments":["arguments","arguments"],"baseDockerfile":"FROM ubuntu:latest\r\nRUN echo \"Hello world!\"","enabled":True,"baseImageRegistry":{"password":"password","address":"address","username":"username"}}},"assets":[{"id":"id","mimeType":"mimeType","unpack":True,"url":"url"},{"id":"id","mimeType":"mimeType","unpack":True,"url":"url"}],"driverProgram":"driverProgram","modelIds":"[mymodel:1, mymodel:2]"},"keys":{"secondaryKey":"secondaryKey","primaryKey":"primaryKey"},"name":"name","description":"description","kvTags":{"key":"kvTags"},"location":"location","properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete(client):
    """Test case for services_delete

    Delete a Service.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_service_token(client):
    """Test case for services_get_service_token

    Generate Service Access Token.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/token'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_query(client):
    """Test case for services_list_query

    Query the list of Services in a Workspace.
    """
    params = [('imageId', 'image_id_example'),
                    ('imageName', 'image_name_example'),
                    ('modelId', 'model_id_example'),
                    ('modelName', 'model_name_example'),
                    ('name', 'name_example'),
                    ('count', 56),
                    ('computeType', 'compute_type_example'),
                    ('$skipToken', 'skip_token_example'),
                    ('tags', 'tags_example'),
                    ('properties', 'properties_example'),
                    ('expand', False),
                    ('orderby', UpdatedAtDesc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_service_keys(client):
    """Test case for services_list_service_keys

    Lists Service keys.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_patch(client):
    """Test case for services_patch

    Patch a Service.
    """
    patch = [openapi_server.JsonPatchOperation()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        json=patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_query_by_id(client):
    """Test case for services_query_by_id

    Get a Service.
    """
    params = [('expand', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_regenerate_service_keys(client):
    """Test case for services_regenerate_service_keys

    Regenerate Service Keys.
    """
    request = {"keyValue":"keyValue","keyType":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

