from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v20_database_strains_barcode_get_request import ApiV20DatabaseStrainsBarcodeGetRequest
from openapi_server import util


async def api_v20_database_strains_barcode_get(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_strains_barcode_get

    Strain metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseStrainsBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_strains_barcode_post(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_strains_barcode_post

    Strain metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseStrainsBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_strains_barcode_put(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_strains_barcode_put

    Strain metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseStrainsBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_strains_get(request: web.Request, database, continent=None, offset=None, sample_accession=None, latitude=None, collection_month=None, antigenic_formulas=None, strain_name=None, lab_contact=None, sortorder=None, limit=None, serotype=None, region=None, country=None, collection_date=None, return_all=None, only_fields=None, source_niche=None, collection_year=None, secondary_sample_accession=None, source_details=None, substrains=None, version=None, source_type=None, orderby=None, my_strains=None, collection_time=None, county=None, uberstrain=None, comment=None, longitude=None, reldate=None, assembly_barcode=None, barcode=None, postcode=None, city=None) -> web.Response:
    """api_v20_database_strains_get

    Strain metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param continent: 
    :type continent: str
    :param offset: Cursor position in results
    :type offset: int
    :param sample_accession: 
    :type sample_accession: str
    :param latitude: 
    :type latitude: float
    :param collection_month: 
    :type collection_month: int
    :param antigenic_formulas: 
    :type antigenic_formulas: str
    :param strain_name: 
    :type strain_name: str
    :param lab_contact: 
    :type lab_contact: str
    :param sortorder: Order of search results: asc or desc
    :type sortorder: str
    :param limit: Number of results per page
    :type limit: int
    :param serotype: 
    :type serotype: str
    :param region: 
    :type region: str
    :param country: 
    :type country: str
    :param collection_date: 
    :type collection_date: int
    :param return_all: 
    :type return_all: bool
    :param only_fields: 
    :type only_fields: List[str]
    :param source_niche: 
    :type source_niche: str
    :param collection_year: 
    :type collection_year: int
    :param secondary_sample_accession: 
    :type secondary_sample_accession: str
    :param source_details: 
    :type source_details: str
    :param substrains: 
    :type substrains: bool
    :param version: 
    :type version: int
    :param source_type: 
    :type source_type: str
    :param orderby: Field to order by. Default: barcode
    :type orderby: str
    :param my_strains: 
    :type my_strains: bool
    :param collection_time: 
    :type collection_time: str
    :param county: 
    :type county: str
    :param uberstrain: 
    :type uberstrain: str
    :param comment: 
    :type comment: str
    :param longitude: 
    :type longitude: float
    :param reldate: 
    :type reldate: int
    :param assembly_barcode: 
    :type assembly_barcode: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: List[str]
    :param postcode: 
    :type postcode: str
    :param city: 
    :type city: str

    """
    return web.Response(status=200)
