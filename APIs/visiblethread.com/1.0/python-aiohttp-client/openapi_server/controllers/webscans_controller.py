from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_scan import NewScan
from openapi_server.models.new_scan_response import NewScanResponse
from openapi_server.models.scan_response_detailed import ScanResponseDetailed
from openapi_server.models.scan_response_summary import ScanResponseSummary
from openapi_server.models.web_response_not_ready import WebResponseNotReady
from openapi_server.models.web_url_detail import WebUrlDetail
from openapi_server import util


async def get_scan_by_id(request: web.Request, scan_id) -> web.Response:
    """Get data from a previously run scan

    Get data from a previously run scan, identified by **scanId**

    :param scan_id: Id of scan to fetch
    :type scan_id: int

    """
    return web.Response(status=200)


async def get_scan_url_by_id(request: web.Request, scan_id, url_id) -> web.Response:
    """Gets data for a particular scan/webUrl

    Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

    :param scan_id: Id of scan
    :type scan_id: int
    :param url_id: Id of url to fetch
    :type url_id: int

    """
    return web.Response(status=200)


async def run_scan(request: web.Request, body) -> web.Response:
    """Run a new scan

    The scan runs in the background but returns immediately with a JSON response containing an \&quot;id\&quot; that represents your scan.         You can use this id in other requests to retrieve your scan result.   Also, an \&quot;id\&quot; is returned for each url which can be used to retrieve detailed results for individual scan urls. 

    :param body: Scan title and webUrls to analyze
    :type body: dict | bytes

    """
    body = NewScan.from_dict(body)
    return web.Response(status=200)


async def webscans_get(request: web.Request, ) -> web.Response:
    """Get your list of scans

    Get your list of scans


    """
    return web.Response(status=200)
