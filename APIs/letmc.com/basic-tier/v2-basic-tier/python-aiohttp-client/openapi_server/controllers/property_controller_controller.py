from typing import List, Dict
from aiohttp import web

from openapi_server.models.photo_model_results import PhotoModelResults
from openapi_server.models.property_facility_model_results import PropertyFacilityModelResults
from openapi_server.models.property_model import PropertyModel
from openapi_server.models.property_model_results import PropertyModelResults
from openapi_server.models.property_room_model_results import PropertyRoomModelResults
from openapi_server.models.tenancy_model_results import TenancyModelResults
from openapi_server import util


async def property_controller_get_properties_facilities(request: web.Request, short_name, property_id, offset, count) -> web.Response:
    """A collection of facilities linked to a block, property or room

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_id: The unique ID of the Property
    :type property_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def property_controller_get_properties_photos(request: web.Request, short_name, property_id, offset, count) -> web.Response:
    """A collection showing all the photos linked to a specific block, property or room

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_id: The unique ID of the Property
    :type property_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def property_controller_get_properties_rooms(request: web.Request, short_name, property_id, offset, count) -> web.Response:
    """A collection of the rooms that belong to this property or block

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_id: The unique ID of the Property
    :type property_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def property_controller_get_properties_tenancies(request: web.Request, short_name, property_id, offset, count) -> web.Response:
    """A collection of all tenancies associated with this block, property or room

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_id: The unique ID of the Property
    :type property_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def property_controller_get_property_eer_download(request: web.Request, short_name, property_structure_id) -> web.Response:
    """Downloads the energy efficiency report (EER) graph for a property

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_structure_id: The unique ID of the property structure
    :type property_structure_id: str

    """
    return web.Response(status=200)


async def property_controller_get_property_eir_download(request: web.Request, short_name, property_structure_id) -> web.Response:
    """Downloads the environmental impact report (EIR) graph for a property

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_structure_id: The unique ID of the property structure
    :type property_structure_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_property_properties_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all properties within a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier2_short_name_property_properties_property_idget(request: web.Request, short_name, property_id) -> web.Response:
    """Get a specific property given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_id: The unique ID of the Property
    :type property_id: str

    """
    return web.Response(status=200)
