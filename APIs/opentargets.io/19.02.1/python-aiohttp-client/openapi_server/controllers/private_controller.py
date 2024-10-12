from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_api_docs(request: web.Request, ) -> web.Response:
    """Browse API documentation

    Access api docs as served by Redoc


    """
    return web.Response(status=200)


async def get_api_swagger_ui(request: web.Request, ) -> web.Response:
    """Browse interactive API documentation

    Interactive API docs using swagger-ui


    """
    return web.Response(status=200)


async def get_autocomplete(request: web.Request, q, size=None) -> web.Response:
    """Get &#x60;autocomplete&#x60; objects.

    Search for the closest term to autocomplete in the search box. 

    :param q: A full text query.
    :type q: str
    :param size: Maximum amount of results to return. Defaults to 5.
    :type size: str

    """
    return web.Response(status=200)


async def get_disease_by_id(request: web.Request, disease) -> web.Response:
    """Find information about a disease

    Get &#x60;disease&#x60; objects. 

    :param disease: An EFO identifier.
    :type disease: str

    """
    return web.Response(status=200)


async def get_drug_by_id(request: web.Request, drug_id, drug_id2) -> web.Response:
    """Get drug by ID

    Get &#x60;drug&#x60; objects. 

    :param drug_id: An ID in the drug index.
    :type drug_id: str
    :param drug_id2: Automatically added
    :type drug_id2: str

    """
    return web.Response(status=200)


async def get_ec_oby_id(request: web.Request, eco_id) -> web.Response:
    """Get evidence code by ID

    Get &#x60;ECO&#x60; objects. 

    :param eco_id: An [evidence code ontology](http://www.ebi.ac.uk/ols/v2/browse.do?ontName&#x3D;ECO) ID.
    :type eco_id: str

    """
    return web.Response(status=200)


async def get_quick_search(request: web.Request, q, size=None) -> web.Response:
    """Search most relevant results

    Get &#x60;search-result&#x60; objects. Enables search bar functionality. 

    :param q: A full text query.
    :type q: str
    :param size: Maximum amount of results to return. Defaults to 5.
    :type size: str

    """
    return web.Response(status=200)


async def get_relation_by_efoid(request: web.Request, disease) -> web.Response:
    """Find related entities by disease

    Get &#x60;relation&#x60; objects starting from diseases. 

    :param disease: An EFO gene identifier.
    :type disease: str

    """
    return web.Response(status=200)


async def get_relation_by_ensgid(request: web.Request, target) -> web.Response:
    """Find related entities by target

    Get &#x60;relation&#x60; objects starting from diseases. 

    :param target: An Ensembl gene identifier.
    :type target: str

    """
    return web.Response(status=200)


async def get_swagger(request: web.Request, ) -> web.Response:
    """Get OpenAPI schema

    Get swagger.yaml specs for the API


    """
    return web.Response(status=200)


async def get_target_by_ensgid(request: web.Request, target) -> web.Response:
    """Find information about a target

    Get &#x60;target&#x60; objects. 

    :param target: An Ensembl gene ID for the target of interest.
    :type target: str

    """
    return web.Response(status=200)


async def get_target_expression_by_ensgid(request: web.Request, gene) -> web.Response:
    """Query expression levels

    Get &#x60;gene-expression&#x60; objects. 

    :param gene: An Ensembl gene identifier.
    :type gene: str

    """
    return web.Response(status=200)


async def post_best_hit_search(request: web.Request, body) -> web.Response:
    """Find the best hit

    Fire the search method for multiple strings 

    :param body: list of strings to search for
    :type body: str

    """
    return web.Response(status=200)


async def post_disease_by_id(request: web.Request, body) -> web.Response:
    """Find information about a list of diseases

    Get &#x60;disease&#x60; objects. 

    :param body: An EFO identifier.
    :type body: str

    """
    return web.Response(status=200)


async def post_enrichment_target(request: web.Request, body) -> web.Response:
    """Enrichment analysis

    Returns an enrichment analysis for a list of targets passed in the body 

    :param body: IDs of the targets to do the enrichment analysis for.
    :type body: str

    """
    return web.Response(status=200)


async def post_relation(request: web.Request, body) -> web.Response:
    """Find related entities

    Get &#x60;relation&#x60; objects. 

    :param body: An Ensembl gene identifier.
    :type body: str

    """
    return web.Response(status=200)


async def post_target_by_ensgid(request: web.Request, body) -> web.Response:
    """Find information about a list of targets

    Get &#x60;target&#x60; objects. Used for the target profile page. 

    :param body: An Ensembl gene identifier.
    :type body: str

    """
    return web.Response(status=200)


async def post_target_expression_by_ensgid(request: web.Request, body) -> web.Response:
    """Batch query expression levels

    Get &#x60;gene-expression&#x60; objects. 

    :param body: An Ensembl gene identifier.
    :type body: str

    """
    return web.Response(status=200)
