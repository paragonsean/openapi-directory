from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_forward import AutoForward
from openapi_server.models.auto_reply import AutoReply
from openapi_server.models.create_mailbox_request import CreateMailboxRequest
from openapi_server.models.mailbox import Mailbox
from openapi_server.models.mailbox_detail import MailboxDetail
from openapi_server.models.update_mailbox_password_request import UpdateMailboxPasswordRequest
from openapi_server import util


async def change_mailbox_password(request: web.Request, mailbox_name, mailbox_name2, body=None) -> web.Response:
    """Change password for mailbox

    

    :param mailbox_name: Mailbox name.
    :type mailbox_name: str
    :param mailbox_name2: Automatically added
    :type mailbox_name2: str
    :param body: Contains the new password.
    :type body: dict | bytes

    """
    body = UpdateMailboxPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def configure_mailbox_auto_forward(request: web.Request, mailbox_name, mailbox_name2, body=None) -> web.Response:
    """Configure auto-forward for mailbox

    

    :param mailbox_name: Mailbox name.
    :type mailbox_name: str
    :param mailbox_name2: Automatically added
    :type mailbox_name2: str
    :param body: Contains the auto-forward information.
    :type body: dict | bytes

    """
    body = AutoForward.from_dict(body)
    return web.Response(status=200)


async def configure_mailbox_auto_reply(request: web.Request, mailbox_name, mailbox_name2, body=None) -> web.Response:
    """Configure auto-reply for mailbox

    

    :param mailbox_name: Mailbox name.
    :type mailbox_name: str
    :param mailbox_name2: Automatically added
    :type mailbox_name2: str
    :param body: Contains the auto-reply information.
    :type body: dict | bytes

    """
    body = AutoReply.from_dict(body)
    return web.Response(status=200)


async def create_mailbox(request: web.Request, body=None) -> web.Response:
    """Create a new mailbox.

    

    :param body: The add mailbox request.
    :type body: dict | bytes

    """
    body = CreateMailboxRequest.from_dict(body)
    return web.Response(status=200)


async def delete_mailbox(request: web.Request, mailbox_name, mailbox_name2) -> web.Response:
    """Delete a mailbox

    

    :param mailbox_name: Mailbox name.
    :type mailbox_name: str
    :param mailbox_name2: Automatically added
    :type mailbox_name2: str

    """
    return web.Response(status=200)


async def get_mailbox(request: web.Request, mailbox_name, mailbox_name2) -> web.Response:
    """Get a specific mailbox

    

    :param mailbox_name: Mailbox name.
    :type mailbox_name: str
    :param mailbox_name2: Automatically added
    :type mailbox_name2: str

    """
    return web.Response(status=200)


async def get_mailboxes(request: web.Request, domain_name=None) -> web.Response:
    """Gets your mailboxes.

    Currently only supports getting the mailboxes filtered by domain name.

    :param domain_name: Obligated domain name for getting mailboxes.
    :type domain_name: str

    """
    return web.Response(status=200)
