from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_property_sales(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_property_sales_property_address=None, search_db_property_sales_city=None, search_db_property_sales_zipcode=None, search_db_property_sales_sale_price=None, search_db_property_sales_sale_date=None, search_db_property_sales_seller=None, search_db_property_sales_buyer=None, search_db_property_sales_type=None, search_db_property_sales_building_description=None, search_db_property_sales_building_design=None, search_db_property_sales_subdivision=None, search_db_property_sales_location=None) -> web.Response:
    """Search API for &#39;Property Sales&#39; entry type

    API to search for entries of type Property Sales

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_property_sales_property_address: Property Address
    :type search_db_property_sales_property_address: str
    :param search_db_property_sales_city: City
    :type search_db_property_sales_city: str
    :param search_db_property_sales_zipcode: Zip Code
    :type search_db_property_sales_zipcode: str
    :param search_db_property_sales_sale_price: Sale Price
    :type search_db_property_sales_sale_price: float
    :param search_db_property_sales_sale_date: Sale Date
    :type search_db_property_sales_sale_date: str
    :param search_db_property_sales_seller: Seller
    :type search_db_property_sales_seller: str
    :param search_db_property_sales_buyer: Buyer
    :type search_db_property_sales_buyer: str
    :param search_db_property_sales_type: Property Type
    :type search_db_property_sales_type: str
    :param search_db_property_sales_building_description: Building Description
    :type search_db_property_sales_building_description: str
    :param search_db_property_sales_building_design: Building Design
    :type search_db_property_sales_building_design: str
    :param search_db_property_sales_subdivision: Subdivision
    :type search_db_property_sales_subdivision: str
    :param search_db_property_sales_location: Location
    :type search_db_property_sales_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
