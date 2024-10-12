from typing import List, Dict
from aiohttp import web

from openapi_server.models.enrichment_gene_request import EnrichmentGeneRequest
from openapi_server.models.enrichment_request import EnrichmentRequest
from openapi_server import util


async def get_enrichment_data_using_post(request: web.Request, body) -> web.Response:
    """Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology

    

    :param body: geneRequest
    :type body: dict | bytes

    """
    body = EnrichmentGeneRequest.from_dict(body)
    return web.Response(status=200)


async def get_enrichment_data_using_post1(request: web.Request, body) -> web.Response:
    """Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group

    

    :param body: enrichmentRequest
    :type body: dict | bytes

    """
    body = EnrichmentRequest.from_dict(body)
    return web.Response(status=200)
