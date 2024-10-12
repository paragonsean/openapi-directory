from typing import List, Dict
from aiohttp import web

from openapi_server.models.co2 import CO2
from openapi_server.models.co2_list200_response import Co2List200Response
from openapi_server import util


async def co2_list(request: web.Request, ppm=None, _date=None, date__range=None, ordering=None, page=None, limit=None) -> web.Response:
    """co2_list

    CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

    :param ppm: 
    :type ppm: 
    :param _date: 
    :type _date: str
    :param date__range: Multiple values may be separated by commas.
    :type date__range: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param limit: Number of results to return per page.
    :type limit: int

    """
    return web.Response(status=200)


async def co2_read(request: web.Request, _date) -> web.Response:
    """co2_read

    CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

    :param _date: 
    :type _date: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)
