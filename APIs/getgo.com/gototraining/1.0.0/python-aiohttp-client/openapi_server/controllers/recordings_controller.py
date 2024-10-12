from typing import List, Dict
from aiohttp import web

from openapi_server.models.recordings_list_for_training import RecordingsListForTraining
from openapi_server import util


async def get_recording_download_by_id(request: web.Request, authorization, training_key, recording_id) -> web.Response:
    """Get Download for Online Recordings

    This call provides the download for the given recording by returning a 302 redirect to the original file.

    :param authorization: Access token
    :type authorization: str
    :param training_key: The key of the training
    :type training_key: int
    :param recording_id: the unique id of the recording
    :type recording_id: int

    """
    return web.Response(status=200)


async def get_recordings_for_training(request: web.Request, authorization, training_key) -> web.Response:
    """Get Online Recordings for Training

    This call retrieves information on all online recordings for a given training. If there are none, it returns an empty list.

    :param authorization: Access token
    :type authorization: str
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)
