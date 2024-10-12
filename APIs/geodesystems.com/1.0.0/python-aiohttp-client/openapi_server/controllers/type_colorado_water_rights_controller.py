from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_colorado_water_rights(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_colorado_water_rights_structure_name=None, search_db_colorado_water_rights_structure_type=None, search_db_colorado_water_rights_water_source=None, search_db_colorado_water_rights_county=None, search_db_colorado_water_rights_adjudication_date=None, search_db_colorado_water_rights_appropriation_date=None, search_db_colorado_water_rights_priority_no=None, search_db_colorado_water_rights_decreed_uses=None, search_db_colorado_water_rights_net_absolute=None, search_db_colorado_water_rights_net_conditional=None, search_db_colorado_water_rights_net_apex_absolute=None, search_db_colorado_water_rights_net_apex_conditional=None, search_db_colorado_water_rights_decreed_units=None, search_db_colorado_water_rights_seasonal_limits=None, search_db_colorado_water_rights_comments=None, search_db_colorado_water_rights_more_information=None, search_db_colorado_water_rights_location=None) -> web.Response:
    """Search API for &#39;Colorado Water Rights&#39; entry type

    API to search for entries of type Colorado Water Rights

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
    :param search_db_colorado_water_rights_structure_name: Structure Name
    :type search_db_colorado_water_rights_structure_name: str
    :param search_db_colorado_water_rights_structure_type: Structure Type
    :type search_db_colorado_water_rights_structure_type: str
    :param search_db_colorado_water_rights_water_source: Water Source
    :type search_db_colorado_water_rights_water_source: str
    :param search_db_colorado_water_rights_county: County
    :type search_db_colorado_water_rights_county: str
    :param search_db_colorado_water_rights_adjudication_date: Adjudication Date
    :type search_db_colorado_water_rights_adjudication_date: str
    :param search_db_colorado_water_rights_appropriation_date: Appropriation Date
    :type search_db_colorado_water_rights_appropriation_date: str
    :param search_db_colorado_water_rights_priority_no: Priority No
    :type search_db_colorado_water_rights_priority_no: str
    :param search_db_colorado_water_rights_decreed_uses: Decreed Uses
    :type search_db_colorado_water_rights_decreed_uses: str
    :param search_db_colorado_water_rights_net_absolute: Net Absolute
    :type search_db_colorado_water_rights_net_absolute: float
    :param search_db_colorado_water_rights_net_conditional: Net Conditional
    :type search_db_colorado_water_rights_net_conditional: float
    :param search_db_colorado_water_rights_net_apex_absolute: Net Apex Absolute
    :type search_db_colorado_water_rights_net_apex_absolute: float
    :param search_db_colorado_water_rights_net_apex_conditional: Net Apex Conditional
    :type search_db_colorado_water_rights_net_apex_conditional: float
    :param search_db_colorado_water_rights_decreed_units: Decreed Units
    :type search_db_colorado_water_rights_decreed_units: str
    :param search_db_colorado_water_rights_seasonal_limits: Seasonal Limits
    :type search_db_colorado_water_rights_seasonal_limits: str
    :param search_db_colorado_water_rights_comments: Comments
    :type search_db_colorado_water_rights_comments: str
    :param search_db_colorado_water_rights_more_information: More Information
    :type search_db_colorado_water_rights_more_information: str
    :param search_db_colorado_water_rights_location: Location
    :type search_db_colorado_water_rights_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
