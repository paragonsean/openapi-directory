from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.notification_rule import NotificationRule
from openapi_server.models.notification_rule_update import NotificationRuleUpdate
from openapi_server.models.notification_rules import NotificationRules
from openapi_server.models.post_notification_rule import PostNotificationRule
from openapi_server import util


async def create_notification_rule(request: web.Request, body) -> web.Response:
    """Add a notification rule

    

    :param body: Notification rule to create
    :type body: dict | bytes

    """
    body = PostNotificationRule.from_dict(body)
    return web.Response(status=200)


async def delete_notification_rules_id(request: web.Request, rule_id, zap_trace_span=None) -> web.Response:
    """Delete a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_notification_rules_id_labels_id(request: web.Request, rule_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete label from a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_notification_rules(request: web.Request, org_id, zap_trace_span=None, offset=None, limit=None, check_id=None, tag=None) -> web.Response:
    """List all notification rules

    

    :param org_id: Only show notification rules that belong to a specific organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param check_id: Only show notifications that belong to the specific check ID.
    :type check_id: str
    :param tag: Only return notification rules that \&quot;would match\&quot; statuses which contain the tag key value pairs provided.
    :type tag: str

    """
    return web.Response(status=200)


async def get_notification_rules_id(request: web.Request, rule_id, zap_trace_span=None) -> web.Response:
    """Retrieve a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_notification_rules_id_labels(request: web.Request, rule_id, zap_trace_span=None) -> web.Response:
    """List all labels for a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_notification_rules_id(request: web.Request, rule_id, body, zap_trace_span=None) -> web.Response:
    """Update a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param body: Notification rule update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = NotificationRuleUpdate.from_dict(body)
    return web.Response(status=200)


async def post_notification_rule_id_labels(request: web.Request, rule_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def put_notification_rules_id(request: web.Request, rule_id, body, zap_trace_span=None) -> web.Response:
    """Update a notification rule

    

    :param rule_id: The notification rule ID.
    :type rule_id: str
    :param body: Notification rule update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = NotificationRule.from_dict(body)
    return web.Response(status=200)
