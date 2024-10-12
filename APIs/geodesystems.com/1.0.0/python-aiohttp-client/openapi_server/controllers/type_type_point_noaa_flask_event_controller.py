from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_type_point_noaa_flask_event(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_type_point_noaa_flask_event_site_id=None, search_type_point_noaa_flask_event_parameter=None, search_type_point_noaa_flask_event_project=None, search_type_point_noaa_flask_event_lab_id_number=None, search_type_point_noaa_flask_event_measurement_group=None) -> web.Response:
    """Search API for &#39;NOAA Flask Event Measurements&#39; entry type

    API to search for entries of type NOAA Flask Event Measurements

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
    :param search_type_point_noaa_flask_event_site_id: Site ID
    :type search_type_point_noaa_flask_event_site_id: str
    :param search_type_point_noaa_flask_event_parameter: Parameter
    :type search_type_point_noaa_flask_event_parameter: str
    :param search_type_point_noaa_flask_event_project: Project
    :type search_type_point_noaa_flask_event_project: str
    :param search_type_point_noaa_flask_event_lab_id_number: Lab ID Number
    :type search_type_point_noaa_flask_event_lab_id_number: str
    :param search_type_point_noaa_flask_event_measurement_group: Measurement Group
    :type search_type_point_noaa_flask_event_measurement_group: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
