from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_server.models.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_castegroup_out import BatchPersonalNameCastegroupOut
from openapi_server.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_server.models.batch_personal_name_geo_subclassification_out import BatchPersonalNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_religioned_out import BatchPersonalNameReligionedOut
from openapi_server.models.batch_personal_name_subdivision_in import BatchPersonalNameSubdivisionIn
from openapi_server.models.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
from openapi_server.models.personal_name_castegroup_out import PersonalNameCastegroupOut
from openapi_server.models.personal_name_geo_subclassification_out import PersonalNameGeoSubclassificationOut
from openapi_server.models.personal_name_religioned_out import PersonalNameReligionedOut
from openapi_server import util


async def castegroup_indian_full(request: web.Request, sub_division_iso31662, personal_name_full) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.

    

    :param sub_division_iso31662: 
    :type sub_division_iso31662: str
    :param personal_name_full: 
    :type personal_name_full: str

    """
    return web.Response(status=200)


async def castegroup_indian_full_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameSubdivisionIn.from_dict(body)
    return web.Response(status=200)


async def religion(request: web.Request, sub_division_iso31662, personal_name_full) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).

    

    :param sub_division_iso31662: 
    :type sub_division_iso31662: str
    :param personal_name_full: 
    :type personal_name_full: str

    """
    return web.Response(status=200)


async def religion_indian_full_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameSubdivisionIn.from_dict(body)
    return web.Response(status=200)


async def subclassification_indian(request: web.Request, first_name, last_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str

    """
    return web.Response(status=200)


async def subclassification_indian_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGeoIn.from_dict(body)
    return web.Response(status=200)


async def subclassification_indian_full(request: web.Request, full_name) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.

    

    :param full_name: 
    :type full_name: str

    """
    return web.Response(status=200)


async def subclassification_indian_full_batch(request: web.Request, body=None) -> web.Response:
    """[USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameGeoIn.from_dict(body)
    return web.Response(status=200)
