from typing import List, Dict
from aiohttp import web

from openapi_server.models.molecules import Molecules
from openapi_server import util


async def get_molecules_using_get(request: web.Request, canonical_smiles=None, inchi_key=None, limit=None, molecule_chembl_id=None, page=None) -> web.Response:
    """Get ChEMBL molecules

    

    :param canonical_smiles: canonicalSmiles
    :type canonical_smiles: List[str]
    :param inchi_key: inchiKey
    :type inchi_key: List[str]
    :param limit: limit
    :type limit: int
    :param molecule_chembl_id: moleculeChemblId
    :type molecule_chembl_id: List[str]
    :param page: page
    :type page: int

    """
    return web.Response(status=200)
