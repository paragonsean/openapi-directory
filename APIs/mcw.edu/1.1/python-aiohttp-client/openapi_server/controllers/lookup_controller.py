from typing import List, Dict
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.rgdid_list_request import RGDIDListRequest
from openapi_server import util


async def get_ensembl_gene_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an Ensembl Gene  ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_ensembl_gene_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to Ensembl Gene IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_ensembl_protein_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an Ensembl Protein ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_ensembl_protein_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to Ensembl Protein IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_ensembl_transcript_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an Ensembl Transcript ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_ensembl_transcript_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to Ensembl Transcript IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_gen_bank_nucleotide_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to a GenBank Nucleotide ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_gen_bank_nucleotide_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to GenBank Nucleotide IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_gen_bank_protein_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to a GenBank Protein ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_gen_bank_protein_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to GenBank Protein IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_gene_types_using_get(request: web.Request, ) -> web.Response:
    """Returns a list of gene types avialable in RGD

    


    """
    return web.Response(status=200)


async def get_gtex_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an GTEx ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_gtex_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to GTEx IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_hgnc_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an HGNC ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_hgnc_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to HGNC IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_maps_using_get(request: web.Request, species_type_key) -> web.Response:
    """Return a list assembly maps for a species

    

    :param species_type_key: RGD species type key. A full list of keys is available throught the lookup service.  1&#x3D;human, 2&#x3D;mouse, 3&#x3D;rat,ect
    :type species_type_key: int

    """
    return web.Response(status=200)


async def get_maps_using_get1(request: web.Request, acc_id) -> web.Response:
    """Return a standardUnit for an ontology if it exists

    

    :param acc_id: RGD term acc
    :type acc_id: str

    """
    return web.Response(status=200)


async def get_mgi_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an MGI ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_mgi_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to MGI IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_ncbi_gene_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to an NCBI Gene ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_ncbi_gene_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to NCBI Gene IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)


async def get_species_types_using_get(request: web.Request, ) -> web.Response:
    """Return a Map of species type keys available in RGD

    


    """
    return web.Response(status=200)


async def get_uni_prot_mapping_using_get(request: web.Request, rgd_id) -> web.Response:
    """Translate an RGD ID to a UniProt ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_uni_prot_mapping_using_post(request: web.Request, body=None) -> web.Response:
    """Translate RGD IDs to UniProt IDs

    

    :param body: data
    :type body: dict | bytes

    """
    body = RGDIDListRequest.from_dict(body)
    return web.Response(status=200)
