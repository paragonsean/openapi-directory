# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.variable import Variable
from openapi_server.models.variables import Variables


pytestmark = pytest.mark.asyncio

async def test_delete_variables_id(client):
    """Test case for delete_variables_id

    Delete a variable
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/variables/{variable_id}'.format(variable_id='variable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_variables_id_labels_id(client):
    """Test case for delete_variables_id_labels_id

    Delete a label from a variable
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/variables/{variable_id}/labels/{label_id}'.format(variable_id='variable_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables(client):
    """Test case for get_variables

    List all variables
    """
    params = [('org', 'org_example'),
                    ('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/variables',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables_id(client):
    """Test case for get_variables_id

    Retrieve a variable
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/variables/{variable_id}'.format(variable_id='variable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables_id_labels(client):
    """Test case for get_variables_id_labels

    List all labels for a variable
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/variables/{variable_id}/labels'.format(variable_id='variable_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_variables_id(client):
    """Test case for patch_variables_id

    Update a variable
    """
    body = {"createdAt":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","arguments":{"values":{"query":"query","language":"language"},"type":"query"},"links":{"org":"https://openapi-generator.tech","self":"https://openapi-generator.tech","labels":"https://openapi-generator.tech"},"id":"id","orgID":"orgID","selected":["selected","selected"],"labels":[{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}},{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}}],"updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/variables/{variable_id}'.format(variable_id='variable_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_variables(client):
    """Test case for post_variables

    Create a variable
    """
    body = {"createdAt":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","arguments":{"values":{"query":"query","language":"language"},"type":"query"},"links":{"org":"https://openapi-generator.tech","self":"https://openapi-generator.tech","labels":"https://openapi-generator.tech"},"id":"id","orgID":"orgID","selected":["selected","selected"],"labels":[{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}},{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}}],"updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/variables',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_variables_id_labels(client):
    """Test case for post_variables_id_labels

    Add a label to a variable
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/variables/{variable_id}/labels'.format(variable_id='variable_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_variables_id(client):
    """Test case for put_variables_id

    Replace a variable
    """
    body = {"createdAt":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","arguments":{"values":{"query":"query","language":"language"},"type":"query"},"links":{"org":"https://openapi-generator.tech","self":"https://openapi-generator.tech","labels":"https://openapi-generator.tech"},"id":"id","orgID":"orgID","selected":["selected","selected"],"labels":[{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}},{"name":"name","id":"id","orgID":"orgID","properties":{"color":"ffb3b3","description":"this is a description"}}],"updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/variables/{variable_id}'.format(variable_id='variable_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

