from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_annotation_info import AlertAnnotationInfo
from openapi_server.models.alert_attachment_info import AlertAttachmentInfo
from openapi_server.models.alert_filter_public import AlertFilterPublic
from openapi_server.models.alert_info import AlertInfo
from openapi_server.models.alert_notification_info import AlertNotificationInfo
from openapi_server.models.alert_report import AlertReport
from openapi_server.models.change_alert_status_filter_info import ChangeAlertStatusFilterInfo
from openapi_server.models.change_alert_status_info import ChangeAlertStatusInfo
from openapi_server.models.change_alert_status_multiple_info import ChangeAlertStatusMultipleInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.overview_alert import OverviewAlert
from openapi_server.models.overview_alert_paged_results_public import OverviewAlertPagedResultsPublic
from openapi_server.models.raise_alert_info import RaiseAlertInfo
from openapi_server import util


async def alerts_acknowledge_all_post(request: web.Request, user_id=None, body=None) -> web.Response:
    """Confirms all visible alerts

    This method confirms all unhandled alerts your team currently has by a specific user.

    :param user_id: User ID of the user to be used to acknowledge the alarms.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusFilterInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_acknowledge_multiple_post(request: web.Request, body=None) -> web.Response:
    """Acknowlegde multiple alerts

    This method confirms all alerts provided.

    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusMultipleInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_alert_id_acknowledge_post(request: web.Request, alert_id, body=None) -> web.Response:
    """Acknowledge an alert

    

    :param alert_id: Id to acknowledge an alert.
    :type alert_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_alert_id_annotate_post(request: web.Request, alert_id, body=None) -> web.Response:
    """Annotate Alert

    Annotates an alert by given Annotation Info.

    :param alert_id: Id of the alert to annotate.
    :type alert_id: str
    :param body: Annotation Information.
    :type body: dict | bytes

    """
    body = AlertAnnotationInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_alert_id_annotations_get(request: web.Request, alert_id) -> web.Response:
    """Get annotations of an alert

    Get annotations of an alert by id.

    :param alert_id: Id of the requested Alert.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_alert_id_attachments_attachment_id_get(request: web.Request, alert_id, attachment_id, width=None, height=None, scale=None) -> web.Response:
    """Gets a specified attachment of a specified alert.

    

    :param alert_id: Id of the alert that contains the wanted attachment.
    :type alert_id: str
    :param attachment_id: Id of the attachment, that you want to retrieve.
    :type attachment_id: str
    :param width: Optional parameter defining the wanted width of the picture that is retrieved.
    :type width: int
    :param height: Optional parameter defining the wanted height of the picture that is retrieved.
    :type height: int
    :param scale: Optional parameter defining whether it&#39;s wanted to scale the retrieved image. Default is set to  true.
    :type scale: bool

    """
    return web.Response(status=200)


async def alerts_alert_id_attachments_get(request: web.Request, alert_id) -> web.Response:
    """Get attachments of an alert

    Get attachments of an alert by id.

    :param alert_id: Id of the requested Alert.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_alert_id_close_post(request: web.Request, alert_id, body=None) -> web.Response:
    """Close an alert

    

    :param alert_id: Id to acknowledge an alert.
    :type alert_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_alert_id_get(request: web.Request, alert_id) -> web.Response:
    """Get Alert

    Gets an alert by id.

    :param alert_id: Id of the requested Alert.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_alert_id_notifications_get(request: web.Request, alert_id) -> web.Response:
    """Get alert notifications

    Get notifications of all users by alert id.

    :param alert_id: Id of the requested Alert.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_alert_id_overview_get(request: web.Request, alert_id) -> web.Response:
    """Get an overview alert.

    Get overview alert by id.

    :param alert_id: Id of the requested Alert.
    :type alert_id: str

    """
    return web.Response(status=200)


async def alerts_alert_id_undo_acknowledge_post(request: web.Request, alert_id, body=None) -> web.Response:
    """Undo the acknowledgement of an alert.

    This method tries to undo an alert acknowledgement.

    :param alert_id: 
    :type alert_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_alert_id_undo_close_post(request: web.Request, alert_id, body=None) -> web.Response:
    """Undo the closure of an alert.

    This method tries to undo an alert close.

    :param alert_id: 
    :type alert_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_close_all_post(request: web.Request, user_id=None, body=None) -> web.Response:
    """Close all acknowledged alerts.

    This method closes all acknowledged alerts your team currently has.

    :param user_id: User ID of the user to be used to close the alarms.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusFilterInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_close_multiple_post(request: web.Request, body=None) -> web.Response:
    """Close multiple alerts

    This method closes all alerts provided.

    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusMultipleInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_paged_post(request: web.Request, max_results=None, user_id=None, body=None) -> web.Response:
    """Gets alerts paged

    

    :param max_results: Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                  Number of alerts could be less if filtered but at least 1.
    :type max_results: int
    :param user_id: User ID of the user you want to get alerts for.
    :type user_id: str
    :param body: The filter defines which alerts are supposed to be retrieved.
    :type body: dict | bytes

    """
    body = AlertFilterPublic.from_dict(body)
    return web.Response(status=200)


async def alerts_post(request: web.Request, body=None) -> web.Response:
    """Trigger Alert

    Triggers a new alert for your team. All team members on duty will receive alert notifications.

    :param body: Alert to raise.
    :type body: dict | bytes

    """
    body = RaiseAlertInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_report_get(request: web.Request, user_id=None) -> web.Response:
    """Get Alert Report

    Returns information about the occurred alert volume in different time periods as well as information about the  response behaviour (amount of confirmed and unhandled alerts) of your team members.

    :param user_id: User ID of the user for whom you want a report.
    :type user_id: str

    """
    return web.Response(status=200)


async def alerts_undo_acknowledge_multiple_post(request: web.Request, body=None) -> web.Response:
    """Queue undo of multiple acknowledgments.

    This method tries to undo the acknowledgement of multiple alerts via a queue. The operation is handled in the background.

    :param body: Configure which user should be undone for which alerts.
    :type body: dict | bytes

    """
    body = ChangeAlertStatusMultipleInfo.from_dict(body)
    return web.Response(status=200)


async def alerts_undo_close_multiple_post(request: web.Request, body=None) -> web.Response:
    """Withdraw closure of multiple alerts

    This method tries to undo multiple alert closes. The operation is handled in the background.

    :param body: 
    :type body: dict | bytes

    """
    body = ChangeAlertStatusMultipleInfo.from_dict(body)
    return web.Response(status=200)
