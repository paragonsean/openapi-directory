from typing import List, Dict
from aiohttp import web

from openapi_server.models.anonymization_data import AnonymizationData
from openapi_server.models.export_set_id import ExportSetId
from openapi_server.models.image import Image
from openapi_server.models.image_attribute import ImageAttribute
from openapi_server.models.image_information import ImageInformation
from openapi_server.models.images_post_request import ImagesPostRequest
from openapi_server.models.tag_mapping import TagMapping
from openapi_server import util


async def images_delete_post(request: web.Request, image_ids) -> web.Response:
    """images_delete_post

    bulk delete a sequence of images according to the supplied image IDs. This is the same as a sequence of DELETE requests to /images/{id}

    :param image_ids: IDs of images to delete
    :type image_ids: List[int]

    """
    return web.Response(status=200)


async def images_export_get(request: web.Request, id) -> web.Response:
    """images_export_get

    download the export set with the supplied export set ID as a zip archive

    :param id: ID of export set to download
    :type id: int

    """
    return web.Response(status=200)


async def images_export_post(request: web.Request, image_ids) -> web.Response:
    """images_export_post

    create an export set, a group of image IDs of images to export. The export set will contain the selected images. The export set is available for download 12 hours before it is automatically deleted.

    :param image_ids: ids of images to export
    :type image_ids: List[int]

    """
    return web.Response(status=200)


async def images_id_anonymize_put_0(request: web.Request, id, tag_values) -> web.Response:
    """images_id_anonymize_put_0

    delete the selected image and replace it with an anonymized version

    :param id: ID of image to anonymize
    :type id: int
    :param tag_values: specification of values for anonymous DICOM attributes
    :type tag_values: dict | bytes

    """
    tag_values = AnonymizationData.from_dict(tag_values)
    return web.Response(status=200)


async def images_id_anonymized_post_0(request: web.Request, id, tag_values) -> web.Response:
    """images_id_anonymized_post_0

    get an anonymized version of the image with the supplied ID

    :param id: ID of image for which to get anonymized dataset
    :type id: int
    :param tag_values: specification of values for anonymous DICOM attributes
    :type tag_values: dict | bytes

    """
    tag_values = AnonymizationData.from_dict(tag_values)
    return web.Response(status=200)


async def images_id_attributes_get(request: web.Request, id) -> web.Response:
    """images_id_attributes_get

    list all DICOM attributes of the dataset corresponding to the supplied image ID

    :param id: ID of image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_delete(request: web.Request, id) -> web.Response:
    """images_id_delete

    Delete the image with the supplied ID

    :param id: ID of image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_get(request: web.Request, id) -> web.Response:
    """images_id_get

    fetch dataset corresponding to the supplied image ID

    :param id: ID of image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_imageinformation_get(request: web.Request, id) -> web.Response:
    """images_id_imageinformation_get

    get basic information about the pixel data of an image

    :param id: ID of image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_modify_put(request: web.Request, id, tag_path_value_mappings) -> web.Response:
    """images_id_modify_put

    modify and/or insert image attributes according to the input tagpath-value mappings

    :param id: ID of image to modify
    :type id: int
    :param tag_path_value_mappings: specification of tag paths and corresponding values to insert or modify
    :type tag_path_value_mappings: list | bytes

    """
    tag_path_value_mappings = [TagMapping.from_dict(d) for d in tag_path_value_mappings]
    return web.Response(status=200)


async def images_id_png_get(request: web.Request, id, framenumber=None, windowmin=None, windowmax=None, imageheight=None) -> web.Response:
    """images_id_png_get

    get a PNG image representation of the image corresponding to the supplied ID

    :param id: ID of image
    :type id: int
    :param framenumber: frame/slice to show
    :type framenumber: int
    :param windowmin: intensity window minimum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
    :type windowmin: int
    :param windowmax: intensity window maximum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
    :type windowmax: int
    :param imageheight: height of PNG image. If not specified or set to zero, the image height will equal that of the data
    :type imageheight: int

    """
    return web.Response(status=200)


async def images_jpeg_post(request: web.Request, studyid, jpeg_bytes, description=None) -> web.Response:
    """images_jpeg_post

    add a JPEG image to slicebox. The image data will be wrapped in a DICOM file and added as a new series belonging to the study with the supplied ID

    :param studyid: ID of study to add new series to
    :type studyid: int
    :param jpeg_bytes: The jpeg image data
    :type jpeg_bytes: 
    :param description: DICOM series description of the resulting secondary capture series
    :type description: str

    """
    return web.Response(status=200)


async def images_post(request: web.Request, body) -> web.Response:
    """images_post

    add a DICOM dataset to slicebox

    :param body: 
    :type body: dict | bytes

    """
    body = ImagesPostRequest.from_dict(body)
    return web.Response(status=200)
