# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model import Model
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.model_operational_state import ModelOperationalState
from openapi_server.models.paginated_model_list import PaginatedModelList


pytestmark = pytest.mark.asyncio

async def test_m_l_models_delete(client):
    """Test case for m_l_models_delete

    Delete the specified Model.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_l_models_get_metrics(client):
    """Test case for m_l_models_get_metrics

    Retrieve the metrics for a Model.
    """
    params = [('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}/metrics'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_l_models_list_query(client):
    """Test case for m_l_models_list_query

    Query the list of Models in a workspace.
    """
    params = [('name', 'name_example'),
                    ('framework', 'framework_example'),
                    ('description', 'description_example'),
                    ('count', 56),
                    ('$skipToken', 'skip_token_example'),
                    ('tags', 'tags_example'),
                    ('properties', 'properties_example'),
                    ('runId', 'run_id_example'),
                    ('orderBy', CreatedAtDesc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_l_models_patch(client):
    """Test case for m_l_models_patch

    Patch a specific model.
    """
    patch = [openapi_server.JsonPatchOperation()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        json=patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_l_models_query_by_id(client):
    """Test case for m_l_models_query_by_id

    Gets a model.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_l_models_register(client):
    """Test case for m_l_models_register

    Register a model.
    """
    model = {"modifiedTime":"2000-01-23T04:56:07.000+00:00","parentModelId":"sklearn_mnist_root:1","description":"A mnist model, first version.","datasets":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"mimeType":"mimeType","version":1,"url":"url","framework":"framework","frameworkVersion":"frameworkVersion","name":"sklearn_mnist","createdTime":"2000-01-23T04:56:07.000+00:00","kvTags":{"key":"kvTags"},"id":"sklearn_mnist:1","runId":"runId","unpack":True,"experimentName":"experimentName","properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/modelmanagement/v1.0/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', workspace='workspace_example'),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

