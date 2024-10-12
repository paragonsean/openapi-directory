from typing import List, Dict
from aiohttp import web

from openapi_server.models.assays import Assays
from openapi_server import util


async def get_assays_using_get(request: web.Request, assay_chembl_id=None, assay_org=None, assay_type=None, limit=None, page=None, target_chembl_id=None) -> web.Response:
    """Get ChEMBL assays

    

    :param assay_chembl_id: assayChemblId
    :type assay_chembl_id: List[str]
    :param assay_org: assayOrg
    :type assay_org: List[str]
    :param assay_type: assayType
    :type assay_type: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int
    :param target_chembl_id: targetChemblId
    :type target_chembl_id: List[str]

    """
    return web.Response(status=200)
