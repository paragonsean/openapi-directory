from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def compare_faces_using_get(request: web.Request, access_key, secret_key, face_hashes, show_details=None) -> web.Response:
    """Compare several faces identified by faceHash, without depending on mapping faces to profiles

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param face_hashes: The IDs of the faces which you want compared, comma-separated
    :type face_hashes: List[str]
    :param show_details: Show details
    :type show_details: bool

    """
    return web.Response(status=200)


async def perform_analysis_using_post(request: web.Request, access_key, secret_key, store_analysis_picture=None, store_face_pictures=None, store_result=None, retention_time=None, picture_url=None, algorithm_version=None, auto_rotate=None, skip_exif=None, wait_for_picture_upload=None, filters=None, options=None, picture=None) -> web.Response:
    """Perform detection on a given picture or picture URL

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param store_analysis_picture: Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
    :type store_analysis_picture: bool
    :param store_face_pictures: Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
    :type store_face_pictures: bool
    :param store_result: Boolean value indicating whether you want the result of the analysis to be stored
    :type store_result: bool
    :param retention_time: How many seconds the results should be retained in stoarage?
    :type retention_time: int
    :param picture_url: The URL of the picture, assuming it is served by a third party server. Server should be accesible from the Internet or through another netwoek by VisageCloud infrastructure
    :type picture_url: str
    :param algorithm_version: Algorithm version (V2 is more performant but not backward compatible)
    :type algorithm_version: str
    :param auto_rotate: Auto-rotate to find flipped or rotate faces
    :type auto_rotate: bool
    :param skip_exif: Skip EXIF rotation procesing
    :type skip_exif: bool
    :param wait_for_picture_upload: Waits until the picture is successfully uploaded, before returning the response back the the client
    :type wait_for_picture_upload: bool
    :param filters: [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
    :type filters: List[str]
    :param options: [For advanced users only] Options for preprocessing of image.
    :type options: str
    :param picture: The multipart/form-data version of the image, in case a direct upload is used. At least one of picture or pictureURL must be present
    :type picture: str

    """
    return web.Response(status=200)


async def perform_recognition_using_post(request: web.Request, access_key, secret_key, collection_id, store_analysis_picture=None, store_face_pictures=None, store_result=None, retention_time=None, labels=None, attribute_filters=None, picture_url=None, algorithm_version=None, auto_rotate=None, skip_exif_rotation_processing=None, wait_for_picture_upload=None, filters=None, options=None, picture=None) -> web.Response:
    """Perform labeled recognition on a given picture or picture URL

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param store_analysis_picture: Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
    :type store_analysis_picture: bool
    :param store_face_pictures: Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
    :type store_face_pictures: bool
    :param store_result: Boolean value indicating whether you want the result of the analysis to be stored
    :type store_result: bool
    :param retention_time: How many seconds the results should be retained in stoarage?
    :type retention_time: int
    :param labels: Labels associated with the given picture or picture URL
    :type labels: List[str]
    :param attribute_filters: Filters that will be applied on the recognition operation
    :type attribute_filters: List[str]
    :param picture_url: The URL of the picture
    :type picture_url: str
    :param algorithm_version: Algorithm version (V2 is more performant but not backward compatible)
    :type algorithm_version: str
    :param auto_rotate: Auto-rotate to find flipped or rotate faces
    :type auto_rotate: bool
    :param skip_exif_rotation_processing: Skip EXIF rotation procesing
    :type skip_exif_rotation_processing: bool
    :param wait_for_picture_upload: Waits until the picture is successfully uploaded, before returning the response back the the client
    :type wait_for_picture_upload: bool
    :param filters: [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
    :type filters: List[str]
    :param options: [For advanced users only] Options for preprocessing of image.
    :type options: str
    :param picture: The picture itself
    :type picture: str

    """
    return web.Response(status=200)


async def retrieve_analysis_using_get(request: web.Request, access_key, secret_key, analysis_id) -> web.Response:
    """Retrieve a complete analysis object including both detection and recognition information

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param analysis_id: The ID of the analysis for which the data will be retrieved
    :type analysis_id: str

    """
    return web.Response(status=200)


async def retrive_latest_using_get(request: web.Request, access_key, secret_key, count=None) -> web.Response:
    """Retrieve the last *count* operations per current account

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param count: How many records to retrieve at a time
    :type count: int

    """
    return web.Response(status=200)
