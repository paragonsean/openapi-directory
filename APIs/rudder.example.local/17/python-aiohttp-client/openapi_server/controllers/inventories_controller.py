from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_watcher_restart200_response import FileWatcherRestart200Response
from openapi_server.models.file_watcher_start200_response import FileWatcherStart200Response
from openapi_server.models.file_watcher_stop200_response import FileWatcherStop200Response
from openapi_server.models.queue_information200_response import QueueInformation200Response
from openapi_server.models.upload_inventory200_response import UploadInventory200Response
from openapi_server import util


async def file_watcher_restart(request: web.Request, ) -> web.Response:
    """Restart inventory watcher

    Restart the inventory watcher if necessary


    """
    return web.Response(status=200)


async def file_watcher_start(request: web.Request, ) -> web.Response:
    """Start inventory watcher

    Start the inventory watcher if necessary


    """
    return web.Response(status=200)


async def file_watcher_stop(request: web.Request, ) -> web.Response:
    """Stop inventory watcher

    Stop the inventory watcher if necessary


    """
    return web.Response(status=200)


async def queue_information(request: web.Request, ) -> web.Response:
    """Get information about inventory processing queue

    Provide information about the current state of the inventory processor


    """
    return web.Response(status=200)


async def upload_inventory(request: web.Request, file=None, signature=None) -> web.Response:
    """Upload an inventory for processing

    Upload an inventory to the web application

    :param file: The inventory file. The original file name is used to check extension, that should be .xml[.gz] or .ocs[.gz]
    :type file: str
    :param signature: The signature file. The original file name is used to check extension, that should be ${originalInventoryFileName}.sign[.gz]
    :type signature: str

    """
    return web.Response(status=200)
