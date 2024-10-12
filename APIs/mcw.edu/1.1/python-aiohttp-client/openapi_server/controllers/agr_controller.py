from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_affected_genomic_models_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)


async def get_alleles_for_taxon_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get gene allele records submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)


async def get_expression_for_taxon_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get expression annotations submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)


async def get_genes_for_latest_assembly_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get gene records submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)


async def get_phenotypes_for_taxon_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get phenotype annotations submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)


async def get_variants_for_taxon_using_get(request: web.Request, taxon_id) -> web.Response:
    """Get basic variant records submitted by RGD to AGR by taxonId

    

    :param taxon_id: The taxon ID for species
    :type taxon_id: str

    """
    return web.Response(status=200)
