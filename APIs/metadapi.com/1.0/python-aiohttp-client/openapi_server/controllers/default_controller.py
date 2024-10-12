from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.get_distance200_response import GetDistance200Response
from openapi_server.models.get_msagroups200_response import GetMsagroups200Response
from openapi_server.models.get_msagroups_msacode200_response import GetMsagroupsMsacode200Response
from openapi_server.models.get_radius200_response import GetRadius200Response
from openapi_server.models.get_radius400_response import GetRadius400Response
from openapi_server.models.get_radius401_response import GetRadius401Response
from openapi_server.models.get_zipc_v1401_response import GetZipcV1401Response
from openapi_server.models.get_zipcode200_response import GetZipcode200Response
from openapi_server.models.get_zipcode401_response import GetZipcode401Response
from openapi_server.models.get_zipcode403_response import GetZipcode403Response
from openapi_server.models.zip_code_response import ZipCodeResponse
from openapi_server import util


async def get_distance(request: web.Request, zip_code1, zip_code2) -> web.Response:
    """Distance Between 2 Zip Codes

    Gets the distance (in miles and kilometers) between 2 zip codes passed as parameters. There are 2 mandatory query parameters (zipCode1 and zipCode2). 

    :param zip_code1: Zip Code 1
    :type zip_code1: str
    :param zip_code2: Zip Code 2
    :type zip_code2: str

    """
    return web.Response(status=200)


async def get_msagroups(request: web.Request, limit, offset, state_code=None) -> web.Response:
    """List All MSA Groups

    This end point lists all the Metropolitan and Micropolitan Statistical Areas in the United States with the corresponding states and counties that make up the group. 

    :param limit: Number of records to return in each page. Max value: 50.
    :type limit: int
    :param offset: Offset is the position in the dataset to start retrieval of records.
    :type offset: int
    :param state_code: Parameter for state code.
    :type state_code: str

    """
    return web.Response(status=200)


async def get_msagroups_msacode(request: web.Request, msa_code) -> web.Response:
    """Metro/Micro Statistical Area Details

    Gets the details of a single Metropolitan Statistical Area code passed as a path parameter.

    :param msa_code: 5 digit MSA (Metropolitan Statistical Area) code.
    :type msa_code: str

    """
    return web.Response(status=200)


async def get_radius(request: web.Request, zip_code, radius, uom) -> web.Response:
    """Zip Code Radius

    Endpoint that returns the zip codes that fall within the specified radius of another zip code. The returned zip codes are sorted by distance.

    :param zip_code: 5 Digit US Zip Code
    :type zip_code: str
    :param radius: Radius distance.  Max 322 km or 200 mi
    :type radius: int
    :param uom: Unit of Measure
    :type uom: str

    """
    return web.Response(status=200)


async def get_zipc_v1(request: web.Request, ) -> web.Response:
    """Validate License Key

    Endpoint used to validate license key only. Returns 204 on Success


    """
    return web.Response(status=200)


async def get_zipcode(request: web.Request, zipcode) -> web.Response:
    """Zip Code Details

    Gets the details of a single Zip code. 

    :param zipcode: 5 Digit US Zip Code
    :type zipcode: str

    """
    return web.Response(status=200)


async def get_zipcodes(request: web.Request, offset=None, limit=None, zipcode=None, usps_main_city_key=None, zip_classification_code=None, usps_facility_code=None, usps_delivery_code=None, usps_carrier_route_sort_code=None, unique_zip_name_ind=None, usps_finance_number=None, state_code=None, state_fips_code=None, county_fips_code=None, division_code=None, region_code=None, msa_code=None) -> web.Response:
    """List all Zip Codes

    Returns a list of zip codes. Results are always paginated. Visit the [Zip Code Data API](https://www.metadapi.com/API-Products/API-Product-Details/zip-code-api) product page for information on how to get an API key.

    :param offset: Offset is the position in the dataset to start retrieval of records.
    :type offset: 
    :param limit: Number of records to return in each page.
    :type limit: 
    :param zipcode: 5 Digit Zip Code query parameter. Can have multiple values (separated by comma).
    :type zipcode: str
    :param usps_main_city_key: Parameter for USPS City / Town key identifier for the main city of the zip code.
    :type usps_main_city_key: str
    :param zip_classification_code: Parameter for zipClassificationCode
    :type zip_classification_code: str
    :param usps_facility_code: Parameter for facility code.
    :type usps_facility_code: str
    :param usps_delivery_code: Parameter for delivery code.
    :type usps_delivery_code: str
    :param usps_carrier_route_sort_code: Parameter for carrier route sort code.
    :type usps_carrier_route_sort_code: str
    :param unique_zip_name_ind: Parameter for unique zip name indicator.
    :type unique_zip_name_ind: bool
    :param usps_finance_number: Parameter for finance number.
    :type usps_finance_number: str
    :param state_code: Parameter for state code.
    :type state_code: str
    :param state_fips_code: Parameter for State FIPS code.
    :type state_fips_code: str
    :param county_fips_code: Parameter for county FIPS code.
    :type county_fips_code: str
    :param division_code: Parameter for division code. 
    :type division_code: str
    :param region_code: Parameter for region code. 
    :type region_code: str
    :param msa_code: Parameter for msaCode.
    :type msa_code: str

    """
    return web.Response(status=200)
