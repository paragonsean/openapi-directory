from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_summary(request: web.Request, ein=None, search_term=None, city=None, state=None, zip_code=None, category=None, eligible=None, start=None, rows=None) -> web.Response:
    """Get summary data!

    &lt;p&gt;This operation provides summary data.&lt;/p&gt;

    :param ein: Employer Identification Number (EIN)
    :type ein: str
    :param search_term: Charity Name or Keyword. Example: humane society or cancer
    :type search_term: str
    :param city: City Name. Example: Miami
    :type city: str
    :param state: State Name - Two letter state abbreviation
    :type state: str
    :param zip_code: Zipcode Value - 5 digit zipcode value
    :type zip_code: str
    :param category: Category Value Selected from Categories API
    :type category: str
    :param eligible: eligible&#x3D;1 will return only organizations that are tax deductible and in good standing with the IRS
    :type eligible: str
    :param start: Record Set Start Position
    :type start: str
    :param rows: Records Per Page. Default Value &#x3D; 20
    :type rows: str

    """
    return web.Response(status=200)
