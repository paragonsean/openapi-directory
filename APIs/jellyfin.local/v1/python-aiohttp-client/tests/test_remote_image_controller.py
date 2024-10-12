# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.image_provider_info import ImageProviderInfo
from openapi_server.models.image_type import ImageType
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_image_result import RemoteImageResult


pytestmark = pytest.mark.asyncio

async def test_download_remote_image(client):
    """Test case for download_remote_image

    Downloads a remote image for an item.
    """
    params = [('type', openapi_server.ImageType()),
                    ('imageUrl', 'image_url_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/RemoteImages/Download'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_image(client):
    """Test case for get_remote_image

    Gets a remote image.
    """
    params = [('imageUrl', 'image_url_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Images/Remote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_image_providers(client):
    """Test case for get_remote_image_providers

    Gets available remote image providers for an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/RemoteImages/Providers'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_images(client):
    """Test case for get_remote_images

    Gets available remote images for an item.
    """
    params = [('type', openapi_server.ImageType()),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('providerName', 'provider_name_example'),
                    ('includeAllLanguages', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/RemoteImages'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

