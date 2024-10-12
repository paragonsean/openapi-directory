from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_chart_info_using_get(request: web.Request, species_type_key, ref_rgd_id, term_string) -> web.Response:
    """Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla).  Reference RGD ID for a study works like a filter.

    

    :param species_type_key: Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla 
    :type species_type_key: int
    :param ref_rgd_id: Reference RGD ID for a study
    :type ref_rgd_id: int
    :param term_string: List of term accession IDs
    :type term_string: str

    """
    return web.Response(status=200)


async def get_chart_info_using_get1(request: web.Request, species_type_key, term_string) -> web.Response:
    """Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla)

    

    :param species_type_key: Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla 
    :type species_type_key: int
    :param term_string: List of term accession IDs
    :type term_string: str

    """
    return web.Response(status=200)
