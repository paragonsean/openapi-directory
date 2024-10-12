from typing import List, Dict
from aiohttp import web

from openapi_server.models.watched_directory import WatchedDirectory
from openapi_server import util


async def directorywatches_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """directorywatches_get

    get a list of watch directories. Each watch directory and its sub-directories are watched for incoming DICOM files, which are read and imported into slicebox.

    :param startindex: start index of returned slice of watched directories
    :type startindex: int
    :param count: size of returned slice of watched directories
    :type count: int

    """
    return web.Response(status=200)


async def directorywatches_id_delete(request: web.Request, id) -> web.Response:
    """directorywatches_id_delete

    stop watching and remove the directory corresponding to the supplied ID

    :param id: id of directory to stop watching
    :type id: int

    """
    return web.Response(status=200)


async def directorywatches_post(request: web.Request, watched_directory=None) -> web.Response:
    """directorywatches_post

    add a new directory to watch for incoming DICOM files

    :param watched_directory: directory to setup a watch for. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type watched_directory: dict | bytes

    """
    watched_directory = WatchedDirectory.from_dict(watched_directory)
    return web.Response(status=200)
