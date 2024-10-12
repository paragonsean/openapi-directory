# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_h_tml_render(client):
    """Test case for h_tml_render

    HTML Render
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'content': 'content_example',
        'css': 'css_example',
        'delay': 0,
        'footer': 'footer_example',
        'format': 'PDF',
        'grayscale': False,
        'header': 'header_example',
        'ignore_certificate_errors': False,
        'image_height': 56,
        'image_width': 1024,
        'landscape': False,
        'margin': 0,
        'margin_bottom': 0,
        'margin_left': 0,
        'margin_right': 0,
        'margin_top': 0,
        'page_height': 3.4,
        'page_size': 'A4',
        'page_width': 3.4,
        'timeout': 300,
        'title': 'title_example',
        'zoom': 1
        }
    response = await client.request(
        method='POST',
        path='/html-render',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_image_resize(client):
    """Test case for image_resize

    Image Resize
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'bg_color': 'transparent',
        'format': 'png',
        'height': 56,
        'image_url': 'image_url_example',
        'resize_mode': 'scale',
        'width': 56
        }
    response = await client.request(
        method='POST',
        path='/image-resize',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_image_watermark(client):
    """Test case for image_watermark

    Image Watermark
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'bg_color': 'transparent',
        'format': 'png',
        'height': 56,
        'image_url': 'image_url_example',
        'opacity': 50,
        'position': 'center',
        'resize_mode': 'scale',
        'watermark_url': 'watermark_url_example',
        'width': 56
        }
    response = await client.request(
        method='POST',
        path='/image-watermark',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_q_r_code(client):
    """Test case for q_r_code

    QR Code
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'bg_color': '#ffffff',
        'content': 'content_example',
        'fg_color': '#000000',
        'height': 256,
        'width': 256
        }
    response = await client.request(
        method='POST',
        path='/qr-code',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

