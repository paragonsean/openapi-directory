from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_database_straindata_get(request: web.Request, database, continent=None, offset=None, sample_accession=None, latitude=None, collection_month=None, strain_name=None, lab_contact=None, sortorder=None, n50=None, limit=None, serotype=None, region=None, country=None, collection_date=None, custom_fields=None, only_fields=None, source_niche=None, collection_year=None, secondary_sample_accession=None, source_details=None, substrains=None, version=None, source_type=None, orderby=None, my_strains=None, collection_time=None, county=None, uberstrain=None, top_species=None, comment=None, longitude=None, reldate=None, barcode=None, postcode=None, email=None, assembly_status=None, city=None) -> web.Response:
    """api_v20_database_straindata_get

    Strain data

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
    :param strain_name: 
    :type strain_name: str
    :param lab_contact: 
    :type lab_contact: str
    :param sortorder: Order of search results: asc or desc
    :type sortorder: str
    :param n50: 
    :type n50: int
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
    :param custom_fields: 
    :type custom_fields: str
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
    :param orderby: Field to order by. Default: strain barcode
    :type orderby: str
    :param my_strains: 
    :type my_strains: bool
    :param collection_time: 
    :type collection_time: str
    :param county: 
    :type county: str
    :param uberstrain: 
    :type uberstrain: str
    :param top_species: 
    :type top_species: str
    :param comment: 
    :type comment: str
    :param longitude: 
    :type longitude: float
    :param reldate: 
    :type reldate: int
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS
    :type barcode: List[str]
    :param postcode: 
    :type postcode: str
    :param email: 
    :type email: str
    :param assembly_status: 
    :type assembly_status: str
    :param city: 
    :type city: str

    """
    return web.Response(status=200)
