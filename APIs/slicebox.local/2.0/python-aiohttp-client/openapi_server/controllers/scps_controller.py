from typing import List, Dict
from aiohttp import web

from openapi_server.models.scp import Scp
from openapi_server import util


async def scps_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """scps_get

    get a list of DICOM SCPs. Each SCP is a server for receiving DICOM images from e.g. a PACS system.

    :param startindex: start index of returned slice of SCPs
    :type startindex: int
    :param count: size of returned slice of SCPs
    :type count: int

    """
    return web.Response(status=200)


async def scps_id_delete(request: web.Request, id) -> web.Response:
    """scps_id_delete

    shut down and remove the SCP corresponding to the supplied ID

    :param id: id of SCP to remove
    :type id: int

    """
    return web.Response(status=200)


async def scps_post(request: web.Request, scp=None) -> web.Response:
    """scps_post

    add a new SCP for receiving DICOM images

    :param scp: SCP information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type scp: dict | bytes

    """
    scp = Scp.from_dict(scp)
    return web.Response(status=200)
