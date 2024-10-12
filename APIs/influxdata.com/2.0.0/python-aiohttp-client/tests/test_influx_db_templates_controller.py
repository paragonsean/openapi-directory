# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.export_template_request import ExportTemplateRequest
from openapi_server.models.list_stacks200_response import ListStacks200Response
from openapi_server.models.patch_stack_request import PatchStackRequest
from openapi_server.models.post_stack_request import PostStackRequest
from openapi_server.models.stack import Stack
from openapi_server.models.template_apply import TemplateApply
from openapi_server.models.template_inner import TemplateInner
from openapi_server.models.template_summary import TemplateSummary


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_apply_template(client):
    """Test case for apply_template

    Apply or dry-run an InfluxDB Template
    """
    body = {"template":{"sources":["sources","sources"],"contents":[{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"},{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"}],"contentType":"contentType"},"dryRun":True,"stackID":"stackID","templates":[{"sources":["sources","sources"],"contents":[{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"},{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"}],"contentType":"contentType"},{"sources":["sources","sources"],"contents":[{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"},{"apiVersion":"apiVersion","meta":{"name":"name"},"spec":"{}"}],"contentType":"contentType"}],"remotes":[{"contentType":"contentType","url":"url"},{"contentType":"contentType","url":"url"}],"actions":[{"action":"skipKind","properties":{"kind":"Bucket"}},{"action":"skipKind","properties":{"kind":"Bucket"}}],"envRefs":{"key":"TemplateApply_envRefs_value"},"secrets":{"key":"secrets"},"orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/templates/apply',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stack(client):
    """Test case for create_stack

    Create a new stack
    """
    body = {"urls":["urls","urls"],"name":"name","description":"description","orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/stacks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_stack(client):
    """Test case for delete_stack

    Delete a stack and associated resources
    """
    params = [('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/stacks/{stack_id}'.format(stack_id='stack_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_template(client):
    """Test case for export_template

    Export a new Influx Template
    """
    body = openapi_server.ExportTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/templates/export',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_stacks(client):
    """Test case for list_stacks

    List all installed InfluxDB templates
    """
    params = [('orgID', 'org_id_example'),
                    ('name', 'name_example'),
                    ('stackID', 'stack_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stacks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_stack(client):
    """Test case for read_stack

    Retrieve a stack
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stacks/{stack_id}'.format(stack_id='stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uninstall_stack(client):
    """Test case for uninstall_stack

    Uninstall an InfluxDB Stack
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/stacks/{stack_id}/uninstall'.format(stack_id='stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stack(client):
    """Test case for update_stack

    Update an InfluxDB Stack
    """
    body = {"name":"name","description":"description","additionalResources":[{"resourceID":"resourceID","templateMetaName":"templateMetaName","kind":"kind"},{"resourceID":"resourceID","templateMetaName":"templateMetaName","kind":"kind"}],"templateURLs":["templateURLs","templateURLs"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/stacks/{stack_id}'.format(stack_id='stack_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

