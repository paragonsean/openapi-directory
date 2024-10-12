from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.substance_composition import SubstanceComposition
from openapi_server import util


async def get_substance_composition(request: web.Request, db, uuid, all=None, page=None, pagesize=None) -> web.Response:
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


async def get_substance_structures(request: web.Request, db, uuid, page=None, pagesize=None) -> web.Response:
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


async def search_by_identifier(request: web.Request, db, term, representation, search=None, b64search=None, casesens=None, bundle_uri=None, sameas=None, page=None, pagesize=None) -> web.Response:
    """Exact chemical structure search

    Returns compounds found

    :param db: Database ID
    :type db: str
    :param term: search term type
    :type term: str
    :param representation: 
    :type representation: str
    :param search: Compound identifier (SMILES, InChI, name, registry identifiers)
    :type search: str
    :param b64search: Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter
    :type b64search: str
    :param casesens: Case sensitive search if yes
    :type casesens: bool
    :param bundle_uri: Bundle URI
    :type bundle_uri: str
    :param sameas: Ontology URI to define groups of columns
    :type sameas: str
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def search_by_similarity(request: web.Request, db, search=None, b64search=None, type=None, threshold=None, dataset_uri=None, filter_by_substance=None, bundle_uri=None, sameas=None, mol=None, page=None, pagesize=None) -> web.Response:
    """Exact similarity search

    Returns similar compounds

    :param db: Database ID
    :type db: str
    :param search: Compound identifier (SMILES, InChI, name, registry identifiers)
    :type search: str
    :param b64search: Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter
    :type b64search: str
    :param type: Defines the expected content of the search parameter
    :type type: str
    :param threshold: Similarity threshold
    :type threshold: 
    :param dataset_uri: Restrict the search within the AMBIT dataset specified with the URI
    :type dataset_uri: str
    :param filter_by_substance: Restrict the search within the set of structures with assigned substances
    :type filter_by_substance: bool
    :param bundle_uri: If the structure is used in the specified bundle URI, the selection tag will be returned
    :type bundle_uri: str
    :param sameas: Ontology URI to define groups of columns
    :type sameas: str
    :param mol: Only for application/json; to include mol as JSON field
    :type mol: bool
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)


async def search_by_smarts(request: web.Request, db, search=None, b64search=None, type=None, dataset_uri=None, filter_by_substance=None, bundle_uri=None, sameas=None, mol=None, page=None, pagesize=None) -> web.Response:
    """Substructure search

    Returns compounds with the specified substructure

    :param db: Database ID
    :type db: str
    :param search: Compound identifier (SMILES, InChI, name, registry identifiers)
    :type search: str
    :param b64search: Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter
    :type b64search: str
    :param type: Defines the expected content of the search parameter
    :type type: str
    :param dataset_uri: Restrict the search within the AMBIT dataset specified with the URI
    :type dataset_uri: str
    :param filter_by_substance: Restrict the search within the set of structures with assigned substances
    :type filter_by_substance: bool
    :param bundle_uri: If the structure is used in the specified bundle URI, the selection tag will be returned
    :type bundle_uri: str
    :param sameas: Ontology URI to define groups of columns
    :type sameas: str
    :param mol: Only for application/json; to include mol as JSON field
    :type mol: bool
    :param page: Starting page
    :type page: int
    :param pagesize: Page size
    :type pagesize: int

    """
    return web.Response(status=200)
