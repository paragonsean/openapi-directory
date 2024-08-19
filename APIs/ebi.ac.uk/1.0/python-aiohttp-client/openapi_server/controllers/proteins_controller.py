from typing import List, Dict
from aiohttp import web

from openapi_server.models.proteins import Proteins
from openapi_server import util


async def get_proteins_using_get(request: web.Request, accession=None, ec=None, full_name=None, gene=None, go=None, interpro=None, limit=None, omim=None, orphanet=None, page=None, pfam=None, reactome=None, tax_id=None) -> web.Response:
    """Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) &amp; SARS2(2697049)

    

    :param accession: accession
    :type accession: List[str]
    :param ec: ec
    :type ec: List[str]
    :param full_name: fullName
    :type full_name: List[str]
    :param gene: gene
    :type gene: List[str]
    :param go: go
    :type go: List[str]
    :param interpro: interpro
    :type interpro: List[str]
    :param limit: limit
    :type limit: int
    :param omim: omim
    :type omim: List[str]
    :param orphanet: orphanet
    :type orphanet: List[str]
    :param page: page
    :type page: int
    :param pfam: pfam
    :type pfam: List[str]
    :param reactome: reactome
    :type reactome: List[str]
    :param tax_id: taxId
    :type tax_id: List[int]

    """
    return web.Response(status=200)
