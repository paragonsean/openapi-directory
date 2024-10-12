from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_notification_channels_request import AddNotificationChannelsRequest
from openapi_server.models.add_notification_channels_response import AddNotificationChannelsResponse
from openapi_server.models.batch_get_frame_metric_data_request import BatchGetFrameMetricDataRequest
from openapi_server.models.batch_get_frame_metric_data_response import BatchGetFrameMetricDataResponse
from openapi_server.models.configure_agent_request import ConfigureAgentRequest
from openapi_server.models.configure_agent_response import ConfigureAgentResponse
from openapi_server.models.create_profiling_group_request import CreateProfilingGroupRequest
from openapi_server.models.create_profiling_group_response import CreateProfilingGroupResponse
from openapi_server.models.describe_profiling_group_response import DescribeProfilingGroupResponse
from openapi_server.models.get_findings_report_account_summary_response import GetFindingsReportAccountSummaryResponse
from openapi_server.models.get_notification_configuration_response import GetNotificationConfigurationResponse
from openapi_server.models.get_policy_response import GetPolicyResponse
from openapi_server.models.get_profile_response import GetProfileResponse
from openapi_server.models.get_recommendations_response import GetRecommendationsResponse
from openapi_server.models.list_findings_reports_response import ListFindingsReportsResponse
from openapi_server.models.list_profile_times_response import ListProfileTimesResponse
from openapi_server.models.list_profiling_groups_response import ListProfilingGroupsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.post_agent_profile_request import PostAgentProfileRequest
from openapi_server.models.put_permission_request import PutPermissionRequest
from openapi_server.models.put_permission_response import PutPermissionResponse
from openapi_server.models.remove_notification_channel_response import RemoveNotificationChannelResponse
from openapi_server.models.remove_permission_response import RemovePermissionResponse
from openapi_server.models.submit_feedback_request import SubmitFeedbackRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_profiling_group_request import UpdateProfilingGroupRequest
from openapi_server.models.update_profiling_group_response import UpdateProfilingGroupResponse
from openapi_server import util


