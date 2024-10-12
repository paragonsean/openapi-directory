from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_results import AutocompleteResults
from openapi_server.models.lay_results import LayResults
from openapi_server.models.search_result import SearchResult
from openapi_server import util


async def get_autocomplete(request: web.Request, term, fq=None, category=None, prefix=None, include_eqs=None, boost_fx=None, boost_q=None, taxon=None, rows=None, start=None, highlight_class=None, min_match=None, exclude_groups=None, minimal_tokenizer=None) -> web.Response:
    """Returns list of matching concepts or entities using lexical search

    

    :param term: 
    :type term: str
    :param fq: fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
    :type fq: List[str]
    :param category: e.g. gene, disease
    :type category: List[str]
    :param prefix: ontology prefix: HP, -MONDO
    :type prefix: List[str]
    :param include_eqs: Include equivalent ids in prefix filter
    :type include_eqs: bool
    :param boost_fx: boost function e.g. pow(edges,0.334)
    :type boost_fx: List[str]
    :param boost_q: boost query e.g. category:genotype^-10
    :type boost_q: List[str]
    :param taxon: taxon filter, eg NCBITaxon:9606, includes inferred taxa
    :type taxon: List[str]
    :param rows: number of rows
    :type rows: int
    :param start: row number to start from
    :type start: str
    :param highlight_class: highlight class
    :type highlight_class: str
    :param min_match: minimum should match parameter, see solr docs for details
    :type min_match: str
    :param exclude_groups: Exclude grouping classes (classes with subclasses)
    :type exclude_groups: bool
    :param minimal_tokenizer: set to true to use the minimal tokenizer, good for variants and genotypes
    :type minimal_tokenizer: bool

    """
    return web.Response(status=200)


async def get_search_entities(request: web.Request, term, fq=None, category=None, prefix=None, include_eqs=None, boost_fx=None, boost_q=None, taxon=None, rows=None, start=None, highlight_class=None, min_match=None, exclude_groups=None, minimal_tokenizer=None) -> web.Response:
    """Returns list of matching concepts or entities using lexical search

    

    :param term: search string, e.g. shh, parkinson, femur
    :type term: str
    :param fq: fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
    :type fq: List[str]
    :param category: e.g. gene, disease
    :type category: List[str]
    :param prefix: ontology prefix: HP, -MONDO
    :type prefix: List[str]
    :param include_eqs: Include equivalent ids in prefix filter
    :type include_eqs: bool
    :param boost_fx: boost function e.g. pow(edges,0.334)
    :type boost_fx: List[str]
    :param boost_q: boost query e.g. category:genotype^-10
    :type boost_q: List[str]
    :param taxon: taxon filter, eg NCBITaxon:9606, includes inferred taxa
    :type taxon: List[str]
    :param rows: number of rows
    :type rows: int
    :param start: row number to start from
    :type start: str
    :param highlight_class: highlight class
    :type highlight_class: str
    :param min_match: minimum should match parameter, see solr docs for details
    :type min_match: str
    :param exclude_groups: Exclude grouping classes (classes with subclasses)
    :type exclude_groups: bool
    :param minimal_tokenizer: set to true to use the minimal tokenizer, good for variants and genotypes
    :type minimal_tokenizer: bool

    """
    return web.Response(status=200)


async def get_search_hpo_entities(request: web.Request, term, rows=None, start=None, phenotype_group=None, phenotype_group_label=None, anatomical_system=None, anatomical_system_label=None, highlight_class=None) -> web.Response:
    """Returns list of matching concepts or entities using lexical search

    

    :param term: search string, e.g. muscle atrophy, frequent infections
    :type term: str
    :param rows: number of rows
    :type rows: int
    :param start: row number to start from
    :type start: str
    :param phenotype_group: phenotype group id
    :type phenotype_group: str
    :param phenotype_group_label: phenotype group label
    :type phenotype_group_label: str
    :param anatomical_system: anatomical system id
    :type anatomical_system: str
    :param anatomical_system_label: anatomical system label
    :type anatomical_system_label: str
    :param highlight_class: highlight class
    :type highlight_class: str

    """
    return web.Response(status=200)
