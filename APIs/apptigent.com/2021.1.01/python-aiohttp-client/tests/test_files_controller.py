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

from openapi_server.models.input_qr_code import InputQRCode
from openapi_server.models.output_string import OutputString


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_convert_image(client):
    """Test case for convert_image

    Files - Convert Image
    """
    headers = { 
        'Accept': 'image/png',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('format', PNG)
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_crop_image(client):
    """Test case for crop_image

    Files - Crop Image
    """
    headers = { 
        'Accept': 'image/png',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('height', 3.4)
    data.add_field('width', 3.4)
    data.add_field('file', '/path/to/file')
    data.add_field('position', TopLeft)
    response = await client.request(
        method='POST',
        path='/api/utilities/CropImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_to_string(client):
    """Test case for file_to_string

    Files - File to string
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/utilities/FileToString',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_flip_image(client):
    """Test case for flip_image

    Files - Flip Image
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('orientation', Horizontal)
    response = await client.request(
        method='POST',
        path='/api/utilities/FlipImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_qr_code(client):
    """Test case for generate_qr_code

    Files - Generate QR code
    """
    input_qr_code = openapi_server.InputQRCode()
    headers = { 
        'Accept': 'image/png',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/GenerateQRCode',
        headers=headers,
        json=input_qr_code,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_resize_image(client):
    """Test case for resize_image

    Files - Resize Image
    """
    headers = { 
        'Accept': 'image/png',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('algorithm', Bicubic (default))
    data.add_field('file', '/path/to/file')
    data.add_field('height', 3.4)
    data.add_field('units', Pixels)
    data.add_field('width', 3.4)
    response = await client.request(
        method='POST',
        path='/api/utilities/ResizeImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_rotate_image(client):
    """Test case for rotate_image

    Files - Rotate Image
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('degrees', 'degrees_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/utilities/RotateImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_watermark_image(client):
    """Test case for watermark_image

    Files - Watermark Image
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('color', '000000')
    data.add_field('file', '/path/to/file')
    data.add_field('font', Arial)
    data.add_field('horizontal', Center)
    data.add_field('size', 3.4)
    data.add_field('text', 'text_example')
    data.add_field('vertical', Center)
    response = await client.request(
        method='POST',
        path='/api/utilities/WatermarkImage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

