# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_template200_response import CreateTemplate200Response
from openapi_server.models.delete_template200_response import DeleteTemplate200Response
from openapi_server.models.get_editor_url200_response import GetEditorUrl200Response
from openapi_server.models.get_templates200_response import GetTemplates200Response
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.template_definition_new import TemplateDefinitionNew


pytestmark = pytest.mark.asyncio

async def test_copy_template(client):
    """Test case for copy_template

    Copy template
    """
    params = [('templateId', 19375),
                    ('name', 'My copied template')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/templates/templateId/copy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_template(client):
    """Test case for create_template

    Create template
    """
    body = {"layout":{"margins":{"top":0.5,"left":0.5,"bottom":0.5,"right":0.5},"orientation":"portrait","unit":"cm","emptyLabels":0,"format":"A4","width":21,"repeatLayout":{"format":"A4","width":21,"height":29.7},"rotaion":0,"height":29.7},"pages":[{"margins":{"bottom":0.5,"right":0.5},"components":[{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1},{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1}],"width":21,"height":29.7},{"margins":{"bottom":0.5,"right":0.5},"components":[{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1},{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1}],"width":21,"height":29.7}],"isDraft":True,"name":"Invoice template","tags":["invoice","orders"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/templates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_template(client):
    """Test case for delete_template

    Delete template
    """
    params = [('templateId', 19375)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/templates/templateId',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editor_url(client):
    """Test case for get_editor_url

    Open editor
    """
    body = None
    params = [('templateId', 19375),
                    ('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/templates/templateId/editor',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template(client):
    """Test case for get_template

    Get template
    """
    params = [('templateId', 19375)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/templates/templateId',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_templates(client):
    """Test case for get_templates

    Get templates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/templates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_template(client):
    """Test case for update_template

    Update template
    """
    body = {"layout":{"margins":{"top":0.5,"left":0.5,"bottom":0.5,"right":0.5},"orientation":"portrait","unit":"cm","emptyLabels":0,"format":"A4","width":21,"repeatLayout":{"format":"A4","width":21,"height":29.7},"rotaion":0,"height":29.7},"pages":[{"margins":{"bottom":0.5,"right":0.5},"components":[{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1},{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1}],"width":21,"height":29.7},{"margins":{"bottom":0.5,"right":0.5},"components":[{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1},{"zindex":102,"top":4.2,"left":2.5,"dataIndex":"line_items","width":3.5,"cls":"labelComponent","id":"component-12313","value":"${price}","height":1}],"width":21,"height":29.7}],"isDraft":True,"name":"Invoice template","tags":["invoice","orders"]}
    params = [('templateId', 19375)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/templates/templateId',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

