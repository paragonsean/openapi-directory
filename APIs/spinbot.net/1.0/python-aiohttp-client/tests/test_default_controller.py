# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    Return the user credit information.
    """
    params = [('key', 'key_example')]
    headers = { 
        'Accept': '*/*',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/acc',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_article(client):
    """Test case for post_article

    Extracting the main article of the given URL.
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'key': 'special-key',
    }
    data = FormData()
    data.add_field('key', 'key_example')
    data.add_field('url', 'url_example')
    data.add_field('faster_mode', 'faster_mode_example')
    response = await client.request(
        method='POST',
        path='/api/article',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_pretty_spinner(client):
    """Test case for post_pretty_spinner

    Human readable auto rewrite your article.
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'key': 'special-key',
    }
    data = FormData()
    data.add_field('key', 'key_example')
    data.add_field('text', 'text_example')
    data.add_field('keep', 'keep_example')
    data.add_field('accuracy', 'accuracy_example')
    response = await client.request(
        method='POST',
        path='/api/pretty-spinner',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_spinner(client):
    """Test case for post_spinner

    Rewriting (spinning) your input article.
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'key': 'special-key',
    }
    data = FormData()
    data.add_field('key', 'key_example')
    data.add_field('text', 'text_example')
    response = await client.request(
        method='POST',
        path='/api/spinner',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_spintax(client):
    """Test case for post_spintax

    Generate Spintax format for the input article
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'key': 'special-key',
    }
    data = FormData()
    data.add_field('key', 'key_example')
    data.add_field('text', 'text_example')
    data.add_field('full_mode', 'full_mode_example')
    response = await client.request(
        method='POST',
        path='/api/spintax',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

