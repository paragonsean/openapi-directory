from typing import List, Dict
from aiohttp import web

from openapi_server.models.facet import Facet
from openapi_server.models.investigation import Investigation
from openapi_server.models.substance_study import SubstanceStudy
from openapi_server.models.substance_study_summary import SubstanceStudySummary
from openapi_server import util


async def get_endpoint_summary(request: web.Request, db, top=None, category=None) -> web.Response:
    """Search endpoint summary

    Returns endpoint summary

    :param db: Database ID
    :type db: str
    :param top: Top endpoint category
    :type top: str
    :param category: Endpoint category (The value in the protocol.category.code field)
    :type category: str

    """
    return web.Response(status=200)


async def get_investigation_results(request: web.Request, db, type, search, inchikey=None, id=None, page=None, pagesize=None) -> web.Response:
    """Details of multiple studies

    Multiple studies in tabular form

    :param db: Database ID
    :type db: str
    :param type: query type
    :type type: str
    :param search: Search parameter, UUID of the investigation or a substance
    :type search: str
    :param inchikey: Search parameter, InChI key(s) of the substance component(s), comma delimited
    :type inchikey: str
    :param id: Search parameter, chemical structure or substance identifier(s), comma delimited
    :type id: str
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def get_substance_study(request: web.Request, db, uuid, top=None, category=None, property_uri=None, _property=None, investigation_uuid=None, page=None, pagesize=None) -> web.Response:
    """get substance study

    Returns substance study representation

    :param db: Database ID
    :type db: str
    :param uuid: Substance UUID
    :type uuid: str
    :param top: Top endpoint category
    :type top: str
    :param category: Endpoint category (The value in the protocol.category.code field)
    :type category: str
    :param property_uri: Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    :type property_uri: str
    :param _property: Property UUID
    :type _property: str
    :param investigation_uuid: Investigation UUID, a code to link different studies
    :type investigation_uuid: str
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def get_substance_study_summary(request: web.Request, db, uuid, top=None, category=None, property_uri=None, _property=None, result=None, page=None, pagesize=None) -> web.Response:
    """Get study summary for the substance

    Study summary

    :param db: Database ID
    :type db: str
    :param uuid: Substance UUID
    :type uuid: str
    :param top: Top endpoint category
    :type top: str
    :param category: Endpoint category (The value in the protocol.category.code field)
    :type category: str
    :param property_uri: Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    :type property_uri: str
    :param _property: Property UUID, see Property service
    :type _property: str
    :param result: If true will group by topcategory,endpointcategory,interpretation result
    :type result: bool
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)
