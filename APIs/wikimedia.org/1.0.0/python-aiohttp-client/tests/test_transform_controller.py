# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cx_dict import CxDict
from openapi_server.models.cx_languagepairs import CxLanguagepairs
from openapi_server.models.cx_list_tools import CxListTools
from openapi_server.models.cx_mt import CxMt
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transform_html_from_from_lang_to_to_lang_post(client):
    """Test case for transform_html_from_from_lang_to_to_lang_post

    Machine-translate content
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'html': 'html_example'
        }
    response = await client.request(
        method='POST',
        path='/api/rest_v1/transform/html/from/{from_lang}/to/{to_lang}'.format(from_lang='from_lang_example', to_lang='to_lang_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transform_html_from_from_lang_to_to_lang_provider_post(client):
    """Test case for transform_html_from_from_lang_to_to_lang_provider_post

    Machine-translate content
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'html': 'html_example'
        }
    response = await client.request(
        method='POST',
        path='/api/rest_v1/transform/html/from/{from_lang}/to/{to_lang}/{provider}'.format(from_lang='from_lang_example', to_lang='to_lang_example', provider='provider_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_list_languagepairs_get(client):
    """Test case for transform_list_languagepairs_get

    Lists the language pairs supported by the back-end
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/list/languagepairs/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_list_pair_from_to_get(client):
    """Test case for transform_list_pair_from_to_get

    Lists the tools available for a language pair
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/list/pair/{_from}/{to}'.format(_from='_from_example', to='to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_list_tool_tool_from_get(client):
    """Test case for transform_list_tool_tool_from_get

    Lists the tools and language pairs available for the given tool category
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/list/tool/{tool}/{_from}'.format(tool='tool_example', _from='_from_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_list_tool_tool_from_to_get(client):
    """Test case for transform_list_tool_tool_from_to_get

    Lists the tools and language pairs available for the given tool category
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/list/tool/{tool}/{_from}/{to}'.format(tool='tool_example', _from='_from_example', to='to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_list_tool_tool_get(client):
    """Test case for transform_list_tool_tool_get

    Lists the tools and language pairs available for the given tool category
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/list/tool/{tool}'.format(tool='tool_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_word_from_from_lang_to_to_lang_word_get(client):
    """Test case for transform_word_from_from_lang_to_to_lang_word_get

    Fetch the dictionary meaning of a word
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/word/from/{from_lang}/to/{to_lang}/{word}'.format(from_lang='from_lang_example', to_lang='to_lang_example', word='word_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_word_from_from_lang_to_to_lang_word_provider_get(client):
    """Test case for transform_word_from_from_lang_to_to_lang_word_provider_get

    Fetch the dictionary meaning of a word
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider}'.format(from_lang='from_lang_example', to_lang='to_lang_example', word='word_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

