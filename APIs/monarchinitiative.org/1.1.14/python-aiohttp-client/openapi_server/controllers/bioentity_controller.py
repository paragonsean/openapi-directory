from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.association_results import AssociationResults
from openapi_server.models.bio_object import BioObject
from openapi_server.models.d2_p_association_results import D2PAssociationResults
from openapi_server.models.named_object import NamedObject
from openapi_server import util


async def get_anatomy_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a given anatomy

    

    :param id: CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_anatomy_gene_by_taxon_associations(request: web.Request, taxid, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns gene IDs for all genes associated with a given anatomy, filtered by taxon

    For example, + NCBITaxon:10090 (mouse)

    :param taxid: Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
    :type taxid: str
    :param id: CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_case_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns diseases associated with a case

    

    :param id: CURIE identifier for a case
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_case_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns genotypes associated with a case

    

    :param id: CURIE identifier for a case
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_case_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns models associated with a case

    

    :param id: CURIE identifier for a case
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_case_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns phenotypes associated with a case

    

    :param id: CURIE identifier for a case
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_case_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns variants associated with a case

    

    :param id: CURIE identifier for a case
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_disease_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a disease

    

    :param id: CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_disease_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None, association_type=None) -> web.Response:
    """Returns genes associated with a disease

    

    :param id: CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str
    :param association_type: Additional filters: causal, non_causal, both
    :type association_type: str

    """
    return web.Response(status=200)


async def get_disease_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a disease

    

    :param id: CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_disease_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns associations to models of the disease

    In the association object returned, the subject will be the disease, and the object will be the model. The model may be a gene or genetic element.  If the query disease is a general class, the association subject may be to a specific disease.  In some cases the association will be *direct*, for example if a paper asserts a genotype is a model of a disease.  In other cases, the association will be *indirect*, for example, chaining over orthology. In these cases the chain will be reflected in the *evidence graph*  * TODO: provide hook into owlsim for dynamic computation of models by similarity

    :param id: CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_disease_model_taxon_associations(request: web.Request, taxon, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns associations to models of the disease constrained by taxon

    See /disease/&lt;id&gt;/models route for full details

    :param taxon: CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used
    :type taxon: str
    :param id: CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_disease_pathway_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns pathways associated with a disease

    

    :param id: CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_disease_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with disease

    

    :param id: CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_disease_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a disease

    

    :param id: CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_disease_substance_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns substances associated with a disease

    e.g. drugs or small molecules used to treat

    :param id: CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_disease_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns variants associated with a disease

    

    :param id: CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_function_associations(request: web.Request, id, start=None, rows=None, evidence=None) -> web.Response:
    """Returns annotations associated to a function term

    

    :param id: CURIE identifier of a function term (e.g. GO:0044598)
    :type id: str
    :param start: beginning row
    :type start: int
    :param rows: number of rows
    :type rows: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: List[str]

    """
    return web.Response(status=200)


async def get_function_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None, relationship_type=None) -> web.Response:
    """Returns genes associated to a GO term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0044598
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str
    :param relationship_type: relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;)
    :type relationship_type: str

    """
    return web.Response(status=200)


async def get_function_publication_associations(request: web.Request, id, start=None, rows=None, evidence=None) -> web.Response:
    """Returns publications associated to a GO term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0044598
    :type id: str
    :param start: beginning row
    :type start: int
    :param rows: number of rows
    :type rows: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: List[str]

    """
    return web.Response(status=200)


async def get_function_taxon_associations(request: web.Request, id, start=None, rows=None, evidence=None) -> web.Response:
    """Returns taxons associated to a GO term

    

    :param id: CURIE identifier of a GO term, e.g. GO:0044598
    :type id: str
    :param start: beginning row
    :type start: int
    :param rows: number of rows
    :type rows: int
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: List[str]

    """
    return web.Response(status=200)


