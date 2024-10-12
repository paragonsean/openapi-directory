from typing import List, Dict
from aiohttp import web

from openapi_server.models.image import Image
from openapi_server.models.image_create_summary import ImageCreateSummary
from openapi_server.models.image_file_create_batch import ImageFileCreateBatch
from openapi_server.models.image_id_create_batch import ImageIdCreateBatch
from openapi_server.models.image_tag_create_batch import ImageTagCreateBatch
from openapi_server.models.image_tag_create_summary import ImageTagCreateSummary
from openapi_server.models.image_url_create_batch import ImageUrlCreateBatch
from openapi_server import util


async def create_images_from_data(request: web.Request, project_id, training_key, image_data, tag_ids=None) -> web.Response:
    """Add the provided images to the set of training images

    This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param image_data: 
    :type image_data: str
    :param tag_ids: The tags ids with which to tag each image. Limited to 20
    :type tag_ids: List[str]

    """
    return web.Response(status=200)


async def create_images_from_files(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the provided batch of images to the set of training images

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: The batch of image files to add. Limited to 64 images and 20 tags per batch
    :type body: dict | bytes

    """
    body = ImageFileCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_images_from_predictions(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the specified predicted images to the set of training images

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: Image and tag ids. Limited to 64 images and 20 tags per batch
    :type body: dict | bytes

    """
    body = ImageIdCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_images_from_urls(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the provided images urls to the set of training images

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: Image urls and tag ids. Limited to 64 images and 20 tags per batch
    :type body: dict | bytes

    """
    body = ImageUrlCreateBatch.from_dict(body)
    return web.Response(status=200)


async def delete_image_tags(request: web.Request, project_id, image_ids, tag_ids, training_key) -> web.Response:
    """Remove a set of tags from a set of images

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param image_ids: Image ids. Limited to 64 images
    :type image_ids: List[str]
    :param tag_ids: Tags to be deleted from the specified images. Limited to 20 tags
    :type tag_ids: List[str]
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def delete_images(request: web.Request, project_id, image_ids, training_key) -> web.Response:
    """Delete images from the set of training images

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param image_ids: Ids of the images to be deleted. Limited to 256 images per batch
    :type image_ids: List[str]
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_tagged_images(request: web.Request, project_id, training_key, iteration_id=None, tag_ids=None, order_by=None, take=None, skip=None) -> web.Response:
    """Get tagged images for a given project iteration

    This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace
    :type iteration_id: str
    :type iteration_id: str
    :param tag_ids: An list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20
    :type tag_ids: List[str]
    :param order_by: The ordering. Defaults to newest
    :type order_by: str
    :param take: Maximum number of images to return. Defaults to 50, limited to 256
    :type take: int
    :param skip: Number of images to skip before beginning the image batch. Defaults to 0
    :type skip: int

    """
    return web.Response(status=200)


async def get_untagged_images(request: web.Request, project_id, training_key, iteration_id=None, order_by=None, take=None, skip=None) -> web.Response:
    """Get untagged images for a given project iteration

    This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace
    :type iteration_id: str
    :type iteration_id: str
    :param order_by: The ordering. Defaults to newest
    :type order_by: str
    :param take: Maximum number of images to return. Defaults to 50, limited to 256
    :type take: int
    :param skip: Number of images to skip before beginning the image batch. Defaults to 0
    :type skip: int

    """
    return web.Response(status=200)


async def post_image_tags(request: web.Request, project_id, training_key, body) -> web.Response:
    """Associate a set of images with a set of tags

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: Batch of image tags. Limited to 128 tags per batch
    :type body: dict | bytes

    """
    body = ImageTagCreateBatch.from_dict(body)
    return web.Response(status=200)
