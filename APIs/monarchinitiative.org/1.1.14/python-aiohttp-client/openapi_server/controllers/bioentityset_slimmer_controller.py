from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_entity_set_anatomy_slimmer(request: web.Request, subject, slim, exclude_automatic_assertions=None, rows=None, start=None) -> web.Response:
    """For a given gene(s), summarize its annotations over a defined set of slim

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    :type slim: List[str]
    :param exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int

    """
    return web.Response(status=200)


async def get_entity_set_function_slimmer(request: web.Request, subject, slim, relationship_type=None, exclude_automatic_assertions=None, rows=None, start=None) -> web.Response:
    """For a given gene(s), summarize its annotations over a defined set of slim

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    :type slim: List[str]
    :param relationship_type: relationship type (&#39;involved_in&#39; or &#39;acts_upstream_of_or_within&#39;)
    :type relationship_type: str
    :param exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int

    """
    return web.Response(status=200)


async def get_entity_set_phenotype_slimmer(request: web.Request, subject, slim, exclude_automatic_assertions=None, rows=None, start=None) -> web.Response:
    """For a given gene(s), summarize its annotations over a defined set of slim

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
    :type slim: List[str]
    :param exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int

    """
    return web.Response(status=200)
