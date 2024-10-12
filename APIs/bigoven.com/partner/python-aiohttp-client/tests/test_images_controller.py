# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_images_controller_recipe_photos_response import API2ControllersWebAPIImagesControllerRecipePhotosResponse
from openapi_server.models.big_oven_model_api_image import BigOvenModelAPIImage


pytestmark = pytest.mark.asyncio

async def test_images_get(client):
    """Test case for images_get

    Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/images'.format(recipe_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_get_pending_by_user(client):
    """Test case for images_get_pending_by_user

    Gets the pending by user.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/photos/pending',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_get_recipe_photos(client):
    """Test case for images_get_recipe_photos

    Get all the photos for a recipe
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/photos'.format(recipe_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_get_scan_images(client):
    """Test case for images_get_scan_images

    Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/scans'.format(recipe_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_upload_recipe_image(client):
    """Test case for images_upload_recipe_image

    POST: /recipe/{recipeId}/image?lat=42&amp;lng=21&amp;caption=this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \"form-data\", then add a line item with \"key\" column set to \"file\" and on the right,               change the type of the input from Text to File.  Browse and choose a JPG.
    """
    params = [('caption', 'caption_example'),
                    ('lat', 3.4),
                    ('lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/{recipe_id}/image'.format(recipe_id='recipe_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_upload_user_avatar(client):
    """Test case for images_upload_user_avatar

    POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \"form-data\", then add a line item with \"key\" column set to \"file\" and on the right,              change the type of the input from Text to File.  Browse and choose a JPG.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/image/avatar',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

