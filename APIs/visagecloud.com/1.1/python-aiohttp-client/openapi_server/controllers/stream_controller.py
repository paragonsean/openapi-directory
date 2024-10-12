from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def add_stream_using_post(request: web.Request, access_key, secret_key, name, url, method=None, username=None, password=None, skip_frames_with_no_faces=None, retention_time=None, store_original_frames=None, store_attendance_faces=None, store_attendance_frames=None, is_active=None, associated_collections=None, attributes=None) -> web.Response:
    """Create new stream with given name

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param name: The name of the stream that will be created
    :type name: str
    :param url: The url of the stream
    :type url: str
    :param method: Streaming method
    :type method: str
    :param username: Username
    :type username: str
    :param password: Password
    :type password: str
    :param skip_frames_with_no_faces: Boolean value indicating whether you want the original picture to be stored for later retrieval
    :type skip_frames_with_no_faces: bool
    :param retention_time: Number of seconds for frames to be kept. Default is 605000s (7 days)
    :type retention_time: int
    :param store_original_frames: Boolean value indicating whether you want the original picture to be stored for later retrieval
    :type store_original_frames: bool
    :param store_attendance_faces: Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
    :type store_attendance_faces: bool
    :param store_attendance_frames: Boolean value indicating whether you want to store permanently store frames with a recognized face in them
    :type store_attendance_frames: bool
    :param is_active: Boolean value indicating whether the stream is currently active or not
    :type is_active: bool
    :param associated_collections: List of collection ids which will be used to measure attendance
    :type associated_collections: List[str]
    :param attributes: Attributes of the stream
    :type attributes: str

    """
    return web.Response(status=200)


async def cleanup_stream_using_patch(request: web.Request, access_key, secret_key, stream_id, interval) -> web.Response:
    """Cleanup frames older than specified timeframe

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream that will be stopped
    :type stream_id: str
    :param interval: Frames older than interval (seconds) will be cleaned up
    :type interval: int

    """
    return web.Response(status=200)


async def get_frame_image_using_get(request: web.Request, access_key, secret_key, stream_id, timestamp) -> web.Response:
    """Get individual frame image

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream for which the frames will be retrieved
    :type stream_id: str
    :param timestamp: Timestamp of frame to retrieve
    :type timestamp: int

    """
    return web.Response(status=200)


async def get_last_n_attedance_using_get(request: web.Request, access_key, secret_key, stream_ids=None, count=None) -> web.Response:
    """Get last N recognized individuals from stream

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param stream_ids: The id of the stream for which the frames will be retrieved
    :type stream_ids: List[str]
    :param count: How many frames to retrieve at a time
    :type count: int

    """
    return web.Response(status=200)


async def get_last_n_frames_using_get(request: web.Request, access_key, secret_key, stream_id, count=None, collection_id=None, labels=None, attribute_filters=None) -> web.Response:
    """Get last processed N frames from stream

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream for which the frames will be retrieved
    :type stream_id: str
    :param count: How many frames to retrieve at a time
    :type count: int
    :param collection_id: The collection id you want to run recognition against
    :type collection_id: str
    :param labels: Labels associated with the given picture or picture URL
    :type labels: List[str]
    :param attribute_filters: Filters that will be applied on the recognition operation
    :type attribute_filters: List[str]

    """
    return web.Response(status=200)


async def get_stream_using_get(request: web.Request, access_key, secret_key, stream_id) -> web.Response:
    """Get an existing stream with a given ID

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream for which the data will be retrieved
    :type stream_id: str

    """
    return web.Response(status=200)


async def remove_stream_using_delete(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Delete existing stream

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the stream that will be removed
    :type id: str

    """
    return web.Response(status=200)


async def start_stream_using_patch(request: web.Request, access_key, secret_key, stream_id) -> web.Response:
    """Start existing stream

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream that will be started
    :type stream_id: str

    """
    return web.Response(status=200)


async def stop_stream_using_patch(request: web.Request, access_key, secret_key, stream_id) -> web.Response:
    """Stop existing stream

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream that will be stopped
    :type stream_id: str

    """
    return web.Response(status=200)


async def streams_by_account_using_get(request: web.Request, access_key, secret_key) -> web.Response:
    """Show status of all streams from account

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str

    """
    return web.Response(status=200)


async def update_stream_using_patch(request: web.Request, access_key, secret_key, stream_id, name=None, url=None, method=None, username=None, password=None, skip_frames_with_no_faces=None, retention_time=None, store_original_frames=None, store_attendance_faces=None, store_attendance_frames=None, is_active=None, associated_collections=None, attributes=None) -> web.Response:
    """Update an existing stream with a given ID

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param stream_id: The id of the stream that will be updated
    :type stream_id: str
    :param name: The name of the stream that will be updated
    :type name: str
    :param url: The url of the stream
    :type url: str
    :param method: Streaming method
    :type method: str
    :param username: Username
    :type username: str
    :param password: Password
    :type password: str
    :param skip_frames_with_no_faces: Boolean value indicating whether you want the original picture to be stored for later retrieval
    :type skip_frames_with_no_faces: bool
    :param retention_time: Number of seconds for frames to be kept
    :type retention_time: int
    :param store_original_frames: Boolean value indicating whether you want the original picture to be stored for later retrieval
    :type store_original_frames: bool
    :param store_attendance_faces: Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
    :type store_attendance_faces: bool
    :param store_attendance_frames: Boolean value indicating whether you want to store permanently store frames with a recognized face in them
    :type store_attendance_frames: bool
    :param is_active: Boolean value indicating whether the stream is currently active or not
    :type is_active: bool
    :param associated_collections: List of collection ids which will be used to measure attendance
    :type associated_collections: List[str]
    :param attributes: Attributes of the stream
    :type attributes: str

    """
    return web.Response(status=200)
