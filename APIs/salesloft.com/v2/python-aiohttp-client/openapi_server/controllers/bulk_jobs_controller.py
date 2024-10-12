from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_job import BulkJob
from openapi_server import util


async def v2_bulk_jobs_get(request: web.Request, state=None, id=None, per_page=None) -> web.Response:
    """List bulk jobs

    Fetches multiple bulk job records. The records can be filtered, paged, and sorted according to the respective parameters.

    :param state: The state of the bulk job. Accepts multiple states. Each state must be one of: open, executing, done
    :type state: List[str]
    :param id: Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123)
    :type id: dict | bytes
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int

    """
    id = .from_dict(id)
    return web.Response(status=200)


async def v2_bulk_jobs_id_get(request: web.Request, id) -> web.Response:
    """Fetch a bulk job

    Fetches a bulk job, by ID only.

    :param id: The id for the Bulk Job
    :type id: int

    """
    return web.Response(status=200)


async def v2_bulk_jobs_id_put(request: web.Request, id, name=None, ready_to_execute=None) -> web.Response:
    """Update a bulk job

    Updates a bulk job&#39;s name and / or marks a bulk job as &#39;ready_to_execute&#39;.  May only be updated if the bulk job is still in an \&quot;open\&quot; state.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

    :param id: The id for the bulk job to which the job data relates
    :type id: int
    :param name: Name for your bulk job
    :type name: str
    :param ready_to_execute: Whether the job is ready to be executed. Must be true or false.
    :type ready_to_execute: bool

    """
    return web.Response(status=200)


async def v2_bulk_jobs_post(request: web.Request, type, name=None) -> web.Response:
    """Create a bulk job

    Creates a bulk job. The type of the bulk job must be included when created.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

    :param type: Type of bulk job. Must be a valid type. Follow link to the bulk job details page above to view supported types.
    :type type: str
    :param name: Name for your bulk job
    :type name: str

    """
    return web.Response(status=200)