async def get_gene_anatomy_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns anatomical entities associated with a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:13434
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a gene

    

    :param id: CURIE identifier of gene, e.g. HGNC:613, HGNC:11025
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_gene_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None, association_type=None) -> web.Response:
    """Returns diseases associated with gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str
    :param association_type: Additional filters: causal, non_causal, both
    :type association_type: str

    """
    return web.Response(status=200)


async def get_gene_expression_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns expression events for a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_function_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns function associations for a gene

    IMPLEMENTATION DETAILS ----------------------  Note: currently this is implemented as a query to the GO/AmiGO solr instance. This directly supports IDs such as:   - ZFIN e.g. ZFIN:ZDB-GENE-050417-357  Note that the AmiGO GOlr natively stores MGI annotations to MGI:MGI:nn. However, the standard for biolink is MGI:nnnn, so you should use this (will be transparently mapped to legacy ID)  Additionally, for some species such as Human, GO has the annotation attached to the UniProt ID. Again, this should be transparently handled; e.g. you can use NCBIGene:6469, and this will be mapped behind the scenes for querying.

    :param id: id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_gene_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a gene

    

    :param id: CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_homolog_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, homology_type=None, direct_taxon=None) -> web.Response:
    """Returns homologs for a gene

    

    :param id: id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default)
    :type taxon: List[str]
    :param homology_type: P (paralog), O (Ortholog) or LDO (least-diverged ortholog)
    :type homology_type: str
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool

    """
    return web.Response(status=200)


async def get_gene_interactions(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns interactions for a gene

    

    :param id: id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns models associated with a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:17988
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_ortholog_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Return diseases associated with orthologs of a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_ortholog_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Return phenotypes associated with orthologs for a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_pathway_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns pathways associated with gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a gene

    

    :param id: CURIE identifier of gene, e.g. NCBIGene:4750
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_gene_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns variants associated with a gene

    

    :param id: CURIE identifier of gene, e.g. HGNC:10896
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_generic_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns associations for an entity regardless of the type

    

    :param id: 
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_generic_object(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns basic info on object of any type

    

    :param id: id, e.g. NCBIGene:84570
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_generic_object_by_type(request: web.Request, type, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, get_association_counts=None, distinct_counts=None) -> web.Response:
    """Return basic info on an object for a given type

    

    :param type: bioentity type
    :type type: str
    :param id: id, e.g. NCBIGene:84570
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param get_association_counts: Get association counts
    :type get_association_counts: bool
    :param distinct_counts: Get distinct counts for associations (to be used in conjunction with &#39;get_association_counts&#39; parameter)
    :type distinct_counts: bool

    """
    return web.Response(status=200)


async def get_genotype_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_genotype_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes-genotype associations

    Genotypes may be related to one another according to the GENO model

    :param id: CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns models associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a genotype

    

    :param id: CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_genotype_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes-variant associations

    

    :param id: CURIE identifier of genotype, e.g. MONARCH:FBgeno422705
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_goterm_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, relationship_type=None) -> web.Response:
    """Returns associations to GO terms for a gene

    

    :param id: CURIE identifier of a GO term, e.g. GO:0044598
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param relationship_type: relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;)
    :type relationship_type: str

    """
    return web.Response(status=200)


async def get_model_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a model

    

    :param id: CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_model_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a model

    

    :param id: CURIE identifier for a model, e.g. MGI:5573196
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_model_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a model

    

    :param id: CURIE identifier for a model, e.g. MMRRC:042787
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_model_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a model

    

    :param id: CURIE identifier for a model, e.g. Coriell:NA16660
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_model_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with a model

    

    :param id: id
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_model_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a model

    

    :param id: CURIE identifier for a model, e.g. MGI:5644542
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_model_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns variants associated with a model

    

    :param id: CURIE identifier for a model, e.g. MMRRC:042787
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_pathway_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a pathway

    

    :param id: CURIE any pathway element. E.g. REACT:R-HSA-5387390
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_pathway_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a pathway

    

    :param id: CURIE any pathway element. E.g. REACT:R-HSA-5387390
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_pathway_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with a pathway

    

    :param id: CURIE any pathway element. E.g. REACT:R-HSA-5387390
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_anatomy_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns anatomical entities associated with a phenotype

    Example IDs:   * MP:0008521 abnormal Bowman membrane

    :param id: CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_phenotype_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_phenotype_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a phenotype

    

    :param id: CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level), 
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_gene_by_taxon_associations(request: web.Request, taxid, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns gene IDs for all genes associated with a given phenotype, filtered by taxon

    For example, MP:0001569 + NCBITaxon:10090 (mouse)

    :param taxid: Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
    :type taxid: str
    :param id: Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_phenotype_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_pathway_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns pathways associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_phenotype_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns variants associated with a phenotype

    

    :param id: Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns models associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_publication_variant_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns variants associated with a publication

    

    :param id: CURIE identifier for a publication, e.g. PMID:11751940
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_substance_participant_in_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns associations between an activity and process and the specified substance

    Examples relationships:   * substance is a metabolite of a process  * substance is synthesized by a process  * substance is modified by an activity  * substance elicits a response program/pathway  * substance is transported by activity or pathway  For example, CHEBI:40036 (amitrole)

    :param id: CURIE identifier of substance, e.g. CHEBI:40036
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_substance_role_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns associations between given drug and roles

    Roles may be human-oriented (e.g. pesticide) or molecular (e.g. enzyme inhibitor)

    :param id: CURIE identifier of substance, e.g. CHEBI:40036
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_substance_treats_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns substances associated with a disease

    e.g. drugs or small molecules used to treat

    :param id: CURIE identifier of substance, e.g. CHEBI:40036
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_variant_case_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns cases associated with a variant

    

    :param id: CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_variant_disease_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns diseases associated with a variant

    

    :param id: CURIE identifier of variant, e.g. ClinVarVariant:14925
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_variant_gene_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genes associated with a variant

    

    :param id: CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_variant_genotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns genotypes associated with a variant

    

    :param id: CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_variant_model_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None) -> web.Response:
    """Returns models associated with a variant

    

    :param id: CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool

    """
    return web.Response(status=200)


