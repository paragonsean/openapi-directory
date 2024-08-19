from typing import List, Dict
from aiohttp import web

from openapi_server.models.report_usage_batch_request import ReportUsageBatchRequest
from openapi_server.models.report_usage_batch_response import ReportUsageBatchResponse
from openapi_server import util


async def v3_usage_batches_id_put(request: web.Request, id, body=None) -> web.Response:
    """Report usage of assets via a batch format.

    # Report Usage  Use this endpoint to report the usages of a set of assets. The count of assets submitted in a single batch to this endpoint is limited to 1000. Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded. In this case, you will need to remove the invalid asset Ids from the query request and re-submit the query.  ##  Quickstart  You&#39;ll need an API key and a [Resource Owner Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource. Please see our [Getting Started](http://developers.gettyimages.com/en/getting-started.html) page for more information on how to sign up for an API key.   _Note_: Date of use can be in any unambiguous date format. 

    :param id: Specifies a unique batch transaction id to identify the report.
    :type id: str
    :param body: Specifies up to 1000 sets of asset Id, usage count, and date of use to submit usages for.               Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded.               All dates must be on or before this date and the format should be ISO 8601 (ex: YYYY-MM-DD), time is not needed.
    :type body: dict | bytes

    """
    body = ReportUsageBatchRequest.from_dict(body)
    return web.Response(status=200)
