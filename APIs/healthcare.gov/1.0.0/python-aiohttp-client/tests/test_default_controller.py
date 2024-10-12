# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.articles_list import ArticlesList
from openapi_server.models.blog_list import BlogList
from openapi_server.models.blog_page import BlogPage
from openapi_server.models.glossary_list import GlossaryList
from openapi_server.models.glossary_page import GlossaryPage
from openapi_server.models.page import Page
from openapi_server.models.question_page import QuestionPage
from openapi_server.models.questions_list import QuestionsList
from openapi_server.models.state_page import StatePage
from openapi_server.models.states_list import StatesList
from openapi_server.models.topics_list import TopicsList


pytestmark = pytest.mark.asyncio

async def test_api_articlesmedia_type_extension_get(client):
    """Test case for api_articlesmedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/articles{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_blogmedia_type_extension_get(client):
    """Test case for api_blogmedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/blog{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_glossarymedia_type_extension_get(client):
    """Test case for api_glossarymedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/glossary{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_questionsmedia_type_extension_get(client):
    """Test case for api_questionsmedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/questions{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_statesmedia_type_extension_get(client):
    """Test case for api_statesmedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/states{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_topicsmedia_type_extension_get(client):
    """Test case for api_topicsmedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/topics{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blog_page_namemedia_type_extension_get(client):
    """Test case for blog_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/blog/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_es_blog_page_namemedia_type_extension_get(client):
    """Test case for es_blog_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/es/blog/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_es_glossary_page_namemedia_type_extension_get(client):
    """Test case for es_glossary_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/es/glossary/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_es_page_namemedia_type_extension_get(client):
    """Test case for es_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/es/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_es_question_page_namemedia_type_extension_get(client):
    """Test case for es_question_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/es/question/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_es_state_namemedia_type_extension_get(client):
    """Test case for es_state_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/es/{state_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', state_name='state_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_glossary_page_namemedia_type_extension_get(client):
    """Test case for glossary_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/glossary/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_page_namemedia_type_extension_get(client):
    """Test case for page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/html',
    }
    response = await client.request(
        method='GET',
        path='/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_question_page_namemedia_type_extension_get(client):
    """Test case for question_page_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/question/{page_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', page_name='page_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_state_namemedia_type_extension_get(client):
    """Test case for state_namemedia_type_extension_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/{state_namemedia_type_extension}'.format(media_type_extension='media_type_extension_example', state_name='state_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

