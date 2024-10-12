from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotated_gene_request import AnnotatedGeneRequest
from openapi_server.models.gene import Gene
from openapi_server.models.mapped_gene import MappedGene
from openapi_server.models.mapped_gene_position import MappedGenePosition
from openapi_server.models.ortholog_request import OrthologRequest
from openapi_server import util


async def get_all_annotated_genes_using_get(request: web.Request, acc_id) -> web.Response:
    """Return a list of genes annotated to an ontology term

    

    :param acc_id: Accesstion ID
    :type acc_id: str

    """
    return web.Response(status=200)


async def get_annotated_genes_using_post(request: web.Request, body=None) -> web.Response:
    """Return a list of genes annotated to an ontology term

    

    :param body: data
    :type body: dict | bytes

    """
    body = AnnotatedGeneRequest.from_dict(body)
    return web.Response(status=200)


async def get_gene_alleles_using_get(request: web.Request, rgd_id) -> web.Response:
    """Return a list of gene alleles

    

    :param rgd_id: RGD ID of gene
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_gene_by_map_key_using_get(request: web.Request, map_key) -> web.Response:
    """Return a list of all genes with position information for an assembly

    

    :param map_key: A list of RGD assembly map keys can be found in the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_gene_by_rgd_id_using_get(request: web.Request, rgd_id) -> web.Response:
    """Get a gene record by RGD ID

    

    :param rgd_id: The RGD ID of a Gene in RGD
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_gene_by_symbol_using_get(request: web.Request, symbol, species_type_key) -> web.Response:
    """Get a gene record by symbol and species type key

    

    :param symbol: Gene Symbol
    :type symbol: str
    :param species_type_key: Species type key.  A list of species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_gene_orthologs_using_get(request: web.Request, rgd_id) -> web.Response:
    """Return a list of gene orthologs

    

    :param rgd_id: RGD ID of a gene
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_genes_annotated_using_get(request: web.Request, acc_id, species_type_key) -> web.Response:
    """Return a list of genes annotated to an ontology term

    

    :param acc_id: Ontology term accession ID
    :type acc_id: str
    :param species_type_key: Species type key.  A list of species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_genes_by_affy_id_using_get(request: web.Request, affy_id, species_type_key) -> web.Response:
    """Return a list of genes for an affymetrix ID

    

    :param affy_id: Affymetrix ID
    :type affy_id: str
    :param species_type_key: A list of RGD species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_genes_by_alias_symbol_using_get(request: web.Request, alias_symbol, species_type_key) -> web.Response:
    """Return a list of genes for an alias and species

    

    :param alias_symbol: Gene alias symbol
    :type alias_symbol: str
    :param species_type_key: A list of RGD species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_genes_by_keyword_using_get(request: web.Request, keyword, species_type_key) -> web.Response:
    """Return a list of genes by keyword and species type key

    

    :param keyword: Search keyword
    :type keyword: str
    :param species_type_key: Species type key.  A list of species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_genes_by_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Return a list of genes position and map key

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: A list of RGD assembly map keys can be found in the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_genes_by_species_using_get(request: web.Request, species_type_key) -> web.Response:
    """Return a list of all genes for a species in RGD

    

    :param species_type_key: A list of RGD species type keys can be found in the lookup service
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_genes_in_region_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Return a list of genes in region

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: A list of RGD assembly map keys can be found in the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_mapped_genes_by_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Return a list of genes position and map key

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: A list of RGD assembly map keys can be found in the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_orthologs_by_list_using_post(request: web.Request, body) -> web.Response:
    """Return a list of gene orthologs

    

    :param body: orthologRequest
    :type body: dict | bytes

    """
    body = OrthologRequest.from_dict(body)
    return web.Response(status=200)
