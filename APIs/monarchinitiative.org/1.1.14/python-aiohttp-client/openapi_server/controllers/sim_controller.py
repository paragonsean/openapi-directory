from typing import List, Dict
from aiohttp import web

from openapi_server.models.compare_input import CompareInput
from openapi_server.models.sim_result import SimResult
from openapi_server.models.sufficiency_output import SufficiencyOutput
from openapi_server.models.sufficiency_post_input import SufficiencyPostInput
from openapi_server import util


async def get_annotation_score(request: web.Request, id=None, absent_id=None) -> web.Response:
    """Get annotation score

    

    :param id: Phenotype identifier (eg HP:0004935)
    :type id: List[str]
    :param absent_id: absent phenotype (eg HP:0002828)
    :type absent_id: List[str]

    """
    return web.Response(status=200)


async def get_sim_compare(request: web.Request, is_feature_set=None, metric=None, ref_id=None, query_id=None) -> web.Response:
    """Compare a reference profile vs one profiles

    

    :param is_feature_set: set to true if *all* input ids are phenotypic features, else set to false
    :type is_feature_set: bool
    :param metric: Metric for computing similarity
    :type metric: str
    :param ref_id: A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    :type ref_id: List[str]
    :param query_id: A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    :type query_id: List[str]

    """
    return web.Response(status=200)


async def get_sim_search(request: web.Request, is_feature_set=None, metric=None, id=None, limit=None, taxon=None) -> web.Response:
    """Search for phenotypically similar diseases or model genes

    

    :param is_feature_set: set to true if *all* input ids are phenotypic features, else set to false
    :type is_feature_set: bool
    :param metric: Metric for computing similarity
    :type metric: str
    :param id: A phenotype or identifier that is composed of phenotypes (eg disease, gene)
    :type id: List[str]
    :param limit: number of rows, max 500
    :type limit: int
    :param taxon: ncbi taxon id
    :type taxon: str

    """
    return web.Response(status=200)


async def post_annotation_score(request: web.Request, body) -> web.Response:
    """Get annotation score

    

    :param body: 
    :type body: dict | bytes

    """
    body = SufficiencyPostInput.from_dict(body)
    return web.Response(status=200)


async def post_sim_compare(request: web.Request, body) -> web.Response:
    """Compare a reference profile vs one or more profiles

    

    :param body: 
    :type body: dict | bytes

    """
    body = CompareInput.from_dict(body)
    return web.Response(status=200)
