from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_feedback import AlertFeedback
from openapi_server.models.alert_feedbacks import AlertFeedbacks
from openapi_server import util


async def services_add_alert_feedback(request: web.Request, service_name, api_version, alert_feedback) -> web.Response:
    """services_add_alert_feedback

    Adds an alert feedback submitted by customer.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param alert_feedback: The alert feedback.
    :type alert_feedback: dict | bytes

    """
    alert_feedback = AlertFeedback.from_dict(alert_feedback)
    return web.Response(status=200)


async def services_list_alert_feedback(request: web.Request, service_name, short_name, api_version) -> web.Response:
    """services_list_alert_feedback

    Gets a list of all alert feedback for a given tenant and alert type.

    :param service_name: The name of the service.
    :type service_name: str
    :param short_name: The name of the alert.
    :type short_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
