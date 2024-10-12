from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_event_source_request import ActivateEventSourceRequest
from openapi_server.models.cancel_replay_request import CancelReplayRequest
from openapi_server.models.cancel_replay_response import CancelReplayResponse
from openapi_server.models.create_api_destination_request import CreateApiDestinationRequest
from openapi_server.models.create_api_destination_response import CreateApiDestinationResponse
from openapi_server.models.create_archive_request import CreateArchiveRequest
from openapi_server.models.create_archive_response import CreateArchiveResponse
from openapi_server.models.create_connection_request import CreateConnectionRequest
from openapi_server.models.create_connection_response import CreateConnectionResponse
from openapi_server.models.create_endpoint_request import CreateEndpointRequest
from openapi_server.models.create_endpoint_response import CreateEndpointResponse
from openapi_server.models.create_event_bus_request import CreateEventBusRequest
from openapi_server.models.create_event_bus_response import CreateEventBusResponse
from openapi_server.models.create_partner_event_source_request import CreatePartnerEventSourceRequest
from openapi_server.models.create_partner_event_source_response import CreatePartnerEventSourceResponse
from openapi_server.models.deactivate_event_source_request import DeactivateEventSourceRequest
from openapi_server.models.deauthorize_connection_request import DeauthorizeConnectionRequest
from openapi_server.models.deauthorize_connection_response import DeauthorizeConnectionResponse
from openapi_server.models.delete_api_destination_request import DeleteApiDestinationRequest
from openapi_server.models.delete_archive_request import DeleteArchiveRequest
from openapi_server.models.delete_connection_request import DeleteConnectionRequest
from openapi_server.models.delete_connection_response import DeleteConnectionResponse
from openapi_server.models.delete_endpoint_request import DeleteEndpointRequest
from openapi_server.models.delete_event_bus_request import DeleteEventBusRequest
from openapi_server.models.delete_partner_event_source_request import DeletePartnerEventSourceRequest
from openapi_server.models.delete_rule_request import DeleteRuleRequest
from openapi_server.models.describe_api_destination_request import DescribeApiDestinationRequest
from openapi_server.models.describe_api_destination_response import DescribeApiDestinationResponse
from openapi_server.models.describe_archive_request import DescribeArchiveRequest
from openapi_server.models.describe_archive_response import DescribeArchiveResponse
from openapi_server.models.describe_connection_request import DescribeConnectionRequest
from openapi_server.models.describe_connection_response import DescribeConnectionResponse
from openapi_server.models.describe_endpoint_request import DescribeEndpointRequest
from openapi_server.models.describe_endpoint_response import DescribeEndpointResponse
from openapi_server.models.describe_event_bus_request import DescribeEventBusRequest
from openapi_server.models.describe_event_bus_response import DescribeEventBusResponse
from openapi_server.models.describe_event_source_request import DescribeEventSourceRequest
from openapi_server.models.describe_event_source_response import DescribeEventSourceResponse
from openapi_server.models.describe_partner_event_source_request import DescribePartnerEventSourceRequest
from openapi_server.models.describe_partner_event_source_response import DescribePartnerEventSourceResponse
from openapi_server.models.describe_replay_request import DescribeReplayRequest
from openapi_server.models.describe_replay_response import DescribeReplayResponse
from openapi_server.models.describe_rule_request import DescribeRuleRequest
from openapi_server.models.describe_rule_response import DescribeRuleResponse
from openapi_server.models.disable_rule_request import DisableRuleRequest
from openapi_server.models.enable_rule_request import EnableRuleRequest
from openapi_server.models.list_api_destinations_request import ListApiDestinationsRequest
from openapi_server.models.list_api_destinations_response import ListApiDestinationsResponse
from openapi_server.models.list_archives_request import ListArchivesRequest
from openapi_server.models.list_archives_response import ListArchivesResponse
from openapi_server.models.list_connections_request import ListConnectionsRequest
from openapi_server.models.list_connections_response import ListConnectionsResponse
from openapi_server.models.list_endpoints_request import ListEndpointsRequest
from openapi_server.models.list_endpoints_response import ListEndpointsResponse
from openapi_server.models.list_event_buses_request import ListEventBusesRequest
from openapi_server.models.list_event_buses_response import ListEventBusesResponse
from openapi_server.models.list_event_sources_request import ListEventSourcesRequest
from openapi_server.models.list_event_sources_response import ListEventSourcesResponse
from openapi_server.models.list_partner_event_source_accounts_request import ListPartnerEventSourceAccountsRequest
from openapi_server.models.list_partner_event_source_accounts_response import ListPartnerEventSourceAccountsResponse
from openapi_server.models.list_partner_event_sources_request import ListPartnerEventSourcesRequest
from openapi_server.models.list_partner_event_sources_response import ListPartnerEventSourcesResponse
from openapi_server.models.list_replays_request import ListReplaysRequest
from openapi_server.models.list_replays_response import ListReplaysResponse
from openapi_server.models.list_rule_names_by_target_request import ListRuleNamesByTargetRequest
from openapi_server.models.list_rule_names_by_target_response import ListRuleNamesByTargetResponse
from openapi_server.models.list_rules_request import ListRulesRequest
from openapi_server.models.list_rules_response import ListRulesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_targets_by_rule_request import ListTargetsByRuleRequest
from openapi_server.models.list_targets_by_rule_response import ListTargetsByRuleResponse
from openapi_server.models.put_events_request import PutEventsRequest
from openapi_server.models.put_events_response import PutEventsResponse
from openapi_server.models.put_partner_events_request import PutPartnerEventsRequest
from openapi_server.models.put_partner_events_response import PutPartnerEventsResponse
from openapi_server.models.put_permission_request import PutPermissionRequest
from openapi_server.models.put_rule_request import PutRuleRequest
from openapi_server.models.put_rule_response import PutRuleResponse
from openapi_server.models.put_targets_request import PutTargetsRequest
from openapi_server.models.put_targets_response import PutTargetsResponse
from openapi_server.models.remove_permission_request import RemovePermissionRequest
from openapi_server.models.remove_targets_request import RemoveTargetsRequest
from openapi_server.models.remove_targets_response import RemoveTargetsResponse
from openapi_server.models.start_replay_request import StartReplayRequest
from openapi_server.models.start_replay_response import StartReplayResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.test_event_pattern_request import TestEventPatternRequest
from openapi_server.models.test_event_pattern_response import TestEventPatternResponse
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_api_destination_request import UpdateApiDestinationRequest
from openapi_server.models.update_api_destination_response import UpdateApiDestinationResponse
from openapi_server.models.update_archive_request import UpdateArchiveRequest
from openapi_server.models.update_archive_response import UpdateArchiveResponse
from openapi_server.models.update_connection_request import UpdateConnectionRequest
from openapi_server.models.update_connection_response import UpdateConnectionResponse
from openapi_server.models.update_endpoint_request import UpdateEndpointRequest
from openapi_server.models.update_endpoint_response import UpdateEndpointResponse
from openapi_server import util


