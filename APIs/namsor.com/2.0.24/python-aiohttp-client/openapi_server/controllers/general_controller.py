from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_name_geo_in import BatchNameGeoIn
from openapi_server.models.batch_name_in import BatchNameIn
from openapi_server.models.batch_proper_noun_categorized_out import BatchProperNounCategorizedOut
from openapi_server.models.proper_noun_categorized_out import ProperNounCategorizedOut
from openapi_server import util


async def name_type(request: web.Request, proper_noun) -> web.Response:
    """Infer the likely type of a proper noun (personal name, brand name, place name etc.)

    

    :param proper_noun: 
    :type proper_noun: str

    """
    return web.Response(status=200)


async def name_type_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)

    

    :param body: A list of proper names
    :type body: dict | bytes

    """
    body = BatchNameIn.from_dict(body)
    return web.Response(status=200)


async def name_type_geo(request: web.Request, proper_noun, country_iso2) -> web.Response:
    """Infer the likely type of a proper noun (personal name, brand name, place name etc.)

    

    :param proper_noun: 
    :type proper_noun: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)


async def name_type_geo_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)

    

    :param body: A list of proper names
    :type body: dict | bytes

    """
    body = BatchNameGeoIn.from_dict(body)
    return web.Response(status=200)
