from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_ontology_subset(request: web.Request, id) -> web.Response:
    """Returns meta data of an ontology subset (slim)

    

    :param id: name of a slim subset, e.g. goslim_agr, goslim_generic
    :type id: str

    """
    return web.Response(status=200)


async def get_ontology_term(request: web.Request, id) -> web.Response:
    """Returns meta data of an ontology term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0003677
    :type id: str

    """
    return web.Response(status=200)


async def get_ontology_term_graph(request: web.Request, id, graph_type=None) -> web.Response:
    """Returns graph of an ontology term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0000981
    :type id: str
    :param graph_type: graph type (&#39;topology_graph&#39;, &#39;regulates_transitivity_graph&#39; or &#39;neighborhood_graph&#39;)
    :type graph_type: str

    """
    return web.Response(status=200)


async def get_ontology_term_subgraph(request: web.Request, id, cnode=None, include_ancestors=None, include_descendants=None, relation=None, include_meta=None) -> web.Response:
    """Extract a subgraph from an ontology term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0007275
    :type id: str
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


async def get_ontology_term_subsets(request: web.Request, id) -> web.Response:
    """Returns subsets (slims) associated to an ontology term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0006259
    :type id: str

    """
    return web.Response(status=200)


async def get_ontology_terms_shared_ancestor(request: web.Request, subject, object) -> web.Response:
    """Returns the ancestor ontology terms shared by two ontology terms

    

    :param subject: CURIE identifier of a GO term, e.g. GO:0006259
    :type subject: str
    :param object: CURIE identifier of a GO term, e.g. GO:0046483
    :type object: str

    """
    return web.Response(status=200)
