from typing import List, Dict
from aiohttp import web

from openapi_server.models.drugs import Drugs
from openapi_server import util


async def get_drugs_using_get(request: web.Request, accession=None, chembl_id=None, identifier=None, limit=None, name=None, page=None, pubchem_cid=None) -> web.Response:
    """drugs collected from Drugbank

    

    :param accession: accession
    :type accession: List[str]
    :param chembl_id: chemblId
    :type chembl_id: List[str]
    :param identifier: identifier
    :type identifier: List[str]
    :param limit: limit
    :type limit: int
    :param name: name
    :type name: List[str]
    :param page: page
    :type page: int
    :param pubchem_cid: pubchemCid
    :type pubchem_cid: List[str]

    """
    return web.Response(status=200)
