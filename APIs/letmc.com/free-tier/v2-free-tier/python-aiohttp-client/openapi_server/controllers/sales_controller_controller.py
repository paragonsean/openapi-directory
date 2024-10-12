from typing import List, Dict
from aiohttp import web

from openapi_server.models.photo_model_results import PhotoModelResults
from openapi_server.models.property_room_model_results import PropertyRoomModelResults
from openapi_server.models.sales_feature_model_results import SalesFeatureModelResults
from openapi_server.models.sales_feature_type_model import SalesFeatureTypeModel
from openapi_server.models.sales_feature_type_model_results import SalesFeatureTypeModelResults
from openapi_server.models.sales_instruction_model import SalesInstructionModel
from openapi_server.models.sales_instruction_model_results import SalesInstructionModelResults
from openapi_server import util


async def sales_controller_get_advertised_sales(request: web.Request, short_name, branch_id, offset, count, only_developement, only_investements, minimum_price=None, maximum_price=None, minimum_beds=None, minimum_bathrooms=None, minimum_ensuites=None, minimum_toilets=None, minimum_reception=None) -> web.Response:
    """Search all sales properties available given a range of search criteria

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int
    :param only_developement: Show only development properties?
    :type only_developement: bool
    :param only_investements: Show only investment properties?
    :type only_investements: bool
    :param minimum_price: The minimum price to search for
    :type minimum_price: float
    :param maximum_price: The maximum price to search for
    :type maximum_price: float
    :param minimum_beds: The minimum beds to search for
    :type minimum_beds: int
    :param minimum_bathrooms: The minimum bathrooms to search for
    :type minimum_bathrooms: int
    :param minimum_ensuites: The minimum ensuite bathrooms to search for
    :type minimum_ensuites: int
    :param minimum_toilets: The minimum toilets to search for
    :type minimum_toilets: int
    :param minimum_reception: The minimum reception rooms to search for
    :type minimum_reception: int

    """
    return web.Response(status=200)


async def sales_controller_get_eer(request: web.Request, short_name, sales_instruction_id) -> web.Response:
    """Downloads the energy efficiency report (EER) graph for a sales instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str

    """
    return web.Response(status=200)


async def sales_controller_get_eir(request: web.Request, short_name, sales_instruction_id) -> web.Response:
    """Downloads the energy efficiency report (EIR) graph for a sales instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str

    """
    return web.Response(status=200)


async def sales_controller_get_sales_instructions_features(request: web.Request, short_name, sales_instruction_id, offset, count) -> web.Response:
    """A collection of all features linked to a sales instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def sales_controller_get_sales_instructions_floor_plans(request: web.Request, short_name, sales_instruction_id, offset, count) -> web.Response:
    """A collection of floor plans linked to an instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def sales_controller_get_sales_instructions_photos(request: web.Request, short_name, sales_instruction_id, offset, count) -> web.Response:
    """A collection of photos linked to an instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def sales_controller_get_sales_instructions_rooms(request: web.Request, short_name, sales_instruction_id, offset, count) -> web.Response:
    """A collection of rooms linked to an instruction

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_sales_salesfeaturetypes_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all sales feature types linked to a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_sales_salesfeaturetypes_sales_feature_type_idget(request: web.Request, short_name, sales_feature_type_id) -> web.Response:
    """Get a specific sales feature type given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_feature_type_id: The unique ID of the SalesFeatureType
    :type sales_feature_type_id: str

    """
    return web.Response(status=200)


async def v2_tier1_short_name_sales_salesinstructions_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all sales instructions linked to a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_sales_salesinstructions_sales_instruction_idget(request: web.Request, short_name, sales_instruction_id) -> web.Response:
    """Get a specific sales instruction given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param sales_instruction_id: The unique ID of the SalesInstruction
    :type sales_instruction_id: str

    """
    return web.Response(status=200)
