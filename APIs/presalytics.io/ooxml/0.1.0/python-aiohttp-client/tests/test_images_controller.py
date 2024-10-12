# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_pictures import SharedPictures
from openapi_server.models.shared_pictures_details import SharedPicturesDetails


pytestmark = pytest.mark.asyncio

async def test_shared_images_childobjects_get_id(client):
    """Test case for shared_images_childobjects_get_id

    Shared: Get Dependent Objects Tree
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Images/ChildObjects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_images_details_get_id(client):
    """Test case for shared_images_details_get_id

    Shared: Get Details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Images/Details/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_images_get_id(client):
    """Test case for shared_images_get_id

    Images: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Images/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_images_getimage_put_id(client):
    """Test case for shared_images_getimage_put_id

    Image: Download Image
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Images/GetImage/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_images_openofficexml_get_id_updated(client):
    """Test case for shared_images_openofficexml_get_id_updated

    Shared: Get Underlying Xml
    """
    params = [('updated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Images/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shared_images_openofficexml_put_id(client):
    """Test case for shared_images_openofficexml_put_id

    Shared: Modify Underlying Xml
    """
    body = {"openOfficeXml":"openOfficeXml","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Images/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_images_svg_get_id_use_cache(client):
    """Test case for shared_images_svg_get_id_use_cache

    Shared: Get Svg file
    """
    params = [('use_cache', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Images/Svg/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

