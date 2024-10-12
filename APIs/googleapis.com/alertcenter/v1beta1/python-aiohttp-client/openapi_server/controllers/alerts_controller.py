from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_feedback import AlertFeedback
from openapi_server.models.alert_metadata import AlertMetadata
from openapi_server.models.batch_delete_alerts_request import BatchDeleteAlertsRequest
from openapi_server.models.batch_delete_alerts_response import BatchDeleteAlertsResponse
from openapi_server.models.batch_undelete_alerts_request import BatchUndeleteAlertsRequest
from openapi_server.models.batch_undelete_alerts_response import BatchUndeleteAlertsResponse
from openapi_server.models.list_alert_feedback_response import ListAlertFeedbackResponse
from openapi_server.models.list_alerts_response import ListAlertsResponse
from openapi_server.models.undelete_alert_request import UndeleteAlertRequest
from openapi_server import util


async def alertcenter_alerts_batch_delete(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """alertcenter_alerts_batch_delete

    Performs batch delete operation on alerts.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = BatchDeleteAlertsRequest.from_dict(body)
    return web.Response(status=200)


async def alertcenter_alerts_batch_undelete(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """alertcenter_alerts_batch_undelete

    Performs batch undelete operation on alerts.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = BatchUndeleteAlertsRequest.from_dict(body)
    return web.Response(status=200)


async def alertcenter_alerts_delete(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None) -> web.Response:
    """alertcenter_alerts_delete

    Marks the specified alert for deletion. An alert that has been marked for deletion is removed from Alert Center after 30 days. Marking an alert for deletion has no effect on an alert which has already been marked for deletion. Attempting to mark a nonexistent alert for deletion results in a &#x60;NOT_FOUND&#x60; error.

    :param alert_id: Required. The identifier of the alert to delete.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alert is associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str

    """
    return web.Response(status=200)


async def alertcenter_alerts_feedback_create(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None, body=None) -> web.Response:
    """alertcenter_alerts_feedback_create

    Creates new feedback for an alert. Attempting to create a feedback for a non-existent alert returns &#x60;NOT_FOUND&#x60; error. Attempting to create a feedback for an alert that is marked for deletion returns &#x60;FAILED_PRECONDITION&#39; error.

    :param alert_id: Required. The identifier of the alert this feedback belongs to.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alert is associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AlertFeedback.from_dict(body)
    return web.Response(status=200)


async def alertcenter_alerts_feedback_list(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None, filter=None) -> web.Response:
    """alertcenter_alerts_feedback_list

    Lists all the feedback for an alert. Attempting to list feedbacks for a non-existent alert returns &#x60;NOT_FOUND&#x60; error.

    :param alert_id: Required. The alert identifier. The \&quot;-\&quot; wildcard could be used to represent all alerts.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alert is associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str
    :param filter: Optional. A query string for filtering alert feedback results. For more details, see [Query filters](https://developers.google.com/admin-sdk/alertcenter/guides/query-filters) and [Supported query filter fields](https://developers.google.com/admin-sdk/alertcenter/reference/filter-fields#alerts.feedback.list).
    :type filter: str

    """
    return web.Response(status=200)


async def alertcenter_alerts_get(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None) -> web.Response:
    """alertcenter_alerts_get

    Gets the specified alert. Attempting to get a nonexistent alert returns &#x60;NOT_FOUND&#x60; error.

    :param alert_id: Required. The identifier of the alert to retrieve.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alert is associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str

    """
    return web.Response(status=200)


async def alertcenter_alerts_get_metadata(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None) -> web.Response:
    """alertcenter_alerts_get_metadata

    Returns the metadata of an alert. Attempting to get metadata for a non-existent alert returns &#x60;NOT_FOUND&#x60; error.

    :param alert_id: Required. The identifier of the alert this metadata belongs to.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alert metadata is associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str

    """
    return web.Response(status=200)


async def alertcenter_alerts_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer_id=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """alertcenter_alerts_list

    Lists the alerts.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer_id: Optional. The unique identifier of the Google Workspace account of the customer the alerts are associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793).
    :type customer_id: str
    :param filter: Optional. A query string for filtering alert results. For more details, see [Query filters](https://developers.google.com/admin-sdk/alertcenter/guides/query-filters) and [Supported query filter fields](https://developers.google.com/admin-sdk/alertcenter/reference/filter-fields#alerts.list).
    :type filter: str
    :param order_by: Optional. The sort order of the list results. If not specified results may be returned in arbitrary order. You can sort the results in descending order based on the creation timestamp using &#x60;order_by&#x3D;\&quot;create_time desc\&quot;&#x60;. Currently, supported sorting are &#x60;create_time asc&#x60;, &#x60;create_time desc&#x60;, &#x60;update_time desc&#x60;
    :type order_by: str
    :param page_size: Optional. The requested page size. Server may return fewer items than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results the server should return. If empty, a new iteration is started. To continue an iteration, pass in the value from the previous ListAlertsResponse&#39;s next_page_token field.
    :type page_token: str

    """
    return web.Response(status=200)


async def alertcenter_alerts_undelete(request: web.Request, alert_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """alertcenter_alerts_undelete

    Restores, or \&quot;undeletes\&quot;, an alert that was marked for deletion within the past 30 days. Attempting to undelete an alert which was marked for deletion over 30 days ago (which has been removed from the Alert Center database) or a nonexistent alert returns a &#x60;NOT_FOUND&#x60; error. Attempting to undelete an alert which has not been marked for deletion has no effect.

    :param alert_id: Required. The identifier of the alert to undelete.
    :type alert_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UndeleteAlertRequest.from_dict(body)
    return web.Response(status=200)
