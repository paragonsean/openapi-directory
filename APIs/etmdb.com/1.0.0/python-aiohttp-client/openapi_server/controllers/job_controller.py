from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def job_search_read(request: web.Request, job_title) -> web.Response:
    """Return job details search result

    Return job details search result  ### Response Class (Status 200)  * __{job_title}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

    :param job_title: 
    :type job_title: str

    """
    return web.Response(status=200)


async def job_searchall_read(request: web.Request, company_name) -> web.Response:
    """Return job details search result

    Return job details search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

    :param company_name: 
    :type company_name: str

    """
    return web.Response(status=200)
