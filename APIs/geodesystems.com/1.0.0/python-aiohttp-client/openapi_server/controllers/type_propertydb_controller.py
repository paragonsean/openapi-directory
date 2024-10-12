from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_propertydb(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_propertydb_property_id=None, search_db_propertydb_owner=None, search_db_propertydb_address=None, search_db_propertydb_city=None, search_db_propertydb_state=None, search_db_propertydb_value=None, search_db_propertydb_building_type=None, search_db_propertydb_house_size=None, search_db_propertydb_lot_sqft=None, search_db_propertydb_lot_acres=None, search_db_propertydb_price_sqft=None, search_db_propertydb_location=None) -> web.Response:
    """Search API for &#39;Property Database&#39; entry type

    API to search for entries of type Property Database

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
    :param search_db_propertydb_property_id: Property ID
    :type search_db_propertydb_property_id: str
    :param search_db_propertydb_owner: Owner
    :type search_db_propertydb_owner: str
    :param search_db_propertydb_address: Address
    :type search_db_propertydb_address: str
    :param search_db_propertydb_city: City
    :type search_db_propertydb_city: str
    :param search_db_propertydb_state: State
    :type search_db_propertydb_state: str
    :param search_db_propertydb_value: Property Value
    :type search_db_propertydb_value: int
    :param search_db_propertydb_building_type: Building Type
    :type search_db_propertydb_building_type: str
    :param search_db_propertydb_house_size: Building Sq Ft
    :type search_db_propertydb_house_size: int
    :param search_db_propertydb_lot_sqft: Lot Size Sq Ft
    :type search_db_propertydb_lot_sqft: int
    :param search_db_propertydb_lot_acres: Lot Size Acres
    :type search_db_propertydb_lot_acres: float
    :param search_db_propertydb_price_sqft: $-sqft
    :type search_db_propertydb_price_sqft: float
    :param search_db_propertydb_location: Location
    :type search_db_propertydb_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
