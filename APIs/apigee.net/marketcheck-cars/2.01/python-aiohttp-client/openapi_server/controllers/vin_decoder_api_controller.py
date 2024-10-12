from typing import List, Dict
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.error import Error
from openapi_server.models.neo_vin import NeoVIN
from openapi_server.models.specs_auto_complete_response import SpecsAutoCompleteResponse
from openapi_server import util


async def decode(request: web.Request, vin, api_key=None) -> web.Response:
    """VIN Decoder

    Get the basic information on specifications for a car identified by a valid VIN

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def decode_via_epi(request: web.Request, vin, api_key=None) -> web.Response:
    """EPI VIN Decoder

    Get the basic information on specifications for a car identified by a valid VIN from EPI&#39;s decoder

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def decode_via_neo_vin(request: web.Request, vin, api_key=None, include_generic=None, force_decode=None) -> web.Response:
    """NeoVIN Decoder

    Get the basic information on specifications for a car identified by a valid VIN from NeoVIN decoder

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param include_generic: Boolean variable to indicate wheather to include generic data as well in response
    :type include_generic: bool
    :param force_decode: Decode VIN on the fly instead of cached response
    :type force_decode: bool

    """
    return web.Response(status=200)


async def get_taxonomy_terms(request: web.Request, _field, api_key=None, year=None, make=None, model=None, trim=None, body_type=None, body_subtype=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, engine=None, engine_size=None, engine_block=None) -> web.Response:
    """API for getting terms from taxonomy

    Facets on taxonomy

    :param _field: Comma separated list of fields to get terms for
    :type _field: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str

    """
    return web.Response(status=200)


async def specs_car_auto_complete_get(request: web.Request, _field, input, api_key=None, year=None, make=None, model=None, trim=None, body_type=None, body_subtype=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, engine=None, engine_size=None, engine_block=None, ignore_case=None, facet_min_count=None) -> web.Response:
    """API for auto-completion of inputs based on taxonomy

    Auto-complete the inputs of your end users, not from active set but from taxonomy (decoder database)

    :param _field: Field name for which you want auto-completion
    :type _field: str
    :param input: Input entered so far
    :type input: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param ignore_case: Boolean variable to indicate ignore case of current input
    :type ignore_case: bool
    :param facet_min_count: Provide minimum count value for facets
    :type facet_min_count: 

    """
    return web.Response(status=200)
