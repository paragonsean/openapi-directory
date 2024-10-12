from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_mart_case_associations_resource(request: web.Request, taxon, object_category, slim=None) -> web.Response:
    """Bulk download of case associations

    NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

    :param taxon: taxon of case, must be of form NCBITaxon:9606
    :type taxon: str
    :param object_category: Category of entity at link Subject (target), e.g. phenotype, disease
    :type object_category: str
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]

    """
    return web.Response(status=200)


async def get_mart_disease_associations_resource(request: web.Request, taxon, object_category, slim=None) -> web.Response:
    """Bulk download of disease associations

    NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

    :param taxon: taxon of disease, must be of form NCBITaxon:9606
    :type taxon: str
    :param object_category: Category of entity at link Object (target), e.g. phenotype, disease
    :type object_category: str
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]

    """
    return web.Response(status=200)


async def get_mart_gene_associations_resource(request: web.Request, taxon, object_category, slim=None) -> web.Response:
    """Bulk download of gene associations

    NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

    :param taxon: taxon of gene, must be of form NCBITaxon:9606
    :type taxon: str
    :param object_category: Category of entity at link Object (target), e.g. phenotype, disease
    :type object_category: str
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]

    """
    return web.Response(status=200)


async def get_mart_ortholog_associations_resource(request: web.Request, taxon2, taxon1) -> web.Response:
    """Bulk download of orthologs

    

    :param taxon2: object taxon, e.g. NCBITaxon:10090
    :type taxon2: str
    :param taxon1: subject taxon, e.g. NCBITaxon:9606
    :type taxon1: str

    """
    return web.Response(status=200)


async def get_mart_paralog_associations_resource(request: web.Request, taxon2, taxon1) -> web.Response:
    """Bulk download of paralogs

    

    :param taxon2: object taxon, e.g. NCBITaxon:9606
    :type taxon2: str
    :param taxon1: subject taxon, e.g. NCBITaxon:9606
    :type taxon1: str

    """
    return web.Response(status=200)
