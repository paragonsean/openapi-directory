from typing import List, Dict
from aiohttp import web

from openapi_server.models.runbook_draft import RunbookDraft
from openapi_server.models.runbook_draft_undo_edit_result import RunbookDraftUndoEditResult
from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server import util


async def runbook_draft_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_draft_get

    Retrieve the runbook draft identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_draft_get_content(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_draft_get_content

    Retrieve the content of runbook draft identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_draft_replace_content(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version, runbook_content) -> web.Response:
    """runbook_draft_replace_content

    Replaces the runbook draft content.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param runbook_content: The runbook draft content.
    :type runbook_content: 

    """
    return web.Response(status=200)


async def runbook_draft_undo_edit(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_draft_undo_edit

    Undo draft edit to last known published state identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
