from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_monitoring_csv_download_response import JobMonitoringCsvDownloadResponse
from openapi_server.models.job_monitoring_response import JobMonitoringResponse
from openapi_server.models.job_monitoring_summary_by_state import JobMonitoringSummaryByState
from openapi_server.models.job_monitoring_summary_by_type import JobMonitoringSummaryByType
from openapi_server.models.monitoring_email_subscription_request import MonitoringEmailSubscriptionRequest
from openapi_server.models.monitoring_email_subscription_update import MonitoringEmailSubscriptionUpdate
from openapi_server.models.monitoring_subscription_summary import MonitoringSubscriptionSummary
from openapi_server import util


async def create_monitoring_subscription(request: web.Request, body) -> web.Response:
    """Create an email subscription to the job monitoring page

    Creates an email subscription to the job monitoring page, which provides information on jobs based on their type (active, in progress, canceled, scheduled, or succeeded). Users can choose which job states to include in the subscription. The email summarizes the job counts by type in the body, and includes the option to include CSV attachments for every job state selected.

    :param body: All information required to create a job-monitoring email subscription.
    :type body: dict | bytes

    """
    body = MonitoringEmailSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_monitoring_subscription(request: web.Request, subscription_id) -> web.Response:
    """Delete a monitoring page email subscription

    Deletes the specified monitoring page email subscription.

    :param subscription_id: ID of the monitoring subscription to delete.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def get_job_monitoring_info(request: web.Request, limit=None, job_event_status=None, job_type=None, should_include_log_related_job=None, is_first_full=None, object_type=None, object_name=None, node_name=None, effective_sla_domain_id=None, is_on_demand=None, last_update_time=None, after_id=None, sort_by=None, sort_order=None) -> web.Response:
    """Get job monitoring information

    Get the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours.

    :param limit: Maximum number of entries to retrieve. The default value is 25. Value needs to be a positive number.
    :type limit: int
    :param job_event_status: Filters results by the current event status of the job. The filters should be separated by &#39;,&#39;.
    :type job_event_status: List[str]
    :param job_type: Filters results by job type.
    :type job_type: str
    :param should_include_log_related_job: A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;.
    :type should_include_log_related_job: bool
    :param is_first_full: Filter results by first full status.
    :type is_first_full: bool
    :param object_type: Filters results by a specified object type.
    :type object_type: str
    :param object_name: Filters results by the provided value for object_name, using infix search.
    :type object_name: str
    :param node_name: Filter results by node name.
    :type node_name: str
    :param effective_sla_domain_id: Filters results by the provided sla doimain id.
    :type effective_sla_domain_id: str
    :param is_on_demand: Filters results according to their on-demand status.
    :type is_on_demand: bool
    :param last_update_time: All rows updated at or after this time will be returned.
    :type last_update_time: str
    :param after_id: Fetches all rows after given row cursor.
    :type after_id: str
    :param sort_by: The column by which to sort the entries.
    :type sort_by: str
    :param sort_order: The sorting order.
    :type sort_order: str

    """
    last_update_time = util.deserialize_datetime(last_update_time)
    return web.Response(status=200)


async def get_job_monitoring_info_csv_download_link(request: web.Request, job_monitoring_state, job_event_status=None, job_type=None, should_include_log_related_job=None, object_type=None, object_name=None) -> web.Response:
    """Download job monitoring information as a CSV file

    Download the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours as a CSV file. This is a synchronous operation.

    :param job_monitoring_state: State of the jobs in the CSV.
    :type job_monitoring_state: str
    :param job_event_status: Filters results by the current event status of the job.
    :type job_event_status: str
    :param job_type: Filters results by job type.
    :type job_type: str
    :param should_include_log_related_job: A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;.
    :type should_include_log_related_job: bool
    :param object_type: Filters results by a specified object type.
    :type object_type: str
    :param object_name: Filters results by the provided value for object_name, using infix search.
    :type object_name: str

    """
    return web.Response(status=200)


async def get_monitoring_job_count_by_job_state(request: web.Request, job_types=None) -> web.Response:
    """Get job monitoring summary information separated by job state

    Get job summary separated by job state for all running jobs, jobs that have been scheduled and jobs that are complete, for protection and recovery jobs in the past 24 hours.

    :param job_types: Filter by a comma separated list of job types.
    :type job_types: List[str]

    """
    return web.Response(status=200)


async def get_monitoring_job_count_by_job_type(request: web.Request, job_monitoring_state) -> web.Response:
    """Get job monitoring summary information separated by job type

    Get job summaries for protection and recovery jobs, separated by job type, that have been scheduled, are currently running, or completed in the past 24 hours.

    :param job_monitoring_state: Filter by job state.
    :type job_monitoring_state: str

    """
    return web.Response(status=200)


async def get_monitoring_subscription(request: web.Request, subscription_id) -> web.Response:
    """Get a specific monitoring email subscription by id

    Returns a summary of the provided monitoring subscription.

    :param subscription_id: ID of the monitoring subscription to acquire.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def get_monitoring_subscriptions(request: web.Request, ) -> web.Response:
    """Returns all email subscriptions for the monitoring page

    Return all unarchived email subscriptions for monitoring page in a list of summaries sorted by creation time (earliest created first). Each summary contains information for each subscription -- Time attributes - when to send the email -- Email addresses - who to send the email -- Attachments - what attachments should the email include -- Job states - which job states to include in the email (Failure, Scheduled, Success, Active, Canceled). -- Id - the tring that identifies the subscription -- Status - the status of the subscription (Active, Suspended, or Unknown) -- Owner - information about the owner of the subscription -- user id - unique id used to identify the owner -- user name - human-readable name of user the time schedule to send the subscription.


    """
    return web.Response(status=200)


async def update_monitoring_subscription(request: web.Request, subscription_id, body) -> web.Response:
    """Update a monitoring email subscription

    Updates the monitoring email subscription with the subscription ID provided.

    :param subscription_id: ID of the monitoring subscription.
    :type subscription_id: str
    :param body: Information required to update a monitoring subscription.
    :type body: dict | bytes

    """
    body = MonitoringEmailSubscriptionUpdate.from_dict(body)
    return web.Response(status=200)
