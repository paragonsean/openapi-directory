from typing import List, Dict
from aiohttp import web

from openapi_server.models.bug_tracker_get_repo_issue_from_crash200_response import BugTrackerGetRepoIssueFromCrash200Response
from openapi_server.models.bugtracker_get_settings200_response import BugtrackerGetSettings200Response
from openapi_server.models.bugtracker_get_settings_default_response import BugtrackerGetSettingsDefaultResponse
from openapi_server.models.notifications_get_app_email_settings200_response import NotificationsGetAppEmailSettings200Response
from openapi_server.models.notifications_get_user_email_settings200_response import NotificationsGetUserEmailSettings200Response
from openapi_server.models.webhooks_list200_response import WebhooksList200Response
from openapi_server import util


async def bug_tracker_get_repo_issue_from_crash(request: web.Request, crash_group_id, owner_name, app_name) -> web.Response:
    """bug_tracker_get_repo_issue_from_crash

    Get project issue related to a crash group

    :param crash_group_id: CrashGroup Id
    :type crash_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def bugtracker_get_settings(request: web.Request, owner_name, app_name) -> web.Response:
    """bugtracker_get_settings

    Get bug tracker settings for a particular app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def notifications_get_app_email_settings(request: web.Request, owner_name, app_name) -> web.Response:
    """notifications_get_app_email_settings

    Get Email notification settings of user for a particular app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def notifications_get_user_email_settings(request: web.Request, ) -> web.Response:
    """notifications_get_user_email_settings

    Get Default email notification settings for the user


    """
    return web.Response(status=200)


async def webhooks_list(request: web.Request, owner_name, app_name) -> web.Response:
    """webhooks_list

    Get web hooks configured for a particular app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)
