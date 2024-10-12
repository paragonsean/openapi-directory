from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotation_request import AnnotationRequest
from openapi_server.models.map_pair import MapPair
from openapi_server import util


async def get_annotation_count_by_acc_id_and_object_type_using_get(request: web.Request, acc_id, species_type_key, include_children, object_type) -> web.Response:
    """Returns annotation count for ontology accession ID and object type

    

    :param acc_id: Ontology term accession ID
    :type acc_id: str
    :param species_type_key: A list of species type keys can be found using the lookup service
    :type species_type_key: int
    :param include_children: true: return annotations for the term and children, false: return annotations for the term only 
    :type include_children: bool
    :param object_type: A list of object types can be found using the lookup service
    :type object_type: int

    """
    return web.Response(status=200)


async def get_annotation_count_by_acc_id_and_species_using_get(request: web.Request, acc_id, species_type_key, include_children) -> web.Response:
    """Returns annotation count for ontology accession ID and speicies

    

    :param acc_id: Ontology term accession ID
    :type acc_id: str
    :param species_type_key: A list of species type keys can be found using the lookup service
    :type species_type_key: int
    :param include_children: true: return annotations for the term and children, false: return annotations for the term only 
    :type include_children: bool

    """
    return web.Response(status=200)


async def get_annotation_count_by_acc_id_using_get(request: web.Request, acc_id, include_children) -> web.Response:
    """Returns annotation count for ontology accession ID

    

    :param acc_id: Ontology term accession ID
    :type acc_id: str
    :param include_children: true: return annotations for the term and children, false: return annotations for the term only 
    :type include_children: bool

    """
    return web.Response(status=200)


async def get_annotations_by_acc_id_and_rgd_id_using_get(request: web.Request, acc_id, rgd_id) -> web.Response:
    """Returns a list of annotations by RGD ID and ontology term accession ID

    

    :param acc_id: Ontology Term Accession ID
    :type acc_id: str
    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_annotations_by_rgd_id_and_ontology_using_get(request: web.Request, rgd_id, ontology_prefix) -> web.Response:
    """Returns a list of annotations by RGD ID and ontology prefix

    

    :param rgd_id: RGD ID
    :type rgd_id: int
    :param ontology_prefix: Ontology Prefix.  The prefix can be found left of the semicolon in an ontology term accession ID.  As an example, term accession PW:0000034 has the ontology prefix PW
    :type ontology_prefix: str

    """
    return web.Response(status=200)


async def get_annotations_by_rgd_id_using_get(request: web.Request, rgd_id) -> web.Response:
    """Returns a list of annotations by RGD ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_annotations_using_get(request: web.Request, acc_id, species_type_key, include_children) -> web.Response:
    """Returns a list annotations for an ontology term or a term and it&#39;s children

    

    :param acc_id: Ontology term accession ID
    :type acc_id: str
    :param species_type_key: A list of species type keys can be found using the lookup service
    :type species_type_key: int
    :param include_children: true: return annotations for the term and children, false: return annotations for the term only 
    :type include_children: bool

    """
    return web.Response(status=200)


async def get_annotations_using_post(request: web.Request, body=None) -> web.Response:
    """Return a list of genes annotated to an ontology term

    

    :param body: data
    :type body: dict | bytes

    """
    body = AnnotationRequest.from_dict(body)
    return web.Response(status=200)


async def get_annots_by_refrerence_using_get(request: web.Request, ref_rgd_id) -> web.Response:
    """Returns a list of annotations for a reference

    

    :param ref_rgd_id: Reference RGD ID
    :type ref_rgd_id: int

    """
    return web.Response(status=200)


async def get_term_acc_ids_using_get(request: web.Request, rgd_id) -> web.Response:
    """Returns a list ontology term accession IDs annotated to an rgd object

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)
