from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.substance import Substance
from openapi_server.models.substance_composition import SubstanceComposition
from openapi_server.models.substance_study import SubstanceStudy
from openapi_server.models.substance_study_summary import SubstanceStudySummary
from openapi_server import util


async def get_substance_by_uuid(request: web.Request, db, uuid, property_uris=None, page=None, pagesize=None) -> web.Response:
    """Get a substance

    Returns substance representation

    :param db: Database ID
    :type db: str
    :param uuid: Substance UUID
    :type uuid: str
    :param property_uris: Property URIs
    :type property_uris: str
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def get_substance_composition_0(request: web.Request, db, uuid, all=None, page=None, pagesize=None) -> web.Response:
    """Substance composition

    Returns substance composition

    :param db: Database ID
    :type db: str
    :param uuid: Substance UUID
    :type uuid: str
    :param all: true (Show all compositions) false (do not show hidden compositions)
    :type all: bool
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def get_substance_structures_0(request: web.Request, db, uuid, page=None, pagesize=None) -> web.Response:
    """Get substance composition as a dataset

    Returns substance composition

    :param db: Database ID
    :type db: str
    :param uuid: Substance UUID
    :type uuid: str
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def get_substance_study_0(request: web.Request, db, uuid, top=None, category=None, property_uri=None, _property=None, investigation_uuid=None, page=None, pagesize=None) -> web.Response:
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


async def get_substance_study_summary_0(request: web.Request, db, uuid, top=None, category=None, property_uri=None, _property=None, result=None, page=None, pagesize=None) -> web.Response:
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


async def get_substances(request: web.Request, db, search=None, type=None, compound_uri=None, bundle_uri=None, add_dummy_substance=None, studysummary=None, page=None, pagesize=None) -> web.Response:
    """List substances

    Returns a list of substances, according to the search criteria

    :param db: Database ID
    :type db: str
    :param search: Search parameter
    :type search: str
    :param type: 
    :type type: str
    :param compound_uri: If type&#x3D;related finds all substances containing this compound; if typ &#x3D;reference - finds all substances with this compound as reference structure
    :type compound_uri: str
    :param bundle_uri: Retrieves if selected in this bundle
    :type bundle_uri: str
    :param add_dummy_substance: Adds a compound record as substance in JSON; only if type&#x3D;related
    :type add_dummy_substance: bool
    :param studysummary: If true retrieves study summary for each substance
    :type studysummary: bool
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)
