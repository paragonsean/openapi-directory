from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server import util


async def get_entity_set_homologs(request: web.Request, subject=None) -> web.Response:
    """Returns homology associations for a given input set of genes

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]

    """
    return web.Response(status=200)
