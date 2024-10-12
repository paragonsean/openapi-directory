from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_request import AddTagsRequest
from openapi_server.models.cancel_query_request import CancelQueryRequest
from openapi_server.models.cancel_query_response import CancelQueryResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.create_event_data_store_request import CreateEventDataStoreRequest
from openapi_server.models.create_event_data_store_response import CreateEventDataStoreResponse
from openapi_server.models.create_trail_request import CreateTrailRequest
from openapi_server.models.create_trail_response import CreateTrailResponse
from openapi_server.models.delete_channel_request import DeleteChannelRequest
from openapi_server.models.delete_event_data_store_request import DeleteEventDataStoreRequest
from openapi_server.models.delete_resource_policy_request import DeleteResourcePolicyRequest
from openapi_server.models.delete_trail_request import DeleteTrailRequest
from openapi_server.models.deregister_organization_delegated_admin_request import DeregisterOrganizationDelegatedAdminRequest
from openapi_server.models.describe_query_request import DescribeQueryRequest
from openapi_server.models.describe_query_response import DescribeQueryResponse
from openapi_server.models.describe_trails_request import DescribeTrailsRequest
from openapi_server.models.describe_trails_response import DescribeTrailsResponse
from openapi_server.models.get_channel_request import GetChannelRequest
from openapi_server.models.get_channel_response import GetChannelResponse
from openapi_server.models.get_event_data_store_request import GetEventDataStoreRequest
from openapi_server.models.get_event_data_store_response import GetEventDataStoreResponse
from openapi_server.models.get_event_selectors_request import GetEventSelectorsRequest
from openapi_server.models.get_event_selectors_response import GetEventSelectorsResponse
from openapi_server.models.get_import_request import GetImportRequest
from openapi_server.models.get_import_response import GetImportResponse
from openapi_server.models.get_insight_selectors_request import GetInsightSelectorsRequest
from openapi_server.models.get_insight_selectors_response import GetInsightSelectorsResponse
from openapi_server.models.get_query_results_request import GetQueryResultsRequest
from openapi_server.models.get_query_results_response import GetQueryResultsResponse
from openapi_server.models.get_resource_policy_request import GetResourcePolicyRequest
from openapi_server.models.get_resource_policy_response import GetResourcePolicyResponse
from openapi_server.models.get_trail_request import GetTrailRequest
from openapi_server.models.get_trail_response import GetTrailResponse
from openapi_server.models.get_trail_status_request import GetTrailStatusRequest
from openapi_server.models.get_trail_status_response import GetTrailStatusResponse
from openapi_server.models.list_channels_request import ListChannelsRequest
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_event_data_stores_request import ListEventDataStoresRequest
from openapi_server.models.list_event_data_stores_response import ListEventDataStoresResponse
from openapi_server.models.list_import_failures_request import ListImportFailuresRequest
from openapi_server.models.list_import_failures_response import ListImportFailuresResponse
from openapi_server.models.list_imports_request import ListImportsRequest
from openapi_server.models.list_imports_response import ListImportsResponse
from openapi_server.models.list_public_keys_request import ListPublicKeysRequest
from openapi_server.models.list_public_keys_response import ListPublicKeysResponse
from openapi_server.models.list_queries_request import ListQueriesRequest
from openapi_server.models.list_queries_response import ListQueriesResponse
from openapi_server.models.list_tags_request import ListTagsRequest
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_trails_request import ListTrailsRequest
from openapi_server.models.list_trails_response import ListTrailsResponse
from openapi_server.models.lookup_events_request import LookupEventsRequest
from openapi_server.models.lookup_events_response import LookupEventsResponse
from openapi_server.models.put_event_selectors_request import PutEventSelectorsRequest
from openapi_server.models.put_event_selectors_response import PutEventSelectorsResponse
from openapi_server.models.put_insight_selectors_request import PutInsightSelectorsRequest
from openapi_server.models.put_insight_selectors_response import PutInsightSelectorsResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.put_resource_policy_response import PutResourcePolicyResponse
from openapi_server.models.register_organization_delegated_admin_request import RegisterOrganizationDelegatedAdminRequest
from openapi_server.models.remove_tags_request import RemoveTagsRequest
from openapi_server.models.restore_event_data_store_request import RestoreEventDataStoreRequest
from openapi_server.models.restore_event_data_store_response import RestoreEventDataStoreResponse
from openapi_server.models.start_event_data_store_ingestion_request import StartEventDataStoreIngestionRequest
from openapi_server.models.start_import_request import StartImportRequest
from openapi_server.models.start_import_response import StartImportResponse
from openapi_server.models.start_logging_request import StartLoggingRequest
from openapi_server.models.start_query_request import StartQueryRequest
from openapi_server.models.start_query_response import StartQueryResponse
from openapi_server.models.stop_event_data_store_ingestion_request import StopEventDataStoreIngestionRequest
from openapi_server.models.stop_import_request import StopImportRequest
from openapi_server.models.stop_import_response import StopImportResponse
from openapi_server.models.stop_logging_request import StopLoggingRequest
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server.models.update_event_data_store_request import UpdateEventDataStoreRequest
from openapi_server.models.update_event_data_store_response import UpdateEventDataStoreResponse
from openapi_server.models.update_trail_request import UpdateTrailRequest
from openapi_server.models.update_trail_response import UpdateTrailResponse
from openapi_server import util


