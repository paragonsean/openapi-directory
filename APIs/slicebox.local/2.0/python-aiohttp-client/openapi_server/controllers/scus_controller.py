from typing import List, Dict
from aiohttp import web

from openapi_server.models.scu import Scu
from openapi_server import util


async def scus_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """scus_get

    get a list of DICOM SCUs. Each SCU is a client for sending DICOM images to an SCP, e.g. a PACS system.

    :param startindex: start index of returned slice of SCUs
    :type startindex: int
    :param count: size of returned slice of SCUs
    :type count: int

    """
    return web.Response(status=200)


async def scus_id_delete(request: web.Request, id) -> web.Response:
    """scus_id_delete

    remove the SCU corresponding to the supplied ID

    :param id: id of SCU to remove
    :type id: int

    """
    return web.Response(status=200)


async def scus_id_send_post(request: web.Request, id, imageids) -> web.Response:
    """scus_id_send_post

    send the images with the supplied image IDs to a DICOM SCP using the the SCU with the supplied scu ID

    :param id: id of SCU to use for sending
    :type id: int
    :param imageids: array of ids of images to send
    :type imageids: List[int]

    """
    return web.Response(status=200)


async def scus_post(request: web.Request, scu=None) -> web.Response:
    """scus_post

    add a new SCU for sending DICOM images

    :param scu: SCU information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type scu: dict | bytes

    """
    scu = Scu.from_dict(scu)
    return web.Response(status=200)
