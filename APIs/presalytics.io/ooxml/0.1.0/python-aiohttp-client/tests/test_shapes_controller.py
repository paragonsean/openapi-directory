# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.slide_shapes import SlideShapes
from openapi_server.models.slide_shapes_details import SlideShapesDetails


pytestmark = pytest.mark.asyncio

async def test_slides_shapes_childobjects_get_id(client):
    """Test case for slides_shapes_childobjects_get_id

    Slides: Get Dependent Objects Tree
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shapes/ChildObjects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slides_shapes_details_get_id(client):
    """Test case for slides_shapes_details_get_id

    Slides: Get Details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shapes/Details/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slides_shapes_get_id(client):
    """Test case for slides_shapes_get_id

    Shapes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shapes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slides_shapes_openofficexml_get_id_updated(client):
    """Test case for slides_shapes_openofficexml_get_id_updated

    Slides: Get Underlying Xml
    """
    params = [('updated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shapes/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_slides_shapes_openofficexml_put_id(client):
    """Test case for slides_shapes_openofficexml_put_id

    Slides: Modify Underlying Xml
    """
    body = {"openOfficeXml":"openOfficeXml","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Shapes/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slides_shapes_svg_get_id_use_cache(client):
    """Test case for slides_shapes_svg_get_id_use_cache

    Slides: Get Svg file
    """
    params = [('use_cache', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shapes/Svg/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

