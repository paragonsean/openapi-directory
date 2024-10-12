from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server import util


async def get_relation_usage_between_resource(request: web.Request, subject_category, object_category, subject_taxon=None, evidence=None) -> web.Response:
    """All relations used plus count of associations

    

    :param subject_category: 
    :type subject_category: str
    :param object_category: 
    :type object_category: str
    :param subject_taxon: SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    :type subject_taxon: str
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    :type evidence: str

    """
    return web.Response(status=200)


async def get_relation_usage_pivot_label_resource(request: web.Request, subject_taxon=None, evidence=None) -> web.Response:
    """Relation usage count for all subj x obj category combinations, showing label

    

    :param subject_taxon: SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    :type subject_taxon: str
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    :type evidence: str

    """
    return web.Response(status=200)


async def get_relation_usage_pivot_resource(request: web.Request, subject_taxon=None, evidence=None) -> web.Response:
    """Relation usage count for all subj x obj category combinations

    

    :param subject_taxon: SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    :type subject_taxon: str
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    :type evidence: str

    """
    return web.Response(status=200)


async def get_relation_usage_resource(request: web.Request, subject_taxon=None, evidence=None) -> web.Response:
    """All relations used plus count of associations

    

    :param subject_taxon: SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    :type subject_taxon: str
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    :type evidence: str

    """
    return web.Response(status=200)
