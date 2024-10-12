# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_get_content_by_id200_response import ContentGetContentById200Response
from openapi_server.models.content_get_content_type200_response import ContentGetContentType200Response
from openapi_server.models.content_rss_news_articles200_response import ContentRssNewsArticles200Response
from openapi_server.models.content_search_content_with_text200_response import ContentSearchContentWithText200Response
from openapi_server.models.content_search_help_articles200_response import ContentSearchHelpArticles200Response


pytestmark = pytest.mark.asyncio

async def test_content_get_content_by_id(client):
    """Test case for content_get_content_by_id

    
    """
    params = [('head', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/GetContentById/{id}/{locale}'.format(id=56, locale='locale_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_get_content_by_tag_and_type(client):
    """Test case for content_get_content_by_tag_and_type

    
    """
    params = [('head', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/GetContentByTagAndType/{tag}/{type}/{locale}'.format(locale='locale_example', tag='tag_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_get_content_type(client):
    """Test case for content_get_content_type

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/GetContentType/{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_rss_news_articles(client):
    """Test case for content_rss_news_articles

    
    """
    params = [('categoryfilter', 'categoryfilter_example'),
                    ('includebody', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/Rss/NewsArticles/{page_token}'.format(page_token='page_token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_search_content_by_tag_and_type(client):
    """Test case for content_search_content_by_tag_and_type

    
    """
    params = [('currentpage', 56),
                    ('head', True),
                    ('itemsperpage', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/SearchContentByTagAndType/{tag}/{type}/{locale}'.format(locale='locale_example', tag='tag_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_search_content_with_text(client):
    """Test case for content_search_content_with_text

    
    """
    params = [('ctype', 'ctype_example'),
                    ('currentpage', 56),
                    ('head', True),
                    ('searchtext', 'searchtext_example'),
                    ('source', 'source_example'),
                    ('tag', 'tag_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/Search/{locale}'.format(locale='locale_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_search_help_articles(client):
    """Test case for content_search_help_articles

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Content/SearchHelpArticles/{searchtext}/{size}'.format(searchtext='searchtext_example', size='size_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

