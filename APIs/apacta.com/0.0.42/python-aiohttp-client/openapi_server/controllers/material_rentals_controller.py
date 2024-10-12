from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.materials_material_id_rentals_checkout_post_request import MaterialsMaterialIdRentalsCheckoutPostRequest
from openapi_server.models.materials_material_id_rentals_get200_response import MaterialsMaterialIdRentalsGet200Response
from openapi_server.models.materials_material_id_rentals_material_rental_id_get200_response import MaterialsMaterialIdRentalsMaterialRentalIdGet200Response
from openapi_server.models.materials_material_id_rentals_post_request import MaterialsMaterialIdRentalsPostRequest
from openapi_server import util


async def materials_material_id_rentals_checkout_post(request: web.Request, material_id, body=None) -> web.Response:
    """Checkout material rental

    

    :param material_id: 
    :type material_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MaterialsMaterialIdRentalsCheckoutPostRequest.from_dict(body)
    return web.Response(status=200)


async def materials_material_id_rentals_get(request: web.Request, material_id) -> web.Response:
    """Show list of rentals for specific material

    

    :param material_id: 
    :type material_id: str

    """
    return web.Response(status=200)


async def materials_material_id_rentals_material_rental_id_delete(request: web.Request, material_id, material_rental_id) -> web.Response:
    """Delete material rental

    Delete rental for material

    :param material_id: 
    :type material_id: str
    :type material_id: str
    :param material_rental_id: 
    :type material_rental_id: str
    :type material_rental_id: str

    """
    return web.Response(status=200)


async def materials_material_id_rentals_material_rental_id_get(request: web.Request, material_id, material_rental_id) -> web.Response:
    """Show rental foor materi

    

    :param material_id: 
    :type material_id: str
    :param material_rental_id: 
    :type material_rental_id: str

    """
    return web.Response(status=200)


async def materials_material_id_rentals_material_rental_id_put(request: web.Request, material_id, material_rental_id) -> web.Response:
    """Edit material rental

    Edit material rental

    :param material_id: 
    :type material_id: str
    :type material_id: str
    :param material_rental_id: 
    :type material_rental_id: str
    :type material_rental_id: str

    """
    return web.Response(status=200)


async def materials_material_id_rentals_post(request: web.Request, material_id, body=None) -> web.Response:
    """Add material rental

    

    :param material_id: 
    :type material_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MaterialsMaterialIdRentalsPostRequest.from_dict(body)
    return web.Response(status=200)