async def get_variant_phenotype_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns phenotypes associated with a variant

    

    :param id: CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)


async def get_variant_publication_associations(request: web.Request, id, rows=None, start=None, facet=None, facet_fields=None, unselect_evidence=None, exclude_automatic_assertions=None, fetch_objects=None, use_compact_associations=None, slim=None, evidence=None, direct=None, taxon=None, direct_taxon=None, relation=None, sort=None, q=None) -> web.Response:
    """Returns publications associated with a variant

    

    :param id: CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    :type id: str
    :param rows: number of rows
    :type rows: int
    :param start: beginning row
    :type start: int
    :param facet: Enable faceting
    :type facet: bool
    :param facet_fields: Fields to facet on
    :type facet_fields: List[str]
    :param unselect_evidence: If true, excludes evidence objects in response
    :type unselect_evidence: bool
    :param exclude_automatic_assertions: If true, excludes associations that involve IEAs (ECO:0000501)
    :type exclude_automatic_assertions: bool
    :param fetch_objects: If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    :type fetch_objects: bool
    :param use_compact_associations: If true, returns results in compact associations format
    :type use_compact_associations: bool
    :param slim: Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    :type slim: List[str]
    :param evidence: Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    :type evidence: str
    :param direct: Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False
    :type direct: bool
    :param taxon: One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    :type taxon: List[str]
    :param direct_taxon: Set true to exclude inferred taxa
    :type direct_taxon: bool
    :param relation: A relation CURIE to filter associations
    :type relation: str
    :param sort: Sorting responses &lt;field&gt; &lt;desc,asc&gt;
    :type sort: str
    :param q: Query string to filter documents
    :type q: str

    """
    return web.Response(status=200)
