from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_mostemailed_section_time_period_json200_response import GETMostemailedSectionTimePeriodJson200Response
from openapi_server.models.get_mostemailed_section_time_period_json400_response import GETMostemailedSectionTimePeriodJson400Response
from openapi_server.models.get_mostshared_section_time_period_json200_response import GETMostsharedSectionTimePeriodJson200Response
from openapi_server import util


async def g_et_mostemailed_section_time_period_json(request: web.Request, section, time_period) -> web.Response:
    """Most Emailed by Section &amp; Time Period

    

    :param section: Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.  
    :type section: str
    :param time_period: Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content.
    :type time_period: str

    """
    return web.Response(status=200)


async def g_et_mostshared_section_time_period_json(request: web.Request, section, time_period) -> web.Response:
    """Most Shared by Section &amp; Time Period

    

    :param section: Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.  
    :type section: str
    :param time_period: Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content.
    :type time_period: str

    """
    return web.Response(status=200)


async def g_et_mostviewed_section_time_period_json(request: web.Request, section, time_period) -> web.Response:
    """Most Viewed by Section &amp; Time Period

    

    :param section: Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.  
    :type section: str
    :param time_period: Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content.
    :type time_period: str

    """
    return web.Response(status=200)
