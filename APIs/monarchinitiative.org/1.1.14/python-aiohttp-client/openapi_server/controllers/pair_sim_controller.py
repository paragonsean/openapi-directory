from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_pair_sim_jaccard_resource(request: web.Request, id2, id1, object_category=None) -> web.Response:
    """Get pairwise similarity

    

    :param id2: id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644
    :type id2: str
    :param id1: id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465
    :type id1: str
    :param object_category: e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category
    :type object_category: str

    """
    return web.Response(status=200)
