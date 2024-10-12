# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.theme_themes import ThemeThemes
from openapi_server.models.theme_themes_details import ThemeThemesDetails


pytestmark = pytest.mark.asyncio

async def test_theme_themes_childobjects_get_id(client):
    """Test case for theme_themes_childobjects_get_id

    Theme: Get Dependent Objects Tree
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/ChildObjects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_theme_themes_details_get_id(client):
    """Test case for theme_themes_details_get_id

    Theme: Get Details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/Details/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_theme_themes_get_id(client):
    """Test case for theme_themes_get_id

    Themes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_theme_themes_openofficexml_get_id_updated(client):
    """Test case for theme_themes_openofficexml_get_id_updated

    Theme: Get Underlying Xml
    """
    params = [('updated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_theme_themes_openofficexml_put_id(client):
    """Test case for theme_themes_openofficexml_put_id

    Theme: Modify Underlying Xml
    """
    body = {"openOfficeXml":"openOfficeXml","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Themes/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_theme_themes_svg_get_id_use_cache(client):
    """Test case for theme_themes_svg_get_id_use_cache

    Theme: Get Svg file
    """
    params = [('use_cache', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/Svg/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

