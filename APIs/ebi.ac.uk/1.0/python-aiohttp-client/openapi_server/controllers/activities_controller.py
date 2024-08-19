from typing import List, Dict
from aiohttp import web

from openapi_server.models.activities import Activities
from openapi_server import util


async def get_activities_using_get(request: web.Request, assay_chembl_id=None, limit=None, molecule_chembl_id=None, page=None, pchembl_value=None, target_chembl_id=None) -> web.Response:
    """Get ChEMBL activities

    

    :param assay_chembl_id: assayChemblId
    :type assay_chembl_id: List[str]
    :param limit: limit
    :type limit: int
    :param molecule_chembl_id: moleculeChemblId
    :type molecule_chembl_id: List[str]
    :param page: page
    :type page: int
    :param pchembl_value: pchemblValue
    :type pchembl_value: float
    :param target_chembl_id: targetChemblId
    :type target_chembl_id: List[str]

    """
    return web.Response(status=200)
