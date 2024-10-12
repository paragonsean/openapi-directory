from typing import List, Dict
from aiohttp import web

from openapi_server.models.bioassays import Bioassays
from openapi_server import util


async def get_bioassays_using_get(request: web.Request, accession=None, assay_pubchem_id=None, limit=None, ncbi_protein_id=None, page=None) -> web.Response:
    """Get pubchem bioassays

    

    :param accession: accession
    :type accession: List[str]
    :param assay_pubchem_id: assayPubchemId
    :type assay_pubchem_id: List[str]
    :param limit: limit
    :type limit: int
    :param ncbi_protein_id: ncbiProteinId
    :type ncbi_protein_id: List[str]
    :param page: page
    :type page: int

    """
    return web.Response(status=200)
