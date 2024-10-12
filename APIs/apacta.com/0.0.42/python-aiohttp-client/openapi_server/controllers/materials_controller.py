from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.materials_get200_response import MaterialsGet200Response
from openapi_server.models.materials_material_id_get200_response import MaterialsMaterialIdGet200Response
from openapi_server.models.materials_post_request import MaterialsPostRequest
from openapi_server import util


async def materials_get(request: web.Request, barcode=None, name=None, project_id=None, currently_rented=None) -> web.Response:
    """View list of all materials

    

    :param barcode: Used to filter on the &#x60;barcode&#x60; of the materials
    :type barcode: str
    :param name: Used to filter on the &#x60;name&#x60; of the materials
    :type name: str
    :param project_id: Used to find materials used in specific project by &#x60;project_id&#x60;
    :type project_id: str
    :type project_id: str
    :param currently_rented: Used to find currently rented materials
    :type currently_rented: bool

    """
    return web.Response(status=200)


async def materials_material_id_delete(request: web.Request, material_id) -> web.Response:
    """Delete material

    

    :param material_id: 
    :type material_id: str

    """
    return web.Response(status=200)


async def materials_material_id_get(request: web.Request, material_id) -> web.Response:
    """View material

    

    :param material_id: 
    :type material_id: str

    """
    return web.Response(status=200)


async def materials_material_id_put(request: web.Request, material_id) -> web.Response:
    """Edit material

    

    :param material_id: 
    :type material_id: str

    """
    return web.Response(status=200)


async def materials_post(request: web.Request, body=None) -> web.Response:
    """Add material

    

    :param body: 
    :type body: dict | bytes

    """
    body = MaterialsPostRequest.from_dict(body)
    return web.Response(status=200)
