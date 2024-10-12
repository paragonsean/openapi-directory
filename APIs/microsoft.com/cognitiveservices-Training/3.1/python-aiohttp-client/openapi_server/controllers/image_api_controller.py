from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image import Image
from openapi_server.models.image_create_summary import ImageCreateSummary
from openapi_server.models.image_file_create_batch import ImageFileCreateBatch
from openapi_server.models.image_id_create_batch import ImageIdCreateBatch
from openapi_server.models.image_region_create_batch import ImageRegionCreateBatch
from openapi_server.models.image_region_create_summary import ImageRegionCreateSummary
from openapi_server.models.image_tag_create_batch import ImageTagCreateBatch
from openapi_server.models.image_tag_create_summary import ImageTagCreateSummary
from openapi_server.models.image_url_create_batch import ImageUrlCreateBatch
from openapi_server.models.suggested_tag_and_region_query import SuggestedTagAndRegionQuery
from openapi_server.models.suggested_tag_and_region_query_token import SuggestedTagAndRegionQueryToken
from openapi_server.models.tag_filter import TagFilter
from openapi_server import util


async def create_image_regions(request: web.Request, project_id, training_key, body) -> web.Response:
    """Create a set of image regions.

    This API accepts a batch of image regions, and optionally tags, to update existing images with region information.  There is a limit of 64 entries in the batch.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Batch of image regions which include a tag and bounding box. Limited to 64.
    :type body: dict | bytes

    """
    body = ImageRegionCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_image_tags(request: web.Request, project_id, training_key, body) -> web.Response:
    """Associate a set of images with a set of tags.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Batch of image tags. Limited to 128 tags per batch.
    :type body: dict | bytes

    """
    body = ImageTagCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_images_from_data(request: web.Request, project_id, training_key, image_data, tag_ids=None) -> web.Response:
    """Add the provided images to the set of training images.

    This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
    :type image_data: str
    :param tag_ids: The tags ids with which to tag each image. Limited to 20.
    :type tag_ids: List[str]

    """
    return web.Response(status=200)


async def create_images_from_files(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the provided batch of images to the set of training images.

    This API accepts a batch of files, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: The batch of image files to add. Limited to 64 images and 20 tags per batch.
    :type body: dict | bytes

    """
    body = ImageFileCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_images_from_predictions(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the specified predicted images to the set of training images.

    This API creates a batch of images from predicted images specified. There is a limit of 64 images and 20 tags.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Image and tag ids. Limited to 64 images and 20 tags per batch.
    :type body: dict | bytes

    """
    body = ImageIdCreateBatch.from_dict(body)
    return web.Response(status=200)


async def create_images_from_urls(request: web.Request, project_id, training_key, body) -> web.Response:
    """Add the provided images urls to the set of training images.

    This API accepts a batch of urls, and optionally tags, to create images. There is a limit of 64 images and 20 tags.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Image urls and tag ids. Limited to 64 images and 20 tags per batch.
    :type body: dict | bytes

    """
    body = ImageUrlCreateBatch.from_dict(body)
    return web.Response(status=200)


async def delete_image_regions(request: web.Request, project_id, region_ids, training_key) -> web.Response:
    """Delete a set of image regions.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param region_ids: Regions to delete. Limited to 64.
    :type region_ids: List[str]
    :param training_key: API key.
    :type training_key: str

    """
    return web.Response(status=200)


async def delete_image_tags(request: web.Request, project_id, image_ids, tag_ids, training_key) -> web.Response:
    """Remove a set of tags from a set of images.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param image_ids: Image ids. Limited to 64 images.
    :type image_ids: List[str]
    :param tag_ids: Tags to be deleted from the specified images. Limited to 20 tags.
    :type tag_ids: List[str]
    :param training_key: API key.
    :type training_key: str

    """
    return web.Response(status=200)


async def delete_images(request: web.Request, project_id, training_key, image_ids=None, all_images=None, all_iterations=None) -> web.Response:
    """Delete images from the set of training images.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param image_ids: Ids of the images to be deleted. Limited to 256 images per batch.
    :type image_ids: List[str]
    :param all_images: Flag to specify delete all images, specify this flag or a list of images. Using this flag will return a 202 response to indicate the images are being deleted.
    :type all_images: bool
    :param all_iterations: Removes these images from all iterations, not just the current workspace. Using this flag will return a 202 response to indicate the images are being deleted.
    :type all_iterations: bool

    """
    return web.Response(status=200)


async def get_images_by_ids(request: web.Request, project_id, training_key, image_ids=None, iteration_id=None) -> web.Response:
    """Get images by id for a given project iteration.

    This API will return a set of Images for the specified tags and optionally iteration. If no iteration is specified the  current workspace is used.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param image_ids: The list of image ids to retrieve. Limited to 256.
    :type image_ids: List[str]
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str

    """
    return web.Response(status=200)


async def get_tagged_image_count(request: web.Request, project_id, training_key, iteration_id=None, tag_ids=None) -> web.Response:
    """Gets the number of images tagged with the provided {tagIds}.

    The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str
    :param tag_ids: A list of tags ids to filter the images to count. Defaults to all tags when null.
    :type tag_ids: List[str]

    """
    return web.Response(status=200)


async def get_tagged_images(request: web.Request, project_id, training_key, iteration_id=None, tag_ids=None, order_by=None, take=None, skip=None) -> web.Response:
    """Get tagged images for a given project iteration.

    This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str
    :param tag_ids: A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
    :type tag_ids: List[str]
    :param order_by: The ordering. Defaults to newest.
    :type order_by: str
    :param take: Maximum number of images to return. Defaults to 50, limited to 256.
    :type take: int
    :param skip: Number of images to skip before beginning the image batch. Defaults to 0.
    :type skip: int

    """
    return web.Response(status=200)


async def get_untagged_image_count(request: web.Request, project_id, training_key, iteration_id=None) -> web.Response:
    """Gets the number of untagged images.

    This API returns the images which have no tags for a given project and optionally an iteration. If no iteration is specified the  current workspace is used.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str

    """
    return web.Response(status=200)


async def get_untagged_images(request: web.Request, project_id, training_key, iteration_id=None, order_by=None, take=None, skip=None) -> web.Response:
    """Get untagged images for a given project iteration.

    This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str
    :param order_by: The ordering. Defaults to newest.
    :type order_by: str
    :param take: Maximum number of images to return. Defaults to 50, limited to 256.
    :type take: int
    :param skip: Number of images to skip before beginning the image batch. Defaults to 0.
    :type skip: int

    """
    return web.Response(status=200)


async def query_suggested_image_count(request: web.Request, project_id, iteration_id, training_key, body) -> web.Response:
    """Get count of images whose suggested tags match given tags and their probabilities are greater than or equal to the given threshold. Returns count as 0 if none found.

    This API takes in tagIds to get count of untagged images per suggested tags for a given threshold.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: IterationId to use for the suggested tags and regions.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Model that contains tagIds, threshold and projectType to query by.
    :type body: dict | bytes

    """
    body = TagFilter.from_dict(body)
    return web.Response(status=200)


async def query_suggested_images(request: web.Request, project_id, iteration_id, training_key, body) -> web.Response:
    """Get untagged images whose suggested tags match given tags. Returns empty array if no images are found.

    This API will fetch untagged images filtered by suggested tags Ids. It returns an empty array if no images are found.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: IterationId to use for the suggested tags and regions.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Contains properties we need to query suggested images.
    :type body: dict | bytes

    """
    body = SuggestedTagAndRegionQueryToken.from_dict(body)
    return web.Response(status=200)
