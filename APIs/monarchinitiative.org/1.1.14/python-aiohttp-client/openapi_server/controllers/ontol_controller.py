from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_extract_ontology_subgraph_resource(request: web.Request, node, ontology, cnode=None, include_ancestors=None, include_descendants=None, relation=None, include_meta=None) -> web.Response:
    """Extract a subgraph from an ontology

    

    :param node: class ID, e.g. HP:0001288
    :type node: str
    :param ontology: ontology ID, e.g. go, uberon, mp, hp
    :type ontology: str
    :param cnode: Additional classes
    :type cnode: List[str]
    :param include_ancestors: Include Ancestors
    :type include_ancestors: bool
    :param include_descendants: Include Descendants
    :type include_descendants: bool
    :param relation: Additional classes
    :type relation: List[str]
    :param include_meta: Include metadata in response
    :type include_meta: bool

    """
    return web.Response(status=200)


async def get_information_content_resource(request: web.Request, subject_category, object_category, subject_taxon, evidence=None) -> web.Response:
    """Returns information content (IC) for a set of relevant ontology classes

    &#x60;&#x60;&#x60; IC &#x3D; -log2( freq(t) / popSize ) &#x60;&#x60;&#x60;  Here the frequency and population is calculated for a particular dataset: e.g. all human disease-phenotype associations

    :param subject_category: 
    :type subject_category: str
    :param object_category: 
    :type object_category: str
    :param subject_taxon: 
    :type subject_taxon: str
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    :type evidence: str

    """
    return web.Response(status=200)


async def post_extract_ontology_subgraph_resource(request: web.Request, node, ontology, cnode=None, include_ancestors=None, include_descendants=None, relation=None, include_meta=None) -> web.Response:
    """Extract a subgraph from an ontology

    

    :param node: class ID, e.g. HP:0001288
    :type node: str
    :param ontology: ontology ID, e.g. go, uberon, mp, hp
    :type ontology: str
    :param cnode: Additional classes
    :type cnode: List[str]
    :param include_ancestors: Include Ancestors
    :type include_ancestors: bool
    :param include_descendants: Include Descendants
    :type include_descendants: bool
    :param relation: Additional classes
    :type relation: List[str]
    :param include_meta: Include metadata in response
    :type include_meta: bool

    """
    return web.Response(status=200)
