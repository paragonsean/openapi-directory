from typing import List, Dict
from aiohttp import web

from openapi_server.models.pubchem_compounds import PubchemCompounds
from openapi_server import util


async def get_compounds_using_get(request: web.Request, canonical_smiles=None, cid=None, inchi_key=None, limit=None, page=None) -> web.Response:
    """Get pubchem compounds

    

    :param canonical_smiles: canonicalSmiles
    :type canonical_smiles: List[str]
    :param cid: cid
    :type cid: List[str]
    :param inchi_key: inchiKey
    :type inchi_key: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int

    """
    return web.Response(status=200)
