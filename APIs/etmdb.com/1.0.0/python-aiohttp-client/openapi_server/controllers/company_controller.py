from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def company_search_read(request: web.Request, company_name) -> web.Response:
    """Return company search result

    Return company search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search companies,  For more details on how companies are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/-updated_date

    :param company_name: 
    :type company_name: str

    """
    return web.Response(status=200)