async def add_notification_channels(request: web.Request, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_notification_channels

    Add up to 2 anomaly notifications channels for a profiling group.

    :param profiling_group_name: The name of the profiling group that we are setting up notifications for.
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AddNotificationChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_frame_metric_data(request: web.Request, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, end_time=None, period=None, start_time=None, target_resolution=None) -> web.Response:
    """batch_get_frame_metric_data

     Returns the time series of values for a requested list of frame metrics from a time period.

    :param profiling_group_name:  The name of the profiling group associated with the the frame metrics used to return the time series values. 
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param end_time:  The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type end_time: str
    :param period:  The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (&lt;code&gt;PT24H&lt;/code&gt; or &lt;code&gt;P1D&lt;/code&gt;). 
    :type period: str
    :param start_time:  The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type start_time: str
    :param target_resolution: &lt;p&gt;The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;P1D&lt;/code&gt; — 1 day &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT1H&lt;/code&gt; — 1 hour &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT5M&lt;/code&gt; — 5 minutes &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type target_resolution: str

    """
    body = BatchGetFrameMetricDataRequest.from_dict(body)
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def configure_agent(request: web.Request, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """configure_agent

     Used by profiler agents to report their current state and to receive remote configuration updates. For example, &lt;code&gt;ConfigureAgent&lt;/code&gt; can be used to tell an agent whether to profile or not and for how long to return profiling data. 

    :param profiling_group_name:  The name of the profiling group for which the configured agent is collecting profiling data. 
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ConfigureAgentRequest.from_dict(body)
    return web.Response(status=200)


async def create_profiling_group(request: web.Request, client_token, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_profiling_group

    Creates a profiling group.

    :param client_token:  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries. 
    :type client_token: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProfilingGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_profiling_group(request: web.Request, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profiling_group

    Deletes a profiling group.

    :param profiling_group_name: The name of the profiling group to delete.
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_profiling_group(request: web.Request, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_profiling_group

     Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; object that contains information about the requested profiling group. 

    :param profiling_group_name:  The name of the profiling group to get information about. 
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_findings_report_account_summary(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, daily_reports_only=None, max_results=None, next_token=None) -> web.Response:
    """get_findings_report_account_summary

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html\&quot;&gt; &lt;code&gt;FindingsReportSummary&lt;/code&gt; &lt;/a&gt; objects that contain analysis results for all profiling groups in your AWS account. 

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param daily_reports_only: A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to only return reports from daily profiles. If set to &lt;code&gt;True&lt;/code&gt;, only analysis data from daily profiles is returned. If set to &lt;code&gt;False&lt;/code&gt;, analysis data is returned from smaller time windows (for example, one hour).
    :type daily_reports_only: bool
    :param max_results: The maximum number of results returned by &lt;code&gt; GetFindingsReportAccountSummary&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def get_notification_configuration(request: web.Request, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_notification_configuration

    Get the current configuration for anomaly notifications for a profiling group.

    :param profiling_group_name: The name of the profiling group we want to get the notification configuration for.
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_policy(request: web.Request, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_policy

     Returns the JSON-formatted resource-based policy on a profiling group. 

    :param profiling_group_name: The name of the profiling group.
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_profile(request: web.Request, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, accept=None, end_time=None, max_depth=None, period=None, start_time=None) -> web.Response:
    """get_profile

    &lt;p&gt; Gets the aggregated profile of a profiling group for a specified time range. Amazon CodeGuru Profiler collects posted agent profiles for a profiling group into aggregated profiles. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;note&amp;gt; &amp;lt;p&amp;gt; Because aggregated profiles expire over time &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt; is not idempotent. &amp;lt;/p&amp;gt; &amp;lt;/note&amp;gt; &amp;lt;p&amp;gt; Specify the time range for the requested aggregated profile using 1 or 2 of the following parameters: &amp;lt;code&amp;gt;startTime&amp;lt;/code&amp;gt;, &amp;lt;code&amp;gt;endTime&amp;lt;/code&amp;gt;, &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;. The maximum time range allowed is 7 days. If you specify all 3 parameters, an exception is thrown. If you specify only &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;, the latest aggregated profile is returned. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; Aggregated profiles are available with aggregation periods of 5 minutes, 1 hour, and 1 day, aligned to UTC. The aggregation period of an aggregated profile determines how long it is retained. For more information, see &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;AggregatedProfileTime&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;. The aggregated profile&#39;s aggregation period determines how long it is retained by CodeGuru Profiler. &amp;lt;/p&amp;gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 5 minutes, the aggregated profile is retained for 15 days. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 1 hour, the aggregated profile is retained for 60 days. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 1 day, the aggregated profile is retained for 3 years. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &amp;lt;p&amp;gt;There are two use cases for calling &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt;.&amp;lt;/p&amp;gt; &amp;lt;ol&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If you want to return an aggregated profile that already exists, use &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;ListProfileTimes&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt; to view the time ranges of existing aggregated profiles. Use them in a &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt; request to return a specific, existing aggregated profile. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If you want to return an aggregated profile for a time range that doesn&#39;t align with an existing aggregated profile, then CodeGuru Profiler makes a best effort to combine existing aggregated profiles from the requested time range and return them as one aggregated profile. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; If aggregated profiles do not exist for the full time range requested, then aggregated profiles for a smaller time range are returned. For example, if the requested time range is from 00:00 to 00:20, and the existing aggregated profiles are from 00:15 and 00:25, then the aggregated profiles from 00:15 to 00:20 are returned. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ol&amp;gt; &lt;/code&gt;&lt;/pre&gt;

    :param profiling_group_name: The name of the profiling group to get.
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param accept: &lt;p&gt; The format of the returned profiling data. The format maps to the &lt;code&gt;Accept&lt;/code&gt; and &lt;code&gt;Content-Type&lt;/code&gt; headers of the HTTP request. You can specify one of the following: or the default . &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/json&amp;lt;/code&amp;gt; — standard JSON format &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/x-amzn-ion&amp;lt;/code&amp;gt; — the Amazon Ion data format. For more information, see &amp;lt;a href&#x3D;&amp;quot;http://amzn.github.io/ion-docs/&amp;quot;&amp;gt;Amazon Ion&amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &lt;/code&gt;&lt;/pre&gt;
    :type accept: str
    :param end_time: &lt;p&gt; The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. &lt;/p&gt; &lt;p&gt; If you specify &lt;code&gt;endTime&lt;/code&gt;, then you must also specify &lt;code&gt;period&lt;/code&gt; or &lt;code&gt;startTime&lt;/code&gt;, but not both. &lt;/p&gt;
    :type end_time: str
    :param max_depth:  The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method &lt;code&gt;A&lt;/code&gt;, which calls method &lt;code&gt;B&lt;/code&gt;, which calls method &lt;code&gt;C&lt;/code&gt;, which calls method &lt;code&gt;D&lt;/code&gt;, then the depth is 4. If the &lt;code&gt;maxDepth&lt;/code&gt; is set to 2, then the aggregated profile contains representations of methods &lt;code&gt;A&lt;/code&gt; and &lt;code&gt;B&lt;/code&gt;. 
    :type max_depth: int
    :param period: &lt;p&gt; Used with &lt;code&gt;startTime&lt;/code&gt; or &lt;code&gt;endTime&lt;/code&gt; to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, &lt;code&gt;P1DT1H1M1S&lt;/code&gt;. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; To get the latest aggregated profile, specify only &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt;
    :type period: str
    :param start_time: &lt;p&gt;The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.&lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; If you specify &amp;lt;code&amp;gt;startTime&amp;lt;/code&amp;gt;, then you must also specify &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt; or &amp;lt;code&amp;gt;endTime&amp;lt;/code&amp;gt;, but not both. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt;
    :type start_time: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def get_recommendations(request: web.Request, end_time, profiling_group_name, start_time, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, locale=None) -> web.Response:
    """get_recommendations

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html\&quot;&gt; &lt;code&gt;Recommendation&lt;/code&gt; &lt;/a&gt; objects that contain recommendations for a profiling group for a given time period. A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html\&quot;&gt; &lt;code&gt;Anomaly&lt;/code&gt; &lt;/a&gt; objects that contains details about anomalies detected in the profiling group for the same time period is also returned. 

    :param end_time:  The start time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type end_time: str
    :param profiling_group_name:  The name of the profiling group to get analysis data about. 
    :type profiling_group_name: str
    :param start_time:  The end time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type start_time: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param locale: &lt;p&gt; The language used to provide analysis. Specify using a string that is one of the following &lt;code&gt;BCP 47&lt;/code&gt; language codes. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;de-DE&lt;/code&gt; - German, Germany &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;en-GB&lt;/code&gt; - English, United Kingdom &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;en-US&lt;/code&gt; - English, United States &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;es-ES&lt;/code&gt; - Spanish, Spain &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;fr-FR&lt;/code&gt; - French, France &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;it-IT&lt;/code&gt; - Italian, Italy &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ja-JP&lt;/code&gt; - Japanese, Japan &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ko-KR&lt;/code&gt; - Korean, Republic of Korea &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pt-BR&lt;/code&gt; - Portugese, Brazil &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;zh-CN&lt;/code&gt; - Chinese, China &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;zh-TW&lt;/code&gt; - Chinese, Taiwan &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type locale: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def list_findings_reports(request: web.Request, end_time, profiling_group_name, start_time, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, daily_reports_only=None, max_results=None, next_token=None) -> web.Response:
    """list_findings_reports

    List the available reports for a given profiling group and time range.

    :param end_time:  The end time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type end_time: str
    :param profiling_group_name: The name of the profiling group from which to search for analysis data.
    :type profiling_group_name: str
    :param start_time:  The start time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    :type start_time: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param daily_reports_only: A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to only return reports from daily profiles. If set to &lt;code&gt;True&lt;/code&gt;, only analysis data from daily profiles is returned. If set to &lt;code&gt;False&lt;/code&gt;, analysis data is returned from smaller time windows (for example, one hour).
    :type daily_reports_only: bool
    :param max_results: The maximum number of report results returned by &lt;code&gt;ListFindingsReports&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListFindingsReports&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListFindingsReports&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListFindingsReportsRequest&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def list_profile_times(request: web.Request, end_time, period, profiling_group_name, start_time, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, order_by=None) -> web.Response:
    """list_profile_times

    Lists the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.

    :param end_time: The end time of the time range from which to list the profiles.
    :type end_time: str
    :param period: &lt;p&gt; The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;P1D&lt;/code&gt; — 1 day &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT1H&lt;/code&gt; — 1 hour &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT5M&lt;/code&gt; — 5 minutes &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type period: str
    :param profiling_group_name: The name of the profiling group.
    :type profiling_group_name: str
    :param start_time: The start time of the time range from which to list the profiles.
    :type start_time: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of profile time results returned by &lt;code&gt;ListProfileTimes&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListProfileTimes&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListProfileTimes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. 
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListProfileTimes&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str
    :param order_by: The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to &lt;code&gt;TIMESTAMP_DESCENDING&lt;/code&gt;. 
    :type order_by: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def list_profiling_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_description=None, max_results=None, next_token=None) -> web.Response:
    """list_profiling_groups

     Returns a list of profiling groups. The profiling groups are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; objects. 

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param include_description: A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to include a description. If &lt;code&gt;true&lt;/code&gt;, then a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; objects that contain detailed information about profiling groups is returned. If &lt;code&gt;false&lt;/code&gt;, then a list of profiling group names is returned.
    :type include_description: bool
    :param max_results: The maximum number of profiling groups results returned by &lt;code&gt;ListProfilingGroups&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListProfilingGroups&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListProfilingGroups&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. 
    :type max_results: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListProfilingGroups&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

     Returns a list of the tags that are assigned to a specified resource. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the resource that contains the tags to return. 
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def post_agent_profile(request: web.Request, content_type, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, profile_token=None) -> web.Response:
    """post_agent_profile

     Submits profiling data to an aggregated profile of a profiling group. To get an aggregated profile that is created with this profiling data, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html\&quot;&gt; &lt;code&gt;GetProfile&lt;/code&gt; &lt;/a&gt;. 

    :param content_type: &lt;p&gt; The format of the submitted profiling data. The format maps to the &lt;code&gt;Accept&lt;/code&gt; and &lt;code&gt;Content-Type&lt;/code&gt; headers of the HTTP request. You can specify one of the following: or the default . &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/json&amp;lt;/code&amp;gt; — standard JSON format &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/x-amzn-ion&amp;lt;/code&amp;gt; — the Amazon Ion data format. For more information, see &amp;lt;a href&#x3D;&amp;quot;http://amzn.github.io/ion-docs/&amp;quot;&amp;gt;Amazon Ion&amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &lt;/code&gt;&lt;/pre&gt;
    :type content_type: str
    :param profiling_group_name:  The name of the profiling group with the aggregated profile that receives the submitted profiling data. 
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param profile_token:  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries. 
    :type profile_token: str

    """
    body = PostAgentProfileRequest.from_dict(body)
    return web.Response(status=200)


async def put_permission(request: web.Request, action_group, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_permission

    &lt;p&gt; Adds permissions to a profiling group&#39;s resource-based policy that are provided using an action group. If a profiling group doesn&#39;t have a resource-based policy, one is created for it using the permissions in the action group and the roles and users in the &lt;code&gt;principals&lt;/code&gt; parameter. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; The one supported action group that can be added is &amp;lt;code&amp;gt;agentPermission&amp;lt;/code&amp;gt; which grants &amp;lt;code&amp;gt;ConfigureAgent&amp;lt;/code&amp;gt; and &amp;lt;code&amp;gt;PostAgent&amp;lt;/code&amp;gt; permissions. For more information, see &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html&amp;quot;&amp;gt;Resource-based policies in CodeGuru Profiler&amp;lt;/a&amp;gt; in the &amp;lt;i&amp;gt;Amazon CodeGuru Profiler User Guide&amp;lt;/i&amp;gt;, &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;ConfigureAgent&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;, and &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;PostAgentProfile&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; The first time you call &amp;lt;code&amp;gt;PutPermission&amp;lt;/code&amp;gt; on a profiling group, do not specify a &amp;lt;code&amp;gt;revisionId&amp;lt;/code&amp;gt; because it doesn&#39;t have a resource-based policy. Subsequent calls must provide a &amp;lt;code&amp;gt;revisionId&amp;lt;/code&amp;gt; to specify which revision of the resource-based policy to add the permissions to. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; The response contains the profiling group&#39;s JSON-formatted resource policy. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt;

    :param action_group:  Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, &lt;code&gt;agentPermissions&lt;/code&gt;, which grants permission to perform actions required by the profiling agent, &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgentProfile&lt;/code&gt; permissions. 
    :type action_group: str
    :param profiling_group_name: The name of the profiling group to grant access to.
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def remove_notification_channel(request: web.Request, channel_id, profiling_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_notification_channel

    Remove one anomaly notifications channel for a profiling group.

    :param channel_id: The id of the channel that we want to stop receiving notifications.
    :type channel_id: str
    :param profiling_group_name: The name of the profiling group we want to change notification configuration for.
    :type profiling_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def remove_permission(request: web.Request, action_group, profiling_group_name, revision_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_permission

     Removes permissions from a profiling group&#39;s resource-based policy that are provided using an action group. The one supported action group that can be removed is &lt;code&gt;agentPermission&lt;/code&gt; which grants &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgent&lt;/code&gt; permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html\&quot;&gt;Resource-based policies in CodeGuru Profiler&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Profiler User Guide&lt;/i&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html\&quot;&gt; &lt;code&gt;ConfigureAgent&lt;/code&gt; &lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html\&quot;&gt; &lt;code&gt;PostAgentProfile&lt;/code&gt; &lt;/a&gt;. 

    :param action_group:  Specifies an action group that contains the permissions to remove from a profiling group&#39;s resource-based policy. One action group is supported, &lt;code&gt;agentPermissions&lt;/code&gt;, which grants &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgentProfile&lt;/code&gt; permissions. 
    :type action_group: str
    :param profiling_group_name: The name of the profiling group.
    :type profiling_group_name: str
    :param revision_id:  A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions. 
    :type revision_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def submit_feedback(request: web.Request, anomaly_instance_id, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_feedback

    Sends feedback to CodeGuru Profiler about whether the anomaly detected by the analysis is useful or not.

    :param anomaly_instance_id: The universally unique identifier (UUID) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html\&quot;&gt; &lt;code&gt;AnomalyInstance&lt;/code&gt; &lt;/a&gt; object that is included in the analysis data.
    :type anomaly_instance_id: str
    :param profiling_group_name: The name of the profiling group that is associated with the analysis data.
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SubmitFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

     Use to assign one or more tags to a resource. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the resource that the tags are added to. 
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

     Use to remove one or more tags from a resource. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the resource that contains the tags to remove. 
    :type resource_arn: str
    :param tag_keys:  A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. 
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_profiling_group(request: web.Request, profiling_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_profiling_group

    Updates a profiling group.

    :param profiling_group_name: The name of the profiling group to update.
    :type profiling_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProfilingGroupRequest.from_dict(body)
    return web.Response(status=200)