async def activate_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """activate_event_source

    Activates a partner event source that has been deactivated. Once activated, your matching event bus will start receiving events from the event source.

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
    body = ActivateEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_replay(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_replay

    Cancels the specified replay.

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
    body = CancelReplayRequest.from_dict(body)
    return web.Response(status=200)


async def create_api_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_api_destination

    Creates an API destination, which is an HTTP invocation endpoint configured as a target for events.

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
    body = CreateApiDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def create_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_archive

    Creates an archive of events with the specified settings. When you create an archive, incoming events might not immediately start being sent to the archive. Allow a short period of time for changes to take effect. If you do not specify a pattern to filter events sent to the archive, all events are sent to the archive except replayed events. Replayed events are not sent to an archive.

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
    body = CreateArchiveRequest.from_dict(body)
    return web.Response(status=200)


async def create_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_connection

    Creates a connection. A connection defines the authorization type and credentials to use for authorization with an API destination HTTP endpoint.

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
    body = CreateConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_endpoint

    Creates a global endpoint. Global endpoints improve your application&#39;s availability by making it regional-fault tolerant. To do this, you define a primary and secondary Region with event buses in each Region. You also create a Amazon Route 53 health check that will tell EventBridge to route events to the secondary Region when an \&quot;unhealthy\&quot; state is encountered and events will be routed back to the primary Region when the health check reports a \&quot;healthy\&quot; state.

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
    body = CreateEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def create_event_bus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_event_bus

    Creates a new event bus within your account. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.

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
    body = CreateEventBusRequest.from_dict(body)
    return web.Response(status=200)


async def create_partner_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_partner_event_source

    &lt;p&gt;Called by an SaaS partner to create a partner event source. This operation is not used by Amazon Web Services customers.&lt;/p&gt; &lt;p&gt;Each partner event source can be used by one Amazon Web Services account to create a matching partner event bus in that Amazon Web Services account. A SaaS partner must create one partner event source for each Amazon Web Services account that wants to receive those event types. &lt;/p&gt; &lt;p&gt;A partner event source creates events based on resources within the SaaS partner&#39;s service or application.&lt;/p&gt; &lt;p&gt;An Amazon Web Services account that creates a partner event bus that matches the partner event source can use that event bus to receive events from the partner, and then process them using Amazon Web Services Events rules and targets.&lt;/p&gt; &lt;p&gt;Partner event source names follow this format:&lt;/p&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;partner_name&lt;/i&gt;/&lt;i&gt;event_namespace&lt;/i&gt;/&lt;i&gt;event_name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;i&gt;partner_name&lt;/i&gt; is determined during partner registration and identifies the partner to Amazon Web Services customers. &lt;i&gt;event_namespace&lt;/i&gt; is determined by the partner and is a way for the partner to categorize their events. &lt;i&gt;event_name&lt;/i&gt; is determined by the partner, and should uniquely identify an event-generating resource within the partner system. The combination of &lt;i&gt;event_namespace&lt;/i&gt; and &lt;i&gt;event_name&lt;/i&gt; should help Amazon Web Services customers decide whether to create an event bus to receive these events.&lt;/p&gt;

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
    body = CreatePartnerEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deactivate_event_source

    &lt;p&gt;You can use this operation to temporarily stop receiving events from the specified partner event source. The matching event bus is not deleted. &lt;/p&gt; &lt;p&gt;When you deactivate a partner event source, the source goes into PENDING state. If it remains in PENDING state for more than two weeks, it is deleted.&lt;/p&gt; &lt;p&gt;To activate a deactivated partner event source, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ActivateEventSource.html\&quot;&gt;ActivateEventSource&lt;/a&gt;.&lt;/p&gt;

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
    body = DeactivateEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def deauthorize_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deauthorize_connection

    Removes all authorization parameters from the connection. This lets you remove the secret from the connection so you can reuse it without having to create a new connection.

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
    body = DeauthorizeConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_api_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_api_destination

    Deletes the specified API destination.

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
    body = DeleteApiDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_archive

    Deletes the specified archive.

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
    body = DeleteArchiveRequest.from_dict(body)
    return web.Response(status=200)


async def delete_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_connection

    Deletes a connection.

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
    body = DeleteConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_endpoint

    Delete an existing global endpoint. For more information about global endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html\&quot;&gt;Making applications Regional-fault tolerant with global endpoints and event replication&lt;/a&gt; in the Amazon EventBridge User Guide.

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
    body = DeleteEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def delete_event_bus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_event_bus

    Deletes the specified custom event bus or partner event bus. All rules associated with this event bus need to be deleted. You can&#39;t delete your account&#39;s default event bus.

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
    body = DeleteEventBusRequest.from_dict(body)
    return web.Response(status=200)


async def delete_partner_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_partner_event_source

    &lt;p&gt;This operation is used by SaaS partners to delete a partner event source. This operation is not used by Amazon Web Services customers.&lt;/p&gt; &lt;p&gt;When you delete an event source, the status of the corresponding partner event bus in the Amazon Web Services customer account becomes DELETED.&lt;/p&gt; &lt;p/&gt;

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
    body = DeletePartnerEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule

    &lt;p&gt;Deletes the specified rule.&lt;/p&gt; &lt;p&gt;Before you can delete the rule, you must remove all targets, using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargets.html\&quot;&gt;RemoveTargets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When you delete a rule, incoming events might continue to match to the deleted rule. Allow a short period of time for changes to take effect.&lt;/p&gt; &lt;p&gt;If you call delete rule multiple times for the same rule, all calls will succeed. When you call delete rule for a non-existent custom eventbus, &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is returned.&lt;/p&gt; &lt;p&gt;Managed rules are rules created and managed by another Amazon Web Services service on your behalf. These rules are created by those other Amazon Web Services services to support functionality in those services. You can delete these rules using the &lt;code&gt;Force&lt;/code&gt; option, but you should do so only if you are sure the other service is not still using that rule.&lt;/p&gt;

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
    body = DeleteRuleRequest.from_dict(body)
    return web.Response(status=200)


async def describe_api_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_api_destination

    Retrieves details about an API destination.

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
    body = DescribeApiDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_archive

    Retrieves details about an archive.

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
    body = DescribeArchiveRequest.from_dict(body)
    return web.Response(status=200)


async def describe_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_connection

    Retrieves details about a connection.

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
    body = DescribeConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_endpoint

    Get the information about an existing global endpoint. For more information about global endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html\&quot;&gt;Making applications Regional-fault tolerant with global endpoints and event replication&lt;/a&gt; in the Amazon EventBridge User Guide..

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
    body = DescribeEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def describe_event_bus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_event_bus

    &lt;p&gt;Displays details about an event bus in your account. This can include the external Amazon Web Services accounts that are permitted to write events to your default event bus, and the associated policy. For custom event buses and partner event buses, it displays the name, ARN, policy, state, and creation time.&lt;/p&gt; &lt;p&gt; To enable your account to receive events from other accounts on its default event bus, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html\&quot;&gt;PutPermission&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about partner event buses, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\&quot;&gt;CreateEventBus&lt;/a&gt;.&lt;/p&gt;

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
    body = DescribeEventBusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_event_source

    This operation lists details about a partner event source that is shared with your account.

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
    body = DescribeEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_partner_event_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_partner_event_source

    An SaaS partner can use this operation to list details about a partner event source that they have created. Amazon Web Services customers do not use this operation. Instead, Amazon Web Services customers can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html\&quot;&gt;DescribeEventSource&lt;/a&gt; to see details about a partner event source that is shared with them.

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
    body = DescribePartnerEventSourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_replay(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_replay

    Retrieves details about a replay. Use &lt;code&gt;DescribeReplay&lt;/code&gt; to determine the progress of a running replay. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you use &lt;code&gt;StartReplay&lt;/code&gt; and specify an &lt;code&gt;EventStartTime&lt;/code&gt; and an &lt;code&gt;EventEndTime&lt;/code&gt; that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use &lt;code&gt;DescribeReplay&lt;/code&gt; to determine the progress of a replay. The value returned for &lt;code&gt;EventLastReplayedTime&lt;/code&gt; indicates the time within the specified time range associated with the last event replayed.

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
    body = DescribeReplayRequest.from_dict(body)
    return web.Response(status=200)


async def describe_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_rule

    &lt;p&gt;Describes the specified rule.&lt;/p&gt; &lt;p&gt;DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html\&quot;&gt;ListTargetsByRule&lt;/a&gt;.&lt;/p&gt;

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
    body = DescribeRuleRequest.from_dict(body)
    return web.Response(status=200)


async def disable_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_rule

    &lt;p&gt;Disables the specified rule. A disabled rule won&#39;t match any events, and won&#39;t self-trigger if it has a schedule expression.&lt;/p&gt; &lt;p&gt;When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.&lt;/p&gt;

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
    body = DisableRuleRequest.from_dict(body)
    return web.Response(status=200)


async def enable_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_rule

    &lt;p&gt;Enables the specified rule. If the rule does not exist, the operation fails.&lt;/p&gt; &lt;p&gt;When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Allow a short period of time for changes to take effect.&lt;/p&gt;

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
    body = EnableRuleRequest.from_dict(body)
    return web.Response(status=200)


async def list_api_destinations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_api_destinations

    Retrieves a list of API destination in the account in the current Region.

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
    body = ListApiDestinationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_archives(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_archives

    Lists your archives. You can either list all the archives or you can provide a prefix to match to the archive names. Filter parameters are exclusive.

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
    body = ListArchivesRequest.from_dict(body)
    return web.Response(status=200)


async def list_connections(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_connections

    Retrieves a list of connections from the account.

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
    body = ListConnectionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_endpoints(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_endpoints

    List the global endpoints associated with this account. For more information about global endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html\&quot;&gt;Making applications Regional-fault tolerant with global endpoints and event replication&lt;/a&gt; in the Amazon EventBridge User Guide..

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
    body = ListEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def list_event_buses(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_event_buses

    Lists all the event buses in your account, including the default event bus, custom event buses, and partner event buses.

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
    body = ListEventBusesRequest.from_dict(body)
    return web.Response(status=200)


async def list_event_sources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_event_sources

    You can use this to see all the partner event sources that have been shared with your Amazon Web Services account. For more information about partner event sources, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\&quot;&gt;CreateEventBus&lt;/a&gt;.

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
    body = ListEventSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_partner_event_source_accounts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_partner_event_source_accounts

    An SaaS partner can use this operation to display the Amazon Web Services account ID that a particular partner event source name is associated with. This operation is not used by Amazon Web Services customers.

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
    body = ListPartnerEventSourceAccountsRequest.from_dict(body)
    return web.Response(status=200)


async def list_partner_event_sources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_partner_event_sources

    An SaaS partner can use this operation to list all the partner event source names that they have created. This operation is not used by Amazon Web Services customers.

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
    body = ListPartnerEventSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_replays(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_replays

    Lists your replays. You can either list all the replays or you can provide a prefix to match to the replay names. Filter parameters are exclusive.

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
    body = ListReplaysRequest.from_dict(body)
    return web.Response(status=200)


async def list_rule_names_by_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rule_names_by_target

    Lists the rules for the specified target. You can see which of the rules in Amazon EventBridge can invoke a specific target in your account.

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
    body = ListRuleNamesByTargetRequest.from_dict(body)
    return web.Response(status=200)


async def list_rules(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rules

    &lt;p&gt;Lists your Amazon EventBridge rules. You can either list all the rules or you can provide a prefix to match to the rule names.&lt;/p&gt; &lt;p&gt;ListRules does not list the targets of a rule. To see the targets associated with a rule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html\&quot;&gt;ListTargetsByRule&lt;/a&gt;.&lt;/p&gt;

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
    body = ListRulesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with an EventBridge resource. In EventBridge, rules and event buses can be tagged.

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_targets_by_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_targets_by_rule

    Lists the targets assigned to the specified rule.

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
    body = ListTargetsByRuleRequest.from_dict(body)
    return web.Response(status=200)


async def put_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_events

    &lt;p&gt;Sends custom events to Amazon EventBridge so that they can be matched to rules.&lt;/p&gt; &lt;note&gt; &lt;p&gt;PutEvents will only process nested JSON up to 1100 levels deep.&lt;/p&gt; &lt;/note&gt;

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
    body = PutEventsRequest.from_dict(body)
    return web.Response(status=200)


async def put_partner_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_partner_events

    This is used by SaaS partners to write events to a customer&#39;s partner event bus. Amazon Web Services customers do not use this operation.

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
    body = PutPartnerEventsRequest.from_dict(body)
    return web.Response(status=200)


async def put_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_permission

    &lt;p&gt;Running &lt;code&gt;PutPermission&lt;/code&gt; permits the specified Amazon Web Services account or Amazon Web Services organization to put events to the specified &lt;i&gt;event bus&lt;/i&gt;. Amazon EventBridge (CloudWatch Events) rules in your account are triggered by these events arriving to an event bus in your account. &lt;/p&gt; &lt;p&gt;For another account to send events to your account, that external account must have an EventBridge rule with your account&#39;s event bus as a target.&lt;/p&gt; &lt;p&gt;To enable multiple Amazon Web Services accounts to put events to your event bus, run &lt;code&gt;PutPermission&lt;/code&gt; once for each of these accounts. Or, if all the accounts are members of the same Amazon Web Services organization, you can run &lt;code&gt;PutPermission&lt;/code&gt; once specifying &lt;code&gt;Principal&lt;/code&gt; as \&quot;*\&quot; and specifying the Amazon Web Services organization ID in &lt;code&gt;Condition&lt;/code&gt;, to grant permissions to all accounts in that organization.&lt;/p&gt; &lt;p&gt;If you grant permissions using an organization, then accounts in that organization must specify a &lt;code&gt;RoleArn&lt;/code&gt; with proper permissions when they use &lt;code&gt;PutTarget&lt;/code&gt; to add your account&#39;s event bus as a target. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html\&quot;&gt;Sending and Receiving Events Between Amazon Web Services Accounts&lt;/a&gt; in the &lt;i&gt;Amazon EventBridge User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The permission policy on the event bus cannot exceed 10 KB in size.&lt;/p&gt;

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
    body = PutPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def put_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_rule

    &lt;p&gt;Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html\&quot;&gt;DisableRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A single rule watches for events from a single event bus. Events generated by Amazon Web Services services go to your account&#39;s default event bus. Events generated by SaaS partner services or applications go to the matching partner event bus. If you have custom applications or services, you can specify whether their events go to your default event bus or a custom event bus that you have created. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\&quot;&gt;CreateEventBus&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are updating an existing rule, the rule is replaced with what you specify in this &lt;code&gt;PutRule&lt;/code&gt; command. If you omit arguments in &lt;code&gt;PutRule&lt;/code&gt;, the old values for those arguments are not kept. Instead, they are replaced with null values.&lt;/p&gt; &lt;p&gt;When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Allow a short period of time for changes to take effect.&lt;/p&gt; &lt;p&gt;A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.&lt;/p&gt; &lt;p&gt;When you initially create a rule, you can optionally assign one or more tags to the rule. Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only rules with certain tag values. To use the &lt;code&gt;PutRule&lt;/code&gt; operation and assign tags, you must have both the &lt;code&gt;events:PutRule&lt;/code&gt; and &lt;code&gt;events:TagResource&lt;/code&gt; permissions.&lt;/p&gt; &lt;p&gt;If you are updating an existing rule, any tags you specify in the &lt;code&gt;PutRule&lt;/code&gt; operation are ignored. To update the tags of an existing rule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Most services in Amazon Web Services treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.&lt;/p&gt; &lt;p&gt;In EventBridge, it is possible to create rules that lead to infinite loops, where a rule is fired repeatedly. For example, a rule might detect that ACLs have changed on an S3 bucket, and trigger software to change them to the desired state. If the rule is not written carefully, the subsequent change to the ACLs fires the rule again, creating an infinite loop.&lt;/p&gt; &lt;p&gt;To prevent this, write the rules so that the triggered actions do not re-fire the same rule. For example, your rule could fire only if ACLs are found to be in a bad state, instead of after any change. &lt;/p&gt; &lt;p&gt;An infinite loop can quickly cause higher than expected charges. We recommend that you use budgeting, which alerts you when charges exceed your specified limit. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html\&quot;&gt;Managing Your Costs with Budgets&lt;/a&gt;.&lt;/p&gt;

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
    body = PutRuleRequest.from_dict(body)
    return web.Response(status=200)


async def put_targets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_targets

    &lt;p&gt;Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.&lt;/p&gt; &lt;p&gt;Targets are the resources that are invoked when a rule is triggered.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Each rule can have up to five (5) targets associated with it at one time.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can configure the following as targets for Events:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html\&quot;&gt;API destination&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-gateway-target.html\&quot;&gt;API Gateway&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Batch job queue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CloudWatch group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CodeBuild project&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CodePipeline&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 &lt;code&gt;CreateSnapshot&lt;/code&gt; API call&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 Image Builder&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 &lt;code&gt;RebootInstances&lt;/code&gt; API call&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 &lt;code&gt;StopInstances&lt;/code&gt; API call&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 &lt;code&gt;TerminateInstances&lt;/code&gt; API call&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ECS task&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html\&quot;&gt;Event bus in a different account or Region&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-bus-to-bus.html\&quot;&gt;Event bus in the same account and Region&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Firehose delivery stream&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Glue workflow&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html#incident-tracking-auto-eventbridge\&quot;&gt;Incident Manager response plan&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Inspector assessment template&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Kinesis stream&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lambda function&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redshift cluster&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redshift Serverless workgroup&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;SageMaker Pipeline&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;SNS topic&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;SQS queue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Step Functions state machine&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Systems Manager Automation&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Systems Manager OpsItem&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Systems Manager Run Command&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Creating rules with built-in targets is supported only in the Amazon Web Services Management Console. The built-in targets are &lt;code&gt;EC2 CreateSnapshot API call&lt;/code&gt;, &lt;code&gt;EC2 RebootInstances API call&lt;/code&gt;, &lt;code&gt;EC2 StopInstances API call&lt;/code&gt;, and &lt;code&gt;EC2 TerminateInstances API call&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For some target types, &lt;code&gt;PutTargets&lt;/code&gt; provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the &lt;code&gt;KinesisParameters&lt;/code&gt; argument. To invoke a command on multiple EC2 instances with one rule, you can use the &lt;code&gt;RunCommandParameters&lt;/code&gt; field.&lt;/p&gt; &lt;p&gt;To be able to make API calls against the resources that you own, Amazon EventBridge needs the appropriate permissions. For Lambda and Amazon SNS resources, EventBridge relies on resource-based policies. For EC2 instances, Kinesis Data Streams, Step Functions state machines and API Gateway APIs, EventBridge relies on IAM roles that you specify in the &lt;code&gt;RoleARN&lt;/code&gt; argument in &lt;code&gt;PutTargets&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/auth-and-access-control-eventbridge.html\&quot;&gt;Authentication and Access Control&lt;/a&gt; in the &lt;i&gt;Amazon EventBridge User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If another Amazon Web Services account is in the same region and has granted you permission (using &lt;code&gt;PutPermission&lt;/code&gt;), you can send events to that account. Set that account&#39;s event bus as a target of the rules in your account. To send the matched events to the other account, specify that account&#39;s event bus as the &lt;code&gt;Arn&lt;/code&gt; value when you run &lt;code&gt;PutTargets&lt;/code&gt;. If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/eventbridge/pricing/\&quot;&gt;Amazon EventBridge Pricing&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;Input&lt;/code&gt;, &lt;code&gt;InputPath&lt;/code&gt;, and &lt;code&gt;InputTransformer&lt;/code&gt; are not available with &lt;code&gt;PutTarget&lt;/code&gt; if the target is an event bus of a different Amazon Web Services account.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a &lt;code&gt;RoleArn&lt;/code&gt; with proper permissions in the &lt;code&gt;Target&lt;/code&gt; structure. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html\&quot;&gt;Sending and Receiving Events Between Amazon Web Services Accounts&lt;/a&gt; in the &lt;i&gt;Amazon EventBridge User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about enabling cross-account events, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html\&quot;&gt;PutPermission&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Input&lt;/b&gt;, &lt;b&gt;InputPath&lt;/b&gt;, and &lt;b&gt;InputTransformer&lt;/b&gt; are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;b&gt;Input&lt;/b&gt; is specified in the form of valid JSON, then the matched event is overridden with this constant.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;b&gt;InputPath&lt;/b&gt; is specified in the form of JSONPath (for example, &lt;code&gt;$.detail&lt;/code&gt;), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;b&gt;InputTransformer&lt;/b&gt; is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you specify &lt;code&gt;InputPath&lt;/code&gt; or &lt;code&gt;InputTransformer&lt;/code&gt;, you must use JSON dot notation, not bracket notation.&lt;/p&gt; &lt;p&gt;When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.&lt;/p&gt; &lt;p&gt;This action can partially fail if too many requests are made at the same time. If that happens, &lt;code&gt;FailedEntryCount&lt;/code&gt; is non-zero in the response and each entry in &lt;code&gt;FailedEntries&lt;/code&gt; provides the ID of the failed target and the error code.&lt;/p&gt;

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
    body = PutTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def remove_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_permission

    Revokes the permission of another Amazon Web Services account to be able to put events to the specified event bus. Specify the account to revoke by the &lt;code&gt;StatementId&lt;/code&gt; value that you associated with the account when you granted it permission with &lt;code&gt;PutPermission&lt;/code&gt;. You can find the &lt;code&gt;StatementId&lt;/code&gt; by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html\&quot;&gt;DescribeEventBus&lt;/a&gt;.

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
    body = RemovePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def remove_targets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_targets

    &lt;p&gt;Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A successful execution of &lt;code&gt;RemoveTargets&lt;/code&gt; doesn&#39;t guarantee all targets are removed from the rule, it means that the target(s) listed in the request are removed.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect.&lt;/p&gt; &lt;p&gt;This action can partially fail if too many requests are made at the same time. If that happens, &lt;code&gt;FailedEntryCount&lt;/code&gt; is non-zero in the response and each entry in &lt;code&gt;FailedEntries&lt;/code&gt; provides the ID of the failed target and the error code.&lt;/p&gt;

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
    body = RemoveTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def start_replay(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_replay

    Starts the specified replay. Events are not necessarily replayed in the exact same order that they were added to the archive. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you specify an &lt;code&gt;EventStartTime&lt;/code&gt; and an &lt;code&gt;EventEndTime&lt;/code&gt; that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use &lt;code&gt;DescribeReplay&lt;/code&gt; to determine the progress of a replay. The value returned for &lt;code&gt;EventLastReplayedTime&lt;/code&gt; indicates the time within the specified time range associated with the last event replayed.

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
    body = StartReplayRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified EventBridge resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In EventBridge, rules and event buses can be tagged.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt;

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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def test_event_pattern(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_event_pattern

    &lt;p&gt;Tests whether the specified event pattern matches the provided event.&lt;/p&gt; &lt;p&gt;Most services in Amazon Web Services treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.&lt;/p&gt;

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
    body = TestEventPatternRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified EventBridge resource. In Amazon EventBridge (CloudWatch Events), rules and event buses can be tagged.

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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_api_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_api_destination

    Updates an API destination.

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
    body = UpdateApiDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def update_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_archive

    Updates the specified archive.

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
    body = UpdateArchiveRequest.from_dict(body)
    return web.Response(status=200)


async def update_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_connection

    Updates settings for a connection.

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
    body = UpdateConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_endpoint

    Update an existing endpoint. For more information about global endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html\&quot;&gt;Making applications Regional-fault tolerant with global endpoints and event replication&lt;/a&gt; in the Amazon EventBridge User Guide..

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
    body = UpdateEndpointRequest.from_dict(body)
    return web.Response(status=200)
