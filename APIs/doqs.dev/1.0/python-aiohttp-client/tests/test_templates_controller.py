# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.fill_template_request import FillTemplateRequest
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_ok_http_url import ResponseOkHttpUrl
from openapi_server.models.response_ok_list_apps_api_routes_templates_template import ResponseOkListAppsApiRoutesTemplatesTemplate
from openapi_server.models.response_ok_none_type import ResponseOkNoneType
from openapi_server.models.response_ok_template import ResponseOkTemplate
from openapi_server.models.update_template_request import UpdateTemplateRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create(client):
    """Test case for create

    Create
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apiKeyAuth': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/templates',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_templates_id_delete(client):
    """Test case for delete_templates_id_delete

    Delete 
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/templates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fill(client):
    """Test case for fill

    Fill
    """
    body = {"data":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/{id}/fill'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Get Template
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/templates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_templates_id_file_get(client):
    """Test case for get_file_templates_id_file_get

    Get File
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/templates/{id}/file'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    List 
    """
    params = [('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    Update
    """
    body = {"name":"name","fields":[{"h_align":"","color":"black","bbox":{"width":1.6027456183070403,"x":0.14658129805029452,"y":0.5962133916683182,"height":1.0800828190461012},"font_size":0,"format":"format","locale":"en_US","type":"date","required":True,"cells":False,"cell_count":0,"name":"name","v_align":"","page":0,"cell_offset":0,"font":""},{"h_align":"","color":"black","bbox":{"width":1.6027456183070403,"x":0.14658129805029452,"y":0.5962133916683182,"height":1.0800828190461012},"font_size":0,"format":"format","locale":"en_US","type":"date","required":True,"cells":False,"cell_count":0,"name":"name","v_align":"","page":0,"cell_offset":0,"font":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/templates/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

