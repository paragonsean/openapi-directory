from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server import util


async def get_association_by_subject_and_assoc_type(request: web.Request, association_type, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None, subject=None, object=None) -> web.Response:
    """Returns list of matching associations of a given type

    

    :param association_type: Association type, eg gene_phenotype
    :type association_type: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param subject: Subject CURIE
    :type subject: str
    :param object: Object CURIE
    :type object: str

    """
    return web.Response(status=200)


async def get_association_by_subject_and_object_category_search(request: web.Request, object_category, subject_category, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None, subject=None, object=None, subject_taxon=None, object_taxon=None, relation=None) -> web.Response:
    """Returns list of matching associations between a given subject and object category

    

    :param object_category: Category of entity at link Object (target), e.g. gene, disease, phenotype
    :type object_category: str
    :param subject_category: Category of entity at link Subject (source), e.g. gene, disease, phenotype
    :type subject_category: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param subject: Subject CURIE
    :type subject: str
    :param object: Object CURIE
    :type object: str
    :param subject_taxon: Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
    :type subject_taxon: str
    :param object_taxon: Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    :type object_taxon: str
    :param relation: Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    :type relation: str

    """
    return web.Response(status=200)


async def get_association_by_subject_category_search(request: web.Request, subject_category, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None, subject_taxon=None, object_taxon=None, relation=None) -> web.Response:
    """Returns list of matching associations for a given subject category

    

    :param subject_category: Category of entity at link Subject (source), e.g. gene, disease, phenotype
    :type subject_category: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param subject_taxon: Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
    :type subject_taxon: str
    :param object_taxon: Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    :type object_taxon: str
    :param relation: Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    :type relation: str

    """
    return web.Response(status=200)


async def get_association_object(request: web.Request, id) -> web.Response:
    """Returns the association with a given identifier

    An association connects, at a minimum, two things, designated subject and object, via some relationship. Associations also include evidence, provenance etc.

    :param id: identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4
    :type id: str

    """
    return web.Response(status=200)


async def get_associations_between(request: web.Request, object, subject, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None) -> web.Response:
    """Returns associations connecting two entities

    Given two entities (e.g. a particular gene and a particular disease), if these two entities are connected (directly or indirectly), then return the association objects describing the connection.

    :param object: Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene
    :type object: str
    :param subject: Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default)
    :type subject: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool

    """
    return web.Response(status=200)


async def get_associations_from(request: web.Request, subject, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None, object_taxon=None, relation=None) -> web.Response:
    """Returns list of matching associations starting from a given subject (source)

    

    :param subject: Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default)
    :type subject: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param object_taxon: Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    :type object_taxon: str
    :param relation: Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    :type relation: str

    """
    return web.Response(status=200)


async def get_associations_to(request: web.Request, object, rows=None, start=None, evidence=None, unselect_evidence=None, exclude_automatic_assertions=None, use_compact_associations=None) -> web.Response:
    """Returns list of matching associations pointing to a given object (target)

    

    :param object: Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene
    :type object: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool

    """
    return web.Response(status=200)