async def add_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags

    Adds one or more tags to a trail, event data store, or channel, up to a limit of 50. Overwrites an existing tag&#39;s value when a new value is specified for an existing tag key. Tag key names must be unique; you cannot have two keys with the same name but different values. If you specify a key without a value, the tag will be created with the specified key and a value of null. You can tag a trail or event data store that applies to all Amazon Web Services Regions only from the Region in which the trail or event data store was created (also known as its home Region).

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AddTagsRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_query

    Cancels a query if the query is not in a terminated state, such as &lt;code&gt;CANCELLED&lt;/code&gt;, &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;TIMED_OUT&lt;/code&gt;, or &lt;code&gt;FINISHED&lt;/code&gt;. You must specify an ARN value for &lt;code&gt;EventDataStore&lt;/code&gt;. The ID of the query that you want to cancel is also required. When you run &lt;code&gt;CancelQuery&lt;/code&gt;, the query status might show as &lt;code&gt;CANCELLED&lt;/code&gt; even if the operation is not yet finished.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CancelQueryRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel

    Creates a channel for CloudTrail to ingest events from a partner or external source. After you create a channel, a CloudTrail Lake event data store can log events from the partner or source that you specify.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_event_data_store(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_event_data_store

    Creates a new event data store.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateEventDataStoreRequest.from_dict(body)
    return web.Response(status=200)


async def create_trail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_trail

    Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateTrailRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel

    Deletes a channel.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteChannelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_event_data_store(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_event_data_store

    &lt;p&gt;Disables the event data store specified by &lt;code&gt;EventDataStore&lt;/code&gt;, which accepts an event data store ARN. After you run &lt;code&gt;DeleteEventDataStore&lt;/code&gt;, the event data store enters a &lt;code&gt;PENDING_DELETION&lt;/code&gt; state, and is automatically deleted after a wait period of seven days. &lt;code&gt;TerminationProtectionEnabled&lt;/code&gt; must be set to &lt;code&gt;False&lt;/code&gt; on the event data store; this operation cannot work if &lt;code&gt;TerminationProtectionEnabled&lt;/code&gt; is &lt;code&gt;True&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After you run &lt;code&gt;DeleteEventDataStore&lt;/code&gt; on an event data store, you cannot run &lt;code&gt;ListQueries&lt;/code&gt;, &lt;code&gt;DescribeQuery&lt;/code&gt;, or &lt;code&gt;GetQueryResults&lt;/code&gt; on queries that are using an event data store in a &lt;code&gt;PENDING_DELETION&lt;/code&gt; state. An event data store in the &lt;code&gt;PENDING_DELETION&lt;/code&gt; state does not incur costs.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteEventDataStoreRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

     Deletes the resource-based policy attached to the CloudTrail channel. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_trail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_trail

    Deletes a trail. This operation must be called from the Region in which the trail was created. &lt;code&gt;DeleteTrail&lt;/code&gt; cannot be called on the shadow trails (replicated trails in other Regions) of a trail that is enabled in all Regions.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteTrailRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_organization_delegated_admin(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_organization_delegated_admin

    Removes CloudTrail delegated administrator permissions from a member account in an organization.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeregisterOrganizationDelegatedAdminRequest.from_dict(body)
    return web.Response(status=200)


async def describe_query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_query

    &lt;p&gt;Returns metadata about a query, including query run time in milliseconds, number of events scanned and matched, and query status. If the query results were delivered to an S3 bucket, the response also provides the S3 URI and the delivery status.&lt;/p&gt; &lt;p&gt;You must specify either a &lt;code&gt;QueryID&lt;/code&gt; or a &lt;code&gt;QueryAlias&lt;/code&gt;. Specifying the &lt;code&gt;QueryAlias&lt;/code&gt; parameter returns information about the last query run for the alias.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeQueryRequest.from_dict(body)
    return web.Response(status=200)


async def describe_trails(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_trails

    Retrieves settings for one or more trails associated with the current Region for your account.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeTrailsRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel

     Returns information about a specific channel. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetChannelRequest.from_dict(body)
    return web.Response(status=200)


async def get_event_data_store(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_event_data_store

    Returns information about an event data store specified as either an ARN or the ID portion of the ARN.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetEventDataStoreRequest.from_dict(body)
    return web.Response(status=200)


async def get_event_selectors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_event_selectors

    &lt;p&gt;Describes the settings for the event selectors that you configured for your trail. The information returned for your event selectors includes the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If your event selector includes read-only events, write-only events, or all events. This applies to both management events and data events.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your event selector includes management events.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your event selector includes data events, the resources on which you are logging data events.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about logging management and data events, see the following topics in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html\&quot;&gt;Logging management events&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\&quot;&gt;Logging data events&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetEventSelectorsRequest.from_dict(body)
    return web.Response(status=200)


async def get_import(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_import

     Returns information about a specific import. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetImportRequest.from_dict(body)
    return web.Response(status=200)


async def get_insight_selectors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_insight_selectors

    &lt;p&gt;Describes the settings for the Insights event selectors that you configured for your trail. &lt;code&gt;GetInsightSelectors&lt;/code&gt; shows if CloudTrail Insights event logging is enabled on the trail, and if it is, which insight types are enabled. If you run &lt;code&gt;GetInsightSelectors&lt;/code&gt; on a trail that does not have Insights events enabled, the operation throws the exception &lt;code&gt;InsightNotEnabledException&lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html\&quot;&gt;Logging CloudTrail Insights Events for Trails &lt;/a&gt; in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetInsightSelectorsRequest.from_dict(body)
    return web.Response(status=200)


async def get_query_results(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """get_query_results

    Gets event data results of a query. You must specify the &lt;code&gt;QueryID&lt;/code&gt; value returned by the &lt;code&gt;StartQuery&lt;/code&gt; operation.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetQueryResultsRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_policy

     Retrieves the JSON text of the resource-based policy document attached to the CloudTrail channel. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def get_trail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_trail

    Returns settings information for a specified trail.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetTrailRequest.from_dict(body)
    return web.Response(status=200)


async def get_trail_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_trail_status

    Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for each trail. This operation returns trail status from a single Region. To return trail status from all Regions, you must call the operation on each Region.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetTrailStatusRequest.from_dict(body)
    return web.Response(status=200)


async def list_channels(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_channels

     Lists the channels in the current account, and their source names. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def list_event_data_stores(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_event_data_stores

    Returns information about all event data stores in the account, in the current Region.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEventDataStoresRequest.from_dict(body)
    return web.Response(status=200)


async def list_import_failures(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_import_failures

     Returns a list of failures for the specified import. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListImportFailuresRequest.from_dict(body)
    return web.Response(status=200)


async def list_imports(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_imports

     Returns information on all imports, or a select set of imports by &lt;code&gt;ImportStatus&lt;/code&gt; or &lt;code&gt;Destination&lt;/code&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListImportsRequest.from_dict(body)
    return web.Response(status=200)


async def list_public_keys(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_public_keys

    &lt;p&gt;Returns all public keys whose private keys were used to sign the digest files within the specified time range. The public key is needed to validate digest files that were signed with its corresponding private key.&lt;/p&gt; &lt;note&gt; &lt;p&gt;CloudTrail uses different private and public key pairs per Region. Each digest file is signed with a private key unique to its Region. When you validate a digest file from a specific Region, you must look in the same Region for its corresponding public key.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPublicKeysRequest.from_dict(body)
    return web.Response(status=200)


async def list_queries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_queries

    Returns a list of queries and query statuses for the past seven days. You must specify an ARN value for &lt;code&gt;EventDataStore&lt;/code&gt;. Optionally, to shorten the list of results, you can specify a time range, formatted as timestamps, by adding &lt;code&gt;StartTime&lt;/code&gt; and &lt;code&gt;EndTime&lt;/code&gt; parameters, and a &lt;code&gt;QueryStatus&lt;/code&gt; value. Valid values for &lt;code&gt;QueryStatus&lt;/code&gt; include &lt;code&gt;QUEUED&lt;/code&gt;, &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;FINISHED&lt;/code&gt;, &lt;code&gt;FAILED&lt;/code&gt;, &lt;code&gt;TIMED_OUT&lt;/code&gt;, or &lt;code&gt;CANCELLED&lt;/code&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListQueriesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_tags

    Lists the tags for the specified trails, event data stores, or channels in the current Region.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTagsRequest.from_dict(body)
    return web.Response(status=200)


async def list_trails(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_trails

    Lists trails that are in the current account.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTrailsRequest.from_dict(body)
    return web.Response(status=200)


async def lookup_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """lookup_events

    &lt;p&gt;Looks up &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events\&quot;&gt;management events&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-insights-events\&quot;&gt;CloudTrail Insights events&lt;/a&gt; that are captured by CloudTrail. You can look up events that occurred in a Region within the last 90 days. Lookup supports the following attributes for management events:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services access key&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Event ID&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Event name&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Event source&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Read only&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Resource name&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Resource type&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;User name&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Lookup supports the following attributes for Insights events:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Event ID&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Event name&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Event source&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;All attributes are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The rate of lookup requests is limited to two per second, per account, per Region. If this limit is exceeded, a throttling error occurs.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = LookupEventsRequest.from_dict(body)
    return web.Response(status=200)


async def put_event_selectors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_event_selectors

    &lt;p&gt;Configures an event selector or advanced event selectors for your trail. Use event selectors or advanced event selectors to specify management and data event settings for your trail. If you want your trail to log Insights events, be sure the event selector enables logging of the Insights event types you want configured for your trail. For more information about logging Insights events, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html\&quot;&gt;Logging Insights events for trails&lt;/a&gt; in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;. By default, trails created without specific event selectors are configured to log all read and write management events, and no data events.&lt;/p&gt; &lt;p&gt;When an event occurs in your account, CloudTrail evaluates the event selectors or advanced event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn&#39;t match any event selector, the trail doesn&#39;t log the event.&lt;/p&gt; &lt;p&gt;Example&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;You create an event selector for a trail and specify that you want write-only events.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The EC2 &lt;code&gt;GetConsoleOutput&lt;/code&gt; and &lt;code&gt;RunInstances&lt;/code&gt; API operations occur in your account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CloudTrail evaluates whether the events match your event selectors.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;RunInstances&lt;/code&gt; is a write-only event and it matches your event selector. The trail logs the event.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;GetConsoleOutput&lt;/code&gt; is a read-only event that doesn&#39;t match your event selector. The trail doesn&#39;t log the event. &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;The &lt;code&gt;PutEventSelectors&lt;/code&gt; operation must be called from the Region in which the trail was created; otherwise, an &lt;code&gt;InvalidHomeRegionException&lt;/code&gt; exception is thrown.&lt;/p&gt; &lt;p&gt;You can configure up to five event selectors for each trail. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html\&quot;&gt;Logging management events&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\&quot;&gt;Logging data events&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html\&quot;&gt;Quotas in CloudTrail&lt;/a&gt; in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either &lt;code&gt;AdvancedEventSelectors&lt;/code&gt; or &lt;code&gt;EventSelectors&lt;/code&gt;, but not both. If you apply &lt;code&gt;AdvancedEventSelectors&lt;/code&gt; to a trail, any existing &lt;code&gt;EventSelectors&lt;/code&gt; are overwritten. For more information about advanced event selectors, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\&quot;&gt;Logging data events&lt;/a&gt; in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutEventSelectorsRequest.from_dict(body)
    return web.Response(status=200)


async def put_insight_selectors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_insight_selectors

    &lt;p&gt;Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail. You also use &lt;code&gt;PutInsightSelectors&lt;/code&gt; to turn off Insights event logging, by passing an empty list of insight types. The valid Insights event types in this release are &lt;code&gt;ApiErrorRateInsight&lt;/code&gt; and &lt;code&gt;ApiCallRateInsight&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To log CloudTrail Insights events on API call volume, the trail must log &lt;code&gt;write&lt;/code&gt; management events. To log CloudTrail Insights events on API error rate, the trail must log &lt;code&gt;read&lt;/code&gt; or &lt;code&gt;write&lt;/code&gt; management events. You can call &lt;code&gt;GetEventSelectors&lt;/code&gt; on a trail to check whether the trail logs management events.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutInsightSelectorsRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

     Attaches a resource-based permission policy to a CloudTrail channel that is used for an integration with an event source outside of Amazon Web Services. For more information about resource-based policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html\&quot;&gt;CloudTrail resource-based policy examples&lt;/a&gt; in the &lt;i&gt;CloudTrail User Guide&lt;/i&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def register_organization_delegated_admin(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_organization_delegated_admin

    Registers an organization’s member account as the CloudTrail delegated administrator.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RegisterOrganizationDelegatedAdminRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags

    Removes the specified tags from a trail, event data store, or channel.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RemoveTagsRequest.from_dict(body)
    return web.Response(status=200)


async def restore_event_data_store(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_event_data_store

    Restores a deleted event data store specified by &lt;code&gt;EventDataStore&lt;/code&gt;, which accepts an event data store ARN. You can only restore a deleted event data store within the seven-day wait period after deletion. Restoring an event data store can take several minutes, depending on the size of the event data store.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RestoreEventDataStoreRequest.from_dict(body)
    return web.Response(status=200)


async def start_event_data_store_ingestion(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_event_data_store_ingestion

    Starts the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN. To start ingestion, the event data store &lt;code&gt;Status&lt;/code&gt; must be &lt;code&gt;STOPPED_INGESTION&lt;/code&gt; and the &lt;code&gt;eventCategory&lt;/code&gt; must be &lt;code&gt;Management&lt;/code&gt;, &lt;code&gt;Data&lt;/code&gt;, or &lt;code&gt;ConfigurationItem&lt;/code&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StartEventDataStoreIngestionRequest.from_dict(body)
    return web.Response(status=200)


async def start_import(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_import

    &lt;p&gt; Starts an import of logged trail events from a source S3 bucket to a destination event data store. By default, CloudTrail only imports events contained in the S3 bucket&#39;s &lt;code&gt;CloudTrail&lt;/code&gt; prefix and the prefixes inside the &lt;code&gt;CloudTrail&lt;/code&gt; prefix, and does not check prefixes for other Amazon Web Services services. If you want to import CloudTrail events contained in another prefix, you must include the prefix in the &lt;code&gt;S3LocationUri&lt;/code&gt;. For more considerations about importing trail events, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html#cloudtrail-trail-copy-considerations\&quot;&gt;Considerations&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; When you start a new import, the &lt;code&gt;Destinations&lt;/code&gt; and &lt;code&gt;ImportSource&lt;/code&gt; parameters are required. Before starting a new import, disable any access control lists (ACLs) attached to the source S3 bucket. For more information about disabling ACLs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html\&quot;&gt;Controlling ownership of objects and disabling ACLs for your bucket&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; When you retry an import, the &lt;code&gt;ImportID&lt;/code&gt; parameter is required. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If the destination event data store is for an organization, you must use the management account to import trail events. You cannot use the delegated administrator account for the organization. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StartImportRequest.from_dict(body)
    return web.Response(status=200)


async def start_logging(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_logging

    Starts the recording of Amazon Web Services API calls and log file delivery for a trail. For a trail that is enabled in all Regions, this operation must be called from the Region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other Regions) of a trail that is enabled in all Regions.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StartLoggingRequest.from_dict(body)
    return web.Response(status=200)


async def start_query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_query

    &lt;p&gt;Starts a CloudTrail Lake query. Use the &lt;code&gt;QueryStatement&lt;/code&gt; parameter to provide your SQL query, enclosed in single quotation marks. Use the optional &lt;code&gt;DeliveryS3Uri&lt;/code&gt; parameter to deliver the query results to an S3 bucket.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartQuery&lt;/code&gt; requires you specify either the &lt;code&gt;QueryStatement&lt;/code&gt; parameter, or a &lt;code&gt;QueryAlias&lt;/code&gt; and any &lt;code&gt;QueryParameters&lt;/code&gt;. In the current release, the &lt;code&gt;QueryAlias&lt;/code&gt; and &lt;code&gt;QueryParameters&lt;/code&gt; parameters are used only for the queries that populate the CloudTrail Lake dashboards.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StartQueryRequest.from_dict(body)
    return web.Response(status=200)


async def stop_event_data_store_ingestion(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_event_data_store_ingestion

    Stops the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN. To stop ingestion, the event data store &lt;code&gt;Status&lt;/code&gt; must be &lt;code&gt;ENABLED&lt;/code&gt; and the &lt;code&gt;eventCategory&lt;/code&gt; must be &lt;code&gt;Management&lt;/code&gt;, &lt;code&gt;Data&lt;/code&gt;, or &lt;code&gt;ConfigurationItem&lt;/code&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StopEventDataStoreIngestionRequest.from_dict(body)
    return web.Response(status=200)


async def stop_import(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_import

     Stops a specified import. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StopImportRequest.from_dict(body)
    return web.Response(status=200)


async def stop_logging(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_logging

    Suspends the recording of Amazon Web Services API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can update a trail without stopping it first. This action is the only way to stop recording. For a trail enabled in all Regions, this operation must be called from the Region in which the trail was created, or an &lt;code&gt;InvalidHomeRegionException&lt;/code&gt; will occur. This operation cannot be called on the shadow trails (replicated trails in other Regions) of a trail enabled in all Regions.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = StopLoggingRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel

    Updates a channel specified by a required channel ARN or UUID.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_event_data_store(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_event_data_store

    &lt;p&gt;Updates an event data store. The required &lt;code&gt;EventDataStore&lt;/code&gt; value is an ARN or the ID portion of the ARN. Other parameters are optional, but at least one optional parameter must be specified, or CloudTrail throws an error. &lt;code&gt;RetentionPeriod&lt;/code&gt; is in days, and valid values are integers between 90 and 2557. By default, &lt;code&gt;TerminationProtection&lt;/code&gt; is enabled.&lt;/p&gt; &lt;p&gt;For event data stores for CloudTrail events, &lt;code&gt;AdvancedEventSelectors&lt;/code&gt; includes or excludes management and data events in your event data store. For more information about &lt;code&gt;AdvancedEventSelectors&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html\&quot;&gt;AdvancedEventSelectors&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For event data stores for Config configuration items, Audit Manager evidence, or non-Amazon Web Services events, &lt;code&gt;AdvancedEventSelectors&lt;/code&gt; includes events of that type in your event data store.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateEventDataStoreRequest.from_dict(body)
    return web.Response(status=200)


async def update_trail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_trail

    Updates trail settings that control what events you are logging, and how to handle log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. &lt;code&gt;UpdateTrail&lt;/code&gt; must be called from the Region in which the trail was created; otherwise, an &lt;code&gt;InvalidHomeRegionException&lt;/code&gt; is thrown.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateTrailRequest.from_dict(body)
    return web.Response(status=200)
