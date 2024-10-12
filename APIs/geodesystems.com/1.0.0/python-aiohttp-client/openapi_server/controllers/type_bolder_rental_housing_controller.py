from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_bolder_rental_housing(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_bolder_rental_housing_propaddr1=None, search_db_bolder_rental_housing_rentaltype=None, search_db_bolder_rental_housing_bldgtype=None, search_db_bolder_rental_housing_dwellunits=None, search_db_bolder_rental_housing_roomunits=None, search_db_bolder_rental_housing_neighbrhd=None, search_db_bolder_rental_housing_complexnm=None, search_db_bolder_rental_housing_name=None, search_db_bolder_rental_housing_persontype=None, search_db_bolder_rental_housing_company=None, search_db_bolder_rental_housing_engcompl=None, search_db_bolder_rental_housing_licenseexp=None, search_db_bolder_rental_housing_licensenum=None, search_db_bolder_rental_housing_ppl1_coname=None, search_db_bolder_rental_housing_person_1=None, search_db_bolder_rental_housing_ppl1_role=None, search_db_bolder_rental_housing_ppl2_coname=None, search_db_bolder_rental_housing_person_2=None, search_db_bolder_rental_housing_ppl2_role=None, search_db_bolder_rental_housing_location=None) -> web.Response:
    """Search API for &#39;Boulder Rental Housing&#39; entry type

    API to search for entries of type Boulder Rental Housing

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
    :param search_db_bolder_rental_housing_propaddr1: Property Address
    :type search_db_bolder_rental_housing_propaddr1: str
    :param search_db_bolder_rental_housing_rentaltype: Rental Type
    :type search_db_bolder_rental_housing_rentaltype: str
    :param search_db_bolder_rental_housing_bldgtype: Building Type
    :type search_db_bolder_rental_housing_bldgtype: str
    :param search_db_bolder_rental_housing_dwellunits: Dwelling Units
    :type search_db_bolder_rental_housing_dwellunits: int
    :param search_db_bolder_rental_housing_roomunits: Room Units
    :type search_db_bolder_rental_housing_roomunits: int
    :param search_db_bolder_rental_housing_neighbrhd: Neighborhood
    :type search_db_bolder_rental_housing_neighbrhd: str
    :param search_db_bolder_rental_housing_complexnm: Complex Name
    :type search_db_bolder_rental_housing_complexnm: str
    :param search_db_bolder_rental_housing_name: Name
    :type search_db_bolder_rental_housing_name: str
    :param search_db_bolder_rental_housing_persontype: Person Type
    :type search_db_bolder_rental_housing_persontype: str
    :param search_db_bolder_rental_housing_company: Company
    :type search_db_bolder_rental_housing_company: str
    :param search_db_bolder_rental_housing_engcompl: Engcompl
    :type search_db_bolder_rental_housing_engcompl: str
    :param search_db_bolder_rental_housing_licenseexp: Expiration Date
    :type search_db_bolder_rental_housing_licenseexp: str
    :param search_db_bolder_rental_housing_licensenum: Licensenum
    :type search_db_bolder_rental_housing_licensenum: str
    :param search_db_bolder_rental_housing_ppl1_coname: Ppl1 Coname
    :type search_db_bolder_rental_housing_ppl1_coname: str
    :param search_db_bolder_rental_housing_person_1: Person 1
    :type search_db_bolder_rental_housing_person_1: str
    :param search_db_bolder_rental_housing_ppl1_role: Ppl1 Role
    :type search_db_bolder_rental_housing_ppl1_role: str
    :param search_db_bolder_rental_housing_ppl2_coname: Ppl2 Coname
    :type search_db_bolder_rental_housing_ppl2_coname: str
    :param search_db_bolder_rental_housing_person_2: Person 2
    :type search_db_bolder_rental_housing_person_2: str
    :param search_db_bolder_rental_housing_ppl2_role: Ppl2 Role
    :type search_db_bolder_rental_housing_ppl2_role: str
    :param search_db_bolder_rental_housing_location: Location
    :type search_db_bolder_rental_housing_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
