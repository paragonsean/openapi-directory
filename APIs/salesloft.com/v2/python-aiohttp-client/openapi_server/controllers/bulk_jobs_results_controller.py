from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_job_result import BulkJobResult
from openapi_server import util


async def v2_bulk_jobs_bulk_jobs_id_results_get(request: web.Request, bulk_jobs_id, status=None, id=None, per_page=None) -> web.Response:
    """List job data for a completed bulk job.

    Fetches multiple job data records for a completed bulk job. Note that until a bulk job&#39;s state is set to &#x60;done&#x60; the returned &#x60;data&#x60; will be an empty array. Pagination is not supported, but cursor based polling is via use of the &#x60;id[gt]&#x60; filter. Pass the last id seen (i.e. &#x60;id[gt]&#x3D;1234&#x60;) in order to get the next batch of records.

    :param bulk_jobs_id: The id for the Bulk Job
    :type bulk_jobs_id: int
    :param status: Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying
    :type status: List[str]
    :param id: Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123)
    :type id: dict | bytes
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int

    """
    id = .from_dict(id)
    return web.Response(status=200)
