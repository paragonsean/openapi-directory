# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.add_password_v14_xx_response import AddPasswordV14XXResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_image_watermark_v1(client):
    """Test case for add_image_watermark_v1

    Add an image watermark to a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('image', '/path/to/file')
    data.add_field('margin', 1)
    data.add_field('transparency', 50)
    response = await client.request(
        method='POST',
        path='/v1/add_watermark/image',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_password_v1(client):
    """Test case for add_password_v1

    Add a password to a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('encryption_algorithm', AES-128)
    data.add_field('file', '/path/to/file')
    data.add_field('password', 'password_example')
    response = await client.request(
        method='POST',
        path='/v1/add_password',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_restrictions_v1(client):
    """Test case for add_restrictions_v1

    Add restrictions to a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('allow_accessibility', True)
    data.add_field('allow_assemble_document', True)
    data.add_field('allow_change_content', True)
    data.add_field('allow_comment_and_fill_form', True)
    data.add_field('allow_copy_content', True)
    data.add_field('allow_fill_form', True)
    data.add_field('allow_print', True)
    data.add_field('allow_print_high_resolution', True)
    data.add_field('encryption_algorithm', AES-128)
    data.add_field('file', '/path/to/file')
    data.add_field('owner_password', 'owner_password_example')
    data.add_field('user_password', 'user_password_example')
    response = await client.request(
        method='POST',
        path='/v1/add_restrictions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_text_watermark_v1(client):
    """Test case for add_text_watermark_v1

    Add a text watermark to a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('color', Gray)
    data.add_field('file', '/path/to/file')
    data.add_field('line_1', 'line_1_example')
    data.add_field('line_2', 'line_2_example')
    data.add_field('line_3', 'line_3_example')
    data.add_field('margin', 1)
    data.add_field('template', 1001)
    data.add_field('transparency', 75)
    response = await client.request(
        method='POST',
        path='/v1/add_watermark/text',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_extract_pages_v1(client):
    """Test case for extract_pages_v1

    Extract pages from a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('first_page', 56)
    data.add_field('last_page', 56)
    response = await client.request(
        method='POST',
        path='/v1/extract_pages',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_merge_documents_v1(client):
    """Test case for merge_documents_v1

    Merge PDF documents
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/v1/merge_documents',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_remove_pages_v1(client):
    """Test case for remove_pages_v1

    Remove pages from a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('first_page', 56)
    data.add_field('last_page', 56)
    response = await client.request(
        method='POST',
        path='/v1/remove_pages',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_remove_password_v1(client):
    """Test case for remove_password_v1

    Remove the password from a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('password', 'password_example')
    response = await client.request(
        method='POST',
        path='/v1/remove_password',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_remove_restrictions_v1(client):
    """Test case for remove_restrictions_v1

    Remove the restrictions from a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/remove_restrictions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_remove_signatures_v1(client):
    """Test case for remove_signatures_v1

    Remove the signatures from a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/remove_signatures',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_reverse_pages_v1(client):
    """Test case for reverse_pages_v1

    Reverse the pages of a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/reverse_pages',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_rotate_pages_v1(client):
    """Test case for rotate_pages_v1

    Rotate pages in a PDF
    """
    headers = { 
        'Accept': 'application/problem+json',
        'Content-Type': 'multipart/form-data',
        'apiKey': 'special-key',
    }
    data = FormData()
    data.add_field('angle', 56)
    data.add_field('file', '/path/to/file')
    data.add_field('first_page', 56)
    data.add_field('last_page', 56)
    response = await client.request(
        method='POST',
        path='/v1/rotate_pages',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

