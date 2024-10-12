from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server import util


async def get_entity_set_associations(request: web.Request, subject=None, background=None, object_category=None, object_slim=None) -> web.Response:
    """Returns compact associations for a given input set

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param background: Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    :type background: List[str]
    :param object_category: E.g. phenotype, function
    :type object_category: str
    :param object_slim: Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    :type object_slim: str

    """
    return web.Response(status=200)


async def get_entity_set_graph_resource(request: web.Request, subject=None, background=None, object_category=None, object_slim=None) -> web.Response:
    """TODO Graph object spanning all entities

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param background: Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    :type background: List[str]
    :param object_category: E.g. phenotype, function
    :type object_category: str
    :param object_slim: Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    :type object_slim: str

    """
    return web.Response(status=200)


async def get_entity_set_summary(request: web.Request, subject=None, background=None, object_category=None, object_slim=None) -> web.Response:
    """Summary statistics for objects associated

    

    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param background: Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    :type background: List[str]
    :param object_category: E.g. phenotype, function
    :type object_category: str
    :param object_slim: Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    :type object_slim: str

    """
    return web.Response(status=200)


async def get_over_representation(request: web.Request, object_category=None, subject=None, background=None, subject_category=None, max_p_value=None, ontology=None, taxon=None) -> web.Response:
    """Summary statistics for objects associated

    

    :param object_category: E.g. phenotype, function
    :type object_category: str
    :param subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    :type subject: List[str]
    :param background: Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    :type background: List[str]
    :param subject_category: Default: gene. Other types may be used e.g. disease but statistics may not make sense
    :type subject_category: str
    :param max_p_value: Exclude results with p-value greater than this
    :type max_p_value: str
    :param ontology: ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank)
    :type ontology: str
    :param taxon: must be NCBITaxon CURIE. Example: NCBITaxon:9606
    :type taxon: str

    """
    return web.Response(status=200)
