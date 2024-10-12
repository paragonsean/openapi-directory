from typing import List, Dict
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_images_controller_recipe_photos_response import API2ControllersWebAPIImagesControllerRecipePhotosResponse
from openapi_server.models.big_oven_model_api_image import BigOvenModelAPIImage
from openapi_server import util


async def images_get(request: web.Request, recipe_id) -> web.Response:
    """Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos.

    

    :param recipe_id: Recipe ID (required)
    :type recipe_id: int

    """
    return web.Response(status=200)


async def images_get_pending_by_user(request: web.Request, ) -> web.Response:
    """Gets the pending by user.

    


    """
    return web.Response(status=200)


async def images_get_recipe_photos(request: web.Request, recipe_id, pg=None, rpp=None) -> web.Response:
    """Get all the photos for a recipe

    

    :param recipe_id: Recipe ID (required)
    :type recipe_id: int
    :param pg: 
    :type pg: int
    :param rpp: 
    :type rpp: int

    """
    return web.Response(status=200)


async def images_get_scan_images(request: web.Request, recipe_id) -> web.Response:
    """Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe.

    

    :param recipe_id: the recipe identifier (int)
    :type recipe_id: int

    """
    return web.Response(status=200)


async def images_upload_recipe_image(request: web.Request, recipe_id, caption=None, lat=None, lng=None) -> web.Response:
    """POST: /recipe/{recipeId}/image?lat&#x3D;42&amp;amp;lng&#x3D;21&amp;amp;caption&#x3D;this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,               change the type of the input from Text to File.  Browse and choose a JPG.

    

    :param recipe_id: 
    :type recipe_id: str
    :param caption: 
    :type caption: str
    :param lat: 
    :type lat: float
    :param lng: 
    :type lng: float

    """
    return web.Response(status=200)


async def images_upload_user_avatar(request: web.Request, ) -> web.Response:
    """POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,              change the type of the input from Text to File.  Browse and choose a JPG.

    


    """
    return web.Response(status=200)
