from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def wages_download_salary_file_get(request: web.Request, date_from=None, date_to=None, company_id=None) -> web.Response:
    """Download salary file

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)
