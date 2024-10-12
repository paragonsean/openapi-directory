# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_create import DocumentCreate
from openapi_server.models.document_update import DocumentUpdate
from openapi_server.models.documents import Documents
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse


pytestmark = pytest.mark.asyncio

async def test_delete_documents_templates_id(client):
    """Test case for delete_documents_templates_id

    Delete a template
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/documents/templates/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_documents_templates_id_labels_id(client):
    """Test case for delete_documents_templates_id_labels_id

    Delete a label from a template
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/documents/templates/{template_id}/labels/{label_id}'.format(template_id='template_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents_templates(client):
    """Test case for get_documents_templates

    List all templates
    """
    params = [('org', 'org_example'),
                    ('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/documents/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents_templates_id(client):
    """Test case for get_documents_templates_id

    Retrieve a template
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/documents/templates/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents_templates_id_labels(client):
    """Test case for get_documents_templates_id_labels

    List all labels for a template
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/documents/templates/{template_id}/labels'.format(template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_documents_templates(client):
    """Test case for post_documents_templates

    Create a template
    """
    body = {"org":"org","meta":{"createdAt":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","templateID":"templateID","type":"type","version":"version","updatedAt":"2000-01-23T04:56:07.000+00:00"},"content":"{}","orgID":"orgID","labels":["labels","labels"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/documents/templates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_documents_templates_id_labels(client):
    """Test case for post_documents_templates_id_labels

    Add a label to a template
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/documents/templates/{template_id}/labels'.format(template_id='template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_documents_templates_id(client):
    """Test case for put_documents_templates_id

    Update a template
    """
    body = {"meta":{"createdAt":"2000-01-23T04:56:07.000+00:00","name":"name","description":"description","templateID":"templateID","type":"type","version":"version","updatedAt":"2000-01-23T04:56:07.000+00:00"},"content":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/documents/templates/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

